# defs is a package which claims to export all constants and some JavaScript objects, but in reality does
#  nothing. This is useful mainly when using an editor like PyCharm, so that it 'knows' that things like Object, Creep,
#  Game, etc. do exist.
from defs import *
from roles.harvester import run_harvest
from roles.upgrader import run_upgrade
from roles.carrier import run_carry
from roles.builder import run_build
from roles.restorer import run_repair
from utils.healthCheck import health_check
from utils.errorCode import SPAWN_ERROR_CODES
from roles.creepType import *

# These are currently required for Transcrypt in order to use the following names in JavaScript.
# Without the 'noalias' pragma, each of the following would be translated into something like 'py_Infinity' or
#  'py_keys' in the output file.
__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def main():
    """
    主游戏逻辑循环。
    """
    harvester_num = 0
    builder_num = 0
    carrier_num = 0
    upgrader_num = 0
    restore_num = 0

    # 运行每个 creep，根据其对应的不同角色运行不同的职能
    for name in Object.keys(Game.creeps):
        creep = Game.creeps[name]
        health_check(creep)
        if creep.memory.role == 'harvester':
            harvester_num += 1
            run_harvest(creep)
        elif creep.memory.role == 'builder':
            builder_num += 1
            run_build(creep)
        elif creep.memory.role == 'carrier':
            carrier_num += 1
            run_carry(creep)
        elif creep.memory.role == 'upgrader':
            upgrader_num += 1
            run_upgrade(creep)
        elif creep.memory.role == 'restore':
            restore_num += 1
            run_repair(creep)

    if Game.time % 20 == 0:
        print(
            "共有建造者{}个,运输者{}个,采集者{}个,升级者{}个,修复者{}个".format(builder_num, carrier_num, harvester_num,
                                                                                upgrader_num, restore_num))
    # 运行每个 spawn
    for name in Object.keys(Game.spawns):
        spawn = Game.spawns[name]
        if not spawn.memory.taskList:
            spawn.memory.taskList = []
        if spawn.memory.taskList and len(spawn.memory.taskList) > 0:
            task = spawn.memory.taskList[0]
            result = spawn.spawnCreep(task['body'], task['name'])
            if result == 0:
                spawn.memory.taskList.remove(task)
            else:
                if result != -6 and result != -3:
                    error_message = SPAWN_ERROR_CODES[result]
                    print(
                        "【房间{}】：[{}]尝试生成creep[{}]失败，原因为:{}".format(spawn.room.name, spawn.name, task['name'],
                                                                              error_message))
        else:
            if Game.gcl.level < 5:
                if builder_num < 1:
                    spawn.createCreep(SMALL_BUILDER.body, SMALL_BUILDER.memory)
                elif carrier_num < 1:
                    spawn.createCreep(SMALL_CARRIER.body, SMALL_CARRIER.memory)
                if upgrader_num < 1:
                    spawn.createCreep(SMALL_UPGRADER.body, SMALL_UPGRADER.memory)
                if harvester_num < 1:
                    spawn.createCreep(SMALL_HARVESTER.body, SMALL_HARVESTER.memory)


module.exports.loop = main

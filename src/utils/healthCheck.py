from ..defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def health_check(creep):
    if not creep.memory.isPushSpawnTask and creep.ticksToLive < 20:
        closest_spawn = creep.pos.findClosestByPath(FIND_MY_SPAWNS)
        if not any(element['type'] == 'CLAIM' for element in creep.body) and creep.pos.inRangeTo(closest_spawn, 1):
            if creep.pos.isNearTo(closest_spawn) and not closest_spawn.spawning:
                closest_spawn.renewCreep(creep)
            else:
                creep.moveTo(closest_spawn)
        else:
            spawns = creep.room.find(FIND_MY_SPAWNS)
            if len(spawns) > 0:
                target_spawn = _.max(spawns, iteratee=lambda s: s.store.getFreeCapacity(RESOURCE_ENERGY))
                target_spawn.memory.taskList.append(
                    {'body': [element['type'] for element in creep.body], 'name': creep.name})
                creep.memory.isPushSpawnTask = True
                print("【房间{}】：{}即将死亡，已向{}推送生成任务".format(creep.room.name, creep.name, target_spawn.name))
            else:
                print("【房间{}】：{}即将死亡，无法推送生成任务，请检查spawn状态".format(creep.room.name, creep.name))

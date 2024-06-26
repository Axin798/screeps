from ..defs import *
from ..utils.errorCode import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def run_upgrade(creep):
    """
    升级者
    :param creep: 要运行的 creep
    """
    # 如果满了，则停止填充并删除来源
    if creep.memory.filling and _.sum(creep.carry) >= creep.carryCapacity:
        creep.memory.filling = False
        del creep.memory.source
    # 如果空了，则填充并删除目标
    elif not creep.memory.filling and creep.carry.energy <= 0:
        creep.memory.filling = True
        del creep.memory.target

    if creep.memory.filling:
        # 有两种获取能量的方式，开采(0)和拿取(1)
        harvest_or_withdraw = creep.memory.harvest_or_withdraw
        # 如果有保存的来源，则使用它
        if creep.memory.source:
            source = Game.getObjectById(creep.memory.source)
            if not source:
                del creep.memory.source
                return
        else:
            # 按照storage、container、source的顺序寻找来源
            source = creep.pos.findClosestByPath(FIND_STRUCTURES,
                                                 {'filter': lambda s:
                                                 s.structureType == STRUCTURE_STORAGE and s.isActive() and s.store[
                                                     RESOURCE_ENERGY] > 0})
            harvest_or_withdraw = 1
            if not source:
                source = creep.pos.findClosestByPath(FIND_STRUCTURES, {
                    'filter': lambda
                        s: s.structureType == STRUCTURE_CONTAINER and s.isActive() and s.store[RESOURCE_ENERGY] > 0})
                harvest_or_withdraw = 1
            if not source:
                source = creep.pos.findClosestByPath(FIND_SOURCES_ACTIVE)
                harvest_or_withdraw = 0
            creep.memory.source = source.id
            creep.memory.harvest_or_withdraw = harvest_or_withdraw
        # 如果靠近了来源，则进行采集或拿取，否则移动过去
        if creep.pos.isNearTo(source):
            if harvest_or_withdraw == 0:
                result = creep.harvest(source)
                if result != 0:
                    error_message = HARVEST_ERROR_CODES[result]
                    print(
                        "【房间{}】：[{}]尝试从{}采集失败，原因为:{}".format(creep.room.name, creep.name, source,
                                                                         error_message))
            else:
                result = creep.withdraw(source, RESOURCE_ENERGY)
                if result != 0:
                    error_message = WITHDRAW_ERROR_CODES[result]
                    print(
                        "【房间{}】：[{}]尝试从{}拿取失败，原因为:{}".format(creep.room.name, creep.name, source,
                                                                         error_message))
        else:
            creep.moveTo(source)

    else:
        # 如果有保存的目标，则使用它
        if creep.memory.target:
            target = Game.getObjectById(creep.memory.target)
            if not target:
                del creep.memory.target
                return
        else:
            # 获取房间控制器
            target = creep.room.controller
            creep.memory.target = target.id
        is_close = creep.pos.inRangeTo(target, 3)
        if is_close:
            result = creep.upgradeController(target)
            if result != 0:
                error_message = UPGRADE_ERROR_CODES[result]
                print(
                    "【房间{}】：[{}]尝试升级控制器失败，原因为:{}".format(creep.room.name, creep.name, error_message))
            # 让creep离控制器更近一点，为其他creep腾出空间。
            if not creep.pos.inRangeTo(target, 2):
                creep.moveTo(target)
        else:
            creep.moveTo(target)

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


def run_harvest(creep):
    """
    采集者
    :param creep: 要运行的 creep
    """
    if creep.memory.target:
        target = Game.getObjectById(creep.memory.target)
    else:
        container = creep.room.find(FIND_STRUCTURES, {
            'filter': lambda s: s.structureType == STRUCTURE_CONTAINER and s.isActive() and s.store.getFreeCapacity(
                RESOURCE_ENERGY) > 0})
        target = None
        for c in container:
            if not Memory.harvestedContainer or c.id not in Memory.harvestedContainer:
                target = c
                break
        if not target:
            print("【房间{}】：未建造container或container已满，采集者{}暂无法运行".format(creep.room.name, creep.name))
        else:
            creep.memory.target = target.id
            Memory.harvestedContainer.append(target.id)
    if creep.pos.inRangeTo(target.pos.x, target.pos.y, 0):
        if target.store.getFreeCapacity(RESOURCE_ENERGY) > 0:
            source = creep.pos.findClosestByPath(FIND_SOURCES)
            result = creep.harvest(source)
            if result != 0:
                error_message = HARVEST_ERROR_CODES[result]
                print(
                    "【房间{}】：[{}]尝试从{}采集失败，原因为:{}".format(creep.room.name, creep.name, source,
                                                                     error_message))
        else:
            print("【房间{}】：{}的容器已满，[{}]已停止采集".format(creep.room.name, target, creep.name))
    else:
        creep.moveTo(target.pos.x, target.pos.y)

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
    if creep.ticksToLive < 10:
        Memory.taskList.append({'body': [element['type'] for element in creep.body], 'name': creep.name})
        print("【房间{}】：{}即将死亡，已推送生成任务".format(creep.room.name, creep.name))
        creep.say("我即将离开，已推送生成任务，请spawn准备生成")

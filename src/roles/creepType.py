from ..defs import *

SMALL_HARVESTER = {
    'body': [WORK, WORK, MOVE],
    'memory': {'role': 'harvester', 'level': 'small'}
}

BIG_HARVESTER = {
    'body': [WORK, WORK, WORK, WORK, WORK, WORK, MOVE, MOVE, MOVE],
    'memory': {'role': 'harvester', 'level': 'big'}
}

SMALL_BUILDER = {
    'body': [WORK, CARRY, MOVE, MOVE],
    'memory': {'role': 'builder', 'level': 'small'}
}

BIG_BUILDER = {
    'body': [WORK, WORK, WORK, CARRY, CARRY, CARRY, MOVE, MOVE, MOVE, MOVE],
    'memory': {'role': 'builder', 'level': 'big'}
}

SMALL_CARRIER = {
    'body': [WORK, CARRY, MOVE, MOVE],
    'memory': {'role': 'carrier', 'level': 'small'}
}

BIG_CARRIER = {
    'body': [WORK, WORK, CARRY, CARRY, CARRY, CARRY, MOVE, MOVE, MOVE, MOVE, MOVE, MOVE],
    'memory': {'role': 'carrier', 'level': 'big'}
}

SMALL_UPGRADER = {
    'body': [WORK, CARRY, MOVE, MOVE],
    'memory': {'role': 'upgrader', 'level': 'small'}
}

BIG_UPGRADER = {
    'body': [WORK, WORK, CARRY, CARRY, CARRY, CARRY, MOVE, MOVE, MOVE, MOVE, MOVE, MOVE],
    'memory': {'role': 'upgrader', 'level': 'big'}
}

SMALL_RESTORER = {
    'body': [WORK, CARRY, MOVE, MOVE, MOVE],
    'memory': {'role': 'restorer', 'level': 'small'}
}

BIG_RESTORER = {
    'body': [WORK, WORK, WORK, CARRY, CARRY, CARRY, MOVE, MOVE, MOVE, MOVE],
    'memory': {'role': 'restorer', 'level': 'big'}
}
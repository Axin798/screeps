# 采集错误码描述字典
HARVEST_ERROR_CODES = {
    0: "操作成功",
    -1: "你不是该 creep 的所有者，或者其他玩家已经占领或者预定了该房间的控制器。",
    -4: "这个 creep 依然在孵化中。",
    -5: "未找到 extractor。你必须建造一个 extractor 来开采矿物。",
    -6: "目标中已经没有可采集的能量或者矿物。",
    -7: "目标不是有效的 source 或者 mineral 对象。",
    -9: "目标太远了。",
    -11: "extractor 仍在冷却中。",
    -12: "这个 creep 身上没有 WORK 部件。"
}

# 传输资源错误码描述字典
TRANSFER_ERROR_CODES = {
    0: "这个操作已经成功纳入计划。",
    -1: "你不是这个 creep 的拥有者。",
    -4: "这个 creep 依然在孵化中。",
    -6: "该 creep 没有携带足够的资源。",
    -7: "目标不是一个能存放指定资源的有效对象。",
    -8: "目标无法携带更多的资源。",
    -9: "目标太远了。",
    -10: "resourceType 不是 RESOURCE_* 常量之一，或者 amount 数量错误。"
}

# 拿取资源错误码描述字典
WITHDRAW_ERROR_CODES = {
    0: "这个操作已经成功纳入计划。",
    -1: "你不是此 creep 的所有者，或者目标位于敌方 rampart 之下。",
    -4: "这个 creep 依然在孵化中。",
    -6: "目标中没有足够数量的资源。",
    -7: "目标不是一个能存储指定资源的对象。",
    -8: "此 creep 的存储已经满了。",
    -9: "目标太远了。",
    -10: "resourceType 不是 RESOURCE_* 常量之一, 或者 amount 数量错误。"
}

# 升级错误码描述字典
UPGRADE_ERROR_CODES = {
    0: "这个操作已经成功纳入计划。",
    -1: "你不是该 creep 或目标控制器的所有者。",
    -4: "这个 creep 依然在孵化中。",
    -6: "这个 creep 没有携带任何能量。",
    -7: "目标不是有效的控制器对象，或控制器的升级被阻滞了。",
    -9: "目标太远了。",
    -12: "这个 creep 身上没有 WORK 部件。"
}

# 建筑错误码描述字典
BUILD_ERROR_CODES = {
    0: "这个操作已经成功纳入计划。",
    -1: "你不是这个 creep 的拥有者。",
    -4: "这个 creep 依然在孵化中。",
    -6: "这个creep没有携带任何能量。",
    -7: "该目标不是一个有效的建筑工地(construction site)或者此处无法建造建筑(有可能是 creep 站在该地块上导致的)。",
    -9: "目标太远了。",
    -12: "这个 creep 身上没有 WORK 部件。"
}

# 修复错误码描述字典
REPAIR_ERROR_CODES = {
    0: "这个操作已经成功纳入计划。",
    -1: "你不是这个 creep 的拥有者。",
    -4: "这个 creep 依然在孵化中。",
    -6: "这个creep没有携带任何能量。",
    -7: "目标不是一个有效的 structure 对象",
    -9: "目标太远了。",
    -12: "这个 creep 身上没有 WORK 部件。"
}

# 生成creep错误码描述字典
SPAWN_ERROR_CODES = {
    0: '这个操作已经成功纳入计划。',
    -1: '你不是该母巢 (spawn) 的所有者。',
    -3: '已经有一个叫这个名字的 creep 了。',
    -4: '这个母巢 (spawn) 已经在孵化另一个 creep 了。',
    -6: '这个母巢 (spawn) 和他的扩展包含的能量不足以孵化具有给定 body 的 creep。',
    -10: 'Body 没有被恰当地描述。',
    -14: '您的房间控制器级别不足以使用此 spawn。'
}

__all__ = [
    HARVEST_ERROR_CODES,
    TRANSFER_ERROR_CODES,
    WITHDRAW_ERROR_CODES,
    UPGRADE_ERROR_CODES,
    BUILD_ERROR_CODES,
    REPAIR_ERROR_CODES,
    SPAWN_ERROR_CODES
]

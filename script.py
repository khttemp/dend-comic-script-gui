# -*- coding: utf-8 -*-

import os
import copy
import traceback

import tkinter
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

from importPy.tkinterScrollbarFrameClass import ScrollbarFrame
from importPy.tkinterEditClass import InputDialog, PasteDialog, HeaderFileInfo
from importPy.decrypt import ComicDecrypt

decryptFile = None
frame = None
copyComicData = None

cmdList = [
    "Tx",
    "TxSize",
    "Alpha",
    "End",
    "Pos",
    "ColorALL",
    "Move",
    "STAGE_BGM",
    "SetFlat3D",
    "ChangeFlat3D",
    "SetCamDir",
    "DisCamDir",
    "Set3DObj",
    "SetWAngleX",
    "SetWAngleY",
    "SetWAngleZ",
    "SetLAngleX",
    "SetLAngleY",
    "SetLAngleZ",
    "SetBoneWAngleX",
    "SetBoneWAngleY",
    "SetBoneWAngleZ",
    "SetBoneLAngleX",
    "SetBoneLAngleY",
    "SetBoneLAngleZ",
    "ShowMesh",
    "HideMesh",
    "PlayAnime",
    "Length_End",
    "SetScall",
    "RACE_START",
    "RACE_END",
    "FADE_STAGE_BGM",
    "CHANGE_SCENE",
    "LPos",
    "LMove",
    "LLoopX",
    "LLoopY",
    "LLoopZ",
    "Angle",
    "AngleLoop",
    "Move2",
    "PosX",
    "PosY",
    "PosZ",
    "PlaySE",
    "SET_MT_NONE",
    "SetCamPos",
    "SetCamTarget",
    "CamMoveWait",
    "SetComic",
    "ComicPos",
    "ComicAlpha",
    "ComicWait",
    "Scene_to_Comic",
    "SKY_DOME",
    "Fill_BG",
    "ComicEnd",
    "CamComtroll",
    "ComicSceneStop",
    "BtnWait",
    "EyeMove",
    "SetZoom",
    "BG_Alpha",
    "BG_Wait",
    "StartCount",
    "WaitMoveEye",
    "WaitFrame",
    "FTV_Play",
    "FTV_Wait",
    "HideMsgWnd",
    "FTV_End",
    "SkipEventPoint",
    "SkipEventFlg",
    "PlayComicSE",
    "StopComicSE",
    "PlayComicBGM",
    "StopComicBGM",
    "VolComicBGM",
    "HideALLComic",
    "Stage_BGM_Vol",
    "SET_CPU_FLG",
    "SET_CPU_MODE",
    "CHK_LENGTH",
    "END_CHK_LENGTH",
    "CHK_POSTION",
    "END_CHK_POSTION",
    "WAIT_MOTION",
    "END_WAIT_MOTION",
    "CHANGE_SPEED",
    "CHANGE_CAM_TYPE",
    "Set2P",
    "CharChk_and_Tx",
    "ChangeR",
    "ChangeG",
    "ChangeB",
    "ChangeColor",
    "SetGray",
    "MoveX",
    "MoveY",
    "MoveZ",
    "SetUV_X",
    "RePlay",
    "IsStart",
    "ShowGoal",
    "CHK_WIN_TRAIN",
    "END_CHK_WINTRAIN",
    "N_ADD_OBJ",
    "N_POS",
    "START_TIME_LINE",
    "N_MOVE",
    "WAIT_TIME_LINE",
    "N_DEL_OBJ",
    "SCREEN_FADE",
    "N_CHANGE_ANIME",
    "TRAIN_SPEED",
    "TRAIN_FLG",
    "SCENE_LIGHT",
    "CHANGE_CAM_LENGTH",
    "CHANGE_CAM_DIRX",
    "CHANGE_CAM_DIRY",
    "CHANGE_CAM_DIRZ",
    "R_Drift",
    "L_Drift",
    "IS_TRAIN_HIT",
    "TO_RAIL",
    "SLEEP_TRAIN",
    "RandWAngle",
    "RandMove",
    "ADD_OBJ",
    "START_COMIC",
    "SetRand3DObj",
    "Offset3DObj",
    "RandPos",
    "RandPlaySE",
    "RandAngleX",
    "RandAngleY",
    "RandAngleZ",
    "CHK_TRAIN_STATE",
    "END_CHK_TRAIN_STATE",
    "CHK_TRAIN_SPEED_U",
    "CHK_TRAIN_SPEED_D",
    "END_CHK_TRAIN_SPEED_U",
    "END_CHK_TRAIN_SPEED_D",
    "ChkStory_and_Tx",
    "ClearStory_and_Tx",
    "N_L_ANGLE_X",
    "N_L_ANGLE_Y",
    "N_L_ANGLE_Z",
    "Comic_Glay",
    "N_MoveMesh_X",
    "N_MoveMesh_Y",
    "N_MoveMesh_Z",
    "SetComic_Blur",
    "SetComic_Blur_Speed",
    "TRACK_BOMB",
    "Hide_Sky_Doom",
    "ADD_POINT",
    "CHK_POINT",
    "ELSE_CHK_POINT",
    "ELSE_IF_CHK_POINT",
    "END_CHK_POINT",
    "GOTO_SCRIPT",
    "SHEAK_COMIC",
    "STORY_OPEN",
    "STORY_CLEAR",
    "CHAR_OPEN",
    "SAVE_GAME",
    "KEISUKE_COUNT",
    "RandPlayComicSE",
    "TITLE_MODE",
    "GOING",
    "RAND_IF",
    "ELSE_RAND_IF",
    "END_RAND_IF",
    "CHK_SP_BREAK",
    "END_CHK_SP_BREAK",
    "CHK_DRIFT",
    "END_CHK_DRIFT",
    "ENDING_MODE",
    "ChkCause_and_Tx",
    "SET_DRAW_TYPE",
    "To_TxSize",
    "OPEN_CAUSE",
    "DIS_TRAIN_SPEED",
    "CHK_RACE_TIME",
    "END_CHK_RACE_TIME",
    "End_Comic",
    "WAIT_RAIL",
    "END_WAIT_RAIL",
    "COMIC_SCALE",
    "USO_COUNT",
    "WaitRandPlaySE",
    "FROM",
    "GOTO",
    "CHK_TRAIN_TYPE",
    "RAND_IF_AVG",
    "CHK_NOTCH",
    "WAIT_RAIL_ONLY",
    "ONE_TRACK_DRIFT",
    "LAST_STATION",
    "OSSAN",
    "SET_TAIL_SCALE",
    "OPEN_HUTA",
    "SET_GN",
    "MDL_GETINDEX",
    "INDEX_BONE_ROT_X",
    "INDEX_BONE_ROT_Y",
    "INDEX_BONE_ROT_Z",
    "INDEX_BONE_L_ROT_X",
    "INDEX_BONE_L_ROT_Y",
    "INDEX_BONE_L_ROT_Z",
    "CREATE_INDEX",
    "IB_LI_CREATE_ROT_X",
    "IB_LI_CREATE_ROT_Y",
    "IB_LI_CREATE_ROT_Z",
    "IB_LI_SET_ROT_X",
    "IB_LI_SET_ROT_Y",
    "IB_LI_SET_ROT_Z",
    "IB_LI_SET_LOOP_X",
    "IB_LI_SET_LOOP_Y",
    "IB_LI_SET_LOOP_Z",
    "ADD_MY_OBJ",
    "INDEX_BONE_L_POS_X",
    "INDEX_BONE_L_POS_Y",
    "INDEX_BONE_L_POS_Z",
    "IB_LI_CREATE_L_POS_X",
    "IB_LI_CREATE_L_POS_Y",
    "IB_LI_CREATE_L_POS_Z",
    "IB_LI_SET_L_POS_X",
    "IB_LI_SET_L_POS_Y",
    "IB_LI_SET_L_POS_Z",
    "FROM_ADDMT",
    "MOVE_UV_X",
    "MOVE_UV_Y",
    "CREATE_UV_MOVE_X",
    "IB_LI_SET_LOOP_LPOSX",
    "IB_LI_SET_LOOP_LPOSY",
    "IB_LI_SET_LOOP_LPOSZ",
    "RELEASE_ALL_IB_LIST",
    "ADD_MY_OBJ_INDEX",
    "TO_TAGET_POS",
    "ATK_HIT",
    "ATK_END",
    "SET_RELEASE_PARAM",
    "CREATE_LENSFLEAR",
    "SET_LENSFLEAR_PARAM",
    "SET_LENSFLEAR_MT",
    "RAIL_POS_TO_BUFF",
    "BUFF_TO_CAM_POS",
    "BUFF_TO_TARGET_POS",
    "FTV_BASE_PROC",
    "FTV_NEXT_PROC",
    "MDL_INDEX_TO_VIEW",
    "SET_FOG_LENGTH",
    "SET_UV_MOVE_X",
    "SET_UV_LOOP_X",
    "CREATE_MESH_INDEX",
    "SET_MESH_INDEX",
    "INDEX_BONE_L_ADD_ROT_X",
    "INDEX_BONE_L_ADD_ROT_Y",
    "INDEX_BONE_L_ADD_ROT_Z",
    "CHANGE_SCALL",
    "CHK_CLEAR_STORY",
    "CHK_OPEN_STORY",
    "SET_LENSFLEAR_ALL_FLG",
    "CHK_USE_CHAR",
    "SET_OBJ_FOG_NO",
    "SET_OBJ_RENDER_ID",
    "PLAY_STAGE_BGM",
    "CHANGE_TRAIN_FOG",
    "FIRST_OBJ_SET_ANIME",
    "SET_CAMPOINT_2P2C",
    "SET_CAMPOINT_1P2C",
    "CAM_POINT_PER",
    "CAM_TARGET_PER",
    "SET_CAM_POINT_LENGTH",
    "SET_CAM_OFFSET",
    "START_WIPER",
    "CREATE_TRAIN_ORG",
    "ORG_SET_RAIL",
    "ORG_ADD",
    "SET_CAMPOINT_K",
    "ORG_SET_POS",
    "ORG_SET_FOG",
    "ORG_RELEASE",
    "PLAY_FTV_END",
    "CNG_TRAIN_MAT_COL",
    "CNG_ORG_MAT_COL",
    "IS_CAUTION",
    "ENDWAIT_COMIC",
    "SET_COMIC_BG_COLOR",
    "TX_2_TRAIN",
    "CHANGE_MT_COL_TRAIN",
    "CNG_MT_COL",
    "RETURN",
    "ReLoadSE",
    "BASE_POINT_CAM",
    "STOP_3D",
    "STOP_STAGE_BGM",
    "TRAIN_UD",
    "SET_CAM_TARGET_OFFSET",
    "SET_CAM_POINT_1T_ROT",
    "SET_CAM_T_LENGHT",
    "SET_CAM_T_ROT_X",
    "SET_CAM_T_ROT_Y",
    "SET_CAM_T_OFFSET",
    "NO_OUTRUN",
    "SET_WHEEL_FIRE",
    "RELOAD_OP_TRAIN",
    "BackR_Drift",
    "BackL_Drift",
    "CHK_MOTION",
    "ORG_SET_STYLE_POS",
    "RECREATE_TRAIN",
    "SET_CAMPOINT_1P2T",
    "BUFF_TO_SC_CAM_POS",
    "SC_ORG_MODE_CHANGE",
    "SC_ORG_INIT_POS",
    "SC_ORG_SET_POS",
    "SC_ORG_SET_ROT",
    "SC_ORG_SET_X_ROT",
    "SC_ORG_SET_Y_ROT",
    "SC_ORG_SET_Z_ROT",
    "SET_SC_KOTEI_CAM_POS",
    "SET_SC_KOTEI_CAM_T_POS",
    "START_SC_WIPER",
    "SUPER_DRIFT",
    "CNG_TRAIN_NO_MAT_COL",
    "ERR_CMD",
    "K_HN",
    "TO_TRACK_RAIL",
    "IS_NO_DRAMA",
    "CNG_TRAIN_NO_MAT_RGBA",
    "SHOW_RECORD",
    "WAIT_RECORD_END",
    "IB_LI_SET_UPDATE_FLG",
    "PTCL_SCALL",
    "PTCL_COLOR",
    "PTCL_ALPHA",
    "PTCL_DRAWTYPE",
    "PTCL_ANGLE",
    "PTCL_RAND_ANGLE",
    "PTCL_RAND_COLOR",
    "PTCL_RAND_ALPHA",
    "PTCL_RAND_SCALL",
    "IB_ADD_PTCL",
    "PTCL_RAND_TONE_COLOR",
    "IS_ALPHA_END",
    "PTCL_L_POS",
    "PTCL_RAND_L_POS",
    "CREATE_MAT_COLOR_R_INTERLIST",
    "CREATE_MAT_EMISSIVE_R_INTERLIST",
    "SET_MAT_COLOR_R",
    "SET_MAT_COLOR_G",
    "SET_MAT_COLOR_B",
    "SET_MAT_COLOR_LOOP",
    "SET_MAT_EMISSIVE_R",
    "SET_MAT_EMISSIVE_G",
    "SET_MAT_EMISSIVE_B",
    "SET_MAT_EMISSIVE_LOOP",
    "CREATE_MAT_COLOR_G_INTERLIST",
    "CREATE_MAT_EMISSIVE_G_INTERLIST",
    "CREATE_MAT_COLOR_B_INTERLIST",
    "CREATE_MAT_EMISSIVE_B_INTERLIST",
    "CREATE_UV_MOVE_Y",
    "SET_UV_MOVE_Y",
    "SET_UV_LOOP_Y",
    "INDEX_RAND_ROT_X",
    "INDEX_RAND_ROT_Y",
    "INDEX_RAND_ROT_Z",
    "INDEX_RAND_POS_X",
    "INDEX_RAND_POS_Y",
    "INDEX_RAND_POS_Z",
    "RAND_SHOW_MESH",
    "INDEX_RAND_SCALL",
    "ADD_CHILD_OBJ",
    "ADD_OBJ_INDEX",
    "GAS_TARBIN",
    "ENGINE_START",
    "CHANGE_CHILDOBJ_ANIME",
    "IB_SET_W_MT",
    "CHK_OBJ_PARAM",
    "SET_OBJ_PARAM",
    "INDEX_DIR_CAM",
    "CNG_MT_LIGHT",
    "ADD_OBJ_INDEX2",
    "CNG_MT_ALPHA",
    "CREATE_MAT_ALPHA_INTERLIST",
    "SET_MAT_ALPHA",
    "RESTART_MESH_LIST",
    "RAIL_ANIME_CHANGE",
    "STOP_COMIC_SE_ALL",
    "HURIKO",
    "FTV_PLAY_AND_PREV",
    "FTV_END_INHERIT",
    "STATION_NAME_PRIORITY",
    "ALL_FIT",
    "SWAP_TX",
    "CNG_TX",
    "CHK_CAUSE",
    "CNG_ANIME",
    "CHK_OUHUKU",
    "SET_TRAIN_PTCL_AREA",
    "WAIT_DOSAN_LENGTH",
    "END_DOSAN_LENGTH",
    "DOSANSEN",
    "MESH_INDEX_SE_UV_ANIME_FLG",
    "WEATHER",
    "TRAIN_DIR",
    "IS_USE_CHAR",
    "QUICK_SAVE_EVENT",
    "NONE_GOAL",
    "ENGINE_STOP",
    "IS_BTL_MODE",
    "IS_FREE_MODE",
    "FIRST_OBJ_SET_ANIME_SCENE",
    "G_HIDE_MESH",
    "G_SHOW_MESH",
    "STOP_WIPER",
    "TRAIN_ANIME_CHANGE",
    "MESH_INDEX_UV_RESTRT",
    "SET_COMIC_COLOR",
    "CHK_OUTRUN_CNT",
    "CHK_D_AND_NOTCH",
    "ADD_CPU_LEN_OUTRUN",
    "ADD_CPU_SPEED_D_AND_NOTCH",
    "CHK_HIT_CNT",
    "TOP_SPEED_HOSYO",
    "SET_ROOT_BLOCK",
    "RIFT",
    "COLLISION",
    "DIR_VIEW_CHANGE",
    "CHK_RAIL_NO",
    "TRACK_CHANGE",
    "CHK_LENGTH_DIR",
    "CHK_POS_DIR",
    "TRUE_CLASH",
    "KATARIN_RUN",
    "DRAW_UI",
    "STOP_SCRIPT_BGM",
    "SET_STATION_NO",
    "SET_CPU_BREAKE",
    "AMB_ANIME",
    "ONE_DRIFT_FALSE",
    "L_One_Drift",
    "R_One_Drift",
    "Ret_One_Drift",
    "FRONT_JUMP",
    "REAR_JUMP",
    "FRONT_MOVE_X",
    "TRACK_MOVE",
    "TRAIN_JUMP",
    "SET_LIGHT",
    "SET_COL_KASENCHU",
    "SET_KAISO",
    "SET_FOR",
    "CHK_TRAIN_COL",
    "VOL_SCRIPT_BGM",
    "IF_NOTCH",
    "SET_BRIND_SW",
    "SET_MIKOSHI",
    "ADD_FIRE",
    "BREAKE_OR_HIT",
    "OUTRUN",
    "SOFT_ATK",
    "RAIL_STOP",
    "CHANGE_OUHUKU_LINE",
    "BRIND_ATK",
    "OPEN_POS_DLG",
    "PLAY_STAGEBGM_BLOCK",
    "SET_BTL_POINT",
    "CAM_TRAIN",
    "PLAY_SCRIPT_BGM",
    "CNG_FOR",
    "SET_RAILBLOCK_CHECKER",
    "RAIN_SE",
    "TRAIN_STOP",
    "KOTEICAM_BLEND",
    "SCRIPT_RAIN",
    "LINE_CHANGE",
    "WAIT_RAIL_MORE_ONLY",
    "SET_SE_VOL",
    "CAM_TARGET_TRACK",
    "DECAL_D37",
    "DECAL_D39",
    "DECAL_SMOKE",
    "RAIL_PRIORITY",
    "GET_KEY",
    "SHOW_LIGHT",
    "SHOW_IN_LIGHT",
    "FOG_POW",
    "STORY_WIN",
    "RAIN_PARTICLE",
    "D39_FIRE",
    "SET_CPU_SPEED",
    "BODY_AUDIO_PLAY",
    "BODY_AUDIO_STOP",
    "CNG_FADE_SPRITE",
    "RAIL_DRIFT_CHK",
    "INQ_WAIT",
    "CNG_SCCAM_TRAIN",
    "STOP_TRAIN_SE",
    "PLAY_SCRIPT_BGM_TIME",
    "CNG_BODY_COLOR",
    "LOAD_TRAIN",
    "SHOW_BLOCK",
    "UPDATE_LIGHT_FRARE",
    "WAIT_RAIL_MORE_GOTO",
    "CREATE_AURA",
    "AURA_ALPHA",
    "SET_LV_JUMP",
    "CREATE_EFFECT_CAM",
    "TO_EFFECT_CAM",
    "EFFECT_CAM_POW",
    "EFFECT_CAM_COLOR",
    "EFFECT_CAM_ALPHA",
    "HIDE_LIGHT",
    "USE_EFFECT_CAM",
    "USE_EFFECT_CAM_RGB",
    "EFFECT_CAM_RGB",
    "COPY_TRAIN_POS",
    "COL_SET",
    "CNG_CPU_TRAIN",
    "BTN_GOTO",
    "NO_TIMESCALE_KOMA",
    "EFFCAM_NOIZE",
    "EFFCAM_GRI",
    "EFFCAM_BLOCKNOISE",
    "CREATE_TQ5000_FLAGMENT",
    "USE_TQ5000_FLAGMENT",
    "TQ5000_FLAGPOS",
    "HUMIKIRI_VOL",
    "TO_EFFECT_CAM_BODY",
    "TO_NORM_CAM",
    "TO_920",
    "NO_TIMESCALE_FVT",
    "CNG_TARGET_BODY",
    "SC_ADD_POINT",
    "CHK_SC_POINT",
    "KAISO_TO_DUEL",
    "SHOW_ST",
    "ORG_UPDATE",
    "SET_RAILBLOCK_POS",
    "SET_LIGHT_OVER",
    "CREATE_STAFFROLL",
    "STAFFROLL_START",
    "WAIT_STAFFROLL",
    "SC_OUTRUN",
    "CREATE_TAKMIS",
    "SET_TAKMIS_POS",
    "SET_TAKMIS_ALPHA",
    "FRONT_DOOR",
    "SET_KOMA_DEPTH",
    "D37_FIRE",
    "AMB_HIT_WAIT",
    "ShowRecord",
    "FIT_PER",
    "CREATE_COMIC_PC",
    "SET_COMIC_PC",
    "PAUSE_STAGE_BGM",
    "SET_KAKAPO",
    "KOMA_KAKAPO",
    "START_TARBINE",
    "END_TARBINE",
    "TARBINE_FTV_START",
    "TARBINE_FTV_END",
    "STORY_ENGINE",
    "RAND_GOTO",
    "KQ_SOUND",
    "STORY_GOTO",
    "PLAY223HONE",
    "RB26",
    "PLAYORGSE",
    "H2300_GOAL",
    "DEKI_BACK_OPEN",
    "DEKI_GN_MOVE",
    "DEKI_TAMIYA_START",
    "DEKI_GN_START",
    "DEKI_SOUND",
    "DEKI_USE_TRANSAM",
    "DEKI_FRONT_OPEN",
    "REV_DRIFT",
    "DEKI_GN_STOP",
    "STORY_GN",
    "IS_ONE_TRACK_DRIFT",
    "SCRIPT_CMD_MAX"
]


def openFile():
    global decryptFile
    file_path = fd.askopenfilename(filetypes=[("COMIC_SCRIPT", "COMIC*.BIN")])

    errorMsg = "予想外のエラーが出ました。\n電車でDのコミックスクリプトではない、またはファイルが壊れた可能性があります。"
    if file_path:
        try:
            filename = os.path.basename(file_path)
            v_fileName.set(filename)
            del decryptFile
            decryptFile = ComicDecrypt(file_path, cmdList)
            if not decryptFile.open():
                decryptFile.printError()
                mb.showerror(title="エラー", message=errorMsg)
                return
            deleteWidget()
            createWidget()
        except Exception:
            print(traceback.format_exc())
            mb.showerror(title="エラー", message=errorMsg)


def createWidget():
    global decryptFile
    global frame

    btnList = [
        editLineBtn,
        insertLineBtn,
        deleteLineBtn,
        copyLineBtn,
        csvExtractBtn,
        csvLoadAndSaveBtn,
        headerFileEditBtn
    ]
    frame = ScrollbarFrame(scriptLf, v_select, btnList)

    col_tuple = ('番号', 'コマンド名')
    paramList = []
    for i in range(decryptFile.max_param):
        paramList.append("param{0}".format(i+1))
    col_tuple = col_tuple + tuple(paramList)

    frame.tree['columns'] = col_tuple
    frame.tree.column('#0', width=0, stretch='no')

    frame.tree.column('番号', anchor=tkinter.CENTER, width=50)
    frame.tree.column('コマンド名', anchor=tkinter.CENTER, width=120)
    frame.tree.heading('番号', text='番号', anchor=tkinter.CENTER)
    frame.tree.heading('コマンド名', text='コマンド名', anchor=tkinter.CENTER)

    for i in range(decryptFile.max_param):
        col_name = "param{0}".format(i+1)
        frame.tree.column(col_name, anchor=tkinter.CENTER, width=100)
        frame.tree.heading(col_name, text=col_name, anchor=tkinter.CENTER)

    num = 0
    for comicData in decryptFile.comicDataList:
        data = (num, comicData[0])
        paramCnt = comicData[1]
        paramList = []
        for i in range(paramCnt):
            paramList.append(comicData[2+i])
        data = data + tuple(paramList)
        frame.tree.insert(parent='', index='end', iid=num, values=data)
        num += 1
    return num


def deleteWidget():
    children = scriptLf.winfo_children()
    for child in children:
        child.destroy()

    v_select.set("")
    editLineBtn["state"] = "disabled"
    insertLineBtn["state"] = "disabled"
    deleteLineBtn["state"] = "disabled"


def editLine():
    global decryptFile
    global frame
    selectId = frame.tree.selection()[0]
    selectItem = frame.tree.set(selectId)
    result = InputDialog(root, "コマンド修正", decryptFile, int(selectItem["番号"]), selectItem)
    if result.reloadFlag:
        reloadFile()


def insertLine():
    global frame
    selectId = frame.tree.selection()[0]
    selectItem = frame.tree.set(selectId)
    result = InputDialog(root, "コマンド挿入", decryptFile, int(selectItem["番号"]))
    if result.reloadFlag:
        reloadFile()


def deleteLine():
    global frame
    selectId = int(frame.tree.selection()[0])
    warnMsg = "選択した行を削除します。\nそれでもよろしいですか？"
    result = mb.askokcancel(title="警告", message=warnMsg, icon="warning")
    if result:
        if not decryptFile.saveFile("delete", selectId, None):
            decryptFile.printError()
            errorMsg = "保存に失敗しました。\nファイルが他のプログラムによって開かれている\nまたは権限問題の可能性があります"
            mb.showerror(title="保存エラー", message=errorMsg)
            return
        mb.showinfo(title="成功", message="スクリプトを改造しました")
        reloadFile()


def copyLine():
    global frame
    global copyComicData
    comicData = []
    selectId = frame.tree.selection()[0]
    selectItem = frame.tree.set(selectId)
    comicData.append(selectItem["コマンド名"])
    paramCnt = len(selectItem)-2
    comicData.append(paramCnt)
    for i in range(paramCnt):
        f = float(selectItem["param{0}".format(i+1)])
        comicData.append(f)
    copyComicData = copy.deepcopy(comicData)

    mb.showinfo(title="成功", message="コピーしました")
    pasteLineBtn["state"] = "normal"


def pasteLine():
    global decryptFile
    global frame
    global copyComicData
    selectId = frame.tree.selection()[0]
    selectItem = frame.tree.set(selectId)
    num = int(selectItem["番号"])
    result = PasteDialog(root, "コマンドコピー", decryptFile, num, copyComicData)
    if result.reloadFlag:
        reloadFile()


def reloadFile():
    global decryptFile
    global frame
    errorMsg = "予想外のエラーが出ました。\n電車でDのコミックスクリプトではない、またはファイルが壊れた可能性があります。"
    if decryptFile.filePath:
        try:
            if not decryptFile.open():
                decryptFile.printError()
                mb.showerror(title="エラー", message=errorMsg)
                return

            selectId = None
            if v_select.get() != "":
                selectId = int(v_select.get())

            deleteWidget()
            maxIndex = createWidget()
            if selectId is not None:
                if selectId >= maxIndex:
                    selectId = maxIndex - 1
                if selectId - 3 < 0:
                    frame.tree.see(0)
                else:
                    frame.tree.see(selectId - 3)
                frame.tree.selection_set(selectId)
        except Exception:
            print(traceback.format_exc())
            mb.showerror(title="エラー", message=errorMsg)


def csvExtractBtn():
    global decryptFile
    file = v_fileName.get()
    filename = os.path.splitext(os.path.basename(file))[0]
    file_path = fd.asksaveasfilename(initialfile=filename, defaultextension='csv', filetypes=[('comicscript_csv', '*.csv')])
    errorMsg = "CSVで取り出す機能が失敗しました。\n権限問題の可能性があります。"
    if file_path:
        try:
            w = open(file_path, "w")
            for comicData in decryptFile.comicDataList:
                w.write("{0},".format(comicData[0]))
                cmdParaCnt = comicData[1]
                for i in range(cmdParaCnt):
                    w.write("{0}".format(comicData[2 + i]))
                    if i < cmdParaCnt-1:
                        w.write(",")
                w.write("\n")
            w.close()
            mb.showinfo(title="成功", message="CSVで取り出しました")
        except Exception as e:
            print(e)
            mb.showerror(title="エラー", message=errorMsg)


def csvLoadAndSaveBtn():
    global decryptFile
    file_path = fd.askopenfilename(defaultextension='csv', filetypes=[("comicscript_csv", "*.csv")])
    if not file_path:
        return
    f = open(file_path)
    csvLines = f.readlines()
    f.close()

    csvComicDataList = []
    for i in range(len(csvLines)):
        csvComicData = []
        csvLine = csvLines[i].strip()
        arr = csvLine.split(",")
        cmdName = arr[0]
        if cmdName not in cmdList:
            errorMsg = "{0}行目のコマンド[{1}]は\n存在しないコマンドです".format(i+1, cmdName)
            mb.showerror(title="エラー", message=errorMsg)
            return

        comicDataParaList = []
        for j in range(1, len(arr)):
            if arr[j] == "":
                break
            try:
                comicDataParaList.append(float(arr[j]))
            except Exception:
                errorMsg = "{0}行目のコマンドに\n数字に変換できない要素[{1}]が入ってます".format(i+1, arr[j])
                mb.showerror(title="エラー", message=errorMsg)
                return

        csvComicData.append(cmdName)
        cmdParaCnt = len(comicDataParaList)
        csvComicData.append(cmdParaCnt)
        for j in range(len(comicDataParaList)):
            csvComicData.append(comicDataParaList[j])

        csvComicDataList.append(csvComicData)
    warnMsg = "選択したCSVで上書きします。\nそれでもよろしいですか？"
    result = mb.askokcancel(title="警告", message=warnMsg, icon="warning")

    if result:
        if not decryptFile.saveComicList(csvComicDataList):
            decryptFile.printError()
            errorMsg = "保存に失敗しました。\nファイルが他のプログラムによって開かれている\nまたは権限問題の可能性があります"
            mb.showerror(title="保存エラー", message=errorMsg)
            return
        mb.showinfo(title="成功", message="スクリプトを改造しました")
        reloadFile()


def headerFileEditBtn():
    global decryptFile
    result = HeaderFileInfo(root, "ヘッダー情報", decryptFile)
    if result.reloadFlag:
        reloadFile()


root = tkinter.Tk()
root.title("電車でD ComicScript 改造 1.3.3")
root.geometry("900x600")

menubar = tkinter.Menu(root)
menubar.add_cascade(label='ファイルを開く', command=lambda: openFile())
root.config(menu=menubar)

v_fileName = tkinter.StringVar()
fileNameEt = ttk.Entry(root, textvariable=v_fileName, font=("", 14), width=20, state="readonly", justify="center")
fileNameEt.place(relx=0.053, rely=0.03)

selectLb = ttk.Label(text="選択した行番号：", font=("", 14))
selectLb.place(relx=0.05, rely=0.11)

v_select = tkinter.StringVar()
selectEt = ttk.Entry(root, textvariable=v_select, font=("", 14), width=5, state="readonly", justify="center")
selectEt.place(relx=0.22, rely=0.11)

editLineBtn = ttk.Button(root, text="選択した行を修正する", width=25, state="disabled", command=editLine)
editLineBtn.place(relx=0.32, rely=0.03)

insertLineBtn = ttk.Button(root, text="選択した行に挿入する", width=25, state="disabled", command=insertLine)
insertLineBtn.place(relx=0.54, rely=0.03)

deleteLineBtn = ttk.Button(root, text="選択した行を削除する", width=25, state="disabled", command=deleteLine)
deleteLineBtn.place(relx=0.76, rely=0.03)

copyLineBtn = ttk.Button(root, text="選択した行をコピーする", width=25, state="disabled", command=copyLine)
copyLineBtn.place(relx=0.32, rely=0.11)

pasteLineBtn = ttk.Button(root, text="選択した行に貼り付けする", width=25, state="disabled", command=pasteLine)
pasteLineBtn.place(relx=0.54, rely=0.11)

csvExtractBtn = ttk.Button(root, text="CSVで取り出す", width=25, state="disabled", command=csvExtractBtn)
csvExtractBtn.place(relx=0.32, rely=0.19)

csvLoadAndSaveBtn = ttk.Button(root, text="CSVで上書きする", width=25, state="disabled", command=csvLoadAndSaveBtn)
csvLoadAndSaveBtn.place(relx=0.54, rely=0.19)

headerFileEditBtn = ttk.Button(root, text="ヘッダー情報を修正する", width=25, state="disabled", command=headerFileEditBtn)
headerFileEditBtn.place(relx=0.76, rely=0.19)

scriptLf = ttk.LabelFrame(root, text="スクリプト内容")
scriptLf.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.70)

root.mainloop()

# -*- coding: utf-8 -*-

import os
import struct
import copy
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

originImgList = []
originImgSizeList = []
originSeList = []
originBgmList = []
imgList = []
imgSizeList = []
seList = []
bgmList = []
comicDataList = []
copyComicData = []
indexList = []
max_param = 0
byteArr = []
file_path = ""
frame = None

cmd = [
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
    "SCRIPT_CMD_MAX"
]

class Scrollbarframe():
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.pack(expand=True, fill=BOTH)

        self.tree = ttk.Treeview(self.frame, selectmode="browse")

        self.scrollbar_x = ttk.Scrollbar(self.frame, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=lambda f, l: self.scrollbar_x.set(f, l))
        self.scrollbar_x.pack(side=BOTTOM, fill=X)

        self.scrollbar_y = ttk.Scrollbar(self.frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=lambda f, l: self.scrollbar_y.set(f, l))
        self.scrollbar_y.pack(side=RIGHT, fill=Y)

        self.tree.pack(expand=True, fill=BOTH)
        self.tree.bind("<<TreeviewSelect>>", self.treeSelect)

        csvExtractBtn['state'] = 'normal'
        csvLoadAndSaveBtn['state'] = 'normal'
        headerFileEditBtn['state'] = 'normal'
    def treeSelect(self, event):
        selectId = self.tree.selection()[0]
        selectItem = self.tree.set(selectId)
        editLineBtn['state'] = 'normal'
        insertLineBtn['state'] = 'normal'
        deleteLineBtn['state'] = 'normal'
        copyLineBtn['state'] = 'normal'
        v_select.set(selectItem["番号"])
        

class inputDialog(sd.Dialog):
    def __init__(self, master, num, cmdItem=None):
        self.v_paramList = []
        self.num = num
        self.cmdItem = cmdItem
        if self.cmdItem != None:
            self.mode = "edit"
            self.infoMsg = "このまま修正してもよろしいですか？"
            self.p_cmd = self.cmdItem["コマンド名"]
            self.p_cnt = len(self.cmdItem)-2
        else:
            self.mode = "insert"
            self.infoMsg = "このまま挿入してもよろしいですか？"
            self.p_cmd = None
            self.p_cnt = None
        super().__init__(master)
    def body(self, master):
        self.resizable(False, False)
        self.cmdLb = ttk.Label(master, text="コマンド名", width=12, font=("", 14))
        self.cmdLb.grid(row=0, column=0, sticky=N+S)
        self.v_cmd = StringVar()
        cmdCopy = copy.deepcopy(cmd)
        cmdCopy.sort()
        self.cmdCb = ttk.Combobox(master, textvariable=self.v_cmd, width=30, state="readonly", value=cmdCopy)
        self.cmdCb.grid(row=0, column=1, sticky=N+S, pady=10)
        if self.p_cmd != None:
            self.v_cmd.set(self.p_cmd)
        else:
            self.v_cmd.set(cmdCopy[0])

        self.paramCntLb = ttk.Label(master, text="パラメータ数", width=12, font=("", 14))
        self.paramCntLb.grid(row=1, column=0, sticky=N+S)
        self.v_paramCnt = IntVar()
        paramCntList = [cnt for cnt in range(0, 16)]
        self.paramCntCb = ttk.Combobox(master, textvariable=self.v_paramCnt, width=30, state="readonly", value=paramCntList)
        self.paramCntCb.grid(row=1, column=1, sticky=N+S, pady=10)
        if self.p_cnt != None:
            self.v_paramCnt.set(self.p_cnt)
        else:
            self.v_paramCnt.set(0)

        if self.cmdItem == None:
            self.position = ttk.Label(master, text="挿入する位置", width=12, font=("", 14))
            self.position.grid(row=2, column=0, sticky=N+S)
            self.v_position = StringVar()
            positionList = ["後", "前"]
            self.positionCb = ttk.Combobox(master, textvariable=self.v_position, width=30, state="readonly", value=positionList)
            self.positionCb.grid(row=2, column=1, sticky=N+S, pady=10)
            self.v_position.set(positionList[0])

        self.xLine = ttk.Separator(master, orient=HORIZONTAL)
        self.xLine.grid(columnspan=2, row=3, column=0, sticky=E+W, pady=10)

        self.paramFrame = ttk.Frame(master)
        self.paramFrame.grid(columnspan=2, row=4, column=0, sticky=N+E+W+S)

        self.paramLb = ttk.Label(self.paramFrame)
        self.paramLb.grid(row=0, column=0)

        self.paramCntCb.bind('<<ComboboxSelected>>', lambda e: self.selectParam(self.v_paramCnt.get(), self.paramFrame))
        if self.p_cnt != 0:
            self.selectParam(self.v_paramCnt.get(), self.paramFrame, self.cmdItem)

    def selectParam(self, paramCnt, frame, cmdItem=None):
        self.v_paramList = []
        children = frame.winfo_children()
        for child in children:
            child.destroy()

        if paramCnt == 0:
            self.paramLb = ttk.Label(frame)
            self.paramLb.grid(row=0, column=0)

        for i in range(paramCnt):
            self.paramLb = ttk.Label(frame, text="param{0}".format(i+1), font=("", 14))
            self.paramLb.grid(row=i, column=0, sticky=N+S)
            v_param = DoubleVar()
            self.v_paramList.append(v_param)
            self.paramEt = ttk.Entry(frame, textvariable=v_param, width=30)
            self.paramEt.grid(row=i, column=1, sticky=N+S)
        if cmdItem != None:
            for i in range(len(self.v_paramList)):
                self.v_paramList[i].set(cmdItem["param{0}".format(i+1)])

    def buttonbox(self):
        box = Frame(self, padx=5, pady=5)
        self.okBtn = Button(box, text="OK", width=10, command=self.okPress)
        self.okBtn.grid(row=0, column=0, padx=5)
        self.cancelBtn = Button(box, text="Cancel", width=10, command=self.cancel)
        self.cancelBtn.grid(row=0, column=1, padx=5)
        box.pack()

    def okPress(self):
        editParamList = []
        try:
            for var in self.v_paramList:
                num = float(var.get())
                editParamList.append(num)
        except:
            errorMsg = "数字で入力してください。"
            mb.showerror(title="数字エラー", message=errorMsg, parent=self)
            return
        result = mb.askokcancel(title="確認", message=self.infoMsg, parent=self)
        if result:
            self.ok()
            comicData = []
            comicData.append(self.v_cmd.get())
            comicData.append(self.v_paramCnt.get())
            for i in range(self.v_paramCnt.get()):
                comicData.append(editParamList[i])

            if self.mode == "edit":
                comicDataList[self.num] = comicData
            elif self.mode == "insert":
                position = self.v_position.get()
                if position == "後":
                    comicDataList.insert(self.num+1, comicData)
                elif position == "前":
                    comicDataList.insert(self.num, comicData)

            saveFile(comicDataList)

class pasteDialog(sd.Dialog):
    def __init__(self, master, num):
        self.num = num
        super().__init__(master)
    def body(self, master):
        self.resizable(False, False)
        self.posLb = ttk.Label(master, text="挿入する位置を選んでください", font=("", 14))
        self.posLb.pack(padx=10, pady=10)
    def buttonbox(self):
        box = Frame(self, padx=5, pady=5)
        self.frontBtn = Button(box, text="前", font=("", 12), width=10, command=self.frontInsert)
        self.frontBtn.grid(row=0, column=0, padx=5)
        self.backBtn = Button(box, text="後", font=("", 12), width=10, command=self.backInsert)
        self.backBtn.grid(row=0, column=1, padx=5)
        self.cancelBtn = Button(box, text="Cancel", font=("", 12), width=10, command=self.cancel)
        self.cancelBtn.grid(row=0, column=2, padx=5)
        box.pack()
    def frontInsert(self):
        comicDataList.insert(self.num, copyComicData)
        self.save()
    def backInsert(self):
        comicDataList.insert(self.num+1, copyComicData)
        self.save()
    def save(self):
        self.ok()
        saveFile(comicDataList)

class headerFileInfo(sd.Dialog):
    def __init__(self, master, title):
        super(headerFileInfo, self).__init__(parent=master, title=title)

    def body(self, frame):
        global imgList
        global imgSizeList
        global seList
        global bgmList
        global originImgList
        global originImgSizeList
        global originSeList
        global originBgmList
        
        self.selectListNum = 0
        self.selectIndex = 0
        self.dirtyFlag = False
        
        self.btnFrame = Frame(frame, pady=5)
        self.btnFrame.pack()
        self.listFrame = Frame(frame)
        self.listFrame.pack()

        self.modifyBtn = Button(self.btnFrame, font=("", 14), text="修正", state="disabled", command=self.modify)
        self.modifyBtn.grid(padx=10, row=0, column=0, sticky=W+E)
        self.insertBtn = Button(self.btnFrame, font=("", 14), text="挿入", state="disabled", command=self.insert)
        self.insertBtn.grid(padx=10, row=0, column=1, sticky=W+E)
        self.deleteBtn = Button(self.btnFrame, font=("", 14), text="削除", state="disabled", command=self.delete)
        self.deleteBtn.grid(padx=10, row=0, column=2, sticky=W+E)

        self.imgListLb = Label(self.listFrame, font=("", 14), text="画像情報")
        self.imgListLb.grid(row=0, column=0, sticky=W+E)
        
        copyImgList = copy.deepcopy(imgList)
        for i in range(len(copyImgList)):
            copyImgList[i] = "{0:02d}→{1}".format(i, copyImgList[i])
            
        self.v_imgList = StringVar(value=copyImgList)
        self.imgListBox = Listbox(self.listFrame, font=("", 14), listvariable=self.v_imgList)
        self.imgListBox.grid(row=1, column=0, sticky=W+E)
        self.imgListBox.bind('<<ListboxSelect>>', lambda e:self.buttonActive(e, 0, self.imgListBox.curselection()))

        self.padLb = Label(self.listFrame, width=3)
        self.padLb.grid(row=0, column=1, sticky=W+E)
        
        self.imgSizeListLb = Label(self.listFrame, font=("", 14), width=40, text="画像サイズ情報")
        self.imgSizeListLb.grid(row=0, column=2, sticky=W+E)

        copyImgSizeList = copy.deepcopy(imgSizeList)
        for i in range(len(copyImgSizeList)):
            copyImgSizeList[i] = "{0:02d}→img{1:02d}, {2}".format(i, copyImgSizeList[i][0], copyImgSizeList[i][1])
            
        self.v_imgSizeList = StringVar(value=copyImgSizeList)
        self.imgSizeListBox = Listbox(self.listFrame, font=("", 14), listvariable=self.v_imgSizeList)
        self.imgSizeListBox.grid(row=1, column=2, sticky=W+E)
        self.imgSizeListBox.bind('<<ListboxSelect>>', lambda e:self.buttonActive(e, 1, self.imgSizeListBox.curselection()))

        self.seListLb = Label(self.listFrame, font=("", 14), text="SE情報")
        self.seListLb.grid(row=2, column=0, sticky=W+E)

        copySeList = copy.deepcopy(seList)
        for i in range(len(copySeList)):
            copySeList[i] = "{0:02d}→{1} [{2}]".format(i, copySeList[i][0], copySeList[i][1])
        
        self.v_seList = StringVar(value=copySeList)
        self.seListBox = Listbox(self.listFrame, font=("", 14), width=40, listvariable=self.v_seList)
        self.seListBox.grid(row=3, column=0, sticky=W+E)
        self.seListBox.bind('<<ListboxSelect>>', lambda e:self.buttonActive(e, 2, self.seListBox.curselection()))

        self.padLb = Label(self.listFrame, width=3)
        self.padLb.grid(row=2, column=1, sticky=W+E)
        
        self.bgmListLb = Label(self.listFrame, font=("", 14), text="BGM情報")
        self.bgmListLb.grid(row=2, column=2, sticky=W+E)

        copyBgmList = copy.deepcopy(bgmList)
        for i in range(len(copyBgmList)):
            copyBgmList[i] = "{0:02d}→{1} [{2}], [{3}, {4}]".format(i, copyBgmList[i][0], copyBgmList[i][1], copyBgmList[i][2], copyBgmList[i][3])
        
        self.v_bgmList = StringVar(value=copyBgmList)
        self.bgmListBox = Listbox(self.listFrame, font=("", 14), listvariable=self.v_bgmList)
        self.bgmListBox.grid(row=3, column=2, sticky=W+E)
        self.bgmListBox.bind('<<ListboxSelect>>', lambda e:self.buttonActive(e, 3, self.bgmListBox.curselection()))

    def modify(self):
        if self.selectListNum == 0:
            selectName = "画像情報"
            if len(imgList) == 0:
                errorMsg = "{0}に修正する項目はありません".format(selectName)
                mb.showerror(title="エラー", message=errorMsg)
                return
        elif self.selectListNum == 1:
            selectName = "画像サイズ情報"
            if len(imgSizeList) == 0:
                errorMsg = "{0}に修正する項目はありません".format(selectName)
                mb.showerror(title="エラー", message=errorMsg)
                return
        elif self.selectListNum == 2:
            selectName = "SE情報"
            if len(seList) == 0:
                errorMsg = "{0}に修正する項目はありません".format(selectName)
                mb.showerror(title="エラー", message=errorMsg)
                return
        elif self.selectListNum == 3:
            selectName = "BGM情報"
            if len(bgmList) == 0:
                errorMsg = "{0}に修正する項目はありません".format(selectName)
                mb.showerror(title="エラー", message=errorMsg)
                return
            
        headerFileEdit(root, "ヘッダー情報修正", self, self.selectListNum, self.selectIndex, "modify")

    def insert(self):
        headerFileEdit(root, "ヘッダー情報修正", self, self.selectListNum, self.selectIndex, "insert")

    def delete(self):
        if self.selectListNum == 0:
            selectName = "画像情報"
            if len(imgList) == 0:
                errorMsg = "{0}に削除する項目はありません".format(selectName)
                mb.showerror(title="エラー", message=errorMsg)
                return
        elif self.selectListNum == 1:
            selectName = "画像サイズ情報"
            if len(imgSizeList) == 0:
                errorMsg = "{0}に削除する項目はありません".format(selectName)
                mb.showerror(title="エラー", message=errorMsg)
                return
        elif self.selectListNum == 2:
            selectName = "SE情報"
            if len(seList) == 0:
                errorMsg = "{0}に削除する項目はありません".format(selectName)
                mb.showerror(title="エラー", message=errorMsg)
                return
        elif self.selectListNum == 3:
            selectName = "BGM情報"
            if len(bgmList) == 0:
                errorMsg = "{0}に削除する項目はありません".format(selectName)
                mb.showerror(title="エラー", message=errorMsg)
                return

        warnMsg = "{0}の{1}番目を削除します。\nそれでもよろしいですか？".format(selectName, self.selectIndex+1)
        result = mb.askokcancel(title="警告", message=warnMsg, icon="warning", parent=self)

        if result:
            self.dirtyFlag = True
            if self.selectListNum == 0:
                imgList.pop(self.selectIndex)
            elif self.selectListNum == 1:
                imgSizeList.pop(self.selectIndex)
            elif self.selectListNum == 2:
                seList.pop(self.selectIndex)
            elif self.selectListNum == 3:
                bgmList.pop(self.selectIndex)

            mb.showinfo(title="成功", message="ヘッダー情報を修正しました")

            self.imgListBox.delete(0, END)
            copyImgList = copy.deepcopy(imgList)
            for i in range(len(copyImgList)):
                copyImgList[i] = "{0:02d}→{1}".format(i, copyImgList[i])
                self.imgListBox.insert(END, copyImgList[i])
            
            self.imgSizeListBox.delete(0, END)
            copyImgSizeList = copy.deepcopy(imgSizeList)
            for i in range(len(copyImgSizeList)):
                copyImgSizeList[i] = "{0:02d}→img{1:02d}, {2}".format(i, copyImgSizeList[i][0], copyImgSizeList[i][1])
                self.imgSizeListBox.insert(END, copyImgSizeList[i])

            self.seListBox.delete(0, END)
            copySeList = copy.deepcopy(seList)
            for i in range(len(copySeList)):
                copySeList[i] = "{0:02d}→{1} [{2}]".format(i, copySeList[i][0], copySeList[i][1])
                self.seListBox.insert(END, copySeList[i])

            self.bgmListBox.delete(0, END)
            copyBgmList = copy.deepcopy(bgmList)
            for i in range(len(copyBgmList)):
                copyBgmList[i] = "{0:02d}→{1} [{2}], [{3}, {4}]".format(i, copyBgmList[i][0], copyBgmList[i][1], copyBgmList[i][2], copyBgmList[i][3])
                self.bgmListBox.insert(END, copyBgmList[i])

            if self.selectListNum == 0:
                self.imgListBox.select_set(END)
            elif self.selectListNum == 1:
                self.imgSizeListBox.select_set(END)
            elif self.selectListNum == 2:
                self.seListBox.select_set(END)
            elif self.selectListNum == 3:
                self.bgmListBox.select_set(END)

    def buttonActive(self, event, num, value):
        self.selectListNum = num
        self.insertBtn["state"] = "normal"

        if len(value) == 0:
            return
        self.selectIndex = value[0]
        self.modifyBtn["state"] = "normal"
        self.deleteBtn["state"] = "normal"

    def ok(self):
        global file_path
        global byteArr
        global indexList
        
        if self.dirtyFlag:
            result = mb.askokcancel(title="警告", message="変更を保存しますか？", icon="warning", parent=self)
            if result:
                index = 17
                newByteArr = bytearray(byteArr[0:index])

                newByteArr.append(len(imgList))
                for i in range(len(imgList)):
                    img = imgList[i].encode("shift-jis")
                    newByteArr.append(len(img))
                    newByteArr.extend(img)

                newByteArr.append(len(imgSizeList))
                for i in range(len(imgSizeList)):
                    newByteArr.append(imgSizeList[i][0])
                    for j in range(4):
                        tempF = struct.pack("<f", imgSizeList[i][1][j])
                        newByteArr.extend(tempF)

                newByteArr.append(len(seList))
                for i in range(len(seList)):
                    se = seList[i][0].encode("shift-jis")
                    newByteArr.append(len(se))
                    newByteArr.extend(se)
                    newByteArr.append(seList[i][1])

                newByteArr.append(len(bgmList))
                for i in range(len(bgmList)):
                    bgm = bgmList[i][0].encode("shift-jis")
                    newByteArr.append(len(bgm))
                    newByteArr.extend(bgm)
                    newByteArr.append(bgmList[i][1])
                    startF = struct.pack("<f", bgmList[i][2])
                    newByteArr.extend(startF)
                    loopStartF = struct.pack("<f", bgmList[i][3])
                    newByteArr.extend(loopStartF)

                index = indexList[0]
                index -= 3
                newByteArr.extend(byteArr[index:])

                errorMsg = "保存に失敗しました。\nファイルが他のプログラムによって開かれている\nまたは権限問題の可能性があります"
                try:
                    w = open(file_path, "wb")
                    w.write(newByteArr)
                    w.close()
                    mb.showinfo(title="成功", message="スクリプトを改造しました")
                    self.destroy()
                    reloadFile()
                except Exception as e:
                    print(e)
                    mb.showerror(title="保存エラー", message=errorMsg)
                    
        else:
            self.destroy()
        
    def cancel(self):
        global imgList
        global imgSizeList
        global seList
        global bgmList
        global originImgList
        global originImgSizeList
        global originSeList
        global originBgmList
        if self.dirtyFlag:
            result = mb.askokcancel(title="警告", message="変更を取消しますか？", icon="warning", parent=self)
            if result:
                imgList = copy.deepcopy(originImgList)
                imgSizeList = copy.deepcopy(originImgSizeList)
                seList = copy.deepcopy(originSeList)
                bgmList = copy.deepcopy(originBgmList)
                
                mb.showinfo(title="成功", message="変更を取消しました")
                self.destroy()
        else:
            self.destroy()

class headerFileEdit(sd.Dialog):
    global imgList
    global imgSizeList
    global seList
    global bgmList

    def __init__(self, master, title, headerInfo, listNum, listIndex, mode):
        self.selectListNum = listNum
        self.selectIndex = listIndex
        self.headerInfo = headerInfo
        self.mode = mode
        super(headerFileEdit, self).__init__(parent=master, title=title)

    def body(self, frame):
        self.posLb = ttk.Label(frame, text="変更する値", font=("", 12))
        self.posLb.grid(columnspan=2, row=0, column=0, pady=5)
        if self.selectListNum == 0:
            self.imgLb = Label(frame, text="画像ファイル名", font=("", 12))
            self.imgLb.grid(row=1, column=0)
            self.v_img = StringVar()
            if self.mode == "modify":
                self.v_img.set(imgList[self.selectIndex])
            self.imgEt = Entry(frame, textvariable=self.v_img, font=("", 12))
            self.imgEt.grid(row=1, column=1)
        elif self.selectListNum == 1:
            self.imgIndexLb = Label(frame, text="画像ファイル\nINDEX", font=("", 12))
            self.imgIndexLb.grid(row=1, column=0)
            self.imgIndex_xLb = Label(frame, text="x座標", font=("", 12))
            self.imgIndex_xLb.grid(row=2, column=0)
            self.imgIndex_yLb = Label(frame, text="y座標", font=("", 12))
            self.imgIndex_yLb.grid(row=3, column=0)
            self.imgIndex_widthLb = Label(frame, text="横長さ", font=("", 12))
            self.imgIndex_widthLb.grid(row=4, column=0)
            self.imgIndex_heightLb = Label(frame, text="縦長さ", font=("", 12))
            self.imgIndex_heightLb.grid(row=5, column=0)
            self.v_imgIndex = IntVar()
            self.v_imgIndex_x = IntVar()
            self.v_imgIndex_y = IntVar()
            self.v_imgIndex_width = IntVar()
            self.v_imgIndex_height = IntVar()
            if self.mode == "modify":
                self.v_imgIndex.set(int(imgSizeList[self.selectIndex][0]))
                self.v_imgIndex_x.set(int(imgSizeList[self.selectIndex][1][0]))
                self.v_imgIndex_y.set(int(imgSizeList[self.selectIndex][1][1]))
                self.v_imgIndex_width.set(int(imgSizeList[self.selectIndex][1][2]))
                self.v_imgIndex_height.set(int(imgSizeList[self.selectIndex][1][3]))
            self.imgIndexEt = Entry(frame, textvariable=self.v_imgIndex, font=("", 12))
            self.imgIndexEt.grid(row=1, column=1)
            self.imgIndex_xEt = Entry(frame, textvariable=self.v_imgIndex_x, font=("", 12))
            self.imgIndex_xEt.grid(row=2, column=1)
            self.imgIndex_yEt = Entry(frame, textvariable=self.v_imgIndex_y, font=("", 12))
            self.imgIndex_yEt.grid(row=3, column=1)
            self.imgIndex_widthEt = Entry(frame, textvariable=self.v_imgIndex_width, font=("", 12))
            self.imgIndex_widthEt.grid(row=4, column=1)
            self.imgIndex_heightEt = Entry(frame, textvariable=self.v_imgIndex_height, font=("", 12))
            self.imgIndex_heightEt.grid(row=5, column=1)
        elif self.selectListNum == 2:
            self.seLb = Label(frame, text="SEファイル", font=("", 12))
            self.seLb.grid(row=1, column=0)
            self.seFileCntLb = Label(frame, text="グループ取得数", font=("", 12))
            self.seFileCntLb.grid(row=2, column=0)
            self.v_se = StringVar()
            self.v_seFileCnt = IntVar()
            if self.mode == "modify":
                self.v_se.set(seList[self.selectIndex][0])
                self.v_seFileCnt.set(int(seList[self.selectIndex][1]))
            self.seEt = Entry(frame, textvariable=self.v_se, font=("", 12))
            self.seEt.grid(row=1, column=1)
            self.seFileCntEt = Entry(frame, textvariable=self.v_seFileCnt, font=("", 12))
            self.seFileCntEt.grid(row=2, column=1)
        elif self.selectListNum == 3:
            self.bgmLb = Label(frame, text="BGMファイル", font=("", 12))
            self.bgmLb.grid(row=1, column=0)
            self.bgmLoopFlagLb = Label(frame, text="BGMループフラグ", font=("", 12))
            self.bgmLoopFlagLb.grid(row=2, column=0)
            self.bgmStartLb = Label(frame, text="BGM Start位置", font=("", 12))
            self.bgmStartLb.grid(row=3, column=0)
            self.bgmLoopStartLb = Label(frame, text="BGM Loop Start位置", font=("", 12))
            self.bgmLoopStartLb.grid(row=4, column=0)
            self.v_bgm = StringVar()
            self.v_bgmLoopFlag = IntVar()
            self.v_bgmStart = DoubleVar()
            self.v_bgmLoopStart = DoubleVar()
            if self.mode == "modify":
                self.v_bgm.set(bgmList[self.selectIndex][0])
                self.v_bgmLoopFlag.set(int(bgmList[self.selectIndex][1]))
                self.v_bgmStart.set(bgmList[self.selectIndex][2])
                self.v_bgmLoopStart.set(bgmList[self.selectIndex][3])
            self.bgmEt = Entry(frame, textvariable=self.v_bgm, font=("", 12))
            self.bgmEt.grid(row=1, column=1)
            self.bgmLoopFlagCb = ttk.Combobox(frame, width=24, state="readonly", value=["ループしない", "ループする"])
            self.bgmLoopFlagCb.grid(row=2, column=1)
            self.bgmLoopFlagCb.current(self.v_bgmLoopFlag.get())
            self.bgmStartEt = Entry(frame, textvariable=self.v_bgmStart, font=("", 12))
            self.bgmStartEt.grid(row=3, column=1)
            self.bgmLoopStartEt = Entry(frame, textvariable=self.v_bgmLoopStart, font=("", 12))
            self.bgmLoopStartEt.grid(row=4, column=1)

    def validate(self):
        warnMsg = "ヘッダー情報を修正しますか？"
        result = mb.askokcancel(message=warnMsg, icon="warning", parent=self)
        if result:
            try:
                if self.selectListNum == 0:
                    if self.mode == "modify":
                        imgList[self.selectIndex] = self.v_img.get()
                    elif self.mode == "insert":
                        imgList.append(self.v_img.get())
                elif self.selectListNum == 1:
                    if self.mode == "modify":
                        imgSizeList[self.selectIndex][0] = self.v_imgIndex.get()
                        imgSizeList[self.selectIndex][1][0] = self.v_imgIndex_x.get()
                        imgSizeList[self.selectIndex][1][1] = self.v_imgIndex_y.get()
                        imgSizeList[self.selectIndex][1][2] = self.v_imgIndex_width.get()
                        imgSizeList[self.selectIndex][1][3] = self.v_imgIndex_height.get()
                    elif self.mode == "insert":
                        imgSizeList.append([self.v_imgIndex.get(), [
                                self.v_imgIndex_x.get(),
                                self.v_imgIndex_y.get(),
                                self.v_imgIndex_width.get(),
                                self.v_imgIndex_height.get()
                            ]
                        ])
                elif self.selectListNum == 2:
                    if self.mode == "modify":
                        seList[self.selectIndex][0] = self.v_se.get()
                        seList[self.selectIndex][1] = self.v_seFileCnt.get()
                    elif self.mode == "insert":
                        seList.append([self.v_se.get(), self.v_seFileCnt.get()])
                elif self.selectListNum == 3:
                    if self.mode == "modify":
                        bgmList[self.selectIndex][0] = self.v_bgm.get()
                        bgmList[self.selectIndex][1] = int(self.bgmLoopFlagCb.current())
                        bgmList[self.selectIndex][2] = self.v_bgmStart.get()
                        bgmList[self.selectIndex][3] = self.v_bgmLoopStart.get()
                    elif self.mode == "insert":
                        bgmList.append([self.v_bgm.get(),
                                        int(self.bgmLoopFlagCb.current()),
                                        self.v_bgmStart.get(),
                                        self.v_bgmLoopStart.get()
                        ])

                return True
            except:
                errorMsg = "不正な値があります"
                mb.showerror(title="エラー", message=errorMsg)
                return False

    def apply(self):
        self.headerInfo.dirtyFlag = True
        mb.showinfo(title="成功", message="ヘッダー情報を修正しました")

        self.headerInfo.imgListBox.delete(0, END)
        copyImgList = copy.deepcopy(imgList)
        for i in range(len(copyImgList)):
            copyImgList[i] = "{0:02d}→{1}".format(i, copyImgList[i])
            self.headerInfo.imgListBox.insert(END, copyImgList[i])

        self.headerInfo.imgSizeListBox.delete(0, END)
        copyImgSizeList = copy.deepcopy(imgSizeList)
        for i in range(len(copyImgSizeList)):
            copyImgSizeList[i] = "{0:02d}→img{1:02d}, {2}".format(i, copyImgSizeList[i][0], copyImgSizeList[i][1])
            self.headerInfo.imgSizeListBox.insert(END, copyImgSizeList[i])

        self.headerInfo.seListBox.delete(0, END)
        copySeList = copy.deepcopy(seList)
        for i in range(len(copySeList)):
            copySeList[i] = "{0:02d}→{1} [{2}]".format(i, copySeList[i][0], copySeList[i][1])
            self.headerInfo.seListBox.insert(END, copySeList[i])

        self.headerInfo.bgmListBox.delete(0, END)
        copyBgmList = copy.deepcopy(bgmList)
        for i in range(len(copyBgmList)):
            copyBgmList[i] = "{0:02d}→{1} [{2}], [{3}, {4}]".format(i, copyBgmList[i][0], copyBgmList[i][1], copyBgmList[i][2], copyBgmList[i][3])
            self.headerInfo.bgmListBox.insert(END, copyBgmList[i])

def decryptScript(line):
    global imgList
    global imgSizeList
    global seList
    global bgmList
    global originImgList
    global originImgSizeList
    global originSeList
    global originBgmList
    global comicDataList
    global indexList
    global max_param
    size = len(line)
    index = 16
    header = line[0:index]
    if header != b'DEND_COMICSCRIPT':
        raise Exception
    index += 1

    imgCnt = line[index]
    index += 1
    for i in range(imgCnt):
        b = line[index]
        index += 1
        imgName = line[index:index+b].decode("shift-jis")
        index += b
        imgList.append(imgName)

    originImgList = copy.deepcopy(imgList)

    imgSizeCnt = line[index]
    index += 1
    for i in range(imgSizeCnt):
        imgIndex = line[index]
        index += 1
        imgSizeInfo = []
        for j in range(4):
            tempF = struct.unpack("<f", line[index:index+4])[0]
            tempF = int(round(tempF, 5))
            imgSizeInfo.append(tempF)
            index += 4
        imgSizeList.append([imgIndex, imgSizeInfo])

    originImgSizeList = copy.deepcopy(imgSizeList)

    seCnt = line[index]
    index += 1
    for i in range(seCnt):
        b = line[index]
        index += 1
        seName = line[index:index+b].decode("shift-jis")
        index += b
        seFileCnt = line[index]
        index += 1
        seList.append([seName, seFileCnt])

    originSeList = copy.deepcopy(seList)

    bgmCnt = line[index]
    index += 1
    for i in range(bgmCnt):
        b = line[index]
        index += 1
        bgmName = line[index:index+b].decode("shift-jis")
        index += b
        bgmFileCnt = line[index]
        index += 1
        start = struct.unpack("<f", line[index:index+4])[0]
        start = round(start, 5)
        index += 4
        loopStart = struct.unpack("<f", line[index:index+4])[0]
        loopStart = round(loopStart, 5)
        index += 4
        bgmList.append([bgmName, bgmFileCnt, start, loopStart])

    originBgmList = copy.deepcopy(bgmList)

    index += 1
    comicDataCnt = struct.unpack("<h", line[index:index+2])[0]
    index += 2
    
    count = 0
    for i in range(comicDataCnt):
        indexList.append(index)
        if index >= size:
            errorMsg = "注意！設定したコマンド数({0})は、書き込んだコマンド数({1})より多く読もうとしています。".format(comicDataCnt, count)
            mb.showerror(title="エラー", message=errorMsg)
            return None
        comicData = []
        num2 = struct.unpack("<h", line[index:index+2])[0]
        index += 2
        if num2 < 0 or num2 >= len(cmd)-1:
            errorMsg = "定義されてないコマンド番号です({0})。読込を終了します。".format(num2)
            mb.showerror(title="エラー", message=errorMsg)
            return None
        comicData.append(cmd[num2])
        b = line[index]
        index += 1
        if b >= 16:
            b = 16
        if max_param < b:
            max_param = b
        comicData.append(b)
        for j in range(b):
            f = struct.unpack("<f", line[index:index+4])[0]
            index += 4
            f = round(f, 5)
            comicData.append(f)
        
        comicDataList.append(comicData)

def createWidget():
    global comicDataList
    global max_param
    global frame
    frame = Scrollbarframe(scriptLf)

    col_tuple = ('番号', 'コマンド名')
    paramList = []
    for i in range(max_param):
        paramList.append("param{0}".format(i+1))
    col_tuple = col_tuple + tuple(paramList)

    frame.tree['columns'] = col_tuple
    
    frame.tree.column('#0',width=0, stretch='no')
    frame.tree.column('番号', anchor=CENTER, width=50)
    frame.tree.column('コマンド名',anchor=CENTER, width=120)
    for i in range(max_param):
        col_name = "param{0}".format(i+1)
        frame.tree.column(col_name, anchor=CENTER, width=100)

    frame.tree.heading('番号', text='番号',anchor=CENTER)
    frame.tree.heading('コマンド名', text='コマンド名', anchor=CENTER)
    for i in range(max_param):
        col_name = "param{0}".format(i+1)
        frame.tree.heading(col_name,text=col_name, anchor=CENTER)

    index = 0
    for comicData in comicDataList:
        data = (index, comicData[0])
        paramCnt = comicData[1]
        paramList = []
        for i in range(paramCnt):
            paramList.append(comicData[2+i])
        data = data + tuple(paramList)
        frame.tree.insert(parent='', index='end', iid=index ,values=data)
        index += 1

def openFile():
    global byteArr
    global file_path
    file_path = fd.askopenfilename(filetypes=[("COMIC_SCRIPT", "COMIC*.BIN")])

    errorMsg = "予想外のエラーが出ました。\n電車でDのコミックスクリプトではない、またはファイルが壊れた可能性があります。"
    if file_path:
        try:
            filename = os.path.basename(file_path)
            v_fileName.set(filename)
            file = open(file_path, "rb")
            line = file.read()
            byteArr = bytearray(line)
            deleteWidget()
            decryptScript(line)
            createWidget()
            file.close()
        except Exception as e:
            print(e)
            mb.showerror(title="エラー", message=errorMsg)

def editLine():
    global frame
    selectId = frame.tree.selection()[0]
    selectItem = frame.tree.set(selectId)
    inputDialog(root, int(selectItem["番号"]), selectItem)

def insertLine():
    global frame
    selectId = frame.tree.selection()[0]
    selectItem = frame.tree.set(selectId)
    inputDialog(root, int(selectItem["番号"]))

def deleteLine():
    global frame
    global comicDataList
    selectId = int(frame.tree.selection()[0])
    warnMsg = "選択した行を削除します。\nそれでもよろしいですか？"
    result = mb.askokcancel(title="警告", message=warnMsg, icon="warning")
    if result:
        del comicDataList[selectId]
        saveFile(comicDataList)

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
    pasteLineBtn['state'] = 'normal'

def pasteLine():
    global frame
    selectId = frame.tree.selection()[0]
    selectItem = frame.tree.set(selectId)
    num = int(selectItem["番号"])
    pasteDialog(root, num)
        

def saveFile(comicDataList):
    global byteArr
    global file_path
    newByteArr = copy.deepcopy(byteArr)
    index = indexList[0]
    index -= 2
    newByteArr = newByteArr[0:index]

    cmdCnt = struct.pack("<h", len(comicDataList))
    for n in cmdCnt:
        newByteArr.insert(index, n)
        index += 1

    for comicData in comicDataList:
        cmdNum = struct.pack("<h", cmd.index(comicData[0]))
        for n in cmdNum:
            newByteArr.insert(index, n)
            index += 1

        paramCnt = comicData[1]
        byteParam = struct.pack("<c", paramCnt.to_bytes(1, 'big'))
        for n in byteParam:
            newByteArr.insert(index, n)
            index += 1

        for i in range(paramCnt):
            f = struct.pack("<f", comicData[2+i])
            for n in f:
                newByteArr.insert(index, n)
                index += 1

    errorMsg = "保存に失敗しました。\nファイルが他のプログラムによって開かれている\nまたは権限問題の可能性があります"
    try:
        w = open(file_path, "wb")
        w.write(newByteArr)
        w.close()
        mb.showinfo(title="成功", message="スクリプトを改造しました")
        reloadFile()
    except Exception as e:
        print(e)
        mb.showerror(title="保存エラー", message=errorMsg)

def reloadFile():
    global byteArr
    global frame
    global file_path
    errorMsg = "予想外のエラーが出ました。\n電車でDのコミックスクリプトではない、またはファイルが壊れた可能性があります。"
    if file_path:
        try:
            selectId = -1
            filename = os.path.basename(file_path)
            v_fileName.set(filename)
            file = open(file_path, "rb")
            line = file.read()
            byteArr = bytearray(line)
            if v_select.get():
                selectId = int(v_select.get())
            deleteWidget()
            decryptScript(line)
            createWidget()
            file.close()
            if selectId != -1:
                if selectId - 3 < 0:
                    frame.tree.see(0)
                else:
                    frame.tree.see(selectId-3)
                frame.tree.selection_set(selectId)
        except Exception as e:
            print(e)
            mb.showerror(title="エラー", message=errorMsg)


def csvExtractBtn():
    global comicDataList
    file = v_fileName.get()
    filename = os.path.splitext(os.path.basename(file))[0]
    file_path = fd.asksaveasfilename(initialfile=filename, defaultextension='csv', filetypes=[('comicscript_csv', '*.csv')])
    errorMsg = "CSVで取り出す機能が失敗しました。\n権限問題の可能性があります。"
    if file_path:
        try:
            w = open(file_path, "w")
            for comicData in comicDataList:
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
    global comicDataList
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
        if cmdName not in cmd:
            errorMsg = "{0}行目のコマンド[{1}]は\n存在しないコマンドです".format(i+1, cmdName)
            mb.showerror(title="エラー", message=errorMsg)
            break

        comicDataParaList = []
        for j in range(1, len(arr)):
            if arr[j] == "":
                break
            try:
                comicDataParaList.append(float(arr[j]))
            except:
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
        comicDataList = csvComicDataList
        saveFile(comicDataList)

def headerFileEditBtn():
    headerFileInfo(root, "ヘッダー情報")

root = Tk()
root.title("電車でD ComicScript 改造 1.3.1")
root.geometry("900x600")

menubar = Menu(root)
menubar.add_cascade(label='ファイルを開く', command= lambda: openFile())
root.config(menu=menubar)

v_fileName = StringVar()
fileNameEt = ttk.Entry(root, textvariable=v_fileName, font=("",14), width=20, state="readonly", justify="center")
fileNameEt.place(relx=0.053, rely=0.03)

selectLb = ttk.Label(text="選択した行番号：", font=("",14))
selectLb.place(relx=0.05, rely=0.11)

v_select = StringVar()
selectEt = ttk.Entry(root, textvariable=v_select, font=("",14), width=5, state="readonly", justify="center")
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

def deleteWidget():
    global scriptLf
    global imgList
    global imgSizeList
    global seList
    global bgmList
    global comicDataList
    global indexList
    children = scriptLf.winfo_children()
    for child in children:
        child.destroy()

    imgList = []
    imgSizeList = []
    seList = []
    bgmList = []
    comicDataList = []
    indexList = []
    v_select.set("")
    editLineBtn['state'] = 'disabled'
    insertLineBtn['state'] = 'disabled'
    deleteLineBtn['state'] = 'disabled'

root.mainloop()

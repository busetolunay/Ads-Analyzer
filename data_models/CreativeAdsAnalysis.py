from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

# ==========================================
# 1. VISUAL & TECHNICAL LAYER
# ==========================================

class ArtStyle(str, Enum):
    FLAT_2D = "Style_2D_Flat"
    HAND_DRAWN_2D = "Style_2D_HandDrawn"
    PIXEL_ART = "Style_PixelArt"
    LOW_POLY_3D = "Style_3D_LowPoly"
    VOXEL_3D = "Style_3D_Voxel"
    STYLIZED_3D = "Style_3D_Stylized"
    CEL_SHADED = "Style_CelShaded"
    REALISTIC = "Style_Realistic"
    UGC_LIVE_ACTION = "Style_UGC_LiveAction"
    MIXED_REALITY = "Style_Mixed_Reality"

class CameraPerspective(str, Enum):
    ISOMETRIC = "Cam_Isometric"
    TOP_DOWN = "Cam_TopDown"
    SIDE_SCROLL = "Cam_SideScroll"
    FIRST_PERSON = "Cam_FirstPerson"
    THIRD_PERSON_BACK = "Cam_ThirdPerson"
    SPLIT_SCREEN = "Cam_SplitScreen"

class VisualClutterLevel(str, Enum):
    MINIMALIST = "Clutter_Low"
    BALANCED = "Clutter_Medium"
    CHAOTIC = "Clutter_High"

class ColorPalette(str, Enum):
    WARM_URGENT = "Palette_Warm_RedOrange"
    COOL_CALM = "Palette_Cool_BlueGreen"
    NEON_CYBER = "Palette_Neon"
    PASTEL_COZY = "Palette_Pastel"
    HIGH_CONTRAST = "Palette_HighContrast"

# ==========================================
# 2. GAMEPLAY & MECHANICS LAYER
# ==========================================

class GameplayGenre(str, Enum):
    HYPERCASUAL_RUNNER = "Genre_HC_Runner"
    ARCADE_IDLE = "Genre_ArcadeIdle"
    PUZZLE_LOGIC = "Genre_Puzzle_Logic"
    STRATEGY_4X = "Genre_Strategy_4X"
    SIMULATION_TYCOON = "Genre_Sim_Tycoon"
    MERGE_2 = "Genre_Merge2"

class InputMethod(str, Enum):
    JOYSTICK = "Input_Joystick"
    TAP_TIMING = "Input_TapTiming"
    DRAG_SWERVE = "Input_DragSwerve"
    DRAWING = "Input_Drawing"
    ONE_TAP = "Input_OneTap"

class GameplayMechanic(str, Enum):
    DIGGING_MINING = "Mechanic_Digging"
    VACUUM_SUCTION = "Mechanic_Vacuum"
    STACKING_CARRYING = "Mechanic_Stacking"
    BASE_EXPANSION = "Mechanic_BaseExpansion"
    PULL_PIN = "Mechanic_PullPin"
    GATE_RUNNER = "Mechanic_GateRunner"
    DRAW_TO_SAVE = "Mechanic_DrawToSave"
    MERGING = "Mechanic_Merging"
    SORTING_ORGANIZING = "Mechanic_Sorting"
    CRUSHING_DESTROYING = "Mechanic_Crushing"

class GameplayProp(str, Enum):
    # Hazards
    HAZARD_LAVA = "Prop_Hazard_Lava"
    HAZARD_SPIKES = "Prop_Hazard_Spikes"
    HAZARD_SAWS = "Prop_Hazard_Saws"
    # Modifiers
    MATH_GATES = "Prop_MathGates"
    EVOLUTION_DOOR = "Prop_EvolutionDoor"
    CONVEYOR_BELT = "Prop_ConveyorBelt"
    # Items
    MONEY_STACKS = "Prop_MoneyStacks"
    RESOURCE_NODES = "Prop_ResourceNodes"
    COLLECTIBLE_GEMS = "Prop_Collectible_Gems"
    REWARD_CHEST = "Prop_RewardChest"
    WEAPON_HELD = "Prop_Weapon"
    VEHICLE = "Prop_Vehicle"
    # Environment
    CROWD_SWARM = "Prop_CrowdSwarm"
    LOCKED_AREA_GRAY = "Prop_LockedArea"
    LIQUID_GENERIC = "Prop_Liquid_Generic"
    DEBRIS_TRASH = "Prop_Debris_Trash"

# ==========================================
# 3. PSYCHOLOGY & EMOTION LAYER
# ==========================================

class CharacterArchetype(str, Enum):
    STICKMAN = "Char_Stickman"
    NOOB = "Char_Noob"
    PRO = "Char_Pro"
    WORKER_MINER = "Char_Worker"
    MOM_VS_DAD = "Char_Mom_vs_Dad"
    DAMSEL = "Char_Damsel"
    BOSS_MONSTER = "Char_Boss"

class SatisfactionTrigger(str, Enum):
    CLEAN_MAP = "Satisfying_CleanMap"
    PERFECT_FIT = "Satisfying_PerfectFit"
    NUMBER_TICKER = "Satisfying_NumberTicker"
    SMOOTH_PHYSICS = "Satisfying_SmoothPhysics"
    ASMR_SOUND = "Satisfying_ASMR_Sound"

class EmotionTrigger(str, Enum):
    FRUSTRATION = "Emotion_Frustration"
    OCD_TRIGGER = "Emotion_OCD"
    POWER_FANTASY = "Emotion_Power"
    URGENCY = "Emotion_Urgency"
    CURIOSITY = "Emotion_Curiosity"

class FailType(str, Enum):
    LOGIC_FAIL = "Fail_Logic"
    SKILL_FAIL = "Fail_Skill"
    PHYSICS_FAIL = "Fail_Physics"
    STUCK_FAIL = "Fail_Stuck"

# ==========================================
# 4. MARKETING & UI LAYER
# ==========================================

class PointerStyle(str, Enum):
    REAL_HAND = "Pointer_RealHand"
    CARTOON_HAND = "Pointer_CartoonHand"
    ARROW_CURSOR = "Pointer_Arrow"
    GHOST_TOUCH = "Pointer_Ghost"

class TextHook(str, Enum):
    IQ_CHALLENGE = "Hook_IQ_Challenge"
    HARD_BAIT = "Hook_Hard_Bait"
    TUTORIAL_STEP = "Hook_Tutorial"
    EVOLUTION_NARRATIVE = "Hook_Evolution"
    TABOO_SHOCK = "Hook_Taboo"

class CTAElement(str, Enum):
    FAIL_RETRY = "CTA_Fail_Retry"
    INSTALL_BUTTON = "CTA_Install"
    FAKE_PLAYABLE = "CTA_FakePlayable"
    STORE_BADGE = "CTA_StoreBadge"

# ==========================================
# 5. AUDIO LAYER (NEW)
# ==========================================

class MusicGenre(str, Enum):
    EPIC_ORCHESTRAL = "Music_Epic_Orchestral"
    LOFI_CHILL = "Music_LoFi_Chill"
    ELECTRONIC_UPBEAT = "Music_Upbeat_EDM"
    EIGHT_BIT = "Music_8Bit"
    CARTOON_SLAPSTICK = "Music_Slapstick"
    SUSPENSE_HORROR = "Music_Suspense"
    VIRAL_TREND = "Music_Viral_Trend"
    SILENCE = "Music_Silence"

class SoundEffect(str, Enum):
    # Interaction
    COIN_COLLECT = "SFX_Coin_Jingle"
    UI_TAP_CLICK = "SFX_UI_Click"
    FAKE_NOTIFICATION = "SFX_Notification"
    LEVEL_UP = "SFX_LevelUp"
    # Action
    MECHANICAL_DRILL = "SFX_Drill_Loop"
    VACUUM_SUCTION = "SFX_Vacuum_Loop"
    LIQUID_SPLASH = "SFX_Liquid_Splash"
    WEAPON_SHOT = "SFX_Weapon_Shot"
    BUILDING_THUD = "SFX_Building_Pop"
    # Emotion
    ASMR_CRUNCH = "SFX_ASMR_Crunch"
    ASMR_SLIME = "SFX_ASMR_Slime"
    FAIL_BUZZER = "SFX_Fail_Buzzer"
    WIN_CHEER = "SFX_Win_Cheer"

class VoiceOverType(str, Enum):
    AI_GENERIC_TTS = "VO_AI_Generic"
    AI_TIKTOK_VOICE = "VO_AI_TikTok"
    REAL_HUMAN_PRO = "VO_Human_Pro"
    REAL_HUMAN_UGC = "VO_Human_UGC"
    NO_VOICEOVER = "VO_None"

class VoiceOverTone(str, Enum):
    EXCITED_HYPE = "VO_Tone_Excited"
    WHISPERING_ASMR = "VO_Tone_Whispering"
    ANGRY_FRUSTRATED = "VO_Tone_Angry"
    MOCKING = "VO_Tone_Mocking"
    CALM_EXPLANATORY = "VO_Tone_Calm"
    SCARED_PANIC = "VO_Tone_Scared"

class VoiceOverContent(str, Enum):
    TUTORIAL_GUIDE = "Content_Tutorial"
    FALSE_DIFFICULTY = "Content_HardBait"
    PLAYER_REACTION = "Content_Reaction"
    NARRATIVE_STORY = "Content_Story"
    PROMO_OFFER = "Content_Promo"


# ==========================================
# MASTER SCHEMA
# ==========================================

class CreativeAnalysis(BaseModel):
    """
    Comprehensive Multimodal Analysis of Mobile Game Ad Creative.
    Covers Visuals, Gameplay Mechanics, Psychology, Marketing, and Audio.
    """

    # --- Section 1: Visuals ---
    art_style: ArtStyle = Field(
        ..., 
        description=(
            "Classify the dominant visual style:\n"
            "- 'Style_2D_Flat': Zero depth, paper/flash look.\n"
            "- 'Style_2D_HandDrawn': Artistic, brush strokes.\n"
            "- 'Style_PixelArt': Visible retro pixels.\n"
            "- 'Style_3D_LowPoly': Sharp geometric edges, minimal detail.\n"
            "- 'Style_3D_Voxel': Cube-based blocks (Minecraft style).\n"
            "- 'Style_3D_Stylized': Smooth, rounded, high-fidelity cartoon (Mid-core).\n"
            "- 'Style_CelShaded': 3D with black comic-book outlines.\n"
            "- 'Style_Realistic': High-res textures, attempts photorealism.\n"
            "- 'Style_UGC_LiveAction': Real humans or video footage.\n"
            "- 'Style_Mixed_Reality': Game UI overlaid on real-world footage."
        )
    )
    camera_perspective: CameraPerspective = Field(
        ..., 
        description=(
            "Identify the camera angle:\n"
            "- 'Cam_Isometric': Angled top-down (~45°), grid-like view.\n"
            "- 'Cam_TopDown': Directly overhead (90°).\n"
            "- 'Cam_SideScroll': 2D view from the side (Platformer).\n"
            "- 'Cam_FirstPerson': View from character's eyes.\n"
            "- 'Cam_ThirdPerson': Camera follows behind the character's back.\n"
            "- 'Cam_SplitScreen': Two distinct video feeds shown simultaneously."
        )
    )
    visual_clutter: VisualClutterLevel = Field(
        ..., 
        description=(
            "Evaluate screen density:\n"
            "- 'Clutter_Low': Plain background, single focus object.\n"
            "- 'Clutter_Medium': Standard detailed environment.\n"
            "- 'Clutter_High': Screen filled with swarms, massive particle effects, or hundreds of items."
        )
    )
    color_palette: ColorPalette = Field(
        ..., 
        description=(
            "Determine the color psychology:\n"
            "- 'Palette_Warm_RedOrange': Dominant reds/oranges/yellows (Urgency/Danger).\n"
            "- 'Palette_Cool_BlueGreen': Dominant blues/greens (Calm/Strategy).\n"
            "- 'Palette_Neon': Glowing brights on dark backgrounds (Cyberpunk).\n"
            "- 'Palette_Pastel': Soft, desaturated colors (ASMR/Decor).\n"
            "- 'Palette_HighContrast': Stark Black/White/Red (Stickman style)."
        )
    )

    # --- Section 2: Gameplay Mechanics ---
    primary_genre: GameplayGenre = Field(
        ..., 
        description=(
            "Classify the core gameplay loop:\n"
            "- 'Genre_HC_Runner': Auto-forward movement, player steers L/R.\n"
            "- 'Genre_ArcadeIdle': Joystick movement, resource gathering, base building.\n"
            "- 'Genre_Puzzle_Logic': Static screen, pin pulling, drawing, or riddles.\n"
            "- 'Genre_Strategy_4X': Base management, army massing, top-down map.\n"
            "- 'Genre_Sim_Tycoon': Menu-heavy management, money counters.\n"
            "- 'Genre_Merge2': Dragging two identical items together on a grid."
        )
    )
    input_method: Optional[InputMethod] = Field(
        None, 
        description=(
            "Identify the interaction method shown:\n"
            "- 'Input_Joystick': Virtual circle pad or free 360 movement.\n"
            "- 'Input_TapTiming': Tapping at specific moments to jump/stop.\n"
            "- 'Input_DragSwerve': Finger holds screen to slide character L/R.\n"
            "- 'Input_Drawing': Finger draws visible lines on screen.\n"
            "- 'Input_OneTap': Simple tap interaction (Flappy Bird style)."
        )
    )
    mechanics_present: List[GameplayMechanic] = Field(
        default_factory=list,
        description=(
            "Select ALL specific actions visually detected:\n"
            "- 'Mechanic_Digging': Breaking blocks or removing soil/terrain.\n"
            "- 'Mechanic_Vacuum': Using a tool to suck up objects.\n"
            "- 'Mechanic_Stacking': Character carrying a vertical pile of items.\n"
            "- 'Mechanic_BaseExpansion': Unlocking new floor tiles/zones (often gray to colored).\n"
            "- 'Mechanic_PullPin': Sliding keys/pins to move fluids or objects.\n"
            "- 'Mechanic_GateRunner': Passing through gates with math (+, x, -).\n"
            "- 'Mechanic_DrawToSave': Drawing ink lines to shield a character.\n"
            "- 'Mechanic_Merging': Dragging two items together to form a new one.\n"
            "- 'Mechanic_Sorting': Organizing items by color or type into containers.\n"
            "- 'Mechanic_Crushing': Hydraulic press, shredding, or destroying items."
        )
    )
    props_detected: List[GameplayProp] = Field(
        default_factory=list,
        description=(
            "Identify specific game objects:\n"
            "- 'Prop_Hazard_Lava': Red/Orange liquid danger zones.\n"
            "- 'Prop_Hazard_Spikes': Stationary sharp obstacles.\n"
            "- 'Prop_Hazard_Saws': Moving circular saws or spinning blades.\n"
            "- 'Prop_MathGates': Translucent gates displaying math operations (+, x, /).\n"
            "- 'Prop_CrowdSwarm': Large groups of stickmen or units moving as a liquid mass.\n"
            "- 'Prop_EvolutionDoor': Gates labeled with years (1900->2000) or status (Poor->Rich).\n"
            "- 'Prop_MoneyStacks': Piles of cash, gold bars, or coins visibly sitting on the ground.\n"
            "- 'Prop_LockedArea': Grayed-out or silhouette zones waiting to be unlocked.\n"
            "- 'Prop_RewardChest': Treasure chests, gift boxes, or safes.\n"
            "- 'Prop_Collectible_Gems': Floating items like diamonds, stars, or keys.\n"
            "- 'Prop_Vehicle': Cars, tanks, or planes driven by the character.\n"
            "- 'Prop_Weapon': Held items like guns, swords, giant hammers, or bats.\n"
            "- 'Prop_ConveyorBelt': Moving floors transporting items.\n"
            "- 'Prop_ResourceNodes': Breakable environment objects like trees, rocks, or ore veins.\n"
            "- 'Prop_Liquid_Generic': Blue water, green acid, or purple slime (Distinct from Lava).\n"
            "- 'Prop_Debris_Trash': Scattered garbage, dust, or stains meant to be cleaned."
        )
    )
    
    # --- Section 3: Psychology ---
    character_archetype: Optional[CharacterArchetype] = Field(
        None, 
        description=(
            "Identify the protagonist type:\n"
            "- 'Char_Stickman': Generic, single-color figure.\n"
            "- 'Char_Noob': Character failing, looking confused, or dressed poorly.\n"
            "- 'Char_Pro': Character with high-level gear/skins playing well.\n"
            "- 'Char_Worker': Character with hardhat/tools (Drill/Idle games).\n"
            "- 'Char_Mom_vs_Dad': Two characters compared at the top of the screen.\n"
            "- 'Char_Damsel': Character in distress, tied up, or crying.\n"
            "- 'Char_Boss': Large enemy character."
        )
    )
    emotional_hooks: List[EmotionTrigger] = Field(
        default_factory=list, 
        description=(
            "Identify the psychological intent:\n"
            "- 'Emotion_Frustration': Player plays badly on purpose to annoy viewer.\n"
            "- 'Emotion_OCD': Slight misalignments or 'missed one spot' scenarios.\n"
            "- 'Emotion_Power': Effortlessly destroying massive amounts of enemies.\n"
            "- 'Emotion_Urgency': Countdowns, rising hazards, flashing red.\n"
            "- 'Emotion_Curiosity': Mystery boxes or 'What happens next?' hooks."
        )
    )
    satisfaction_factors: List[SatisfactionTrigger] = Field(
        default_factory=list,
        description=(
            "Identify satisfying elements:\n"
            "- 'Satisfying_CleanMap': Converting a dirty/foggy map to a clean one.\n"
            "- 'Satisfying_PerfectFit': Objects sliding perfectly into slots.\n"
            "- 'Satisfying_NumberTicker': Score/Money counters rolling up rapidly.\n"
            "- 'Satisfying_SmoothPhysics': Jelly-like movement or smooth stacking.\n"
            "- 'Satisfying_ASMR_Sound': Visuals implying crunching/slicing textures."
        )
    )
    fail_scenario: Optional[FailType] = Field(
        None, 
        description=(
            "If a fail occurs, categorize it:\n"
            "- 'Fail_Logic': Player makes an obviously wrong puzzle choice.\n"
            "- 'Fail_Skill': Player reacts too slowly or has bad aim.\n"
            "- 'Fail_Physics': A structure collapses or balance is lost.\n"
            "- 'Fail_Stuck': Player wanders aimlessly, unable to find the objective."
        )
    )

    # --- Section 4: Marketing/UI ---
    pointer_style: Optional[PointerStyle] = Field(
        None, 
        description=(
            "Identify the user guidance indicator:\n"
            "- 'Pointer_RealHand': Video footage of a human hand.\n"
            "- 'Pointer_CartoonHand': 2D vector graphic hand.\n"
            "- 'Pointer_3D_Hand': 3D model hand.\n"
            "- 'Pointer_Arrow': Mouse cursor or simple arrow.\n"
            "- 'Pointer_Ghost': Interaction happens without visible indicator."
        )
    )
    text_hooks: List[TextHook] = Field(
        default_factory=list, 
        description=(
            "Analyze text overlays:\n"
            "- 'Hook_IQ_Challenge': Claims of difficulty ('Only 1% pass').\n"
            "- 'Hook_Hard_Bait': Claims of specific failure ('I can't reach Pink').\n"
            "- 'Hook_Tutorial': Instructions ('Hold to dig').\n"
            "- 'Hook_Evolution': Progression narratives ('Lvl 1 vs Lvl 50').\n"
            "- 'Hook_Taboo': Shocking stories (Cheating, Divorce)."
        )
    )
    cta_elements: List[CTAElement] = Field(
        default_factory=list,
        description=(
            "Identify End Card elements:\n"
            "- 'CTA_Fail_Retry': 'Try Again' or 'Revive' prompt.\n"
            "- 'CTA_Install': Standard 'Download'/'Install' button.\n"
            "- 'CTA_FakePlayable': Prompt to play that redirects to store.\n"
            "- 'CTA_StoreBadge': Apple/Google store icons."
        )
    )
    ocr_text_raw: List[str] = Field(
        default_factory=list, 
        description="Extract exact raw text strings from overlays (e.g. 'Level 5', 'Failed!')."
    )

    # --- Section 5: Audio Analysis (Multimodal) ---
    music_genre: Optional[MusicGenre] = Field(
        None,
        description=(
            "Identify the background music style:\n"
            "- 'Music_Epic_Orchestral': Cinematic, war drums, RPG style.\n"
            "- 'Music_LoFi_Chill': Relaxed beats, soft piano.\n"
            "- 'Music_Upbeat_EDM': High energy, fast tempo electronic.\n"
            "- 'Music_8Bit': Retro, chiptune sounds.\n"
            "- 'Music_Slapstick': Tuba, pizzicato strings, goofy sounds (Fail ads).\n"
            "- 'Music_Suspense': Eerie drones, heartbeats.\n"
            "- 'Music_Viral_Trend': Recognizable TikTok/Meme audio loops.\n"
            "- 'Music_Silence': No music track present."
        )
    )
    sfx_detected: List[SoundEffect] = Field(
        default_factory=list,
        description=(
            "Select ALL distinct sound effects heard:\n"
            "- 'SFX_Coin_Jingle': High pitched tinkling/ching sounds.\n"
            "- 'SFX_UI_Click': Standard button sounds.\n"
            "- 'SFX_Notification': Fake message alerts (ding/vibration).\n"
            "- 'SFX_LevelUp': Ascending chime or fanfare.\n"
            "- 'SFX_Drill_Loop': Constant buzzing/grinding mechanics.\n"
            "- 'SFX_Vacuum_Loop': Continuous air suction noise.\n"
            "- 'SFX_Liquid_Splash': Water, slime, or mud sounds.\n"
            "- 'SFX_Weapon_Shot': Gunfire, sword swings, laser blasts.\n"
            "- 'SFX_Building_Pop': Pop/Thud sound when a building completes.\n"
            "- 'SFX_ASMR_Crunch': Crushing dry items, breaking glass.\n"
            "- 'SFX_Fail_Buzzer': 'Womp womp', buzzer, or glass breaking."
        )
    )
    voiceover_type: Optional[VoiceOverType] = Field(
        None,
        description=(
            "Classify the speaker's audio quality:\n"
            "- 'VO_AI_Generic': Standard robotic text-to-speech.\n"
            "- 'VO_AI_TikTok': The specific, upbeat 'Lady' voice common on TikTok.\n"
            "- 'VO_Human_Pro': Studio quality, radio-announcer voice.\n"
            "- 'VO_Human_UGC': Amateur audio quality, likely recorded on phone.\n"
            "- 'VO_None': No voiceover present."
        )
    )
    voiceover_tone: Optional[VoiceOverTone] = Field(
        None,
        description=(
            "Detect the emotional intent of the speaker:\n"
            "- 'VO_Tone_Excited': High energy, shouting, fast paced.\n"
            "- 'VO_Tone_Whispering': Very quiet, close to mic (ASMR).\n"
            "- 'VO_Tone_Angry': Yelling, complaining about difficulty.\n"
            "- 'VO_Tone_Mocking': Sarcastic, making fun of the player.\n"
            "- 'VO_Tone_Calm': Neutral, tutorial style.\n"
            "- 'VO_Tone_Scared': Screaming, reacting to horror."
        )
    )
    voiceover_content_category: Optional[VoiceOverContent] = Field(
        None,
        description=(
            "Categorize the topic being spoken about:\n"
            "- 'Content_Tutorial': Guides like 'Drag to move'.\n"
            "- 'Content_HardBait': Complaints like 'I can't reach pink'.\n"
            "- 'Content_Reaction': Outbursts like 'Oh my god!'.\n"
            "- 'Content_Story': Narratives like 'He cheated on me'.\n"
            "- 'Content_Promo': Offers like 'Download now'."
        )
    )
    transcription_text: str = Field(
        default="",
        description="Verbatim text transcription of any spoken language."
    )

    # --- Section 6: AI Inference ---
    is_fake_gameplay: bool = Field(
        ..., 
        description="TRUE if gameplay (e.g. Pull Pin) seems unrelated to the likely core app genre (e.g. Strategy). FALSE if gameplay looks authentic."
    )
    likely_target_audience: str = Field(
        ...,
        description="Inferred audience based on visuals (e.g. 'Children', 'Casual Adult', 'Hardcore Gamer')."
    )
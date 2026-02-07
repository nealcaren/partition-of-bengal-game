from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

START_SCENE_ID = "opening_decision"


SCENES: Dict[str, Dict[str, Any]] = {
    "opening_decision": {
        "date": "1905-08-12",
        "narration": (
            "**Your Office, Viceregal Lodge — Morning**\n\n"
            "The Partition will be announced in October, but Calcutta already hums with rumor. "
            "On your desk sit three files and an intelligence note, each demanding a different kind of statecraft. "
            "Commissioner Bamfield wants immediate arrests of agitators. Surendranath Banerjee requests an audience "
            "to keep protest constitutional. The Commerce Department proposes a grant to Bengali textile mills to blunt "
            "the swadeshi boycott. Your deputy suggests discreet intelligence gathering before you commit to any course.\n\n"
            "Outside your window, trams clatter and the presses at Bow Bazar begin to roll. "
            "Within weeks, the city will learn the province is to be split. "
            "Your first move will set the tone for everything that follows."
        ),
        "learned": (
            "Early colonial decisions often mixed coercion, consultation, and economic policy. "
            "Each signal shaped how moderates and radicals interpreted the Raj's intentions."
        ),
        "options": [
            {
                "id": "arrest_warrants",
                "label": "Authorize the arrest warrants and disrupt the radical committees before they meet.",
                "effects": {"local_stability": 5, "legitimacy": -5, "swadeshi_momentum": 5, "reputation": 4},
                "set_flags": ["crackdown"],
                "next": "pre_partition_rumors",
            },
            {
                "id": "meet_banerjee",
                "label": "Grant Banerjee an immediate audience and ask for a constitutional petition path.",
                "effects": {"legitimacy": 7, "local_stability": 2, "swadeshi_momentum": -2, "reputation": -2},
                "set_flags": ["moderate_outreach"],
                "next": "pre_partition_rumors",
            },
            {
                "id": "textile_grant",
                "label": "Approve the textile grant and frame it as support for local industry.",
                "effects": {"legitimacy": 3, "local_stability": 2, "swadeshi_momentum": -4, "reputation": 1},
                "set_flags": ["economic_concession"],
                "next": "pre_partition_rumors",
            },
            {
                "id": "dispatch_intel",
                "label": "Send a trusted aide to map the committees and report back quietly.",
                "effects": {"local_stability": 1, "legitimacy": 0, "swadeshi_momentum": -1, "reputation": 0},
                "set_flags": ["intel_network"],
                "next": "pre_partition_rumors",
            },
        ],
    },
    "pre_partition_rumors": {
        "date": "1905-09-05",
        "variants": [
            {
                "requires_flags": ["crackdown"],
                "narration": (
                    "The arrests ripple through College Square. Editors call the warrants a proof of divide-and-rule. "
                    "Moderates bristle at the spectacle, while radicals use the names to recruit. "
                    "Your telegrams report a brief lull in street meetings, but the boycotters are already planning "
                    "their first bonfires of foreign cloth.\n\n"
                    "London urges firmness. Calcutta's business leaders urge calm. "
                    "With the formal proclamation weeks away, the question is whether you double down or recalibrate."
                ),
                "learned": (
                    "Preemptive repression can buy short-term stability but often fuels the legitimacy crisis "
                    "that radicals exploit."
                ),
            },
            {
                "requires_flags": ["moderate_outreach"],
                "narration": (
                    "Banerjee leaves your office with cautious optimism. His papers praise constitutional protest, "
                    "yet radicals accuse him of bargaining with the Raj. "
                    "Petitions circulate through the bhadralok circles, and the bazaars buzz with competing rumors "
                    "about what the Partition will mean.\n\n"
                    "The police report fewer arrests but more pamphlets. "
                    "With October approaching, you must decide how visible your posture will be."
                ),
                "learned": (
                    "Engaging moderates can lower immediate tensions, but it risks pushing radicals to seek "
                    "their own momentum outside constitutional channels."
                ),
            },
            {
                "narration": (
                    "Rumor outpaces fact. The vernacular press treats the Partition as certain, while "
                    "the English-language papers insist it is administrative reform. "
                    "Petitions circulate, secret committees meet, and merchants ask whether the swadeshi boycott "
                    "will hit the bazaars before winter.\n\n"
                    "You have a narrow window to shape expectations before the formal proclamation lands."
                ),
                "learned": (
                    "Ambiguity in colonial policy often invited competing interpretations, which could harden "
                    "into organized resistance."
                ),
            },
        ],
        "option_sets": [
            {
                "requires_flags": ["crackdown"],
                "options": [
                    {
                        "id": "double_down_arrests",
                        "label": "Expand arrests and invoke Section 144 to prevent public meetings.",
                        "effects": {"local_stability": 4, "legitimacy": -6, "swadeshi_momentum": 6, "reputation": 3},
                        "set_flags": ["hardline"],
                        "next": "partition_proclaimed",
                    },
                    {
                        "id": "release_moderates",
                        "label": "Release minor detainees and open a petition channel through Banerjee.",
                        "effects": {"legitimacy": 5, "local_stability": -1, "swadeshi_momentum": -2, "reputation": -1},
                        "set_flags": ["moderate_outreach"],
                        "next": "partition_proclaimed",
                    },
                    {
                        "id": "announce_grants",
                        "label": "Announce textile grants and promise procurement contracts for local mills.",
                        "effects": {"legitimacy": 2, "local_stability": 1, "swadeshi_momentum": -3, "reputation": 1},
                        "set_flags": ["economic_concession"],
                        "next": "partition_proclaimed",
                    },
                    {
                        "id": "expand_cid",
                        "label": "Expand CID surveillance and build dossiers on organizers.",
                        "effects": {"local_stability": 2, "legitimacy": -1, "swadeshi_momentum": -1, "reputation": 0},
                        "set_flags": ["intel_network"],
                        "next": "partition_proclaimed",
                    },
                ],
            },
            {
                "options": [
                    {
                        "id": "limited_section_144",
                        "label": "Impose limited restrictions on mass meetings and keep police visible.",
                        "effects": {"local_stability": 3, "legitimacy": -2, "swadeshi_momentum": 2, "reputation": 2},
                        "set_flags": ["hardline"],
                        "next": "partition_proclaimed",
                    },
                    {
                        "id": "moderate_council",
                        "label": "Convene a council of moderates to draft a formal petition.",
                        "effects": {"legitimacy": 6, "local_stability": 1, "swadeshi_momentum": -3, "reputation": -2},
                        "set_flags": ["moderate_outreach"],
                        "next": "partition_proclaimed",
                    },
                    {
                        "id": "economic_stimulus",
                        "label": "Approve grants and relief contracts to cushion commercial backlash.",
                        "effects": {"legitimacy": 3, "local_stability": 2, "swadeshi_momentum": -4, "reputation": 1},
                        "set_flags": ["economic_concession"],
                        "next": "partition_proclaimed",
                    },
                    {
                        "id": "covert_surveillance",
                        "label": "Order discreet surveillance of swadeshi committees.",
                        "effects": {"local_stability": 2, "legitimacy": 0, "swadeshi_momentum": -1, "reputation": 0},
                        "set_flags": ["intel_network"],
                        "next": "partition_proclaimed",
                    },
                ],
            },
        ],
    },
    "partition_proclaimed": {
        "date": "1905-10-16",
        "narration": (
            "The proclamation arrives. In Calcutta, the streets churn with protest; in Dacca, loyalists "
            "offer garlands to the new provincial capital. The press calls it Banga Bhanga, the breaking of Bengal. "
            "Boycott pickets gather outside cloth shops, and students march with black badges.\n\n"
            "The Governor asks whether to enforce Section 144 and ban gatherings. "
            "Merchants warn that a heavy hand will freeze trade. Muslim elites in the east quietly press "
            "for reassurance that their province will receive funds and posts. "
            "Your response will be read as the first test of the new order."
        ),
        "learned": (
            "The proclamation amplified existing divides: Hindu nationalist anger, Muslim loyalist hopes, "
            "and British anxieties about order."
        ),
        "options": [
            {
                "id": "ban_rallies",
                "label": "Enforce Section 144 and ban rallies in Calcutta for the next fortnight.",
                "effects": {"local_stability": 4, "legitimacy": -5, "swadeshi_momentum": 4, "reputation": 3},
                "set_flags": ["hardline"],
                "next": "boycott_wave",
            },
            {
                "id": "allow_processions",
                "label": "Permit peaceful processions under police escort and avoid mass arrests.",
                "effects": {"legitimacy": 4, "local_stability": -1, "swadeshi_momentum": 2, "reputation": -1},
                "set_flags": ["moderate_outreach"],
                "next": "boycott_wave",
            },
            {
                "id": "symbolic_concessions",
                "label": "Announce scholarships and consultative seats as symbolic concessions.",
                "effects": {"legitimacy": 3, "local_stability": 1, "swadeshi_momentum": -2, "reputation": 0},
                "set_flags": ["economic_concession"],
                "next": "boycott_wave",
            },
            {
                "id": "meet_muslim_elites",
                "label": "Publicly meet Nawab Salimullah and promise attention to eastern districts.",
                "effects": {"legitimacy": 1, "local_stability": 1, "swadeshi_momentum": 1, "reputation": 2},
                "set_flags": ["muslim_loyalists"],
                "next": "boycott_wave",
            },
        ],
    },
    "boycott_wave": {
        "date": "1906-01-20",
        "variants": [
            {
                "requires_flags": ["hardline"],
                "narration": (
                    "The swadeshi boycott takes on the energy of a crusade. Bonfires of foreign cloth burn "
                    "near College Square, and pickets line the market gates. "
                    "Your earlier restrictions are now cited as proof that constitutional methods are futile. "
                    "Meanwhile, merchants plead for protection from crowd pressure.\n\n"
                    "You must choose whether to clamp down, co-opt the movement, or redirect it through "
                    "moderate channels."
                ),
            },
            {
                "requires_flags": ["moderate_outreach"],
                "narration": (
                    "Moderate petitions still circulate, but the streets tell a different story. "
                    "Swadeshi organizers declare boycott a moral duty, and students treat picketing as a rite of passage. "
                    "Your meetings with moderates slow some agitation, yet radicals fill the vacuum with "
                    "fiery speeches and boycotts.\n\n"
                    "The next move will decide whether the boycott hardens or softens."
                ),
            },
            {
                "narration": (
                    "Swadeshi momentum spreads beyond Calcutta into smaller towns. "
                    "Picket lines form outside foreign cloth shops, and merchants ask for protection. "
                    "Reports note a mix of disciplined boycotts and occasional intimidation.\n\n"
                    "You need a policy that either breaks the pickets, absorbs them into policy, or reframes the struggle."
                ),
            },
        ],
        "learned": (
            "Swadeshi was both an economic tactic and a moral campaign. "
            "State responses could suppress, co-opt, or unintentionally intensify it."
        ),
        "options": [
            {
                "id": "crackdown_pickets",
                "label": "Order arrests of picket leaders and prosecute sedition in the press.",
                "effects": {"local_stability": 3, "legitimacy": -4, "swadeshi_momentum": 5, "reputation": 2},
                "set_flags": ["hardline"],
                "next": "municipal_strain",
            },
            {
                "id": "support_industry",
                "label": "Expand grants to mills and promote local procurement contracts.",
                "effects": {"legitimacy": 2, "local_stability": 1, "swadeshi_momentum": -3, "reputation": 1},
                "set_flags": ["economic_concession"],
                "next": "municipal_strain",
            },
            {
                "id": "moderate_channels",
                "label": "Invite moderates to issue a joint appeal for constitutional protest.",
                "effects": {"legitimacy": 5, "local_stability": 1, "swadeshi_momentum": -2, "reputation": -2},
                "set_flags": ["moderate_outreach"],
                "next": "municipal_strain",
            },
            {
                "id": "intel_infiltration",
                "label": "Infiltrate swadeshi committees and quietly disrupt their logistics.",
                "effects": {"local_stability": 2, "legitimacy": -1, "swadeshi_momentum": -2, "reputation": 0},
                "set_flags": ["intel_network"],
                "next": "municipal_strain",
            },
        ],
    },
    "municipal_strain": {
        "date": "1906-06-15",
        "variants": [
            {
                "requires_flags": ["economic_concession"],
                "narration": (
                    "The textile grants keep some mills open, but boycotters accuse you of bribery. "
                    "Municipal finances strain under the cost of policing and relief. "
                    "Strikes flicker in the jute mills, and students boycott classes in sympathy.\n\n"
                    "You need a policy that stabilizes the streets without surrendering authority."
                ),
            },
            {
                "narration": (
                    "Municipal budgets strain under police overtime and disrupted trade. "
                    "Strikes flicker in the jute mills, and student leaders call for a day of fasting and protest. "
                    "Merchants ask for stronger protection, while moderate leaders warn that another heavy-handed move "
                    "will push wavering elites toward the radicals.\n\n"
                    "Your next decision will shape the mid-year tempo of the movement."
                ),
            },
        ],
        "learned": (
            "Economic concessions could soften discontent but also be framed as manipulation. "
            "Municipal governance became a key arena for contesting legitimacy."
        ),
        "options": [
            {
                "id": "press_censorship",
                "label": "Invoke press restrictions and shut down the most incendiary papers.",
                "effects": {"local_stability": 3, "legitimacy": -6, "swadeshi_momentum": 4, "reputation": 2},
                "set_flags": ["hardline"],
                "next": "muslim_league",
            },
            {
                "id": "education_concessions",
                "label": "Launch scholarships and educational grants for both communities.",
                "effects": {"legitimacy": 4, "local_stability": 1, "swadeshi_momentum": -2, "reputation": 0},
                "set_flags": ["economic_concession"],
                "next": "muslim_league",
            },
            {
                "id": "municipal_devolution",
                "label": "Give municipal councils more authority over relief and policing priorities.",
                "effects": {"legitimacy": 3, "local_stability": 1, "swadeshi_momentum": -1, "reputation": -1},
                "set_flags": ["moderate_outreach"],
                "next": "muslim_league",
            },
            {
                "id": "split_gains",
                "label": "Direct extra funds to eastern districts and highlight loyalist cooperation.",
                "effects": {"legitimacy": 1, "local_stability": 1, "swadeshi_momentum": 1, "reputation": 2},
                "set_flags": ["muslim_loyalists"],
                "next": "muslim_league",
            },
        ],
    },
    "muslim_league": {
        "date": "1906-12-30",
        "variants": [
            {
                "requires_flags": ["muslim_loyalists"],
                "narration": (
                    "At Ahsan Manzil in Dacca, Nawab Salimullah hosts delegates who found the All-India Muslim League. "
                    "Your earlier outreach is remembered, and loyalist speeches praise the Raj for creating a Muslim-majority province. "
                    "Hindu leaders in Calcutta read the news as proof of divide-and-rule.\n\n"
                    "How you respond will shape communal politics for years to come."
                ),
            },
            {
                "narration": (
                    "At Ahsan Manzil in Dacca, Nawab Salimullah hosts delegates who found the All-India Muslim League. "
                    "They pledge loyalty to the Raj and argue that Muslim interests need distinct protection. "
                    "Hindu leaders in Calcutta read the news as proof of divide-and-rule.\n\n"
                    "Your response will signal whether you lean into communal balancing or seek a broader equilibrium."
                ),
            },
        ],
        "learned": (
            "The Muslim League's formation marked a new phase of organized communal politics, "
            "complicating nationalist unity."
        ),
        "options": [
            {
                "id": "encourage_league",
                "label": "Attend the League gathering and praise loyal cooperation in the east.",
                "effects": {"local_stability": 2, "legitimacy": -2, "swadeshi_momentum": 2, "reputation": 3},
                "set_flags": ["muslim_loyalists"],
                "next": "radicalization",
            },
            {
                "id": "balance_statement",
                "label": "Issue a balanced statement and meet Congress moderates the same week.",
                "effects": {"legitimacy": 3, "local_stability": 1, "swadeshi_momentum": -1, "reputation": 0},
                "set_flags": ["moderate_outreach"],
                "next": "radicalization",
            },
            {
                "id": "neutral_distance",
                "label": "Keep official distance and focus on law and order messaging.",
                "effects": {"local_stability": 2, "legitimacy": -1, "swadeshi_momentum": 1, "reputation": 1},
                "next": "radicalization",
            },
            {
                "id": "joint_council",
                "label": "Propose a joint Hindu-Muslim advisory council for provincial policy.",
                "effects": {"legitimacy": 4, "local_stability": 1, "swadeshi_momentum": -1, "reputation": -1},
                "set_flags": ["moderate_outreach"],
                "next": "radicalization",
            },
        ],
    },
    "radicalization": {
        "date": "1907-07-15",
        "variants": [
            {
                "requires_flags": ["hardline"],
                "narration": (
                    "Secret societies proliferate. The Anushilan Samiti circulates manuals and drills youths in secrecy. "
                    "Your harsher measures have curbed open rallies but pushed the movement underground. "
                    "Reports mention crude bomb-making experiments and plans against magistrates.\n\n"
                    "You must decide whether to widen the net or try to split radicals from moderates."
                ),
            },
            {
                "narration": (
                    "Secret societies proliferate. The Anushilan Samiti circulates manuals and drills youths in secrecy. "
                    "Moderate leaders warn that punitive policies could make martyrs of the radicals. "
                    "Police ask for authority to act before an attack occurs.\n\n"
                    "The next move balances preemption against political fallout."
                ),
            },
        ],
        "learned": (
            "As repression grows, movements can shift from public protest to clandestine violence, "
            "forcing states to choose between broad crackdowns and targeted intelligence."
        ),
        "options": [
            {
                "id": "broad_crackdown",
                "label": "Authorize mass arrests of suspected radicals across Bengal.",
                "effects": {"local_stability": 4, "legitimacy": -7, "swadeshi_momentum": 6, "reputation": 3},
                "set_flags": ["hardline"],
                "next": "bombing",
            },
            {
                "id": "targeted_surveillance",
                "label": "Use intelligence to make targeted arrests and avoid mass roundups.",
                "effects": {"local_stability": 3, "legitimacy": -2, "swadeshi_momentum": 1, "reputation": 1},
                "set_flags": ["intel_network"],
                "next": "bombing",
            },
            {
                "id": "partition_review",
                "label": "Promise a formal review of the partition within two years.",
                "effects": {"legitimacy": 5, "local_stability": 0, "swadeshi_momentum": -3, "reputation": -2},
                "set_flags": ["moderate_outreach"],
                "next": "bombing",
            },
            {
                "id": "public_works",
                "label": "Launch public works programs to absorb youth and ease unrest.",
                "effects": {"legitimacy": 3, "local_stability": 2, "swadeshi_momentum": -2, "reputation": 1},
                "set_flags": ["economic_concession"],
                "next": "bombing",
            },
        ],
    },
    "bombing": {
        "date": "1908-04-30",
        "variants": [
            {
                "requires_flags": ["intel_network"],
                "narration": (
                    "Your intelligence officers warned of a plot, but the bomb still fell at Muzaffarpur. "
                    "Two British women are killed when the device strikes the wrong carriage. "
                    "The press erupts, and calls for decisive action flood your desk.\n\n"
                    "You must respond to the attack without igniting wider revolt."
                ),
            },
            {
                "narration": (
                    "A bomb explodes at Muzaffarpur, aimed at Magistrate Kingsford. "
                    "Two British women are killed when the device strikes the wrong carriage. "
                    "The press erupts, and calls for decisive action flood your desk.\n\n"
                    "You must respond to the attack without igniting wider revolt."
                ),
            },
        ],
        "learned": (
            "Political violence hardened British resolve but also deepened public sympathy for radicals in some circles."
        ),
        "options": [
            {
                "id": "emergency_powers",
                "label": "Declare emergency powers and authorize sweeping raids.",
                "effects": {"local_stability": 5, "legitimacy": -6, "swadeshi_momentum": 5, "reputation": 2},
                "set_flags": ["hardline"],
                "next": "tilak_trial",
            },
            {
                "id": "judicial_process",
                "label": "Promise swift but transparent trials and avoid collective punishment.",
                "effects": {"legitimacy": 4, "local_stability": -1, "swadeshi_momentum": 1, "reputation": -1},
                "set_flags": ["moderate_outreach"],
                "next": "tilak_trial",
            },
            {
                "id": "protect_moderates",
                "label": "Publicly separate radicals from moderates and meet Banerjee again.",
                "effects": {"legitimacy": 4, "local_stability": 0, "swadeshi_momentum": -2, "reputation": -1},
                "set_flags": ["moderate_outreach"],
                "next": "tilak_trial",
            },
            {
                "id": "aid_relief",
                "label": "Offer relief to victims and appeal for calm across the province.",
                "effects": {"legitimacy": 2, "local_stability": 1, "swadeshi_momentum": -1, "reputation": 0},
                "next": "tilak_trial",
            },
        ],
    },
    "tilak_trial": {
        "date": "1908-07-22",
        "narration": (
            "Bal Tilak is convicted of sedition and sentenced to transportation. "
            "Moderate leaders plead for calm, while radicals cast him as a martyr. "
            "The press in Bombay and Calcutta runs on anger and rumor. "
            "London wants reassurance that the Raj remains in control.\n\n"
            "Your response will set the tone for the final months of this crisis."
        ),
        "learned": (
            "Sedition trials often intensified polarization, with moderates caught between loyalty and popular anger."
        ),
        "options": [
            {
                "id": "support_conviction",
                "label": "Publicly praise the conviction and reinforce sedition enforcement.",
                "effects": {"local_stability": 3, "legitimacy": -5, "swadeshi_momentum": 4, "reputation": 2},
                "set_flags": ["hardline"],
                "next": "end_1908",
            },
            {
                "id": "quiet_restraint",
                "label": "Avoid triumphalism and urge calm in official statements.",
                "effects": {"legitimacy": 2, "local_stability": 1, "swadeshi_momentum": -1, "reputation": 0},
                "set_flags": ["moderate_outreach"],
                "next": "end_1908",
            },
            {
                "id": "limited_reforms",
                "label": "Pair the verdict with limited reforms in education and consultation.",
                "effects": {"legitimacy": 4, "local_stability": 0, "swadeshi_momentum": -2, "reputation": -1},
                "set_flags": ["economic_concession"],
                "next": "end_1908",
            },
            {
                "id": "military_reassurance",
                "label": "Deploy troops in Calcutta as a visible signal of control.",
                "effects": {"local_stability": 3, "legitimacy": -3, "swadeshi_momentum": 2, "reputation": 2},
                "set_flags": ["hardline"],
                "next": "end_1908",
            },
        ],
    },
    "end_1908": {
        "date": "1908-12-31",
        "narration": (
            "The year closes with Bengal still uneasy. "
            "Protests have not vanished, but neither has the administration collapsed. "
            "The files on your desk now look less like emergencies and more like a permanent condition: "
            "boycotts, petitions, loyalist lobbying, and quiet intelligence work.\n\n"
            "History will remember that the Partition was annulled in 1911, "
            "but your tenure is judged on whether you kept the province governable through 1908."
        ),
        "learned": (
            "By 1908, the crisis had hardened into long-term political structures: "
            "boycott networks, communal organizations, and intensified debates about imperial legitimacy."
        ),
        "options": [],
    },
}

OUTCOME_TEXT = {
    "legitimacy_collapse": (
        "Your credibility with elites and officials has shattered. "
        "Petitions no longer reach your desk, and the press treats every proclamation as empty. "
        "London recalls you for failing to preserve the Raj's authority."
    ),
    "stability_collapse": (
        "Riots, strikes, and daily disruptions overwhelm the machinery of governance. "
        "The administration can no longer guarantee basic order, and your post is terminated."
    ),
    "swadeshi_unstoppable": (
        "The boycott has become unstoppable. Merchants refuse British cloth, students organize daily pickets, "
        "and even moderate leaders can no longer contain the movement. "
        "The Partition becomes politically untenable under your watch."
    ),
    "survived": (
        "You have held the line through the end of 1908. "
        "The crisis persists, but the province remains governable, and your position survives."
    ),
}


def parse_date(date_str: Optional[str]):
    if not date_str:
        return None
    try:
        return datetime.strptime(str(date_str), "%Y-%m-%d").date()
    except ValueError:
        return None


def clamp(value: int | float, lo: int = 0, hi: int = 100) -> int:
    return max(lo, min(int(round(value)), hi))


def _flag_set(state: Dict[str, Any]) -> set[str]:
    return set(state.get("flags") or [])


def _matches_conditions(item: Dict[str, Any], flags: set[str], last_action: Optional[str]) -> bool:
    requires_flags = set(item.get("requires_flags") or [])
    forbids_flags = set(item.get("forbids_flags") or [])
    requires_last_action = set(item.get("requires_last_action") or [])
    if requires_flags and not requires_flags.issubset(flags):
        return False
    if forbids_flags and forbids_flags.intersection(flags):
        return False
    if requires_last_action and (last_action not in requires_last_action):
        return False
    return True


def select_variant(scene: Dict[str, Any], state: Dict[str, Any]) -> Dict[str, Any]:
    variants = scene.get("variants") or []
    if not variants:
        return {}
    flags = _flag_set(state)
    last_action = state.get("last_action")
    for variant in variants:
        if _matches_conditions(variant, flags, last_action):
            return variant
    return variants[-1]


def select_options(scene: Dict[str, Any], state: Dict[str, Any]) -> List[Dict[str, Any]]:
    option_sets = scene.get("option_sets") or []
    flags = _flag_set(state)
    last_action = state.get("last_action")
    for opt_set in option_sets:
        if _matches_conditions(opt_set, flags, last_action):
            options = opt_set.get("options") or []
            return [opt for opt in options if _matches_conditions(opt, flags, last_action)]
    options = scene.get("options") or []
    return [opt for opt in options if _matches_conditions(opt, flags, last_action)]


def ensure_scene_date(state: Dict[str, Any], scene_id: str) -> None:
    scene = SCENES.get(scene_id)
    if not scene:
        return
    scene_date = parse_date(scene.get("date"))
    current_date = parse_date(state.get("date"))
    if scene_date and (not current_date or scene_date > current_date):
        state["date"] = scene_date.strftime("%Y-%m-%d")


def build_scene_response(scene_id: str, state: Dict[str, Any]) -> Dict[str, Any]:
    scene = SCENES.get(scene_id)
    if not scene:
        return {
            "narration": "The file cabinet is empty; no further instructions are available.",
            "options": [],
            "learned": "",
        }
    ensure_scene_date(state, scene_id)
    variant = select_variant(scene, state)
    narration = variant.get("narration") or scene.get("narration") or ""
    learned = variant.get("learned") or scene.get("learned") or ""
    options = select_options(scene, state)
    return {
        "narration": narration,
        "options": [{"id": opt["id"], "label": opt["label"]} for opt in options],
        "learned": learned,
    }


def apply_option(state: Dict[str, Any], option: Dict[str, Any]) -> None:
    effects = option.get("effects") or {}
    for key, delta in effects.items():
        current = state.get(key, 0)
        if isinstance(current, (int, float)):
            state[key] = clamp(current + delta)
    flags = _flag_set(state)
    for flag in option.get("set_flags") or []:
        flags.add(flag)
    for flag in option.get("clear_flags") or []:
        flags.discard(flag)
    state["flags"] = sorted(flags)


def find_option(scene_id: str, choice_id: str, state: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    scene = SCENES.get(scene_id)
    if not scene:
        return None
    options = select_options(scene, state)
    for option in options:
        if option.get("id") == choice_id:
            return option
    return None


def build_outcome_narration(reason: str) -> str:
    return OUTCOME_TEXT.get(reason, "")

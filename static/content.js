(function () {
  const OPENING_VIGNETTE = {
    pages: [
      {
        title: "Calcutta, August 1905 -- 6:47 AM",
        text: "The telegram arrived at dawn:\n\n**PARTITION ANNOUNCEMENT CONFIRMED OCTOBER 16 STOP EXPECT VIGOROUS NATIVE RESPONSE STOP CURZON DIRECTS YOU PREPARE GROUND STOP DISCRETION YOURS STOP**\n\nYour bearer has already placed three files on your breakfast table:\n\n**URGENT** -- Police Commissioner seeks approval for preemptive arrests of \"seditious elements\"  \n**PENDING** -- Surendranath Banerjee requests meeting re: constitutional petition  \n**COMMERCIAL** -- Proposal to fund Bengali textile mills (undercut swadeshi appeal?)\n\nOutside your window, Calcutta is waking. 78 million Bengalis are about to learn their province will be split in two.\n\nYou have eight weeks to shape how they receive the news.",
        button: "Open the files",
      },
      {
        title: "The Intelligence Report",
        text: "You break the seal on the police file. Commissioner Bamfield's handwriting is cramped, urgent:\n\n\"College Square organizing committees growing bolder. Bipin Chandra Pal addressed 3,000 last Thursday -- 'foreign cloth is a chain around our necks.' Aurobindo Ghose's journal publishes bomb-making chemistry alongside Bankim's hymns. We have names. Recommend immediate action.\"\n\nClipped to the back: twelve arrest warrants, unsigned.\n\nBut there's a second memo, from your deputy:\n\n\"Sir -- Banerjee's moderates control Congress. Arrest their rivals and we make martyrs. Banerjee himself has requested audience. He'll propose petitions, deputations, constitutional methods. We can channel dissent through him -- if we don't poison the well first.\"\n\nTwo paths. The police want preemptive strikes. Your deputy wants to co-opt the moderates.\n\nAnd beneath both memos, a note in Lord Curzon's hand: \"The Partition is administrative necessity. But Bengal produces poets and revolutionaries in equal measure. Steady hand required.\"",
        button: "Continue",
      },
      {
        title: "The Chessboard",
        text: "On your desk: a map of Bengal marked in three colors.\n\n**Red pins** -- Hindu nationalist strongholds. Calcutta, Dacca University, the vernacular press. Here they're calling the Partition *Banga Bhanga* -- \"the Breaking of Bengal.\" They see cultural dismemberment.\n\n**Green pins** -- Muslim-majority districts in the east. At Ahsan Manzil, Nawab Salimullah has quietly welcomed the news. A Muslim-majority province means canal funding, educational grants, political weight. Your intelligence notes: \"Muslim League forming to protect community interests should Congress radicalize.\"\n\n**Blue pins** -- British commercial interests. Manchester textile importers, Calcutta jute traders, the Port Trust. They need stability. Boycotts mean lost revenue.\n\nThe Partition will split Bengal into:\n- **Eastern Bengal & Assam** -- Muslim-majority, capital at Dacca\n- **Bengal** -- Hindu-majority, centered on Calcutta\n\nOn paper, it's about governing 78 million people more efficiently. Revenue collection. Administrative reach.\n\nBut you've read the internal memos. The ones that don't mention efficiency at all.",
        button: "Continue",
      },
      {
        title: "What London Isn't Saying",
        text: "A dispatch from the India Office, marked *CONFIDENTIAL*:\n\n\"Bengali Hindu elite have grown overly influential -- dominate civil service posts, control vernacular press, lead Congress agitation. Partition will dilute this concentration. A Muslim-majority province provides natural counterweight. Elementary prudence.\"\n\nThey don't use the phrase \"divide and rule.\" They don't have to.\n\nYou close the file. Outside, the first hawkers are setting up in College Square. The *Amrita Bazar Patrika* will hit the streets in an hour. Surendranath Banerjee is probably already drafting his petition.\n\nAnd in some basement printing press, Aurobindo Ghose is writing tomorrow's editorial.\n\nThe question isn't whether Bengal will resist. The question is what form that resistance takes -- and whether you can control it.",
        button: "Continue",
      },
      {
        title: "Your Position",
        text: "You are the Viceroy's private secretary. Not an exalted post -- but an essential one.\n\nCurzon makes policy. You make it work.\n\nThat means:\n- Deciding which petitions reach the Viceroy's desk\n- Recommending when to deploy police -- or when to hold back\n- Allocating discretionary funds for grants, infrastructure, concessions\n- Signaling to Indian elites who is in favor, who is suspect\n\nA successful transition means advancement. Perhaps the governorship of Bombay. Recognition in London.\n\nA botched one means career ruin -- or worse, being the man who ignited rebellion across Britain's richest province.\n\nThe stakes aren't just abstract. Your name will be attached to whatever happens next.",
        button: "Continue",
      },
      {
        title: "The Pressures You'll Face",
        text: "Your tenure survives only while Bengal stays governable. You'll be judged by three measures:\n\n**LEGITIMACY** -- Do Indian elites still believe British administration serves any legitimate purpose? Do they attend your receptions, accept your grants, work within the system? Or have you lost their confidence entirely?\n\n**STABILITY** -- Are the streets calm? Are courts functioning? Or have strikes, riots, and disorder made the province ungovernable?\n\n**SWADESHI MOMENTUM** -- The boycott movement grows weekly. Bonfires of British cloth. *Swadeshi* mills opening. If it becomes unstoppable, the Partition itself becomes untenable.\n\nYou will be **dismissed** if:\n- **Legitimacy collapses:** administrators and elites conclude you've lost control\n- **Stability collapses:** riots overwhelm provincial authority  \n- **Swadeshi Momentum becomes unstoppable:** the boycott makes the Partition unworkable\n\nYou will **succeed** if you reach **31 December 1908** without triggering any of those crises.\n\nHistory remembers that the Partition was annulled in 1911. Will this time be different?",
        button: "Begin Game",
      },
    ],
  };

  const BENGAL_STORY = {
    GAME_VERSION: "v2.3.0",
    START_SCENE_ID: "opening_decision",
    OUTCOME_TEXT: {
      legitimacy_collapse:
        "Your credibility with elites and officials has shattered. Petitions no longer reach your desk, and the press treats every proclamation as empty. London recalls you for failing to preserve the Raj's authority.",
      stability_collapse:
        "Riots, strikes, and daily disruptions overwhelm the machinery of governance. The administration can no longer guarantee basic order, and your post is terminated.",
      swadeshi_unstoppable:
        "The boycott has become unstoppable. Merchants refuse British cloth, students organize daily pickets, and even moderate leaders can no longer contain the movement. The Partition becomes politically untenable under your watch.",
      survived:
        "You have held the line through the end of 1908. The crisis persists, but the province remains governable, and your position survives.",
    },
    SCENES: {
      opening_decision: {
        date: "1905-08-12",
        narration:
          "**Your Office, Viceregal Lodge -- Morning**\n\nThe Partition will be announced in October, but Calcutta already hums with rumor. On your desk sit three files and an intelligence note, each demanding a different kind of statecraft. Commissioner Bamfield wants immediate arrests of agitators. Surendranath Banerjee requests an audience to keep protest constitutional. The Commerce Department proposes a grant to Bengali textile mills to blunt the swadeshi boycott. Your deputy suggests discreet intelligence gathering before you commit to any course.\n\nOutside your window, trams clatter and the presses at Bow Bazar begin to roll. Within weeks, the city will learn the province is to be split. Your first move will set the tone for everything that follows.",
        learned:
          "Early colonial decisions often mixed coercion, consultation, and economic policy. Each signal shaped how moderates and radicals interpreted the Raj's intentions.",
        options: [
          {
            id: "arrest_warrants",
            label:
              "Authorize the arrest warrants and disrupt the radical committees before they meet.",
            effects: {
              local_stability: 5,
              legitimacy: -5,
              swadeshi_momentum: 5,
              reputation: 4,
            },
            set_flags: ["crackdown"],
            next: "pre_partition_rumors",
          },
          {
            id: "meet_banerjee",
            label:
              "Grant Banerjee an immediate audience and ask for a constitutional petition path.",
            effects: {
              legitimacy: 7,
              local_stability: 2,
              swadeshi_momentum: -2,
              reputation: -2,
            },
            set_flags: ["moderate_outreach"],
            next: "pre_partition_rumors",
          },
          {
            id: "textile_grant",
            label:
              "Approve the textile grant and frame it as support for local industry.",
            effects: {
              legitimacy: 3,
              local_stability: 2,
              swadeshi_momentum: -4,
              reputation: 1,
            },
            set_flags: ["economic_concession"],
            next: "pre_partition_rumors",
          },
          {
            id: "dispatch_intel",
            label:
              "Send a trusted aide to map the committees and report back quietly.",
            effects: {
              local_stability: 1,
              legitimacy: 0,
              swadeshi_momentum: -1,
              reputation: 0,
            },
            set_flags: ["intel_network"],
            next: "intel_briefing",
          },
          {
            id: "public_circular",
            label:
              "Issue a public circular emphasizing administrative efficiency and calm.",
            effects: {
              legitimacy: 2,
              local_stability: 1,
              swadeshi_momentum: 0,
              reputation: 1,
            },
            set_flags: ["public_assurance"],
            next: "pre_partition_rumors",
          },
        ],
      },
      intel_briefing: {
        date: "1905-08-28",
        narration:
          "Your aide returns with a quiet dossier: student committees, pamphlet printers, and the back rooms where boycott oaths are sworn. He also notes a second pattern -- business guilds worried more about instability than ideology. The intelligence is clear, but how you use it is a choice in itself.",
        learned:
          "Information could enable targeted action or become a political weapon. How it was used shaped both legitimacy and effectiveness.",
        options: [
          {
            id: "targeted_watchlists",
            label:
              "Create watchlists and instruct the CID to monitor without arrests.",
            effects: { local_stability: 2, legitimacy: -1, swadeshi_momentum: -1, reputation: 1 },
            set_flags: ["intel_network"],
            next: "pre_partition_rumors",
          },
          {
            id: "share_with_moderates",
            label:
              "Privately brief Banerjee on the radicals to encourage distance.",
            effects: { legitimacy: 4, local_stability: 1, swadeshi_momentum: -2, reputation: -1 },
            set_flags: ["moderate_outreach"],
            next: "pre_partition_rumors",
          },
          {
            id: "quiet_delay",
            label:
              "File the report and wait for clearer signals before acting.",
            effects: { legitimacy: 0, local_stability: 0, swadeshi_momentum: 1, reputation: -1 },
            next: "pre_partition_rumors",
          },
          {
            id: "leak_warning",
            label:
              "Allow a subtle leak to the press to warn the public against violence.",
            effects: { legitimacy: -1, local_stability: 1, swadeshi_momentum: -1, reputation: 1 },
            set_flags: ["press_campaign"],
            next: "pre_partition_rumors",
          },
        ],
      },
      pre_partition_rumors: {
        date: "1905-09-05",
        variants: [
          {
            requires_flags: ["crackdown"],
            narration:
              "The arrests ripple through College Square. Editors call the warrants a proof of divide-and-rule. Moderates bristle at the spectacle, while radicals use the names to recruit. Your telegrams report a brief lull in street meetings, but the boycotters are already planning their first bonfires of foreign cloth.\n\nLondon urges firmness. Calcutta's business leaders urge calm. With the formal proclamation weeks away, the question is whether you double down or recalibrate.",
            learned:
              "Preemptive repression can buy short-term stability but often fuels the legitimacy crisis that radicals exploit.",
          },
          {
            requires_flags: ["moderate_outreach"],
            narration:
              "Banerjee leaves your office with cautious optimism. His papers praise constitutional protest, yet radicals accuse him of bargaining with the Raj. Petitions circulate through the bhadralok circles, and the bazaars buzz with competing rumors about what the Partition will mean.\n\nThe police report fewer arrests but more pamphlets. With October approaching, you must decide how visible your posture will be.",
            learned:
              "Engaging moderates can lower immediate tensions, but it risks pushing radicals to seek their own momentum outside constitutional channels.",
          },
          {
            requires_flags: ["public_assurance"],
            narration:
              "Your circulars emphasize efficiency and better governance. Some merchants applaud the steady tone; others read it as a thin veil for divide-and-rule. Pamphlets still proliferate, but the rumors are less fevered than they might have been.\n\nThe question now is how to prepare for the proclamation without appearing weak.",
            learned:
              "Official messaging could dampen panic, but it rarely displaced the suspicions of politically mobilized publics.",
          },
          {
            narration:
              "Rumor outpaces fact. The vernacular press treats the Partition as certain, while the English-language papers insist it is administrative reform. Petitions circulate, secret committees meet, and merchants ask whether the swadeshi boycott will hit the bazaars before winter.\n\nYou have a narrow window to shape expectations before the formal proclamation lands.",
            learned:
              "Ambiguity in colonial policy often invited competing interpretations, which could harden into organized resistance.",
          },
        ],
        option_sets: [
          {
            requires_flags: ["crackdown"],
            options: [
              {
                id: "double_down_arrests",
                label:
                  "Expand arrests and invoke Section 144 to prevent public meetings.",
                effects: { local_stability: 4, legitimacy: -6, swadeshi_momentum: 6, reputation: 3 },
                set_flags: ["hardline"],
                next: "partition_proclaimed",
              },
              {
                id: "release_moderates",
                label:
                  "Release minor detainees and open a petition channel through Banerjee.",
                effects: { legitimacy: 5, local_stability: -1, swadeshi_momentum: -2, reputation: -1 },
                set_flags: ["moderate_outreach"],
                next: "partition_proclaimed",
              },
              {
                id: "issue_carlyle_circular",
                label:
                  "Issue the 'Carlyle Circular' threatening to withdraw grants from schools if students protest.",
                effects: { legitimacy: -3, local_stability: 2, swadeshi_momentum: 3, reputation: 2 },
                set_flags: ["hardline", "education_crackdown"],
                next: "partition_proclaimed",
              },
              {
                id: "expand_cid",
                label:
                  "Expand CID surveillance and build dossiers on organizers.",
                effects: { local_stability: 2, legitimacy: -1, swadeshi_momentum: -1, reputation: 0 },
                set_flags: ["intel_network"],
                next: "partition_proclaimed",
              },
              {
                id: "press_reassure",
                label:
                  "Launch a press campaign stressing administrative reform and benefits for the east.",
                effects: { legitimacy: 1, local_stability: 1, swadeshi_momentum: 0, reputation: 1 },
                set_flags: ["press_campaign"],
                next: "partition_proclaimed",
              },
            ],
          },
          {
            options: [
              {
                id: "limited_section_144",
                label:
                  "Impose limited restrictions on mass meetings and keep police visible.",
                effects: { local_stability: 3, legitimacy: -2, swadeshi_momentum: 2, reputation: 2 },
                set_flags: ["hardline"],
                next: "partition_proclaimed",
              },
              {
                id: "moderate_council",
                label:
                  "Convene a council of moderates to draft a formal petition.",
                effects: { legitimacy: 6, local_stability: 1, swadeshi_momentum: -3, reputation: -2 },
                set_flags: ["moderate_outreach"],
                next: "partition_proclaimed",
              },
              {
                id: "issue_carlyle_circular",
                label:
                  "Issue the 'Carlyle Circular' to deter student participation in boycotts.",
                effects: { legitimacy: -4, local_stability: 2, swadeshi_momentum: 4, reputation: 1 },
                set_flags: ["hardline", "education_crackdown"],
                next: "partition_proclaimed",
              },
              {
                id: "covert_surveillance",
                label:
                  "Order discreet surveillance of swadeshi committees.",
                effects: { local_stability: 2, legitimacy: 0, swadeshi_momentum: -1, reputation: 0 },
                set_flags: ["intel_network"],
                next: "partition_proclaimed",
              },
              {
                id: "public_assurances",
                label:
                  "Deliver a public address promising administrative fairness in both provinces.",
                effects: { legitimacy: 2, local_stability: 1, swadeshi_momentum: 0, reputation: 0 },
                set_flags: ["public_assurance"],
                next: "partition_proclaimed",
              },
            ],
          },
        ],
      },
      partition_proclaimed: {
        date: "1905-10-16",
        variants: [
          {
            requires_flags: ["press_campaign"],
            narration:
              "The proclamation arrives. In Calcutta, the streets churn with protest; in Dacca, loyalists offer garlands to the new provincial capital. Your press campaign keeps some merchants calm, but the air is thick with tension.\n\nToday is Raksha Bandhan, and Rabindranath Tagore has called for a unique form of protest. The Governor asks for instructions: how should the police handle the crowds gathering at the river?",
          },
          {
            narration:
              "The proclamation arrives. It is October 16th. In Calcutta, the streets churn with protest; in Dacca, loyalists offer garlands to the new provincial capital. But in the city, the mood is strangely solemn. Rabindranath Tagore has called for a day of mourning and unity.\n\nThe Governor asks for instructions: how should the police handle the crowds gathering at the river to tie 'rakhis' on one another?",
          },
        ],
        learned:
          "The proclamation amplified existing divides: Hindu nationalist anger, Muslim loyalist hopes, and British anxieties about order.",
        options: [
          {
            id: "ban_rallies",
            label:
              "Enforce Section 144 and ban rallies in Calcutta for the next fortnight.",
            effects: { local_stability: 4, legitimacy: -5, swadeshi_momentum: 4, reputation: 3 },
            set_flags: ["hardline"],
            next: "raksha_bandhan",
          },
          {
            id: "allow_processions",
            label:
              "Permit peaceful processions under police escort and avoid mass arrests.",
            effects: { legitimacy: 4, local_stability: -1, swadeshi_momentum: 2, reputation: -1 },
            set_flags: ["moderate_outreach"],
            next: "raksha_bandhan",
          },
          {
            id: "symbolic_concessions",
            label:
              "Announce scholarships and consultative seats as symbolic concessions.",
            effects: { legitimacy: 3, local_stability: 1, swadeshi_momentum: -2, reputation: 0 },
            set_flags: ["economic_concession"],
            next: "raksha_bandhan",
          },
          {
            id: "meet_muslim_elites",
            label:
              "Publicly meet Nawab Salimullah and promise attention to eastern districts.",
            effects: { legitimacy: 1, local_stability: 1, swadeshi_momentum: 1, reputation: 2 },
            set_flags: ["muslim_loyalists"],
            next: "raksha_bandhan",
          },
          {
            id: "press_controls",
            label:
              "Warn newspapers against incendiary language and threaten closures.",
            effects: { local_stability: 2, legitimacy: -3, swadeshi_momentum: 2, reputation: 1 },
            set_flags: ["press_censorship"],
            next: "raksha_bandhan",
          },
        ],
      },
      raksha_bandhan: {
        date: "1905-10-16",
        narration:
          "**Afternoon**\n\nThe report lands on your desk: tens of thousands bathed in the Ganges this morning. They are now marching through the streets singing *'Amar Sonar Bangla'*. But it is not a riot.\n\nIt is... a festival. Hindus and Muslims are tying yellow threads -- *rakhis* -- on each other's wrists as a vow of brotherhood. Even the police constables look unsure whether to strike or watch. At Federation Hall, Ananda Mohan Bose, sick and carried on a stretcher, has laid the foundation stone of a 'united Bengal'.\n\nIt is a masterstroke of theater. If you crush it, you look like a barbarian. If you ignore it, you admit they are united.",
        learned:
          "Cultural symbols could bypass political censorship, mobilizing emotions that administrative logic could not touch.",
        options: [
          {
            id: "ignore_sentiment",
            label:
              "Instruct police to stand down. 'Let them sing. It changes nothing on the map.'",
            effects: { local_stability: 0, legitimacy: 2, swadeshi_momentum: 2, reputation: -1 },
            next: "boycott_wave",
          },
          {
            id: "disrupt_crowds",
            label:
              "Order police to disperse any crowd blocking traffic. Tear the threads if necessary.",
            effects: { local_stability: 2, legitimacy: -5, swadeshi_momentum: 5, reputation: 2 },
            set_flags: ["hardline"],
            next: "boycott_wave",
          },
          {
            id: "counter_narrative",
            label:
              "Issue a statement praising the 'loyalty' of those who did not march.",
            effects: { local_stability: 1, legitimacy: -2, swadeshi_momentum: 1, reputation: 1 },
            set_flags: ["press_campaign"],
            next: "boycott_wave",
          },
        ],
      },
      boycott_wave: {
        date: "1906-01-20",
        variants: [
          {
            requires_flags: ["hardline"],
            narration:
              "The swadeshi boycott takes on the energy of a crusade. Bonfires of foreign cloth burn near College Square, and pickets line the market gates. Your earlier restrictions are now cited as proof that constitutional methods are futile. Meanwhile, merchants plead for protection from crowd pressure.\n\nYou must choose whether to clamp down, co-opt the movement, or redirect it through moderate channels.",
          },
          {
            requires_flags: ["education_crackdown"],
            narration:
              "The Carlyle Circular has backfired. Instead of silencing students, it has created the 'Anti-Circular Society'. Expelled students are now full-time agitators, manning the boycott lines. Principals complain they are losing control of their campuses.\n\nThe boycott is hardening. You need a strategy to deal with these 'national volunteers'.",
          },
          {
            requires_flags: ["moderate_outreach"],
            narration:
              "Moderate petitions still circulate, but the streets tell a different story. Swadeshi organizers declare boycott a moral duty, and students treat picketing as a rite of passage. Your meetings with moderates slow some agitation, yet radicals fill the vacuum with fiery speeches and boycotts.\n\nThe next move will decide whether the boycott hardens or softens.",
          },
          {
            narration:
              "Swadeshi momentum spreads beyond Calcutta into smaller towns. Picket lines form outside foreign cloth shops, and merchants ask for protection. Reports note a mix of disciplined boycotts and occasional intimidation.\n\nYou need a policy that either breaks the pickets, absorbs them into policy, or reframes the struggle.",
          },
        ],
        learned:
          "Swadeshi was both an economic tactic and a moral campaign. State responses could suppress, co-opt, or unintentionally intensify it.",
        options: [
          {
            id: "crackdown_pickets",
            label:
              "Order arrests of picket leaders and prosecute sedition in the press.",
            effects: { local_stability: 3, legitimacy: -4, swadeshi_momentum: 5, reputation: 2 },
            set_flags: ["hardline"],
            next: "security_backlash",
          },
          {
            id: "support_industry",
            label:
              "Expand grants to mills and promote local procurement contracts.",
            effects: { legitimacy: 2, local_stability: 1, swadeshi_momentum: -3, reputation: 1 },
            set_flags: ["economic_concession"],
            next: "industry_push",
          },
          {
            id: "moderate_channels",
            label:
              "Invite moderates to issue a joint appeal for constitutional protest.",
            effects: { legitimacy: 5, local_stability: 1, swadeshi_momentum: -2, reputation: -2 },
            set_flags: ["moderate_outreach"],
            next: "petition_tour",
          },
          {
            id: "intel_infiltration",
            label:
              "Infiltrate swadeshi committees and quietly disrupt their logistics.",
            effects: { local_stability: 2, legitimacy: -1, swadeshi_momentum: -2, reputation: 0 },
            set_flags: ["intel_network"],
            next: "covert_pressure",
          },
          {
            id: "rural_relief",
            label:
              "Shift attention to rural districts and promise relief funds to blunt boycott outreach.",
            effects: { legitimacy: 2, local_stability: 2, swadeshi_momentum: -1, reputation: 0 },
            set_flags: ["rural_focus"],
            next: "rural_deputation",
          },
        ],
      },
      security_backlash: {
        date: "1906-04-14",
        narration:
          "**The Barisal Crisis**\n\nThe flashpoint has arrived at Barisal. The Provincial Conference met yesterday, defying your ban on the cry 'Bande Mataram'.\n\nPolice charged the procession. Delegates were beaten. Surendranath Banerjee himself was arrested and fined by Magistrate Emerson. The news has electrified the province. Moderate leaders who preached caution are now humiliated; they show you their bruises.\n\nYour policy of 'firmness' has created a unified front of martyrs. The question is no longer about cloth -- it is about the right to speak.",
        learned:
          "Excessive force against respected leaders often collapsed the distinction between moderates and radicals, uniting the opposition.",
        options: [
          {
            id: "curfew_extension",
            label:
              "Back the Magistrate. Extend curfews and authorize rapid-response patrols.",
            effects: { local_stability: 4, legitimacy: -6, swadeshi_momentum: 5, reputation: 3 },
            set_flags: ["hardline"],
            next: "municipal_strain",
          },
          {
            id: "targeted_pullback",
            label:
              "Quietly transfer Magistrate Emerson and rescind the harshest gathering bans.",
            effects: { local_stability: -1, legitimacy: 3, swadeshi_momentum: -1, reputation: -1 },
            set_flags: ["moderate_outreach"],
            next: "municipal_strain",
          },
          {
            id: "compensation_fund",
            label:
              "Create a compensation fund for businesses harmed by the unrest.",
            effects: { local_stability: 1, legitimacy: 2, swadeshi_momentum: -1, reputation: 1 },
            set_flags: ["economic_concession"],
            next: "municipal_strain",
          },
          {
            id: "press_inquiry",
            label:
              "Announce an inquiry into police conduct to calm the bhadralok.",
            effects: { legitimacy: 4, local_stability: -1, swadeshi_momentum: -1, reputation: -2 },
            set_flags: ["moderate_outreach"],
            next: "municipal_strain",
          },
          {
            id: "military_patrols",
            label:
              "Deploy visible military patrols to deter further mass meetings.",
            effects: { local_stability: 3, legitimacy: -5, swadeshi_momentum: 4, reputation: 2 },
            set_flags: ["hardline"],
            next: "municipal_strain",
          },
        ],
      },
      industry_push: {
        date: "1906-03-05",
        narration:
          "Textile owners welcome the grants, but Manchester traders complain loudly to the Governor-General. Swadeshi leaders claim the policy proves the boycott's power. Meanwhile, new apprentices crowd into mills, hoping for work.\n\nThe decision now is whether to deepen the economic strategy or to guard against backlash from London and Calcutta's financiers.",
        learned:
          "Economic concessions could undercut boycotts, but they also reshaped political expectations and imperial trade politics.",
        options: [
          {
            id: "expand_grants",
            label:
              "Expand grants and prioritize local procurement for government contracts.",
            effects: { legitimacy: 3, local_stability: 1, swadeshi_momentum: -3, reputation: 0 },
            set_flags: ["economic_concession"],
            next: "municipal_strain",
          },
          {
            id: "limit_subsidy",
            label:
              "Cap subsidies and emphasize balanced trade to reassure London.",
            effects: { legitimacy: -1, local_stability: 0, swadeshi_momentum: 1, reputation: 2 },
            next: "municipal_strain",
          },
          {
            id: "vocational_schools",
            label:
              "Launch vocational schools to train textile workers and signal long-term reform.",
            effects: { legitimacy: 3, local_stability: 1, swadeshi_momentum: -2, reputation: -1 },
            set_flags: ["education_focus"],
            next: "municipal_strain",
          },
          {
            id: "merchant_compact",
            label:
              "Negotiate a compact with merchant guilds to keep markets open.",
            effects: { local_stability: 2, legitimacy: 1, swadeshi_momentum: -1, reputation: 1 },
            next: "municipal_strain",
          },
          {
            id: "audit_grants",
            label:
              "Order an audit of grant recipients to prevent accusations of patronage.",
            effects: { legitimacy: 2, local_stability: 0, swadeshi_momentum: 0, reputation: 1 },
            next: "municipal_strain",
          },
        ],
      },
      petition_tour: {
        date: "1906-03-05",
        narration:
          "Banerjee and his allies organize a petition tour across Bengal. Crowds are large and orderly, but radicals heckle the stage and accuse moderates of weakness. The press treats the tour as a referendum on the Raj's willingness to listen.\n\nYour response will decide whether constitutional protest remains credible.",
        learned:
          "Moderate leadership depended on the belief that petitions could produce concessions. Without a response, their authority eroded.",
        options: [
          {
            id: "accept_deputation",
            label:
              "Receive the deputation and promise a formal review in London.",
            effects: { legitimacy: 5, local_stability: 1, swadeshi_momentum: -2, reputation: -1 },
            set_flags: ["moderate_outreach"],
            next: "municipal_strain",
          },
          {
            id: "delay_response",
            label:
              "Delay the deputation and insist petitions follow the official timetable.",
            effects: { legitimacy: -2, local_stability: 0, swadeshi_momentum: 2, reputation: 2 },
            next: "municipal_strain",
          },
          {
            id: "council_seats",
            label:
              "Offer additional seats on municipal councils to moderate leaders.",
            effects: { legitimacy: 3, local_stability: 1, swadeshi_momentum: -1, reputation: -1 },
            set_flags: ["moderate_outreach"],
            next: "municipal_strain",
          },
          {
            id: "split_radicals",
            label:
              "Denounce radical speakers and demand moderates publicly disown them.",
            effects: { legitimacy: 1, local_stability: 1, swadeshi_momentum: 1, reputation: 1 },
            set_flags: ["hardline"],
            next: "municipal_strain",
          },
          {
            id: "education_concessions_tour",
            label:
              "Pair the tour with scholarships and educational grants.",
            effects: { legitimacy: 4, local_stability: 1, swadeshi_momentum: -2, reputation: 0 },
            set_flags: ["education_focus"],
            next: "municipal_strain",
          },
        ],
      },
      covert_pressure: {
        date: "1906-03-05",
        narration:
          "CID officers report quiet successes: pamphlet presses seized, key couriers intercepted, and committees forced to meet in smaller rooms. The movement is not broken, but its tempo slows. At the same time, rumors of informants deepen mistrust among students and merchants alike.\n\nDo you keep the pressure hidden or reveal it as a deterrent?",
        learned:
          "Covert tactics could slow mobilization, but secrecy also bred paranoia and suspicion of collaborators.",
        options: [
          {
            id: "targeted_arrests",
            label:
              "Make a few high-profile arrests to signal reach.",
            effects: { local_stability: 2, legitimacy: -3, swadeshi_momentum: 2, reputation: 1 },
            set_flags: ["hardline"],
            next: "municipal_strain",
          },
          {
            id: "keep_hidden",
            label:
              "Keep operations secret and focus on logistics disruption.",
            effects: { local_stability: 2, legitimacy: -1, swadeshi_momentum: -2, reputation: 0 },
            set_flags: ["intel_network"],
            next: "municipal_strain",
          },
          {
            id: "offer_amnesty",
            label:
              "Offer quiet amnesty to minor activists who withdraw.",
            effects: { legitimacy: 3, local_stability: 1, swadeshi_momentum: -2, reputation: -1 },
            set_flags: ["moderate_outreach"],
            next: "municipal_strain",
          },
          {
            id: "press_disclosures",
            label:
              "Leak select intelligence to discredit radical leaders.",
            effects: { legitimacy: -2, local_stability: 1, swadeshi_momentum: 1, reputation: 1 },
            set_flags: ["press_campaign"],
            next: "municipal_strain",
          },
          {
            id: "expand_informants",
            label:
              "Expand informant payments and reward loyal local officials.",
            effects: { local_stability: 2, legitimacy: -1, swadeshi_momentum: -1, reputation: 1 },
            set_flags: ["intel_network"],
            next: "municipal_strain",
          },
        ],
      },
      rural_deputation: {
        date: "1906-03-05",
        narration:
          "A delegation from rural districts arrives with petitions about taxes, flood relief, and fears that the Partition will starve their markets of investment. Swadeshi organizers are beginning to tour the countryside, linking economic hardship to imperial policy.\n\nIf you want to blunt the boycott in the towns, you may need to act in the villages.",
        learned:
          "Rural grievances could be folded into nationalist politics, expanding movements beyond the city core.",
        options: [
          {
            id: "irrigation_plan",
            label:
              "Fund irrigation and canal maintenance in eastern districts.",
            effects: { legitimacy: 3, local_stability: 2, swadeshi_momentum: -2, reputation: 0 },
            set_flags: ["rural_focus"],
            next: "municipal_strain",
          },
          {
            id: "magistrate_tours",
            label:
              "Send magistrates to hold open hearings in district towns.",
            effects: { legitimacy: 2, local_stability: 1, swadeshi_momentum: -1, reputation: -1 },
            set_flags: ["moderate_outreach"],
            next: "municipal_strain",
          },
          {
            id: "ignore_petitions",
            label:
              "Decline rural petitions and focus on Calcutta stability.",
            effects: { legitimacy: -2, local_stability: -1, swadeshi_momentum: 2, reputation: 1 },
            next: "municipal_strain",
          },
          {
            id: "zamindar_compact",
            label:
              "Work through loyal zamindars to calm villages and report unrest.",
            effects: { legitimacy: 1, local_stability: 2, swadeshi_momentum: -1, reputation: 1 },
            set_flags: ["rural_focus"],
            next: "municipal_strain",
          },
          {
            id: "grain_relief",
            label:
              "Open grain relief depots to blunt price spikes.",
            effects: { legitimacy: 2, local_stability: 2, swadeshi_momentum: -1, reputation: 0 },
            set_flags: ["economic_concession"],
            next: "municipal_strain",
          },
        ],
      },
      municipal_strain: {
        date: "1906-06-15",
        variants: [
          {
            requires_flags: ["economic_concession"],
            narration:
              "The grants keep some mills open, but boycotters accuse you of bribery. Municipal finances strain under the cost of policing and relief. Strikes flicker in the jute mills, and students boycott classes in sympathy.\n\nYou need a policy that stabilizes the streets without surrendering authority.",
          },
          {
            requires_flags: ["rural_focus"],
            narration:
              "Rural relief buys you time, but the municipal budget is strained. Strikes flicker in the jute mills, and students boycott classes in sympathy. Merchants demand stronger protection, while moderate leaders warn against another heavy-handed move.\n\nYour next decision will shape the mid-year tempo of the movement.",
          },
          {
            narration:
              "Municipal budgets strain under police overtime and disrupted trade. Strikes flicker in the jute mills, and student leaders call for a day of fasting and protest. Merchants ask for stronger protection, while moderate leaders warn that another heavy-handed move will push wavering elites toward the radicals.\n\nYour next decision will shape the mid-year tempo of the movement.",
          },
        ],
        learned:
          "Economic concessions could soften discontent but also be framed as manipulation. Municipal governance became a key arena for contesting legitimacy.",
        options: [
          {
            id: "press_censorship",
            label:
              "Invoke press restrictions and shut down the most incendiary papers.",
            effects: { local_stability: 3, legitimacy: -6, swadeshi_momentum: 4, reputation: 2 },
            set_flags: ["hardline", "press_censorship"],
            next: "fuller_crisis",
          },
          {
            id: "education_concessions",
            label:
              "Launch scholarships and educational grants for both communities.",
            effects: { legitimacy: 4, local_stability: 1, swadeshi_momentum: -2, reputation: 0 },
            set_flags: ["education_focus"],
            next: "fuller_crisis",
          },
          {
            id: "municipal_devolution",
            label:
              "Give municipal councils more authority over relief and policing priorities.",
            effects: { legitimacy: 3, local_stability: 1, swadeshi_momentum: -1, reputation: -1 },
            set_flags: ["moderate_outreach"],
            next: "fuller_crisis",
          },
          {
            id: "split_gains",
            label:
              "Direct extra funds to eastern districts and highlight loyalist cooperation.",
            effects: { legitimacy: 1, local_stability: 1, swadeshi_momentum: 1, reputation: 2 },
            set_flags: ["muslim_loyalists"],
            next: "fuller_crisis",
          },
          {
            id: "labor_mediation",
            label:
              "Mediate between mill owners and workers to prevent a general strike.",
            effects: { legitimacy: 2, local_stability: 2, swadeshi_momentum: -1, reputation: 0 },
            set_flags: ["labor_conciliation"],
            next: "fuller_crisis",
          },
        ],
      },
      fuller_crisis: {
        date: "1906-08-20",
        narration:
          "**The Fuller Crisis**\n\nSir Bampfylde Fuller, Lieutenant-Governor of Eastern Bengal, has precipitated a crisis. He demanded the disaffiliation of two schools in Sirajganj where students were involved in agitation. Lord Minto, fearing a parliamentary uproar, asked him to withdraw the request.\n\nFuller has responded with an ultimatum: either the schools are punished, or he resigns. The Muslim elite in the east see Fuller as their champion. The Congress sees him as a tyrant. Your advice to the Viceroy will determine the fate of the administration.",
        learned:
          "Administrative ultimatums often forced the colonial state to choose between prestige and political expediency.",
        options: [
          {
            id: "accept_resignation",
            label:
              "Accept Fuller's resignation. Sacrifice the man to save the peace.",
            effects: { legitimacy: 4, local_stability: 1, swadeshi_momentum: -2, reputation: -1 },
            set_flags: ["moderate_outreach"],
            next: "muslim_league",
          },
          {
            id: "back_fuller",
            label:
              "Reject the resignation and back Fuller's hardline stance.",
            effects: { local_stability: -2, legitimacy: -4, swadeshi_momentum: 4, reputation: 2 },
            set_flags: ["hardline", "muslim_loyalists"],
            next: "muslim_league",
          },
          {
            id: "broker_compromise",
            label:
              "Delay the decision and attempt to transfer Fuller quietly later.",
            effects: { legitimacy: -1, local_stability: 0, swadeshi_momentum: 1, reputation: -1 },
            next: "muslim_league",
          },
        ],
      },
      muslim_league: {
        date: "1906-12-30",
        variants: [
          {
            requires_flags: ["muslim_loyalists"],
            narration:
              "At Ahsan Manzil in Dacca, Nawab Salimullah hosts delegates who found the All-India Muslim League. Your earlier outreach is remembered, and loyalist speeches praise the Raj for creating a Muslim-majority province. Hindu leaders in Calcutta read the news as proof of divide-and-rule.\n\nHow you respond will shape communal politics for years to come.",
          },
          {
            narration:
              "At Ahsan Manzil in Dacca, Nawab Salimullah hosts delegates who found the All-India Muslim League. They pledge loyalty to the Raj and argue that Muslim interests need distinct protection. Hindu leaders in Calcutta read the news as proof of divide-and-rule.\n\nYour response will signal whether you lean into communal balancing or seek a broader equilibrium.",
          },
        ],
        learned:
          "The Muslim League's formation marked a new phase of organized communal politics, complicating nationalist unity.",
        options: [
          {
            id: "encourage_league",
            label:
              "Attend the League gathering and praise loyal cooperation in the east.",
            effects: { local_stability: 2, legitimacy: -2, swadeshi_momentum: 2, reputation: 3 },
            set_flags: ["muslim_loyalists"],
            next: "jamalpur_riots",
          },
          {
            id: "balance_statement",
            label:
              "Issue a balanced statement and meet Congress moderates the same week.",
            effects: { legitimacy: 3, local_stability: 1, swadeshi_momentum: -1, reputation: 0 },
            set_flags: ["moderate_outreach"],
            next: "jamalpur_riots",
          },
          {
            id: "neutral_distance",
            label:
              "Keep official distance and focus on law and order messaging.",
            effects: { local_stability: 2, legitimacy: -1, swadeshi_momentum: 1, reputation: 1 },
            next: "jamalpur_riots",
          },
          {
            id: "joint_council",
            label:
              "Propose a joint Hindu-Muslim advisory council for provincial policy.",
            effects: { legitimacy: 4, local_stability: 1, swadeshi_momentum: -1, reputation: -1 },
            set_flags: ["moderate_outreach"],
            next: "jamalpur_riots",
          },
          {
            id: "separate_electorates",
            label:
              "Support separate electorates for Muslims to reassure loyalists.",
            effects: { legitimacy: -2, local_stability: 1, swadeshi_momentum: 2, reputation: 2 },
            set_flags: ["muslim_loyalists"],
            next: "jamalpur_riots",
          },
        ],
      },
      jamalpur_riots: {
        date: "1907-03-10",
        narration:
          "**The Communal Fracture**\n\nThe unity of 1905 is cracking. In Comilla and Jamalpur, riots have erupted. A 'Red Pamphlet' is circulating, urging Muslims to boycott Hindu traders and zamindars. Swadeshi volunteers defending Hindu property are clashing with Muslim tenants.\n\nThe administration faces a dark choice: intervene impartially to stop the violence, or allow the communal wedge to deepen, effectively breaking the Swadeshi movement's back.",
        learned:
          "Communal violence often broke the momentum of nationalist movements, but at the cost of long-term social cohesion.",
        options: [
          {
            id: "impartial_crackdown",
            label:
              "Deploy the army to crush rioters on both sides and ban the Red Pamphlet.",
            effects: { local_stability: 5, legitimacy: 2, swadeshi_momentum: -1, reputation: 1 },
            set_flags: ["hardline"],
            next: "radicalization",
          },
          {
            id: "strategic_inaction",
            label:
              "Order police to 'contain' rather than suppress, allowing the split to widen.",
            effects: { local_stability: -3, legitimacy: -4, swadeshi_momentum: -5, reputation: 2 },
            set_flags: ["divide_and_rule"],
            next: "radicalization",
          },
          {
            id: "peace_committees",
            label:
              "Form joint peace committees with Moderate and Muslim League leaders.",
            effects: { legitimacy: 3, local_stability: 1, swadeshi_momentum: 1, reputation: -1 },
            set_flags: ["moderate_outreach"],
            next: "radicalization",
          },
        ],
      },
      radicalization: {
        date: "1907-07-15",
        variants: [
          {
            requires_flags: ["hardline"],
            narration:
              "Secret societies proliferate. The Anushilan Samiti circulates manuals and drills youths in secrecy. Your harsher measures have curbed open rallies but pushed the movement underground. Reports mention crude bomb-making experiments and plans against magistrates.\n\nYou must decide whether to widen the net or try to split radicals from moderates.",
          },
          {
            narration:
              "Secret societies proliferate. The Anushilan Samiti circulates manuals and drills youths in secrecy. Moderate leaders warn that punitive policies could make martyrs of the radicals. Police ask for authority to act before an attack occurs.\n\nThe next move balances preemption against political fallout.",
          },
        ],
        learned:
          "As repression grows, movements can shift from public protest to clandestine violence, forcing states to choose between broad crackdowns and targeted intelligence.",
        options: [
          {
            id: "broad_crackdown",
            label:
              "Authorize mass arrests of suspected radicals across Bengal.",
            effects: { local_stability: 4, legitimacy: -7, swadeshi_momentum: 6, reputation: 3 },
            set_flags: ["hardline"],
            next: "surat_split",
          },
          {
            id: "targeted_surveillance",
            label:
              "Use intelligence to make targeted arrests and avoid mass roundups.",
            effects: { local_stability: 3, legitimacy: -2, swadeshi_momentum: 1, reputation: 1 },
            set_flags: ["intel_network"],
            next: "surat_split",
          },
          {
            id: "partition_review",
            label:
              "Promise a formal review of the partition within two years.",
            effects: { legitimacy: 5, local_stability: 0, swadeshi_momentum: -3, reputation: -2 },
            set_flags: ["moderate_outreach"],
            next: "surat_split",
          },
          {
            id: "public_works",
            label:
              "Launch public works programs to absorb youth and ease unrest.",
            effects: { legitimacy: 3, local_stability: 2, swadeshi_momentum: -2, reputation: 1 },
            set_flags: ["economic_concession"],
            next: "surat_split",
          },
          {
            id: "press_trials",
            label:
              "Prosecute incendiary editors under sedition laws.",
            effects: { local_stability: 2, legitimacy: -4, swadeshi_momentum: 3, reputation: 2 },
            set_flags: ["press_censorship"],
            next: "surat_split",
          },
        ],
      },
      surat_split: {
        date: "1907-12-26",
        narration:
          "The Indian National Congress meets at Surat and fractures. Moderates and extremists clash on the floor, turning the session into chaos. News of the split races through Bengal: moderates plead for order while radicals celebrate independence from constitutional restraint.\n\nThe split offers an opening but also risks pushing the movement into harder forms.",
        learned:
          "Factional splits within nationalist politics reshaped strategies, with moderation and radicalism competing for legitimacy and mass support.",
        options: [
          {
            id: "court_moderates",
            label:
              "Publicly court the moderates and offer them advisory posts.",
            effects: { legitimacy: 4, local_stability: 1, swadeshi_momentum: -2, reputation: -1 },
            set_flags: ["moderate_outreach"],
            next: "bombing",
          },
          {
            id: "exploit_split",
            label:
              "Exploit the split by isolating extremists through targeted prosecutions.",
            effects: { local_stability: 3, legitimacy: -3, swadeshi_momentum: 2, reputation: 2 },
            set_flags: ["hardline"],
            next: "bombing",
          },
          {
            id: "seek_unity",
            label:
              "Issue a neutral statement urging unity and constitutional methods.",
            effects: { legitimacy: 2, local_stability: 0, swadeshi_momentum: -1, reputation: -1 },
            next: "bombing",
          },
          {
            id: "economic_dividends",
            label:
              "Announce fresh economic grants to undercut radical appeal.",
            effects: { legitimacy: 2, local_stability: 1, swadeshi_momentum: -2, reputation: 1 },
            set_flags: ["economic_concession"],
            next: "bombing",
          },
          {
            id: "communal_reassurance",
            label:
              "Reassure Muslim leaders that their interests remain protected.",
            effects: { legitimacy: 0, local_stability: 1, swadeshi_momentum: 1, reputation: 1 },
            set_flags: ["muslim_loyalists"],
            next: "bombing",
          },
        ],
      },
      bombing: {
        date: "1908-04-30",
        variants: [
          {
            requires_flags: ["intel_network"],
            narration:
              "Your intelligence officers warned of a plot, but the bomb still fell at Muzaffarpur. Two British women are killed when the device strikes the wrong carriage. The press erupts, and calls for decisive action flood your desk.\n\nYou must respond to the attack without igniting wider revolt.",
          },
          {
            narration:
              "A bomb explodes at Muzaffarpur, aimed at Magistrate Kingsford. Two British women are killed when the device strikes the wrong carriage. The press erupts, and calls for decisive action flood your desk.\n\nYou must respond to the attack without igniting wider revolt.",
          },
        ],
        learned:
          "Political violence hardened British resolve but also deepened public sympathy for radicals in some circles.",
        options: [
          {
            id: "emergency_powers",
            label: "Declare emergency powers and authorize sweeping raids.",
            effects: { local_stability: 5, legitimacy: -6, swadeshi_momentum: 5, reputation: 2 },
            set_flags: ["hardline"],
            next: "alipore_case",
          },
          {
            id: "judicial_process",
            label:
              "Promise swift but transparent trials and avoid collective punishment.",
            effects: { legitimacy: 4, local_stability: -1, swadeshi_momentum: 1, reputation: -1 },
            set_flags: ["moderate_outreach"],
            next: "alipore_case",
          },
          {
            id: "protect_moderates",
            label:
              "Publicly separate radicals from moderates and meet Banerjee again.",
            effects: { legitimacy: 4, local_stability: 0, swadeshi_momentum: -2, reputation: -1 },
            set_flags: ["moderate_outreach"],
            next: "alipore_case",
          },
          {
            id: "aid_relief",
            label:
              "Offer relief to victims and appeal for calm across the province.",
            effects: { legitimacy: 2, local_stability: 1, swadeshi_momentum: -1, reputation: 0 },
            next: "alipore_case",
          },
          {
            id: "press_silence",
            label:
              "Silence the most incendiary papers to prevent panic.",
            effects: { local_stability: 2, legitimacy: -4, swadeshi_momentum: 2, reputation: 1 },
            set_flags: ["press_censorship"],
            next: "alipore_case",
          },
        ],
      },
      alipore_case: {
        date: "1908-06-15",
        narration:
          "Police raids uncover a cache of explosives and revolutionary literature in Calcutta. The Alipore case begins to unfold, and the public watches every arrest. Some officials demand a sweeping crackdown; others warn that a show trial could make martyrs.\n\nYour handling of the case will shape the climate leading into the Tilak trial.",
        learned:
          "High-profile trials served both as legal instruments and political theater, often producing unintended symbolic effects.",
        options: [
          {
            id: "fast_track_trials",
            label:
              "Fast-track the Alipore trials to demonstrate imperial resolve.",
            effects: { local_stability: 3, legitimacy: -4, swadeshi_momentum: 3, reputation: 2 },
            set_flags: ["hardline"],
            next: "tilak_trial",
          },
          {
            id: "due_process",
            label:
              "Emphasize due process and allow defense counsel broad access.",
            effects: { legitimacy: 3, local_stability: -1, swadeshi_momentum: 1, reputation: -1 },
            set_flags: ["moderate_outreach"],
            next: "tilak_trial",
          },
          {
            id: "public_briefing",
            label:
              "Hold a public briefing on the evidence to counter rumor.",
            effects: { legitimacy: 2, local_stability: 1, swadeshi_momentum: -1, reputation: 0 },
            set_flags: ["press_campaign"],
            next: "tilak_trial",
          },
          {
            id: "limited_scope",
            label:
              "Keep the case narrowly focused to avoid a mass political backlash.",
            effects: { legitimacy: 2, local_stability: 1, swadeshi_momentum: -1, reputation: -1 },
            next: "tilak_trial",
          },
          {
            id: "expand_net",
            label:
              "Expand raids to affiliated societies across Bengal.",
            effects: { local_stability: 4, legitimacy: -5, swadeshi_momentum: 4, reputation: 2 },
            set_flags: ["hardline"],
            next: "tilak_trial",
          },
        ],
      },
      tilak_trial: {
        date: "1908-07-22",
        narration:
          "Bal Tilak is convicted of sedition and sentenced to transportation. Moderate leaders plead for calm, while radicals cast him as a martyr. The press in Bombay and Calcutta runs on anger and rumor. London wants reassurance that the Raj remains in control.\n\nYour response will set the tone for the final months of this crisis.",
        learned:
          "Sedition trials often intensified polarization, with moderates caught between loyalty and popular anger.",
        options: [
          {
            id: "support_conviction",
            label:
              "Publicly praise the conviction and reinforce sedition enforcement.",
            effects: { local_stability: 3, legitimacy: -5, swadeshi_momentum: 4, reputation: 2 },
            set_flags: ["hardline"],
            next: "end_1908",
          },
          {
            id: "quiet_restraint",
            label:
              "Avoid triumphalism and urge calm in official statements.",
            effects: { legitimacy: 2, local_stability: 1, swadeshi_momentum: -1, reputation: 0 },
            set_flags: ["moderate_outreach"],
            next: "end_1908",
          },
          {
            id: "limited_reforms",
            label:
              "Pair the verdict with limited reforms in education and consultation.",
            effects: { legitimacy: 4, local_stability: 0, swadeshi_momentum: -2, reputation: -1 },
            set_flags: ["economic_concession"],
            next: "end_1908",
          },
          {
            id: "military_reassurance",
            label:
              "Deploy troops in Calcutta as a visible signal of control.",
            effects: { local_stability: 3, legitimacy: -3, swadeshi_momentum: 2, reputation: 2 },
            set_flags: ["hardline"],
            next: "end_1908",
          },
          {
            id: "press_moderation",
            label:
              "Encourage the press to temper rhetoric and highlight legal procedure.",
            effects: { legitimacy: 2, local_stability: 1, swadeshi_momentum: -1, reputation: -1 },
            set_flags: ["press_campaign"],
            next: "end_1908",
          },
        ],
      },
      end_1908: {
        date: "1908-12-31",
        narration:
          "The year closes with Bengal still uneasy. Protests have not vanished, but neither has the administration collapsed. The files on your desk now look less like emergencies and more like a permanent condition: boycotts, petitions, loyalist lobbying, and quiet intelligence work.\n\nHistory will remember that the Partition was annulled in 1911, but your tenure is judged on whether you kept the province governable through 1908.",
        learned:
          "By 1908, the crisis had hardened into long-term political structures: boycott networks, communal organizations, and intensified debates about imperial legitimacy.",
        options: [],
      },
    },
  };

  window.OPENING_VIGNETTE = OPENING_VIGNETTE;
  window.BENGAL_STORY = BENGAL_STORY;
})();
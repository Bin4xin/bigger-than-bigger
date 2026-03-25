#!/bin/zsh
expressions=(
    '📣 What are Y0u f4cking barking ANDDDD Why So Serious?'
    '📣 We are all F4CKING SMALL-TOWN SWOT (LOUDLY).'
    '🥏 ૮₍ • ᴥ • ₎ა ~~APPEARANCE IS THE FIRST PRODUCTIVE FORCE~~; 🥏'

    # Self-deprecating test-taker series
    '📚 Good morning, test-takers! Another day of grinding for exam papers (sweating emoji).'
    '📚 Others graduate from top universities and join big tech, I graduate from a top university and end up screwing bolts in a factory – this is what you call a closed loop.'
    '📚 What''s wrong with being a small-town swot? At least I can still solve problems, what about you? You just lie flat (no mercy).'
    '📚 Back in the day, the teacher said knowledge changes destiny. Now my destiny has indeed changed – for the f***ing worse.'
    '📚 Doing problems until 3 a.m., look up at the mirror: Who the hell is that? Oh, it''s me, a test-taking machine with no future.'

    # Appearance/productivity meme extensions
    '💅 Appearance is the first productive force? Then with my looks, I must be negative productivity, should I pay the company to work here?'
    '💅 Bros, can I trade this face for an RTX 5090 D2? If not, I''ll come back and ask later.'
    '💅 Only the handsome ones have youth, the ugly ones just exist (lighting a cigarette).'
    '💅 Looked in the mirror today, system prompt: Your appearance balance is insufficient, please recharge ASAP.'

    '🤔 Don''t know, bump for help, +3, peace out.'
    '🤔 Front row selling snacks and drinks, please move your feet, comrade.'
    '🤔 You''re right, but Genshin Impact launch... (forgot the rest).'
    '🤔 Holy s***, a dog is barking! Oh sorry, it''s me barking.'
    '🤔 The classic of classics, "Small-town Swot" is here again, this is classic on top of classic.'

    # Angry bros special
    '🤬 You can you up? Oh you can''t, then why the f*** are you talking?'
    '🤬 Getting triggered? Already triggered? Suggest you check your blood pressure.'
    '🤬 No way, no way, does anyone really think swots should be wage slaves for life?'
    '🤬 Lol, you get a sense of superiority just from typing? Suggest you get your head checked.'

    # Cuckold/emotional vent literature (Tieba specialty)
    '🌿 So here''s the thing, my girlfriend... (can''t make it up, next person continue).'
    '🌿 Bros, I think I''ve been cheated on, but she''s really nice to me... oh it was just a dream, wake up, single dog.'
    '🌿 Today at a blind date, the girl asked for 300k bride price, I said I come from a small-town swot background, she said then you have to pay more.'
    '🌿 Three years together, today I found Genshin Impact on her phone, I''m devastated, bros is this normal?'

    # Grad school/civil service/job hunting dark jokes
    '📉 Failed grad school entrance exam, failed civil service exam, failed job hunt, now living off parents, my life is like a test paper with all wrong answers.'
    '📉 A master''s program that accepts scores of 300, and a vocational college that accepts scores of 300, what''s the difference? Oh, the difference is the former requires three more years of study.'
    '📉 Went for an interview today, HR asked what my specialty is, I said I''m good at taking tests, he laughed, I laughed, we all laughed.'
    '📉 Grad school = working for your advisor, working = working for your boss, test-taker = working for life – this is an identity equation.'

    # Abstract memes / mashups
    '🎣 Trolling, huh? Troll, just keep trolling, this fishhook is f***ing rusty.'
    '🎣 You''re right, but Vergil... (Devil May Cry meme).'
    '🎣 Holy s***, ice! Oh sorry, wrong set.'
    '🎣 Just asking, can test-takers be considered a profession now? Like with a license to work?'
    '🎣 Joke of the day: Hard work leads to success. Cold joke of the day: Doing tests can change your fate.'

    # Emo moments (breakdown literature)
    '😭 Studying late at night until I''m emo, open WeChat moments and see some rich kid showing off his new car, silently turn off phone, still have to get up early tomorrow to do problems.'
    '😭 Small-town swots do problems all their lives, only to find out the problems themselves are a scam.'
    '😭 My mom says the neighbor''s kid Er Gou only finished middle school and now runs a factory, and I, a graduate student, work for him – this is knowledge changing fate.'
    '😭 Broke down again today, but it''s okay, break down enough times and you get used to it (lighting a cigarette).'

    # Closing quotes / signatures
    '✍️ Thread closed, if you say more, you''re right. +1 +1 +1 +1 +1 +1 +1 +1 :DDD'
    '✍️ The above content is purely fictional, any resemblance is just you being a test-taker too.'
    '✍️ Tieba bros, the main thing is authenticity (even though it''s all made up).'
)

chosen=${expressions[RANDOM % ${#expressions[@]} + 1]}

if (( $(echo -n "$chosen" | wc -m) > 80 )); then
    truncated=$(echo -n "$chosen" | head -c 80)
    truncated="${truncated}..."
else
    spaces_num=$(( 80 - $(echo -n "$chosen" | wc -m) ))
    truncated=$(printf "%${spaces_num}s%s%${spaces_num}s" "" "$chosen")
fi
echo -n "• $truncated •"
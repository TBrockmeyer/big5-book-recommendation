# big5-book-recommendation
Merging a Big 5 personality traits survey dataset with a 57k books dataset to recommend good reads for personality trait combinations

## Step 1: vectorize 57,000 book titles and their short descriptions ('blurbs')

## Step 2: vectorize the "Big 5 personality traits survey" results of each survey participant
For ease of use, we are first giving the big5 survey results as shortened free-text.
Examples, from https://fetzer.org/sites/default/files/images/stories/pdf/selfmeasures/Personality-BigFiveInventory.pdf:
"I see Myself as Someone Who Does a thorough job. I am a reliable worker, very helpful and unselfish with others. I am quite introverted and I am considerate and kind to almost everyone."
"I am original, I come up with new ideas. In creativity, I am full of energy. I have a very active imagination. I can be a bit careless sometimes."
"I have an assertive personality. I am getting things done. In our clients, I generate a lot of enthusiasm. I am sometimes rude to others, in order to save time."

## Step 3: determine the best complementary books for the personality traits combination
For simplification of this demo, we'll go for a "leverage the cosine distance to close the gaps" approach:
E.g. if a participant has given answer 2 out of 5 to "I feel comfortable around people.", we will weight this answer with 4 (6 minus 2).
If the answer was 5 out of 5 for "I start conversations.", we will weight it with 1 (6 minus 5).

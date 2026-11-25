[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/rendsstwn/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/rendsstwn/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# One picture of the world — 24 November 2026

Thirty news stories from Tuesday, 24 November 2026, packed into a
single 1024 by 1024 image. A United States jury found Huawei guilty
of stealing trade secrets and committing bank fraud on ten of twelve
counts; the IRGC struck a container ship in the Strait of Hormuz;
Israel killed the Hamas internal-security chief in Gaza; Ukraine
says it sank a Russian corvette near Libya; Senegal got its Africa
Cup of Nations title back on appeal; Nvidia gave back part of its
Monday jump; and twenty-four further stories fill out the day.
Reporting drawn from Reuters, AP, AFP, CNN, and Daily Summary Of.

## Inside the picture

A masthead up top, then a wide lead panel for the Huawei verdict,
then a three-column grid carrying the other twenty-nine stories,
each with a headline and a line or two of detail. The footer names
the sources. Everything in the picture happened on the 24th itself:
items from earlier in the week were left out on purpose.

## Running it

    python3 ./main.py

That drops the finished picture at `/output/entry.png`. The program
only copies the bundled `entry.png` with the standard library and
then re-checks what it wrote by length and SHA-256. No network, no
randomness, no timestamps: running it twice gives the same file.

Built for the make.fun bounty "Sum up 24 November's world news in
one image" — https://make.fun/bounty/news-image-20261124

The badges above link to the bounty page and the live leaderboard.

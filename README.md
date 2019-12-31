# AlphaOne

## Motivation

The past few years have observed a growing trend of artificial intelligence (AI) for game playing, including even those that can compete with human players. A notable name is AlphaGO, an AI which utilises supervised learning and reinforcement learning to play Go and achieved [certain results]. Inspired by this machine and strongly desiring to explore how AI can help mankind push its boundaries, we decided to start a project in applying reinforcement learning to game playing, **AlphaOne**.

This project is done as part of the [Math and Science Summer Program 2018] (MaSSP) in Computer Science. Our instructor is [Dr. Hung Ngo], working as a post-doctoral researcher and lecturer at the University of Stuttgart. Our team includes

- Nguyen Quang Minh, *VNU-HCM High School for the Gifted*
- Nguyen Hoang Hai, *Nguyen Binh Khiem High School for the Gifted, Quang Nam, Vietnam*
- Nguyen Duc Thang, *Le Quy Don High School for the Gifted, Ba Ria-Vung Tau, Vietnam*

## Our goal

### During MaSSP

- Applying Q-learning algorithm to the game Flappy Bird

### Further goals

- Making use of convolutional neural networks to extract visual features as input state
- Applying reinforcement learning to Gomoku and Mario

## Our results

- Understanding Flappy Bird game engine as well as referencing the Q-learning approach from GitHub repository [chncyhn/flappybird-qlearning-bot]
- Applying Q-learning algorithm to Flappy Bird with novel state space extraction and discretization methods: 
  - Diagonal distance extraction
  - Non-velocity state space
- Redesigning a fast-running Flappy Bird engine without visualization to increase training efficiency

[certain results]: https://deepmind.com/research/case-studies/alphago-the-story-so-far
[Math and Science Summer Program 2018]: https://masspvn.com
[Dr. Hung Ngo]: https://scholar.google.com/citations?user=6uHe9swAAAAJ&hl=en
[chncyhn/flappybird-qlearning-bot]: https://github.com/chncyhn/flappybird-qlearning-bot

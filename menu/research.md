---
layout: page
title: Research
---

My research focuses on the use of computational and machine learning techniques to study neural functions of the human brain, in healthy and pathological conditions. The main axes of my research lay in three areas:

* [Learning environmental regularities](#learning-environmental-regularities)
* [Outcome prediction in coma patients & consciousness](#outcome-prediction-in-coma-patients-and-consciousness)
* [Computational and machine learning techniques](#computational-and-machine-learning-techniques)

---

## Learning environmental regularities

In our day-to-day lives, we are constantly immersed in streams of sensory information. Often, stimuli from our environment, like sounds, do not occur in a random way, but follow statistical rules and repetitive patterns. Thanks to these rules we are able to learn regularities and form expectations about future events, before these occur. In my research, I am studying the neural and computational mechanisms that allow us to detect violations of anticipated events, in relation to our levels of [consciousness](https://academic.oup.com/brain/article/138/5/1160/406045/Neural-detection-of-complex-sound-sequences-in-the), [attention](http://www.mitpressjournals.org/doi/abs/10.1162/jocn_a_00835?journalCode=jocn), or complexity of these events.

#### Representative publications
* Chouiter L*, Tzovara A* et al. (2015) [Experience-based Auditory Predictions Modulate Brain Activity to Silence as Do Real Sounds.](http://www.mitpressjournals.org/doi/abs/10.1162/jocn_a_00835) J Cogn Neurosci. 27(10):1968-80. *equal contribution.
* Tzovara A, Simonin A, Oddo M, Rossetti AO, De Lucia M. (2015) [Neural detection of complex sound sequences in the absence of consciousness.](https://academic.oup.com/brain/article/138/5/1160/406045/Neural-detection-of-complex-sound-sequences-in-the) Brain 138(Pt 5):1160-6.

---

## Outcome prediction in coma patients and consciousness

During my PhD I have been using machine learning techniques to study auditory processing in post-anoxic comatose patients. In particular, I have applied multivariate EEG decoding techniques to analyze EEG responses to auditory regularities at the single patient level. We were able to show that even patients who are deeply unconscious can detect violations of [simple rules](https://academic.oup.com/brain/article/136/1/81/430538/Progression-of-auditory-discrimination-based-on) and [complex sound sequences](https://academic.oup.com/brain/article/138/5/1160/406045/Neural-detection-of-complex-sound-sequences-in-the) at a neural level. Importantly, the progression of auditory discrimination, quantified by the level of decoding performance over the two first days of coma, was predictive of the patients' chances of awakening, allowing us to establish a clinical predictor of the patients' outcome:

![Auditory discrimination](https://raw.githubusercontent.com/aath0/aath0.github.io/master/assets/img/OutComePred.jpg)
*Tzovara et al., 2013, Brain, [doi:10.1093/brain/aws264](https://www.ncbi.nlm.nih.gov/pubmed/23148350)*

#### Representative publications:

* Tzovara A, Rossetti AO, Spierer L, Grivel J, Murray MM, Oddo M, De Lucia M. (2013) [Progression of auditory discrimination based on neural decoding predicts awakening from coma.](https://academic.oup.com/brain/article-lookup/doi/10.1093/brain/aws264) Brain. 136(1):81-9.
* Tzovara A, Rossetti AO, Juan E, Suys T, Viceic D, Rusca M, Oddo M, De Lucia M. (2016) [Prediction of awakening from hypothermic post anoxic coma based on auditory discrimination.](http://onlinelibrary.wiley.com/doi/10.1002/ana.24622/full) Ann Neurol. doi: 10.1002/ana.24622.

---

## Computational and machine learning techniques
* [Machine learning techniques for analysing EEG data](#machine-learning-techniques-for-analyzing-eeg-data)
* [Modeling skin conductance & pupil responses](#modeling-skin-conductance-and-pupil-size-responses)
* [Reconstruction of subcortical sources using MEG](#reconstruction-of-subcortical-sources-using-meg)

### Machine learning techniques for analyzing EEG data
Studying neural responses to environmental stimuli through electroencephalography (EEG), typically requires averaging hundrents or thousands of single-trial responses, and contrasting them at single electrode locations. During my PhD, I used multivariate techniques to model the distribution of single-trial EEG responses across the scalp, and extract topographic EEG responses in a data-driven way. These techniques can be used to model data at the [single-patient](http://www.sciencedirect.com/science/article/pii/S0165027014003872) level, to decode [decisions from EEG responses](http://www.sciencedirect.com/science/article/pii/S1053811912001632), or to test the role of [temporal intervals in processing environmental stimuli](http://www.sciencedirect.com/science/article/pii/S1053811912001589). 

![Single trial EEG analysis](https://raw.githubusercontent.com/aath0/aath0.github.io/master/assets/img/topogr.jpg)

*Tzovara et al., 2012, Develop. Neuropsychology, [doi: 110.1080/87565641.2011.636851](http://dx.doi.org/10.1080/87565641.2011.636851)*

#### Representative publications
* Tzovara A, Murray MM, Plomp G, Herzog MH, Michel CM, De Lucia M. (2012) [Decoding stimulus-related information from single-trial EEG responses based on voltage topographies.](http://www.sciencedirect.com/science/article/pii/S0031320311001440) Pattern Recognition. 45( 6): 2109–2122.
* Tzovara A, Murray MM, Bourdaud N, Chavarriaga R, del R. Millán J, De Lucia M. (2012) [The timing of exploratory decision-making revealed by single-trial topographic EEG analyses.](http://www.sciencedirect.com/science/article/pii/S1053811912001632) Neuroimage. 60(4):1959-69.
* De Lucia M, Tzovara A. (2015) [Decoding auditory EEG responses in healthy and clinical populations: A comparative study.](http://www.sciencedirect.com/science/article/pii/S0165027014003872) J Neurosci Methods. 250:106-13.

### Modeling skin conductance and pupil size responses
Using environmental cues to predict threat is a crucial skill, encountered in many species, however a computational understanding of this process at a system's level is lacking. We used modeling of psychophysiological responses (i.e. skin conductance and pupil size responses) to study which computational model best predicts activity of the human autonomic nervous system (ANS) during fear conditioning. We found that ANS activity is best explained by a probabilistic learning model that accounts for uncertainty in  threat estimation. Furthermore, skin conductance and pupil responses map onto different learning quantities: pupil size reflects the estimated threat probability, but skin conductance reflects a combination of this and the uncertainty of the estimate.

![Modeling associative learning](https://raw.githubusercontent.com/aath0/aath0.github.io/master/assets/img/Fig3.jpg)


#### Representative publications
* Khemka S*, Tzovara A*, Gerster S, et al, 2017. [Modelling startle eye blink electromyogram to assess fear learning.](https://onlinelibrary.wiley.com/doi/full/10.1111/psyp.12775) Psychophysiology, 54, 202-214.
* Tzovara A, Korn C,  Bach D R, 2018. Human Pavlovian fear conditioning conforms to probabilistic learning. PLOS Computational Biology, in press).

### Reconstruction of subcortical sources using MEG

under construction

# ArWordVec: efficient word embedding models for Arabic tweets

ArWordVec is a collection of pre-trained word embedding model built from huge repository of Arabic tweets in different topics. The aim of these models is to support the community in their Arabic NLP-based research. In order to build an efficient word embedding model on Twitter Arabic data, we decided to collect millions of tweets from multiple domains and hashtags to boost theword embedding model with the diverse usage of the words within the different topics. We collected about 55 Million tweets within different topics covering the educational domain, health care, politics, social affairs, etc.

We have investigated many techniques for building word embedding models with the different parameters, which are **word2vec**, proposed by Google in 2013, that supports the **continuous bag-of-words (CBOW)** and **skip-gram (SG)** approaches, and **GloVe** toolkit, proposed by Stanford NLP Group in 2014. Several models have been generated and named as **‘model-d-w-m’**. For example, **CBOW-500-3-400** is the model built with _CBOW_ approach that has _vector size of 500_, _window size equal to 3_, and the _minimum word count is set to 400_.

## ArWordVec Models - Download
### Word2Vec - Skip Gram (SG)
| Model              | Vector size   | Window size   |     Link    |
| ------------------ |:-------------:|:-------------:|:-----------:|
| SG-300-3-400       | 300           |   3           |[Download][M1] |
| SG-300-5-400       | 300           |   5           |[Download][M2] |
| SG-500-3-400       | 500           |   3           |[Download][M3] |
| SG-500-5-400       | 500           |   5           |[Download][M4] |

### Word2Vec - Continuous Bag-of-words (CBOW)
| Model              | Vector size   | Window size   |     Link    |
| ------------------ |:-------------:|:-------------:|:-----------:|
| CBOW-300-3-400     | 300           |   3           |[Download][M5] |
| CBOW-300-5-400     | 300           |   5           |[Download][M6] |
| CBOW-500-3-400     | 500           |   3           |[Download][M7] |
| CBOW-500-5-400     | 500           |   5           |[Download][M8] |


## ArWordVec Models - How to use
### Install Required Libraries
The above models were built using the `gensim` library that can be installed using `pip` or `conda` using the following commands:

`pip install gensim`

`conda install gensim`

### Load the models
After you download and extract the required ArWordVec model, for example **SG-300-3-400**, you can find three files named as:
  1. SG-300-3-400.model
  2. SG-300-3-400.model.trainables.syn1neg.npy
  3. SG-300-3-400.wv.vectors.npy

You will only use the first one while your are loading the model, **but the other two files must be kept in the same path**.

In your python script, just add the following lines:
```python
import gensim
file_path = 'SG-300-3-400.model'
word_embed = gensim.models.Word2Vec.load(file_path)
```
> For more information about how we preprocess the Arabic tweets before building the models, please check `preprocess_tweets.py` script.

## Acknowledgements
We express our thanks to the administration of the High Performance Computing Center (HPCC) at King Abdulaziz University, Jeddah, Saudi Arabia, for their support and the access to the Aziz Supercomputer that helped us in performing our experiments which require both huge computing capabilities and storage space.

## Citation
M.M. Fouad, A. Mahany, N. Aljohani, R.A. Abbasi, and S.-U. Hassan, “ArWordVec: Efficient word embedding models for arabic tweets,” **Soft Computing**, vol. 24, no. 11, pp. 8061–8068, 2020. https://doi.org/10.1007/s00500-019-04153-6


[M1]: https://rebrand.ly/wsccyws
[M2]: https://rebrand.ly/4cfzcao
[M3]: https://rebrand.ly/7qomutb
[M4]: https://rebrand.ly/xwvpirk
[M5]: https://rebrand.ly/jvfyexo
[M6]: https://rebrand.ly/yyp4d0x
[M7]: https://rebrand.ly/kguzz84
[M8]: https://rebrand.ly/g05sxcy

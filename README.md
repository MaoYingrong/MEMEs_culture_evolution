# How do Communication Meme Evolve in Digital Culture?  

**Introduction**
* This project aims to study the evolution of communication symbols by using Internet memes as a case study. The rise of the internet and social media has brought digital icons to the forefront of communication symbols, transforming them into a fundamental aspect of daily communication. Internet memes represent more than merely humorous images paired with text; they constitute a new genre of online communication that is created, perceived, imitated, remixed, and modified by users across digital platforms (Wiggins & Bowers, 2015). Similar to other forms of popular culture, only a limited number of images capture widespread public attention and the popularity of these chosen images fluctuated over time. Beyond individual meme templates, it is valuable to explore whether there are more significant, macro-level trends in the development of memes within digital culture, as well as the mechanisms driving such trends.  
* Accordingly, this study can be broken down into the following specific questions:
  * Are there macro-level changes observable in the development of internet memes over time?
  * What are the mechanisms that contribute to changes in the forms and popularity of internet memes?     


**Data**:    
  * All posts (2008/12 - 2023/12) from a subreddit called “meme”, which is the earliest and the second largest meme community in Reddit with more than 2.6 million members. Each data point includes the title, meme image, description, posting time, upvote number, upvote ratio, author ID, and comments.
  * Details:
    * Meme: Number of original posts: 1,508,474; Number of posts with images downloaded: 896,449. (filtered_submission, size: 2.8 G); Number of original comments: 7,128,785; Number of filtered comments: 5,303,614. (filteres_comments, size: 6.8 G); Images size: 234G.
    * Memes:
    * Dankmemes: 
   

   
**Methods**:  
  * Data Collection  
    * Based on the metadata obtained from Academic Torrents, download the corresponding image of each post, delete the empty pages (the post was deleted), select the content with .jpg or .png formats, and select corresponding submissions info and comments info.
    * Store all data in the Midway HPC.
  * Data Processing
    * Use a pre-trained neural network (Resnet50) to extract features of all images, then use HDBSCAN clustering methods to group meme images based on whether they’re using the same template.
    * Use a pre-trained model to extract text from meme images.
  * Data Analysis
    * Link all/most meme clusters to the meme template in the [Know Your Meme](https://knowyourmeme.com/) website, which provides a series of tags, such as “animal” ”film
adaptation” and “rage face”. Explore higher-level grouping.
    * Also try to use the results of NLP analysis on titles and text on images, sentiment analysis on each image, upvotes, upvote ratios, and comments, combined with the results of the content analysis above, to measure the ambiguity of meme templates.
    * Divide all data into time units (one week) and calculate the portion of each meme group. Use the number of appearances of meme templates within groups to measure their popularity and dominance over time.
    * Analyze the changing pattern of meme groups.
    * Use time-series statistical models to analyze the evolutionary mechanism of internet memes (Diversification Rate).

# How do Communication Meme Evolve in Digital Culture?  

**Introduction**
* This project aims to study the evolution of communication symbols by using Internet memes as a case study. The rise of the internet and social media has brought digital icons to the forefront of communication symbols, transforming them into a fundamental aspect of daily communication. Internet memes represent more than merely humorous images paired with text; they constitute a new genre of online communication that is created, perceived, imitated, remixed, and modified by users across digital platforms (Wiggins & Bowers, 2015). Similar to other forms of popular culture, only a limited number of images capture widespread public attention and the popularity of these chosen images fluctuated over time. Beyond individual meme templates, it is valuable to explore whether there are more significant, macro-level trends in the development of memes within digital culture, as well as the mechanisms driving such trends.  
* Accordingly, this study can be broken down into the following specific questions:
  * Are there macro-level changes observable in the development of internet memes over time?
  * What are the mechanisms that contribute to changes in the forms and popularity of internet memes?     


**Data**:    
  * All posts (2008/12 - 2023/12) from a subreddit called “meme”, which is the earliest and the second largest meme community in Reddit with more than 2.6 million members. Each data point includes the title, meme image, description, posting time, upvote number, upvote ratio, author ID, and comments.
  * Details:
    * Number of original posts: 1,508,474; Number of posts with images downloaded: 896,449. (filtered_submission, size: 2.8 G)  
    * Number of original comments: 7,128,785; Number of filtered comments: 5,303,614. (filteres_comments, size: 6.8 G)  
    * Images size: 234G.   
   

   
**Methods**:  
  * Data Collection  
    * Based on the metadata obtained from Academic Torrents, download the corresponding image of each post, delete the empty pages (the post was deleted), select the content with .jpg or .png formats, and select corresponding submissions info and comments info.
    * Store all data in the Midway HPC.
  * Data Processing
    * Perform perceptual hashing and Locality Sensitivity Hashing to classify memes into different clusters based on whether they use the same templates (visual characteristics such as the main figure on the images).
    * Extract text from memes and store them in a single file with links to posts.
  * Data Analysis
    * Use natural language processing (NLP) techniques to analyze titles, descriptions, and texts extracted from the memes for content meaning (mainly topic and sentiment).
    * Use upvotes, upvote ratios, and comments, combined with the results of the content analysis above, to measure the ambiguity of meme templates.
    * Use the amount of meme templates’ appearance in a fixed time period (one week or one month) to measure their popularity and dominance over time.
    * Use time-series regression or other models to analyze the progression of memes over time to observe how certain templates or memes evolve. Track changes in meme format, message, and themes as they are adapted and remixed by users. Map out meme variations to explore how collective understanding emerges and whether it encounters twists and turns. Examine how ambiguity or lack thereof might have contributed to their spread across the subreddit.  
  * Case Studies:
    * Select one or a few certain meme templates for more detailed interpretation in the paper. Analyze their evolution, spread, and the types of discourse they generate in the comments. This will help illustrate the dynamic between agency, vagueness, and collective understanding.  


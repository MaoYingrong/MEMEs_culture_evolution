# Exploring Collective Understanding and Ambiguity in Culture Evolution  
## A Study of Meme Production and Dissemination in the Largest Reddit Meme Community

**Introduction**
* This project aims to study the popularity and evolution of memes. Based on
Wiggins’ theory that memes represent a new genre of online communication, I first start by exploring how the customizability of a meme image affects its popularity. While high customizability can encourage creativity and agency, it may also conflict with the establishment of collective understanding. (However, this question may become problematic because of bidirectional causality, or endogeneity, so I’ll look for other features related to communication.) For the part of meme evolution, I want to combine its popularity/dominance analysis with cultural evolution theories, to understand meme evolution from the population level instead of the individual level (for a few meme images).
* This project offers a large-scale, systematic investigation of meme evolution, remixing, and user engagement. By providing a deeper understanding of digital culture, collective meaning-making, and cultural reproduction, this research has broader implications for media studies and our understanding of communication in digital spaces.  
**Research Questions**:  
  * How do internet memes as a genre of communication facilitate the creation of collective understanding within online communities, particularly through production, dissemination, and remixing?  
    * What patterns of interaction, imitation, and modification emerge during the evolution of meme content on the subreddit?  
    * How do users engage with and co-create meaning through memes? Is the process of reaching collective understanding smooth or does it involve disruptions or reinterpretations?  

  * How does the ambiguity (the diversification of sentiment and topics) of meme templates impact their popularity and the process of their spread across the community?  
    * Does a higher degree of vagueness in a meme’s format (in terms of meaning or message) encourage greater creativity and user participation?  
    * How does the balance between ambiguity (agency) and shared cultural understanding affect the viral potential of memes on the subreddit?  


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


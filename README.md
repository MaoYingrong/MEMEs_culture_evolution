# Exploring Collective Understanding and Ambiguity in Culture Evolution  
## A Study of Meme Production and Dissemination in the Largest Reddit Meme Community

**Introduction**
Internet memes are a vital part of digital culture, functioning not as singular units of cultural transmission but as a genre of communication. They are inherently tied to agency, as their production and dissemination involve constant changes, imitations, remixes, and modifications (Wiggins, 2019). Like other cultural forms, memes evolve through interaction, production, and the co-creation of meaning. Shifman (2013) suggests that memes should be understood as “groups of content items created with awareness of each other and sharing common characteristics” (p. 367). This project aims to explore how collective understanding is formed through meme interactions—whether this process is smooth or involves significant reinterpretations—and whether such understanding remains stable or shifts over time. Additionally, the study will examine how the ambiguity of meme templates affects their popularity and spread. While vagueness can encourage creativity and agency, it may also conflict with the establishment of collective understanding.   
Significance: This project offers a large-scale, systematic investigation of meme evolution, remixing, and user engagement. By providing a deeper understanding of digital culture, collective meaning-making, and cultural reproduction, this research has broader implications for media studies and our understanding of communication in digital spaces.

**Research Questions**:  
  * How do internet memes as a genre of communication facilitate the creation of collective understanding within online communities, particularly through production, dissemination, and remixing?  
    * What patterns of interaction, imitation, and modification emerge during the evolution of meme content on the subreddit?  
    * How do users engage with and co-create meaning through memes? Is the process of reaching collective understanding smooth or does it involve disruptions or reinterpretations?  

  * How does the ambiguity (the diversification of sentiment and topics) of meme templates impact their popularity and the process of their spread across the community?  
    * Does a higher degree of vagueness in a meme’s format (in terms of meaning or message) encourage greater creativity and user participation?  
    * How does the balance between ambiguity (agency) and shared cultural understanding affect the viral potential of memes on the subreddit?  


**Data**:    
  * All posts from a subreddit called “meme”, which is the largest meme community in Reddit with about 2.5 million members. Each data point includes the title, meme image, description, posting time, upvote number, upvote ratio, author ID, and comments.
  * Details:
    * Number of original posts: 1,508,474; Number of posts with images downloaded: 896,449. (filtered_submission, size: 2.8 G)  
    * Number of original comments: 7,128,785; Number of filtered comments: 5,303,614. (filteres_comments, size: 6.8 G)  
    * Images size: 234G (images).   
   

   
**Methods**:  
Data Collecting and Pre-processing   
Based on the metadata obtained from Academic Torrents, download the corresponding image of each post, delete the empty pages (the post was deleted), and select the content with .jpg or .png formats.    
Perform image recognition (e.g., through CNN) to classify meme templates and identify relationships between similar memes based on visual characteristics and variations.
Extract text from memes to analyze both visual and textual content.   
Use natural language processing (NLP) techniques to analyze titles, descriptions, and texts extracted from the memes for content meaning (mainly topic and sentiment). 
Use upvotes, upvote ratios, and comments, combined with the results of the content analysis above, to measure the ambiguity of meme templates. 
Use the amount of meme templates’ appearance in a fixed time period (one week or one month) to measure their popularity and dominance over time. 
Use time-series regression or other models to analyze the progression of memes over time to observe how certain templates or memes evolve. Track changes in meme format, message, and themes as they are adapted and remixed by users. Map out meme variations to explore how collective understanding emerges and whether it encounters twists and turns. Examine whether certain memes lead to clear, shared meanings or foster debate, ambiguity, and reinterpretation.
Case Studies:   
Select specific meme templates with different levels of ambiguity for qualitative case studies. Analyze their evolution, spread, and the types of discourse they generate in the comments. This will help illustrate the dynamic between agency, vagueness, and collective understanding.
Examine viral memes to assess how ambiguity or lack thereof might have contributed to their spread across the subreddit.


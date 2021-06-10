# Tagger version 1.0

Tagger is made by @NotSujal

## What is Tagger?

Tagger is a specialised tagbot to store all type of data. Tags are easily customisable within the discord.



## Why Tagger and How Tagger Works?

### Adding a tag
command: `<add [tag] [answer]`

Every User (in discord) is able to **add tags** and **edit tags**.
The users are classified as ***Tagmanagers*** and ***Normal Users***.

Both users and Tagmanagers are able to add tags.
The tags are then stored in the `unverified_tags` list untill they are verified. 

Note: if the tag is unverified then `  ⛔(unverified)` is added to the tag.

### Verification of tags
command: `<verify [tag]`

Only the *TagManagers* can verify the tags to keep the tags SFW.
After verification the tags are then moved to `verified_tags` and  `⚡(is verified) ` is added to the tag.

### searching for a Tag
command: `<tag [query]`

Once the command is deployed, tagger finds the tag in the *verified_tags* and sends the stored output.
If it doesn't finds the tag , it will go through the *unverified_tags* and find the tag.
If it doesn't find the mentioned tag in any of these lists it will search it on google and send the top most output(link) to the user.

### requesting for a tag
command: ` <requestedtags`

If tagger doesn't finds the tag in the saved data.
It will add the tag as a request in `requested_tags`.
All the requested Tags are visible with the help of the command.
A TagManager can satisfy the tag(enter the data) and remove the request from the list.

### remove the satisfied tags
command:`<delrequests [request]`

If the requested tag is NSFW/already satisfied a Tagmanager can delete the request.

### edit tags 
command:(for unverified) `<editunverified [query] [edited_answer]`
command: (for  verified)`<editunverified [query] [edited_answer]`

### more tagmanagers
command: `<addtagmanager`

Using this command you can add new tagmanagers.
only Tagmanagers can summon/recruit new tagmanagers
*ONLY ADD TRUSTED MEMBERS, ANY MISBEHAVE MAY LEAD TO SERIOUS TROUBLE*
**DONOT BEHAVE RUBBISH AS A TAGMNAGER, YOU MIGHT LOOSE THE TAGMANANAGER ROLE**

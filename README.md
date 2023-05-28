# Tagger v1.0

## Overview

Tagger is a professional and versatile tagbot designed to efficiently store various types of data. It offers customizable tags within the Discord platform, allowing users to easily manage and access information.

## Key Features

### Adding Tags
Command: `<add [tag] [answer]`

Both normal users and designated Tag Managers have the ability to add and edit tags. When a tag is added, it is initially stored in the `unverified_tags` list until it undergoes verification. Unverified tags are marked with the symbol ⛔ to indicate their status.

### Tag Verification
Command: `<verify [tag]`

Only Tag Managers have the authority to verify tags, ensuring that all tags remain safe for work (SFW). Once verified, tags are moved to the `verified_tags` list and labeled with the symbol ⚡ to indicate their verified status.

### Tag Search
Command: `<tag [query]`

When this command is executed, Tagger searches for the requested tag within the `verified_tags` list and retrieves the stored information. If the tag is not found in the verified tags, Tagger then searches the `unverified_tags` list. If the tag is still not found, Tagger performs a search on Google and returns the topmost result (link) to the user.

### Tag Requests
Command: `<requestedtags`

If Tagger is unable to locate a requested tag within the saved data, it adds the tag as a request in the `requested_tags` list. All requested tags can be viewed using this command. Tag Managers have the ability to fulfill these requests by providing the relevant data and removing the request from the list.

### Removal of Satisfied Tags
Command: `<delrequests [request]`

Tag Managers can delete requests from the `requested_tags` list if the requested tag is either not safe for work (NSFW) or has already been satisfied.

### Tag Editing
Command (for unverified tags): `<editunverified [query] [edited_answer]`
Command (for verified tags): `<editunverified [query] [edited_answer]`

Users can edit tags using these commands, both for unverified and verified tags.

### Additional Tag Managers
Command: `<addtagmanager`

Tag Managers have the authority to add new Tag Managers using this command. Only trusted members should be added, as any misconduct may lead to serious consequences. It is important for Tag Managers to maintain a professional behavior to retain their role.

Thank you for using Tagger! If you have any questions or require assistance, please contact at sjlchoudhari@gmail.com.

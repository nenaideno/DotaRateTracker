<span style='font-size: 16px;'>

# Afterword

**I did not write a single line of code.**

Code/text for all files you see in the project *(except for this file and git files)* **WAS GENERATED USING ChatGPT 3.5**


## In total, using **ChatGPT 3.5** we wrote:
- Contents of `first.py` file
- Contents of `second.py` file
- The contents of the `gui.py` file
- The contents of the `requirements.txt` file
- Invented project name `DotaRateTracker`
- Invented `description` of the project
- The contents of the file [README.MD](./README.md)
# Target
The purpose of this project was to test the capabilities of ChatGPT 3.5 in writing working code.

# Conclusions
As a conclusion, I can say that everything is not as straightforward as it seems at first glance.
Chat GPT 3.5 is still **not capable** of generating fully working (bug-free) code the first time around. Moreover, we can say with confidence that a person without at least minimal knowledge in **programming** *(the ability to write in any high-level programming language)*, as well as an understanding of **features** of writing a particular software *(in this case - RESTful API Query Principles)*, **won't** be able to write a full working program using **Chat GPT 3.5**.

## While writing a program using **Chat GPT 3.5**, I had to deal with the following nuances:
- Chat GPT occasionally **messed up** in native code. It made mistakes both in **sending a request** *(wrong endpoints)*, and in **reading the response** *(reference to non-existent keys)*.
- Had trouble compiling the **dependency file** *(requirements.txt)*, and **writing the README** *(he also didn't succeed the first time and had to force him to make a few edits)*.

## Otherwise, he showed himself worthy. However, I would like to highlight the following features that *(maybe)* help those who will try to write something on their own using Chat GPT:
1) When forming requests (regarding the content of the program), you should start with the simplest code in terms of execution and structure, and gradually complicate it, leading to the form you need. This will allow ChatGPT to better follow the progress of development, and "deeper" to capture the essence of your idea.
2) If you are going to ask ChatGPT for an alternative version of code already written, or want to make changes while keeping the old version, you can just say something like "Let the code written above be program number N", or start writing a new version from words "Write program number N". This, at the right time, you can force ChatGPT to "forget" a certain version of the program. ("Let's forget program number N").
3) You can send to it messages with errors that occur during the work of the code it wrote, and ask: "rewrite the program, taking into account the correction of the error." It will listen, and most likely - will make changes to the original code that caused the error, returning the new code in full.
4) Keep in mind that in ChatGPT 3.5 there is a limit on the number of tokens for withdrawal. This means it is impossible for the bot to write more than a certain number of characters.If suddenly the writing of the code breaks off in the middle of the presentation, then you can simply ask him to "continue from where he left off." Most likely this will solve the problem. However, it is better not to increase the program so much in size, and if possible, try to separate different functions into different files (look at the point 2)
5) If something is not clear to you, you can ask him to explain the code it wrote.
6) You can roll back to a previously written version of the program. To do this, write something like "Let's forget about some recent changes in the program, and return to this stage ...", after which you need to paste the code that you need to return. It will listen to you, and "roll back" the changes to an earlier version (a kind of analogue of branches in GIT).
7) In general, GUIs are quite difficult for it. However, it is able to do something simple ...

That's all for now, if there are any other tips, I will replenish this file as they appear.
Thanks for reading, and thanks to OpenAI for a unique "development" experience!

</span>
# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  When I first ran the game, it launched in the browser through Streamlit and appeared functional but several bugs became obvious after playing. The hints were backwards. The score was wrong as it didn't change for the first few attempts and went negative randomly and also increased from 0-5 on wrong answers. The attempt counter seemed off for some of the rounds and didn't match the history.The new game button wasn't working either.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|guess:20(lower than actual num) |hint-lower |hint-higher|none |
|Multiple guesses- (99,98,900) | score decreases|score stays positive  |none |
|new game button |launch a new game|nothing happens |none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
claude code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
-Claude code suggested moving 'check_guess' from 'app.py' into 'logic_utils.py'. It suggested fixing the swapped hint messages so that "Too High" returns "Go LOWER" and "Too Low" returns "Go HIGHER". This was correct. I verified it by running 'pytest' and all 3 tests passed, and I also confirmed it worked in the live game by playing a round and checking the hints matched my guesses.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Claude code suggested clearing the text input after clicking New Game by directly setting st.session_state[f'guess_input_{difficulty}'] = ''. This was incorrect because Streamlit doesn't allow modifying a widget's session state after it's been instantiated, and it caused a StreamlitAPIException error. I caught this by running the game and seeing the error, then worked with Claude to fix it using an input_key counter instead.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed when the live game behaved correctly and pytest passed. For the hint bug, I ran pytest and 3 tests passed. I also played the game which also confirmed that a guess of 60 against a secret of 50 correctly returns "Too High" with "Go LOWER". For the button bug, I manually tested by playing and clicking the New Game buttonand verified the score reset to 0 and the text input emptied. Claude code helped me generate the pytest by writing tests that specifically targetted the hint and button fix, which helped me understand what the expected output should be for each scenario.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
The Streamlit app reruns the whole script every time you interact with it, so variables reset unless you store them in session state. I learned this when trying to clear the text input after new game, it kept throwing an error because you can't modify a widget after it's already been created. I ended up using an input_key counter to just make a new input box instead.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I want to keep using FIXME comments before touching any bug as it kept me organized. I also would continue prompting this way by providing details and pinpointing the bug exactly to get accurate results. Next time, I would review the diff more carefully and test each change in more detail before commiting. This project made me realize AI code can look fine but still have hidden logic bugs. I realised the importance of running pytest and manually playing through the game as it showed me things I would not have caught just by reading the code.

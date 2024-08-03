![Screenshot (213)](https://github.com/user-attachments/assets/56bd7acd-0d87-4900-b903-f0e77314590c)
![Screenshot (214)](https://github.com/user-attachments/assets/7ae8081b-b3f7-4ce6-b9ac-56ee6b202121)
### Multi-Agent Workflows

Multi-agent workflows involve breaking down complex tasks into subtasks executed by agents, each assigned a specific role.

#### Examples:
- **Research Report**: Roles include researcher, writer, and fact-checker.
- **Website Development**: Roles include web designer, software engineer, and testing engineer.

### Major Building Blocks for Agentic Systems:
1. **Role-playing**
2. **Tool Use**
3. **Memory**
4. **Guardrails**
5. **Collaboration**

### Applications:
- Customizing resumes to job descriptions
- Performing financial analysis
- Event planning

### Workflow Assembly:
- Define agent cooperation
- Determine delegation of tasks among agents
- Decide execution style: parallel, series, or hierarchical with manager and worker agents

### Key Takeaways:
- Think like a manager of agents
- Identify goals and roles
- Define success criteria
- Shift from regular engineering to multi-agent systems design
### Large Language Models (LLMs) and AI Agents
#### Overview:
- LLMs come in various shapes and sizes from different vendors (e.g., OpenAI, Hugging Face, Ollama).
- They predict the most likely next token in a sequence, enabling tasks like chatting, content creation, and more.

#### Interaction with LLMs:
- Interacting with LLMs, like ChatGPT, involves prompting and providing feedback to improve responses.
- Continuous interaction and feedback refine the model's output, but this can be time-consuming and requires active user involvement.

#### Autonomous AI Agents:
- AI agents can operate autonomously, allowing users to delegate tasks and focus on other work.
- These agents leverage LLMs' extensive training data and text understanding to make decisions and perform tasks independently.
- Agents can ask and answer questions within their process, improving over time.

#### Tool Use and Capabilities:
- AI agents can use tools or capabilities (SKUs) to interact with the external world, such as calling APIs, posting content, and gathering data points.
- This extends the agent's functionality beyond its internal capabilities.

#### Multi-Agent Systems:
- Multi-agent systems build on individual agent behavior, enabling collaboration between multiple agents.
- Each agent can specialize in a specific task (e.g., research, writing), allowing for optimized performance.
- Different agents can run on various LLMs, enhancing the system's overall capabilities.

#### Benefits of Multi-Agent Systems:
- Specialization: Each agent focuses on one task, ensuring high-quality output.
- Diversity: Combining agents with different strengths leads to a more powerful system.
- Collaboration: Agents work together to produce a cohesive final outcome.

#### Building AI Agents:
- Agents can be built from scratch or using frameworks that provide building blocks.
- Training agents carefully is crucial to achieving desired behavior and optimizing performance.

#### Summary:
- Multi-agent systems leverage LLMs and AI agents to perform complex tasks autonomously and collaboratively.
- This approach enhances efficiency, quality, and flexibility in achieving various goals.
![Screenshot (215)](https://github.com/user-attachments/assets/40026866-b422-42f3-9686-07f240cd3230)
![Screenshot (216)](https://github.com/user-attachments/assets/241fc2cf-5120-4c58-a806-1a80f4d9b8aa)

![Screenshot (217)](https://github.com/user-attachments/assets/b2bca7bb-efb8-4a27-ac4d-de8490d49685)
![Screenshot (218)](https://github.com/user-attachments/assets/9f8cc2c5-b687-45e0-a759-009cdbee5165)

![Screenshot (219)](https://github.com/user-attachments/assets/58b3afbe-fb4e-445d-a200-b0dd12f38f8b)

![Screenshot (220)](https://github.com/user-attachments/assets/5d2f4724-4968-4640-9309-380905db9367)
## Video Transcript Notes

### Role Playing
- **Role Playing Importance:** Enhances the responses from agents.
- **Impact:** Allows agents to take on different roles, affecting the quality and relevance of their answers.
- **Example:** 
  - Asking ChatGPT for analysis on Tesla stock.
  - Setting context: “You are a FINRA approved financial analyst.”
  - Result: Different, more contextually relevant answers.
- **Takeaway:** Be mindful in setting appropriate roles for agents to get better results.

### Context Setting
- **Keyword Use:** Using specific keywords like "FINRA" helps direct the type of answer.
- **Customer Success:** Users of crewAl have seen significant improvements with this technique.
- **Guideline:** Carefully choose roles, backstory, and keywords to improve agent responses.

### Agent Building
- **Next Topic:** Building your agents effectively.

### Context Window and Hallucination
- **Context Windows:** Modern LLMs have longer context windows.
- **Issue:** Mixing too much information or tools can increase hallucinations.
- **Advice:** Focus on specific tasks and clear goals for each agent.

### Multiple Agents
- **Better Performance:** Multiple agents focusing on specific tasks perform better than a single multitasking agent.
- **Industry Insight:** Users of crewAl see improved results with multiple agents.

### Tools for Agents
- **Tool Selection:** Providing too many tools can confuse agents.
- **Efficiency:** Choose relevant tools to ensure agents use them effectively.

### Cooperation
- **Importance:** Agents collaborating and bouncing ideas off each other produce better outcomes.
- **Simulated Chat Behavior:** Allows agents to delegate tasks and improve results through feedback.

### Guardrails
- **Necessity:** Prevent agents from derailing, getting stuck, or repeating tools.
- **Implementation:** Guardrails are essential to maintain reliable and consistent results.
- **crewAl Specific:** Guardrails are integrated at the framework level in crewAl.

### Memory
- **Critical Role:** Memory significantly impacts agent effectiveness.
- **Types of Memory:**
  - **Long-Term Memory:** Retains information over extended periods.
  - **Short-Term Memory:** Active during a single session, shared across agents.
  - **Entity Memory:** Specific to entities like customer details.
- **Usage:** Agents learn from past actions to improve future performance.
- **Shared Memory:** Prevents agents from working in silos, fostering better collaboration.
- **Inconsistency Prevention:** Memory helps avoid inconsistencies and unreliable results.

### Conclusion
- **Next Lesson:** How to build your own agents with a focus on practical implementation.

![Screenshot (137)](https://github.com/user-attachments/assets/72706a7d-19b9-49d6-a4bb-87bedc3fcc1a)


![Screenshot (140)](https://github.com/user-attachments/assets/ab34df85-7a20-48dc-946e-52bddbc0d71e)

![Screenshot (141)](https://github.com/user-attachments/assets/9702a8fb-806f-48e8-a538-9f1b48e93084)
![Screenshot (142)](https://github.com/user-attachments/assets/1fbe981b-4bb4-4079-9fb5-2d866b9cbf22)
![Screenshot (143)](https://github.com/user-attachments/assets/593b9fe6-4872-42f2-b7eb-5d16a5aa8d64)
![Screenshot (144)](https://github.com/user-attachments/assets/98eafac1-5222-4a9e-b7a0-421bbdd8866c)
![Screenshot (145)](https://github.com/user-attachments/assets/3bb25711-c908-45a2-bf62-2265e3dea302)
![Screenshot (146)](https://github.com/user-attachments/assets/da1671c7-c165-4359-a343-b26ffa57bfc6)
![Screenshot (164)](https://github.com/user-attachments/assets/999c32b0-7368-4d5f-b4ef-5bd630fac326)

![Screenshot (165)](https://github.com/user-attachments/assets/e5b2149c-e379-490f-8c0f-6159e8bf3c23)


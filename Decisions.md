# Code of the Day App – Architecture Notes

## Key Decisions

1. **Vector Databases & RAG Pipelines**  
   We will use vector databases and simple Retrieval-Augmented Generation (RAG) pipelines for:
   - Code snippet detection
   - Code understanding
   - User input handling
   - Generating contextual understanding and responses

2. **Vector Database Sources**  
   Vector databases can be sourced from many platforms — Hugging Face provides several options and tools for this purpose.

3. **Model & Tooling Stack**  
   We are leveraging Hugging Face models and common ML tools as follows:

   | Task                   | Tool/Library to Use                   | Need to Train?        |
   | ---------------------- | ------------------------------------- | --------------------- |
   | Generate vectors       | `sentence-transformers` (HuggingFace) | ❌ No                  |
   | Compare vectors        | `cosine_similarity` from `sklearn`    | ❌ No                  |
   | Store vectors          | JSON / SQLite / FAISS                 | ❌ No                  |
   | Pull new snippets      | `requests` + GitHub API               | ❌ No                  |
   | (Optional) Gen answers | `StarCoder`, `CodeT5`, `Mistral`      | ❌ No (if using local) |

## Requirements

- **PyTorch**  
  Required to run `sentence-transformers`. While you don’t need to deeply learn PyTorch, having a good grasp of its usage and implications is helpful.

- **CUDA**  
  If running on GPU, you’ll need CUDA installed to enable PyTorch to leverage GPU acceleration.

---

Also you have to intall CUDA and pytorch right now also install CUDA for deeplearning Search exactly

4. **What has been done till now**
using sentence-transformers we were able to chage the SQL database into something that whenever it receives an answer it converts it into verctor embeddings +it sotres the answers, the question and a unique I number,.

)

**Pipeline To-Do List**
 Show the code snippet in the UI

 Take user's input in plain text

 Convert user input into an embedding

 Compare it with original answer embedding

 Use cosine similarity to get a score

**Then:**

 Auto-pull code snippets from GitHub using GitHub API

 Use AI (like Mistral or StarCoder) to auto-generate the expected answer

That way I don’t have to write every answer manually

And the model itself can understand & compare in natural language
# **Python Prompt Generator Tool**

This Python script efficiently generates customized prompts using a template and a CSV file containing key-value pairs.

## **Installation**

**Prerequisites:**

* Python (version 3.x recommended)

**Steps:**

1. **Clone or download the repository:** (Add instructions if the project is on GitHub or similar)
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## **Usage**

**1. Prepare your files:**

   * **key-values.csv:**
     * Create a CSV file with columns representing the keys to be replaced in your template.
     * Each row will define the values for a single prompt.

   * **prompt.txt:**
     * Design your prompt template.
     * Enclose keys from 'key-values.csv' within `**/key/**` tags (e.g., `**/city/**`).

**2. Run the script:**

   ```bash
   python main.py [--description-mode] 
   ```

   * **Optional:** Use `--description-mode` to exclude titles and focus on city names in your prompts.

## **Explanation**

* **CSV File ('key-values.csv')**
   Each column header represents a key to be replaced. Rows contain corresponding values. See example:

   ```csv
   title, city, country
   Explore the Charm of, Paris, France
   A Journey Through, Tokyo, Japan
   ```

* **Prompt Template ('prompt.txt')**
   Use `**/key/**` to mark replacement points. Example:

   ```
   Write a travel blog titled "**/title/**" about the captivating city of **/city/**, **/country/**.
   ```
   
* **Output**
   Generated prompts are saved as individual .txt files within a specified folder.
   ```
   Write a travel blog titled "Explore the Charm of" about the captivating city of Paris, France.
   ```

## **Terminology**

* **key:** A column header in 'key-values.csv', used as an identifier in the template.
* `**/key/**`:  Indicates a placeholder in the template, to be substituted with values from 'key-values.csv'.

## **Contributing**

Feel free to submit bug reports, feature requests, and pull requests! 

## **License**

[Include the appropriate license for your project]

## **Key Improvements:**

* **Concise and Clear Title:** Emphasizes the tool's main functionality.
* **Structured Installation:** Guides users with prerequisites and step-by-step instructions.
* **Detailed Usage:** Explains file preparation and script execution with clarifying examples.
* **Enhanced Explanation:** Provides visuals to demonstrate the CSV structure and prompt template format.
* **Consistent Terminology:** Maintains a glossary for easy reference.
* **Inviting Contributions and Licensing:** Encourages community engagement and clarifies usage rights.


## **Known Exceptions and Error:**

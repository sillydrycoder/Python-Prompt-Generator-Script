# **Python Prompt Generator Tool**

This Python script efficiently generates customized prompts using a template and a CSV file containing key-value pairs.

## **Installation**

**Prerequisites:**

* Python (version 3.x recommended)

**Steps:**

1. **Clone or download the repository.**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## **Usage**

**1. Understand your files (Not necessary already done.):**

   * **key-values.csv:**
     * Create a CSV file with columns representing the keys to be replaced in your template.
     * Each row will define the values for a single prompt.

   * **prompt.txt:**
     * Design your prompt template.
     * Enclose keys from 'key-values.csv' within `**/key/**` tags (e.g., `**/city/**`).

**2. Run the script:**

   ```bash
   python main.py [-d] 
   ```

   * **Optional:** Use `-d` to exclude titles and focus on city names in your prompts.

       > This feature is currently not optimized.

## **Explanation**

* **CSV File ('key-values.csv')**
   Each column header represents a key to be replaced. Rows contain corresponding values. See example:

   ```csv
   title, city, country
   Explore the Charm of, Paris, France
   A Journey Through, Tokyo, Japan
   ```
   ![keyvalue.csv Example](/assets/keyvalues.csv_example.png)


* **Prompt Template ('prompt.txt')**
   Use `**/key/**` to mark replacement points. Example:

   ```
   Write a travel blog titled "**/title/**" about the captivating city of **/city/**, **/country/**.
   ```
   ![prompt.txt Example](/assets/prompt.txt_example.png)

   ![key_example1](/assets/key_example1.png) ![key_example2](/assets/key_example2.png)
   
* **Output**
   Generated prompts are saved as individual .txt files within a specified folder.
   ```
   Write a travel blog titled "Explore the Charm of" about the captivating city of Paris, France.
   ```

## **Terminology**

* **key:** A column header in 'key-values.csv', used as an identifier in the template.
* `**/key/**`:  Indicates a placeholder in the template, to be substituted with values from 'key-values.csv'. 


## **Exceptions and Error:**
   - Template file is empty. Please add some text to it.

      `You need to check your prompt.txt. It might be empty.`

   - CSV file is empty. Please add some data to it.

      `You need to check your key-values.cv. It might be empty.`
      

   - Invalid CSV Headers **`OR`** Invalid CSV columns count. Please make sure the CSV file has the correct format..

      `For now the key-value and template is hard coded. The paid file only works for two key-values City and Title. Make sure the current headers are City,Title. Not less or More`
   

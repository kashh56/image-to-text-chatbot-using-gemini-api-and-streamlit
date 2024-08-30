# Image-to-Text Chatbot Using Gemini API and Streamlit

## 📋 Project Description

This project is a chatbot application that uses the Gemini API and Streamlit to convert images into text and interact with users. Users can upload images, and the chatbot will generate responses based on the content of the images and user queries. 

## 🛠️ Libraries Used

- **Streamlit**: A framework to create interactive web applications.
- **Google Generative AI (Gemini API)**: For generating responses based on user input and image content.
- **PIL (Python Imaging Library)**: To handle image processing.
- **dotenv**: To manage environment variables (for API key).

## 🚀 How It Works

1. **Frontend Interaction**: Users interact with the chatbot through a web interface created using Streamlit.
2. **Image Upload**: Users upload an image which is processed to extract text.
3. **User Query**: Users can enter a query related to the uploaded image.
4. **Gemini API**: The backend sends the user query and image data to the Gemini API to generate a response.

## 📂 Project Structure

- `test.py`: The main Python file containing the Streamlit application code.
- `.env`: File for storing environment variables, including your Gemini API key.

## 🔧 Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/image-to-text-chatbot-using-gemini-api-and-streamlit.git
    cd image-to-text-chatbot-using-gemini-api-and-streamlit
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    - Create a `.env` file in the root directory with your Gemini API key:

      ```env
      GEMINI_API_KEY=your_gemini_api_key
      ```

5. **Run the Application**

    ```bash
    streamlit run test.py
    ```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 📢 Feedback

If you encounter any issues or have suggestions, please reach out.
email - akashanandani.56@gmail.com

Happy coding! 🚀

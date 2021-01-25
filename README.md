<h3> !pip install flask </h3>
<h3> !pip install spacy </h3>
<h3> !python -m spacy download en_core_web_sm </h3>
<h3> !python -m spacy download zh_core_web_sm </h3>


# NLP-Summarizing-tools
1. Download/clone and unzipped the files.
2. Open python console
3. Run <br><code>> cd C:\Users\user\NLP-Summarizing-tools\app\env\Scripts</code>
4. Run <br><code>> activate</code><br>
Example of output: <code>> (env) (base) C:\Users\user\NLP-Summarizing-tools\app\env\Scripts></code>
5. Run <br><code>> cd ../..</code><br>
Example of output: <code>> (env) (base) C:\Users\user\NLP-Summarizing-tools\app></code>
6. Run <br><code>> flask run</code>
<pre><code> Output:
> (env) (base) C:\Users\user\NLP-Summarizing-tools\app>flask run
> * Environment: production
>  WARNING: This is a development server. Do not use it in a production deployment.
>  Use a production WSGI server instead.
> * Debug mode: off
> * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
> 127.0.0.1 - - [24/Jan/2021 07:06:54] "←[37mGET / HTTP/1.1←[0m" 200 -
> 127.0.0.1 - - [24/Jan/2021 07:06:55] "←[33mGET /flag-icon.css HTTP/1.1←[0m" 404 -
> 127.0.0.1 - - [24/Jan/2021 07:06:55] "←[33mGET /flag-icon.min.css HTTP/1.1←[0m" 404 -
> 127.0.0.1 - - [24/Jan/2021 07:06:55] "←[33mGET /scroll-to-top.css HTTP/1.1←[0m" 404 -</code></pre>
7. Go to http://127.0.0.1:5000/ 

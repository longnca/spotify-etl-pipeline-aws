# Detailed Tutorial

## Resources

- Spotify API Documentation: <https://developer.spotify.com/documentation/web-api>
- Spotipy (*note: not Spotify*) Python library documentation: <https://spotipy.readthedocs.io/en/2.22.1/>
- Spotify library on PyPi: <https://pypi.org/project/spotify/>

## Troubleshooting (move down later on)

- Redirect URI: <https://community.spotify.com/t5/Spotify-for-Developers/Redirect-URI-needed/td-p/5067419>.

## Set up environments and requirements

### 1. Set up a virtual environment 

- We should use a virtual environment to manage dependencies. 
- Open the Terminal in VS Code, enter the following:

```bash
python -m venv venv  # This will create a virtual environment named 'venv'
.\venv\Scripts\activate  # This activates the virtual environment on Windows
```

#### Note:

You might get the error `CategoryInfo : SecurityError: (:) [], PSSecurityException` when trying to activate the `venv` due to PowerShell's execution policy. If you get that error, then you should temporarily change the execution policy to allow the activation script to run:

- Open PowerShell (not Terminal or CMD in Windows) as an Administrator.
- Execute the following command: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`.
- There's a message to ask you to confirm about "Execution Policy Change", enter "Y" (Yes).
- After changing the execution policy, try activating your virtual environment again: `.\venv\Scripts\Activate.ps1`.
- Once you are done working in the virtual environment and no longer need to run scripts, you can revert back to the default policy by running: `Set-ExecutionPolicy Restricted -Scope CurrentUser`.

### 2. Install libraries (Spotipy)

Once the environment is activated, you can install the `spotipy` library (Note that it's **Spotipy**, not Spotify) and other libraries if needed (e.g. `pandas`) using pip:

```bash
pip install spotipy 
pip install pandas
```

**Verify installation:** After installation, you can verify that Pandas has been installed correctly in your virtual environment by running:

```bash
pip list
```

### 3. Create a Spotify App

1. Sign up and sign in Spotify for Developers

- Go to: <https://developer.spotify.com/>.
- Sign up a Spotify account if you haven't got one. Then, sign in.
- Go to Dashboard at: <https://developer.spotify.com/dashboard>
- Click on **Create app**.
- Fill in information required. For "**Redirect URI**", enter: `http://localhost/` or `http://localhost:3000`.

2. Set up Spotify API App

- On the Dashboard of the new app, click on "**Settings**".
- Check the information of "Client ID" and "Client secret". We will use them for Python scripting.

### 4. Explore the data in Jupyter Notebook

### 5. Set up AWS
#### 5.1. AWS S3

#### 5.2. AWS Lambda

### 6. Create Lambda function for Extraction

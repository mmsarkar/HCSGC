
import streamlit as st
from appwrite.client import Client
from appwrite.id import ID
from appwrite.services.users import Users

# json web token - jwt

#set up client
client = (Client()
    .set_endpoint('https://[HOSTNAME_OR_IP]/v1') # Your API Endpoint
    .set_project('5df5acd0d48c2')                # Your project ID
    .set_key('919c2db5d4...a2a3346ad2'))          # Your secret API key

#users = new Account(client);
users = Users(client)

user = users.create(
    user_id=ID.unique(),
    email='email@example.com',
    phone=None,
    password='password'
)
#!/usr/bin/env bash

mkdir -p ~/.streamlit

cat > ~/.streamlit/credentials.toml <<EOF
[general]
email = "your_heroku@email_id.com"
EOF

cat > ~/.streamlit/config.toml <<EOF
[server]
headless = true
enableCORS = false
port = ${PORT}
EOF

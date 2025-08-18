# 👋 Welcome to {{ name }}'s GitHub!
{% if linkedin %}[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/{{ linkedin }}) {% endif %}
{% if email %}[![Email](https://img.shields.io/badge/-Email-c14438?style=flat&logo=gmail&logoColor=white)](mailto:{{ email }}) {% endif %}
{% if twitter %}[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat&logo=twitter&logoColor=white)](https://twitter.com/{{ twitter }}) {% endif %}
{% if instagram %}[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat&logo=instagram&logoColor=white)](https://instagram.com/{{ instagram }}) {% endif %}
{% if github %}[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/{{ github }}) [![GitHub Followers](https://img.shields.io/github/followers/{{ github }}?label=Follow&style=social)](https://github.com/{{ github }}) {% endif %}
{% if youtube %}[![YouTube](https://img.shields.io/badge/-YouTube-FF0000?style=flat&logo=youtube&logoColor=white)](https://youtube.com/@{{ youtube }}) {% endif %}
{% if telegram %}[![Telegram](https://img.shields.io/badge/-Telegram-0088cc?style=flat&logo=telegram&logoColor=white)](https://t.me/{{ telegram }}) {% endif %}
{% if website %}[![Website](https://img.shields.io/badge/-Website-4285F4?style=flat&logo=google-chrome&logoColor=white)]({{ website }}) {% endif %}

## ℹ️ About Me
{{ about_me }}
{% if location %}
📍 Location: {{ location }}
{% endif %}
{% if phone %}
📞 Phone: {{ phone }}
{% endif %}

## 🛠️ Skills
{% for skill in skills %}
- {{ skill }}
{% endfor %}

## 💻 Tech Stack
{% for stack in stacks %}
![{{ stack }}](https://img.shields.io/badge/{{ stack | replace(" ", "%20") }}-blue?style=flat&logo={{ stack | lower | replace(" ", "") }}){% endfor %}
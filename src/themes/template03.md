# 👋 Welcome to {{ name }}'s GitHub!

## 👨🏻‍💻 About Me
{% if about_me %}
{{ about_me }}
{% else %}
💡 A passionate developer exploring new technologies and building cool stuff!
{% endif %}
{% if location %}
📍 Based in: {{ location }}
{% endif %}
{% if email %}
✉️ Email: [{{ email }}](mailto:{{ email }})
{% endif %}
{% if website %}
🌐 Website: [{{ website }}]({{ website }})
{% endif %}
{% if phone %}
📞 Phone: {{ phone }}
{% endif %}
<br>
<img alt="Night Coding" src="https://raw.githubusercontent.com/AVS1508/AVS1508/master/assets/Night-Coding.gif" align="right" width="250"/>

## 🛠 Tech Stack
{% if stacks %}
{% for stack in stacks %}
![{{ stack }}](https://img.shields.io/badge/{{ stack | replace(" ", "%20") }}-05122A?style=flat&logo={{ stack | lower | replace(" ", "") }}&logoColor=white){% endfor %}
{% else %}
- Add some tech stacks to show what you work with!
{% endif %}

## 💡 Skills
{% if skills %}
{% for skill in skills %}
- {{ skill }}
{% endfor %}
{% else %}
- Add some skills to showcase your expertise!
{% endif %}

## ⚙️ GitHub Analytics
{% if github %}
<p align="center">
<a href="https://github.com/{{ github }}">
  <img height="180em" src="https://github-readme-stats-eight-theta.vercel.app/api?username={{ github }}&show_icons=true&theme=algolia&include_all_commits=true&count_private=true"/>
  <img height="180em" src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username={{ github }}&layout=compact&langs_count=8&theme=algolia"/>
</a>
</p>
{% endif %}

## 🤝 Connect with Me
<p align="center">
{% if website %}<a href="{{ website }}"><img src="https://img.shields.io/badge/-Website-3423A6?style=flat&logo=google-chrome&logoColor=white"/></a>{% endif %}
{% if linkedin %}<a href="https://linkedin.com/in/{{ linkedin }}"><img src="https://img.shields.io/badge/-{{ linkedin }}-0077B5?style=flat&logo=linkedin&logoColor=white"/></a>{% endif %}
{% if email %}<a href="mailto:{{ email }}"><img src="https://img.shields.io/badge/-{{ email }}-D14836?style=flat&logo=gmail&logoColor=white"/></a>{% endif %}
{% if instagram %}<a href="https://instagram.com/{{ instagram }}"><img src="https://img.shields.io/badge/-@{{ instagram }}-E4405F?style=flat&logo=instagram&logoColor=white"/></a>{% endif %}
{% if twitter %}<a href="https://twitter.com/{{ twitter }}"><img src="https://img.shields.io/badge/-@{{ twitter }}-1DA1F2?style=flat&logo=twitter&logoColor=white"/></a>{% endif %}
{% if telegram %}<a href="https://t.me/{{ telegram }}"><img src="https://img.shields.io/badge/-@{{ telegram }}-0088cc?style=flat&logo=telegram&logoColor=white"/></a>{% endif %}
{% if github %}<a href="https://github.com/{{ github }}"><img src="https://img.shields.io/badge/-@{{ github }}-181717?style=flat&logo=github&logoColor=white"/></a>{% endif %}
{% if youtube %}<a href="https://youtube.com/@{{ youtube }}"><img src="https://img.shields.io/badge/-@{{ youtube }}-FF0000?style=flat&logo=youtube&logoColor=white"/></a>{% endif %}
</p>

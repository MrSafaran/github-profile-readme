# 🌟 {{ name }}'s Profile

## 👤 About
{{ about_me | default("A passionate developer exploring new technologies and building cool stuff!") }}
{% if location %}
📍 **Based in**: {{ location }}
{% endif %}
{% if phone %}
📞 **Contact**: {{ phone }}
{% endif %}
{% if email %}
📧 **Email**: [{{ email }}](mailto:{{ email }})
{% endif %}
{% if website %}
🌐 **Website**: [{{ website }}]({{ website }})
{% endif %}

## 🔗 Socials
{% if github %}
- 🖥️ [GitHub @{{ github }}](https://github.com/{{ github }}) ![GitHub Stars](https://img.shields.io/github/stars/{{ github }}?style=flat-square&color=purple)
{% endif %}
{% if twitter %}
- 🐦 [Twitter @{{ twitter }}](https://twitter.com/{{ twitter }}) ![Twitter](https://img.shields.io/badge/-Twitter-00ACEE?style=flat-square&logo=twitter)
{% endif %}
{% if linkedin %}
- 💼 [LinkedIn @{{ linkedin }}](https://linkedin.com/in/{{ linkedin }}) ![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin)
{% endif %}
{% if instagram %}
- 📸 [Instagram @{{ instagram }}](https://instagram.com/{{ instagram }}) ![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram)
{% endif %}
{% if youtube %}
- 🎥 [YouTube @{{ youtube }}](https://youtube.com/@{{ youtube }}) ![YouTube](https://img.shields.io/badge/-YouTube-FF0000?style=flat-square&logo=youtube)
{% endif %}
{% if telegram %}
- 📬 [Telegram @{{ telegram }}](https://t.me/{{ telegram }}) ![Telegram](https://img.shields.io/badge/-Telegram-0088cc?style=flat-square&logo=telegram)
{% endif %}

## 💡 Skills
{% if skills %}
{% for skill in skills %}
- {{ skill }}
{% endfor %}
{% else %}
- Add some skills to showcase your expertise!
{% endif %}

## 🛠 Tech Stack
{% if stacks %}
{% for stack in stacks %}![{{ stack }}](https://img.shields.io/badge/{{ stack | replace(" ", "%20") }}-353535?style=flat-square&logo={{ stack | lower | replace(" ", "") }})   {% endfor %}
{% else %}
- Add some tech stacks to show what you work with!
{% endif %}

## ⚙️ GitHub Analytics
{% if github %}
<div>
  <img width="45%" align="left" src="https://github-readme-stats.vercel.app/api/top-langs?username={{ github }}&show_icons=true&locale=en&layout=compact" alt="{{ github }}" />
  <img width="50%" src="https://github-readme-streak-stats.herokuapp.com/?user={{ github }}" alt="{{ github }}" />
</div>
{% endif %}

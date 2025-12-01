<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">  

<h3 align="center">container-smbclient</h3>

  <p align="center">
    Containerized wrapper of the smbprotocol python package
    <br />
    <a href="https://github.com/splendidflounder90/torq-caserules"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/splendidflounder90/torq-caserules/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/splendidflounder90/torq-caserules/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project
A method to evaluate case or event data against a set of rules to return a set of matches and the actions to take based on those matches. It simplifies building a large if condition workflows and speeds up returning the actions that should be taken.


### Built With
[![Python][Python.org]][Python-url] [![Docker][Docker.com]][Docker-url]

<!-- TODO ## Features -->


## Environment Variables
* `RULE_LIST`: A list of rules to evaluate. Each rule is a dictionary with the following keys:
* `CASE_DATA`: The case data to evaluate against the rules. This is a dictionary with the keys being the....
* `EVENT_DATA`: The event data to evaluate against the rules.


<!--
## Usage

### Example 1
Write `Hello world!` to a file at `\\server\share\testdir\helloworld.txt`

```sh
docker run -it --rm -e ACTION="create" -e FILE_NAME="helloworld.txt" -e DIRECTORY="share\testdir" -e USERNAME="domain\user" -e PASSWORD="pass" -e SERVER="server" -e FILE_CONTENTS="SGVsbG8gd29ybGQh" ghcr.io/splendidflounder90/container-smbclient 
```
Output
```json
{"output":"File created."}
```
### Example 2
Read the contents of a file at `\\server\share\testdir\helloworld.txt`
```sh
docker run -it --rm -e ACTION="read" -e FILE_NAME="helloworld.txt" -e DIRECTORY="share\testdir" -e USERNAME="domain\user" -e PASSWORD="pass" -e SERVER="server" ghcr.io/splendidflounder90/container-smbclient
```
Output (file contents bas64 encoded)
```json
{"output": "SGVsbG8gd29ybGQh"}
```

### Example 3
Write the contents of a URL to a new file at `\\server\share\testdir\helloworld.txt`

```sh
docker run -it --rm -e ACTION="create" -e FILE_NAME="helloworld.txt" -e DIRECTORY="share\testdir" -e USERNAME="domain\user" -e PASSWORD="pass" -e SERVER="server" -e FILE_CONTENTS="https://raw.githubusercontent.com/splendidflounder90/torq-caserules/refs/heads/main/README.md" ghcr.io/splendidflounder90/torq-caserules 
```
-->


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


### Top contributors:

<a href="https://github.com/splendidflounder90/torq-caserules/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=splendidflounder90/torq-caserules" alt="contrib.rocks image" />
</a>


## License

Distributed under the project_license. See `LICENSE.txt` for more information.


## Contact

Project Link: [https://github.com/splendidflounder90/torq-caserules](https://github.com/splendidflounder90/torq-caserules)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/splendidflounder90/container-smbclient.svg?style=for-the-badge
[contributors-url]: https://github.com/splendidflounder90/container-smbclient/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/splendidflounder90/container-smbclient.svg?style=for-the-badge
[forks-url]: https://github.com/splendidflounder90/container-smbclient/network/members
[stars-shield]: https://img.shields.io/github/stars/splendidflounder90/container-smbclient.svg?style=for-the-badge
[stars-url]: https://github.com/splendidflounder90/container-smbclient/stargazers
[issues-shield]: https://img.shields.io/github/issues/splendidflounder90/container-smbclient.svg?style=for-the-badge
[issues-url]: https://github.com/splendidflounder90/container-smbclient/issues
[license-shield]: https://img.shields.io/github/license/splendidflounder90/container-smbclient.svg?style=for-the-badge
[license-url]: https://github.com/splendidflounder90/container-smbclient/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=fff
[Python-url]: https://www.python.org/
[Docker.com]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=fff
[Docker-url]: https://www.docker.com
Title: Static blogging with Pelican - Part 1
Date: 2014-10-28 23:00
Author: Allan Scullion
Category: Blogging
Tags: Blogging,Pelican,Python
Slug: pelican-1

I have used a number of blogging engines over the years. I started off with Blogger, moved onto a self hosted Wordpress site and then onto the fully hosted solution offered by Squarespace (which is excellent btw).

Each solution had upsides and drawbacks. It was easy to outgrow Blogger. Wordpress was powerful but earlier versions were susceptible to hacking, plus managing plug-ins, MySQL and backups became a drag. Squarespace is superb, but the programmer in me yearned for more control.

I decided to look at some static blogging engines. My goals being:

*	All content should be pre-compiled to static web pages making the end result portable and quick to load
*	As much as possible, remove reliance on the server side web technology stack (PHP, MySQL etc.)
*   All content to be written using plain text [Markdown][md] files
*	The ability to perform staging and testing off-line

On top of these requirements, I also wanted to:

*   Keep my existing photo pages (imported from Flickr albums)
*   Import the comments from my existing blog

After digging around for a bit, I finally settled on [Pelican][pelican] - a static blog generator written in Python.

If you can find your way around the Unix command line, you can be up and running in minutes using the following:

    :::bash
    sudo pip install pelican
    sudo pip install Markdown
    pelican-quickstart

This will create the folder structure for your Pelican project:

```text
yourproject/
├── content
│   └── (pages)
├── output
├── develop_server.sh
├── fabfile.py
├── Makefile
├── pelicanconf.py       # Main settings file
└── publishconf.py       # Settings to use when ready to publish
```

Creating content is easy. Simply create a markdown file in the `content` folder using the following metadata syntax at the top of the file:

```text
Title: Static blogging with Pelican - Part 1
Date: 2014-10-27 18:02
Author: Allan Scullion
Category: Blogging
Tags: Blogging,Pelican,Python
Slug: pelican-1

Page content goes here
```

Save the file, then use the following command[^1]:

```bash
make clean && make html DEBUG=1 && make serve
```

Open your browser to `http://localhost:8000` and behold your new creation.

The `output` folder contains all of the generated HTML files and other assets. The `Makefile` also has a number of commands to publish these using a number of methods, including FTP and rsync+ssh.

In follow up posts, I will cover:

*   Site Templates (you will no doubt hate the standard template)
*   Adding comments using [Disqus][disqus]
*   Plug-ins
*   Automated publishing using [Github][github] and [Codeship][codeship]

[md]: http://daringfireball.net/projects/markdown/basics "Markdown Basics - John Gruber"
[pelican]: http://docs.getpelican.com/ "Pelican Static Blogging Engine"
[github]: https://github.com "Github"
[codeship]: https://codeship.io "Codeship"
[disqus]: https://disqus.com

[^1]: Better still, save it as a shell script, because you will be using it a lot
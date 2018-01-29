Title: Setting up OAuth2 for Gmail
Date: 2014-03-11 15:19
Author: Allan Scullion
Category: Code
Tags: Coding, OAuth, Gmail, nodemailer, node
Slug: setting-up-oauth2-for-gmail

Make sure you setup a project on the [Google Developers Page](https://console.developers.google.com) using the account from which you want to send email.

See the following [link](http://masashi-k.blogspot.co.uk/2013/06/sending-mail-with-gmail-using-xoauth2.html) describing the process of obtaining the required authorization tokens for [nodemailer](nodemailer).

## Extract of important steps {#extractofimportantsteps}

### Step 1 : Installation

```text
npm install nodemailer
```

### Step 2 : Register your Application at Google APIs Console

XOAuth2 is similar with OAuth2, so you need to register your application to Google. Jump to Google APIs Console, then create a project if you don't have, and open "API Access" page.

In this here, when you create a client ID, put "https://developers.google.com/oauthplayground" into the text box for Redirect URIs.

### Step 3 : Open Google OAuth2.0 Playground.

You will obtain refreshToken & accessToken on this step at Google OAuth2.0 Playground. Open the page from https://developers.google.com/oauthplayground, then click the gear button on the right-top.

Set your client ID & client secret that obtained on step2, and select "Access token location:" as "Authorization header w/ Bearer prefix". Then close it.

And set up the scopes. Put "https://mail.google.com/" into the textbox below the service scope list.

Then click [Authorize APIs] button.

### Step 4 : Obtain the "refresh token".

After OAuth2.0 authorization, click [Exchange authorization code for tokens] button. You can get your refresh token.

Use the following javascript template:

```javascript
    var nodemailer = require("nodemailer");

    var smtpTransport = nodemailer.createTransport("SMTP", {
      service: "Gmail",
      auth: {
        XOAuth2: {
          user: "your_email_address@gmail.com", // Your gmail address.
                                                // Not @developer.gserviceaccount.com
          clientId: "your_client_id",
          clientSecret: "your_client_secret",
          refreshToken: "your_refresh_token"
        }
      }
    });

    var mailOptions = {
      from: "your_email_address@gmail.com",
      to: "my_another_email_address@gmail.com",
      subject: "Hello",
      generateTextFromHTML: true,
      html: "<b data-preserve-html-node="true">Hello world</b>"
    };

    smtpTransport.sendMail(mailOptions, function(error, response) {
      if (error) {
        console.log(error);
      } else {
        console.log(response);
      }
      smtpTransport.close();
    });
```
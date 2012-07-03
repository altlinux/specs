Name: appliance-hosting-mail
Summary: Mailserver VE
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

Requires: appliance-ve-std

# IMAP/POP3
Requires: courier-imap
Requires: courier-maildrop
Requires: courier-authlib
Requires: courier-authlib-userdb

# fetch mail from other mailboxes
Requires: fetchmail-daemon

# SMTP-server
Requires: postfix-cyrus
Requires: postfix-pcre
Requires: postfix-pgsql
Requires: postfix-tls

# other
Requires: cyrus-sasl2
Requires: sqlgrey

# spamassassin
Requires: spamassassin-spamc
Requires: spamassassin-spamd

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus


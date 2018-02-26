%define upversion 1.0beta3
Summary: JWChat is a full featured, web-based Jabber client
Name: jwchat
Version: 1.0
Release: alt1.beta3
License: GPL
Group: System/Servers
URL: http://jwchat.sourceforge.net/
Source0: %name-%upversion.tar.gz
Patch0: %name.patch
Packager: Mikhail Pokidko <pma@altlinux.org>
#Requires: python-module-pyxmpp, jabber
Epoch: 1

%description
JWChat is a full featured, web-based Jabber client. Written using AJAX technology it relies on JavaScript and HTML at the client-side onl
It supports basic jabber instant messaging, roster management and groupchats based on the MUC protocol.

%prep
%setup -q -n %name-%upversion
#patch0 -p1

%build

%install
mkdir -p %buildroot/var/www/html/%name 

cp -r ./* %buildroot/var/www/html/%name

%files
%doc README AUTHORS COPYING ChangeLog
/var/www/html/%name/*

%changelog
* Fri Mar 21 2008 Mikhail Pokidko <pma@altlinux.org> 1:1.0-alt1.beta3
- version up. spec cleanup

* Tue Jan 23 2007 Mikhail Pokidko <pma@altlinux.ru> 20060721-alt1
- Initial build


Name: saslfinger
Version: 1.0.3
Release: alt1

Summary: script that seeks to help you debugging your SMTP AUTH setup

Group: System/Servers
License: Public domain
Url: http://postfix.state-of-mind.de/patrick.koetter/saslfinger/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://postfix.state-of-mind.de/patrick.koetter/saslfinger/%name-%version.tar

BuildArch: noarch

%description
saslfinger is a bash utility script that seeks to help you debugging
your SMTP AUTH setup. It gathers various informations about Cyrus SASL
and Postfix from your system and sends it to stdout.

%prep
%setup

%install
install -D %name %buildroot%_bindir/%name
install -D %name.1 %buildroot%_man1dir/%name.1

%files
%doc ChangeLog index.html TODO
%_bindir/%name
%_man1dir/*

%changelog
* Sat Oct 16 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- initial build for ALT Linux Sisyphus

%define sound_dir	%_datadir/asterisk/sounds/
%define sound_lang  en

Name: asterisk-extra-sounds-en-g729
Summary: sounds for Asterisk
Version: alt1.1
Release: alt1.1
License: GPL
Group: System/Servers
BuildArch: noarch
Requires(pre): asterisk-sounds-en-base

Url: http://downloads.asterisk.org/pub/telephony/sounds/releases/%name-%version.tar.gz

Source: %name-%version.tar

BuildRequires: asterisk-build-sounds

%description
%summary

%prep
%setup

%install
ast-install-extra-sounds en g729 %buildroot
%files -f sounds.list

%changelog
* Fri Mar 31 2017 Denis Smirnov <mithraen@altlinux.ru> alt1.1-alt1.1
- update build scripts for prevent core/extra sounds conflicts

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 1.5-alt1
- new version 1.5

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 1.4.15-alt1
- new version 1.4.15

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 1.4.14-alt1
- new version 1.4.14

* Wed Jan 09 2013 Cronbuild Service <cronbuild@altlinux.org> 1.4.13-alt1
- new version 1.4.13

* Sat Dec 29 2012 Cronbuild Service <cronbuild@altlinux.org> 1.4.12-alt1
- new version 1.4.12

* Fri Dec 28 2012 Denis Smirnov <mithraen@altlinux.ru> 1.4.11-alt3
- add watch-file and cronbuild support

* Sun Jul 24 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4.11-alt2
- add requires to asterisk-sounds-en-base

* Tue Jul 19 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4.11-alt1
- first build



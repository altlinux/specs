%define sound_dir	%_datadir/asterisk/sounds/
%define sound_lang  ru

Name: asterisk-core-sounds-ru-sln16
Summary: sounds for Asterisk
Version: 1.4.21
Release: alt3
License: GPL
Group: System/Servers
BuildArch: noarch
Obsoletes: asterisk-sounds-ru-sln16 < %version-%release 
Conflicts: asterisk-sounds-ru-sln16 
Requires(pre): asterisk-sounds-ru-base

Url: http://downloads.asterisk.org/pub/telephony/sounds/releases/%name-%version.tar.gz

Source: %name-%version.tar

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%sound_dir/%sound_lang
cp -a ./ %buildroot%sound_dir/%sound_lang/
find -type f \
    | grep -v sounds.list \
    | grep -vP '^.\/(CREDITS|LICENSE|CHANGES)' \
	| grep -vP '\.txt$' \
    | sed 's!\.\/\(.*\)!%sound_dir%sound_lang/\1!' \
    > sounds.list

find -mindepth 1 -type d \
    | sed 's!\.\/\(.*\)!%%dir %sound_dir%sound_lang/\1!' \
	>> sounds.list

find -type f \
    | grep -P '^.\/(CREDITS|LICENSE|CHANGES)' \
    | sed 's!\.\/\(.*\)!%%doc \1\n%%exclude %sound_dir%sound_lang/\1!' \
	>> sounds.list

find -type f \
    | grep -P '\.txt$' \
    | sed 's!\.\/\(.*\)!%%doc \1\n%%exclude %sound_dir%sound_lang/\1!' \
	>> sounds.list

%files -f sounds.list

%changelog
* Sat Sep 24 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4.21-alt3
- add Obsoletes to old sounds packages

* Sun Jul 24 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4.21-alt2
- add requires to asterisk-sounds-ru-base

* Tue Jul 19 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4.21-alt1
- first build



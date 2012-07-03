Name: asterisk-sounds-extra-en
Summary: sounds for Asterisk
Version: 1.4.9
Release: alt2
License: GPL
Group: System/Servers
BuildArch: noarch
%define sound_dir	%_datadir/asterisk/sounds/
Url: http://www.asterisk.org/
Obsoletes: asterisk-sounds
Conflicts: asterisk-sounds
Conflicts: asterisk-en-sounds < %version-%release
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar
Requires: %name-alaw
Requires: %name-ulaw
Requires: %name-wav
Requires: %name-gsm
Requires: %name-g729
Requires: %name-g722
Requires: %name-sln16

%package alaw
Summary: %summary
Group: %group
Requires(pre): asterisk-base >= 0.6

%description alaw
%summary


%package g722
Summary: %summary
Group: %group
Requires(pre): asterisk-base >= 0.6

%description g722
%summary


%package g729
Summary: %summary
Group: %group
Requires(pre): asterisk-base >= 0.6

%description g729
%summary


%package gsm
Summary: %summary
Group: %group
Requires(pre): asterisk-base >= 0.6

%description gsm
%summary


%package siren14
Summary: %summary
Group: %group
Requires(pre): asterisk-base >= 0.6

%description siren14
%summary


%package siren7
Summary: %summary
Group: %group
Requires(pre): asterisk-base >= 0.6

%description siren7
%summary


%package sln16
Summary: %summary
Group: %group
Requires(pre): asterisk-base >= 0.6

%description sln16
%summary


%package ulaw
Summary: %summary
Group: %group
Requires(pre): asterisk-base >= 0.6

%description ulaw
%summary


%package wav
Summary: %summary
Group: %group
Requires(pre): asterisk-base >= 0.6

%description wav
%summary


%description
Sounds for Asterisk PBX


%prep
%setup
rm -f */CHANGES-asterisk-extra-*
rm -f */CREDITS-asterisk-extra-*
rm -f */*.txt

%install
for d in asterisk-extra-sounds-en*; do
	for s in ha wx; do
		mkdir -p %buildroot%sound_dir/en/$s
		mv -f $d/$s/* %buildroot%sound_dir/en/$s/
		rmdir  $d/$s
	done
	mv -f $d/* %buildroot%sound_dir/en/
done

%files alaw
%dir %sound_dir/en
%dir %sound_dir/en/ha
%dir %sound_dir/en/wx
%sound_dir/en/*.alaw
%sound_dir/en/ha/*.alaw
%sound_dir/en/wx/*.alaw

%files g722
%dir %sound_dir/en
%dir %sound_dir/en/ha
%dir %sound_dir/en/wx
%sound_dir/en/*.g722
%sound_dir/en/ha/*.g722
%sound_dir/en/wx/*.g722

%files g729
%dir %sound_dir/en
%dir %sound_dir/en/ha
%dir %sound_dir/en/wx
%sound_dir/en/*.g729
%sound_dir/en/ha/*.g729
%sound_dir/en/wx/*.g729

%files gsm
%dir %sound_dir/en
%dir %sound_dir/en/ha
%dir %sound_dir/en/wx
%sound_dir/en/*.gsm
%sound_dir/en/ha/*.gsm
%sound_dir/en/wx/*.gsm

%files siren14
%dir %sound_dir/en
%dir %sound_dir/en/ha
%dir %sound_dir/en/wx
%sound_dir/en/*.siren14
%sound_dir/en/ha/*.siren14
%sound_dir/en/wx/*.siren14

%files siren7
%dir %sound_dir/en
%dir %sound_dir/en/ha
%dir %sound_dir/en/wx
%sound_dir/en/*.siren7
%sound_dir/en/ha/*.siren7
%sound_dir/en/wx/*.siren7

%files sln16
%dir %sound_dir/en
%dir %sound_dir/en/ha
%dir %sound_dir/en/wx
%sound_dir/en/*.sln16
%sound_dir/en/ha/*.sln16
%sound_dir/en/wx/*.sln16

%files ulaw
%dir %sound_dir/en
%dir %sound_dir/en/ha
%dir %sound_dir/en/wx
%sound_dir/en/*.ulaw
%sound_dir/en/ha/*.ulaw
%sound_dir/en/wx/*.ulaw

%files wav
%dir %sound_dir/en
%dir %sound_dir/en/ha
%dir %sound_dir/en/wx
%sound_dir/en/*.wav
%sound_dir/en/ha/*.wav
%sound_dir/en/wx/*.wav

%changelog
* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4.9-alt2
- rebuild

* Sun Apr 26 2009 Denis Smirnov <mithraen@altlinux.ru> 1.4.9-alt1
- update to 1.4.9
- add siren7 version
- add siren14 version

* Sun Nov 30 2008 Denis Smirnov <mithraen@altlinux.ru> 1.4.8-alt3
- fix build

* Mon Nov 24 2008 Denis Smirnov <mithraen@altlinux.ru> 1.4.8-alt2
- fix building

* Sat Nov 22 2008 Denis Smirnov <mithraen@altlinux.ru> 1.4.8-alt1
- update to 1.4.8
- add sln16 subpackage

* Fri Jul 25 2008 Denis Smirnov <mithraen@altlinux.ru> 1.4.5-alt4
- move %sound_dir to asterisk-base

* Tue May 01 2007 Denis Smirnov <mithraen@altlinux.ru> 1.4.5-alt3
- fix file conflicts with asterisk-sounds-en

* Mon Apr 30 2007 Denis Smirnov <mithraen@altlinux.ru> 1.4.5-alt2
- split to subpackages with different formats

* Sun Apr 29 2007 Denis Smirnov <mithraen@altlinux.ru> 1.4.5-alt1
- update to 1.4.5

* Sun Dec 24 2006 Denis Smirnov <mithraen@altlinux.ru> 1.4.4-alt1
- silence/* files moved to asterisk-sounds-en

* Sun Nov 26 2006 Denis Smirnov <mithraen@altlinux.ru> 1.4.3-alt2
- fix file conflicts with asterisk-sounds-en

* Fri Oct 27 2006 Denis Smirnov <mithraen@altlinux.ru> 1.4.3-alt1
- Initial build for Sisyphus


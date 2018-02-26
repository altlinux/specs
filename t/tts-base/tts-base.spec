Name: tts-base
Version: 20110207
Release: alt1
Packager: Michael Pozhidaev <msp@altlinux.ru>
BuildArch: noarch
Summary: Scripts for manipulation with installed TTS engine set
Group: System/Configuration/Other
License: GPL

BuildRequires: rpm-macros-tts

Source: %name-%version.tar

%description
This package is the base for all TTS tools configured to be run in ALT Linux distributions.
The main design goal is to make unified configuration rules and 
simplify installation and using of different TTS engines.

%prep
%setup -q
%build

%install
%__install -d -m 755 %buildroot%_ttsdir
%__install -pD -m 755 ./tts-unregister %buildroot%_sbindir/tts-unregister

%files
%_sbindir/*
%_ttsdir

%changelog
* Mon Feb 07 2011 Michael Pozhidaev <msp@altlinux.ru> 20110207-alt1
- Fixed symlink name to remove from /etc/voiceman.d
- Buildreq tts-devel replaced by rpm-macros-tts

* Thu Sep 04 2008 Michael Pozhidaev <msp@altlinux.ru> 20080904-alt1
- Added real content of tts-unregister script

* Wed Aug 06 2008 Michael Pozhidaev <msp@altlinux.ru> 20080806-alt1
- INitial package


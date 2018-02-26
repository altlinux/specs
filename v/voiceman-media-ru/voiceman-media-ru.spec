
Name: voiceman-media-ru
Version: 20111127
Release: alt1
BuildArch: noarch
License: GPL
Group: Sound
Summary: makes speech notification about inserted removable media in Russian through VoiceMan
Conflicts: voiceman-media
Source0: %name-%version.tar.gz

Requires: udev-rules voiceman vorbis-tools

%description
This package contains script for handling UDEV events and producing
speech notifications in Russian of any newly inserted removable media.

%prep
%setup -q
%install
%__install -pD -m 644 %name.rules %buildroot%_sysconfdir/udev/rules.d/50-%name.rules
%__install -pD -m 755 %name %buildroot%_bindir/%name
%__install -pD -m 644 media.ogg %buildroot%_datadir/sounds/voiceman/media.ogg

%files
%_sysconfdir/udev/rules.d/*
%_bindir/*
%_datadir/sounds/voiceman/*

%changelog
* Sun Nov 27 2011 Michael Pozhidaev <msp@altlinux.ru> 20111127-alt1
- Notifications are disabled without logged in users

* Mon Nov 21 2011 Michael Pozhidaev <msp@altlinux.ru> 20111121-alt1
- Initial package for ALT Linux


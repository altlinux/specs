
Name: voiceman-media
Version: 20111127
Release: alt1
BuildArch: noarch
License: GPL
Group: Sound
Summary: makes speech notification about inserted removable media through VoiceMan

Source0: %name-%version.tar.gz

Requires: udev-rules voiceman vorbis-tools

%description
This package contains script for handling UDEV events and producing
speech notifications of any newly inserted removable media.

%prep
%setup -q
%install
%__install -pD -m 644 voiceman-media.rules %buildroot%_sysconfdir/udev/rules.d/50-voiceman-media.rules
%__install -pD -m 755 %name %buildroot%_bindir/%name
%__install -pD -m 644 media.ogg %buildroot%_datadir/sounds/voiceman/media.ogg

%files
%_sysconfdir/udev/rules.d/*
%_bindir/*
%_datadir/sounds/voiceman/*

%changelog
* Sun Nov 27 2011 Michael Pozhidaev <msp@altlinux.ru> 20111127-alt1
- Notifications are disabled without logged in users

* Sat Nov 19 2011 Michael Pozhidaev <msp@altlinux.ru> 20111119-alt1
- Made sensitive to disk type of device rather than partitions

* Fri Mar 18 2011 Michael Pozhidaev <msp@altlinux.ru> 20110318-alt1
- Removed saving information about last attached volume to /tmp

* Mon Jan 04 2010 Michael Pozhidaev <msp@altlinux.ru> 20100104-alt2
- Fixed bug with new device size information

* Mon Jan 04 2010 Michael Pozhidaev <msp@altlinux.ru> 20100104-alt1
- No longer used HAL, UDEV instead

* Sun Nov 08 2009 Michael Pozhidaev <msp@altlinux.ru> 20091108-alt1
- Initial package


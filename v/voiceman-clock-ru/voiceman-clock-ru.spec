
Name: voiceman-clock-ru
Version: 20111127
Release: alt1
BuildArch: noarch
License: GPL
Group: Sound
Summary: The cron script for new hour speech notification in Russian with VoiceMan speech server
Conflicts: voiceman-clock
Source0: %name-%version.tar.gz

Requires: voiceman vixie-cron aplay

%description
This package contains script to make speech notifications of every new hour in Russian language. Install it if you want 
enable these notifications. Be sure voiceman and crond services are running.

%prep
%setup -q
%build

%install
%__install -pD -m755 %name %buildroot%_bindir/%name
%__install -pD -m644 clock.wav %buildroot%_datadir/sounds/voiceman/clock.wav
%__install -pD -m644 %name.crontab %buildroot%_sysconfdir/cron.d/%name

%files
%_bindir/*
%_datadir/sounds/voiceman/*
%_sysconfdir/cron.d/*

%changelog
* Sun Nov 27 2011 Michael Pozhidaev <msp@altlinux.ru> 20111127-alt1
- Notifications are disabled without logged in users

* Fri Nov 18 2011 Michael Pozhidaev <msp@altlinux.ru> 20111118-alt1
- Initial package for ALT Linux


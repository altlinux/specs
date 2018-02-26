Name: fortunes-starcontrol2
Version: 20050904
Release: alt1

Summary: Quotes from famous game Star Control 2
Group: Games/Other
License: distributable
Url: http://sc2.sourceforge.net

BuildArch: noarch

Source: %name-%version.tar.bz2

%description
Quotes from famous old game Star Control 2.
Now this game is available as open source (named "The Ur-Quan Masters")
and can be obtained from http://sc2.sourceforge.net.

%install
%__mkdir_p %buildroot%_gamesdatadir/fortune
bzcat %SOURCE0 | %__tar xf - -C %buildroot%_gamesdatadir/fortune/

%files
%_gamesdatadir/fortune/*

%changelog
* Sun Sep 04 2005 Andrey Rahmatullin <wrar@altlinux.ru> 20050904-alt1
- initial build

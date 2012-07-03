Name: fortunes-oneliners
Version: 20050904
Release: alt1

Summary: Fortune files with quotes with random oneliners
Group: Games/Other
License: GPL
Url: http://eol.init1.nl/content/view/45/54/

BuildArch: noarch

Source: %name-%version.tar.bz2

%description
Fortune files with quotes with random oneliners

%install
%__mkdir_p %buildroot%_gamesdatadir/fortune
bzcat %SOURCE0 | %__tar xf - -C %buildroot%_gamesdatadir/fortune/

%files
%_gamesdatadir/fortune/*

%changelog
* Sun Sep 04 2005 Andrey Rahmatullin <wrar@altlinux.ru> 20050904-alt1
- initial build

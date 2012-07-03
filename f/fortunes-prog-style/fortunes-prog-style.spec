Name: fortunes-prog-style
Version: 20050904
Release: alt1

Summary: Tips from the "Elements of Programming Style"
Group: Games/Other
License: distributable
Url: http://db.ilug-bom.org.in/lug-authors/philip/misc/fortune-mod-prog-style.tar.gz

BuildArch: noarch

Source: %name-%version.tar.bz2

%description
Some fortune quotes from the 69 tips from the "Elements of Programming
Style" by Kernighan and Plaugher.

%install
%__mkdir_p %buildroot%_gamesdatadir/fortune
bzcat %SOURCE0 | %__tar xf - -C %buildroot%_gamesdatadir/fortune/

%files
%_gamesdatadir/fortune/*

%changelog
* Sun Sep 04 2005 Andrey Rahmatullin <wrar@altlinux.ru> 20050904-alt1
- initial build

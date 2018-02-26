Name: fortunes-opensources
Version: 20050904
Release: alt1

Summary: Quotes from the O'Reilly book "Open Sources"
Group: Games/Other
License: distributable
Url: http://www.dibona.com/opensources/index.shtml

BuildArch: noarch

Source: %name-%version.tar.bz2

%description
This a fortune file featuring quotes from the O'Reilly book "Open Sources".
Included are some that did not make it into the final manuscript.

%install
%__mkdir_p %buildroot%_gamesdatadir/fortune
bzcat %SOURCE0 | %__tar xf - -C %buildroot%_gamesdatadir/fortune/

%files
%_gamesdatadir/fortune/*

%changelog
* Sun Sep 04 2005 Andrey Rahmatullin <wrar@altlinux.ru> 20050904-alt1
- initial build

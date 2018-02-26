Name: fortunes-murphy
Version: 20050904
Release: alt1

Summary: Quotes from Murphy's laws
Group: Games/Other
License: GPL
Url: http://lis.snv.jussieu.fr/~rousse/linux

BuildArch: noarch

Source: %name-%version.tar.bz2

%description
This is a collection of more than 1250 Murphy's (& Al) laws, ignominously
stolen from the excellent Ultimate Collection of Murphy's Laws by Andreas Gotz
(http://www.cpuidle.de/murphy.shtml), at format used by the good old fortune
command.

%install
%__mkdir_p %buildroot{%_gamesdatadir/fortune,%_docdir/%name-%version}
bzcat %SOURCE0 | %__tar xf - -C %buildroot%_gamesdatadir/fortune/
%__mv %buildroot%_gamesdatadir/fortune/README %buildroot%_docdir/%name-%version/

%files
%doc %_docdir/%name-%version/
%_gamesdatadir/fortune/*

%changelog
* Sun Sep 04 2005 Andrey Rahmatullin <wrar@altlinux.ru> 20050904-alt1
- initial build

Name: fortunes-sysadmin-top100
Version: 20050904
Release: alt1

Summary: Top 100 things you don't want the sysadmin to say
Group: Games/Other
License: Public Domain
Url: http://people.redhat.com/andrew/humor/100sys.html

BuildArch: noarch

Source: %name-%version.tar.bz2

%description
The top 100 things you don't want the sysadmin to say in fortune format.

%install
%__mkdir_p %buildroot%_gamesdatadir/fortune
bzcat %SOURCE0 | %__tar xf - -C %buildroot%_gamesdatadir/fortune/

%files
%_gamesdatadir/fortune/*

%changelog
* Sun Sep 04 2005 Andrey Rahmatullin <wrar@altlinux.ru> 20050904-alt1
- initial build

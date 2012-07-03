Name: nginx-apt-cache
Version: 1.0
Release: alt2

Summary: Nginx template to work as caching proxy for apt

License: AGPLv3
Group: Development/Other
Url: http://www.altlinux.org/

Source1: apt-cache.conf

BuildArch: noarch

Requires: nginx >= 0.8.0

%description
Nginx template to work as caching proxy for apt.

%prep

%install
mkdir -p %buildroot%_sysconfdir/nginx/sites-available.d/
install -m644 %SOURCE1 %buildroot%_sysconfdir/nginx/sites-available.d/

%files
%_sysconfdir/nginx/sites-available.d/*

%changelog
* Mon Aug 01 2011 Mykola Grechukh <gns@altlinux.ru> 1.0-alt2
- fixed config path

* Mon Aug 01 2011 Mykola Grechukh <gns@altlinux.ru> 1.0-alt1
- initial build

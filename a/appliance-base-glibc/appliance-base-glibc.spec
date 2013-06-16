Url: http://www.altlinux.org/Appliances
Name: appliance-base-glibc
Summary: Virtual package that require all glibc components
BuildArch: noarch
Version: 4.0.1
Release: alt2
License: GPL
Group: System/Base

Requires: glibc
Requires: glibc-core
Requires: glibc-gconv-modules
Requires: glibc-i18ndata
Requires: glibc-locales
Requires: glibc-nss
Requires: glibc-pthread
Requires: glibc-timezones
Requires: glibc-utils

%description
%summary

%files

%changelog
* Sun Jun 16 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt2
- add Url tag

* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus


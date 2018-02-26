%define rtname rt
%define rtminver 3.4.2
%define rtupname RTx
%define statsname stats
%define statsupname Statistics
%define statsarchname RTx-%statsupname
%define rtfullname request-tracker
%define fullname request-tracker-extension-stats
%define wwwroot %_var/www/html
%define webusr apache
%define webgrp apache

Summary: Statistics is an extension to Request Tracker (RT). It is produces statistical information based on RT data.
Name: %fullname
Version: 0.1.8
Release: alt2
Group: Networking/WWW
License: GPL
Url:http://wiki.bestpractical.com/index.cgi?RT3StatisticsPackage 
Source:ftp://anonftp.mqsoftware.com/kfh/RT/%statsarchname-%version.tar.gz
BuildArch: noarch

BuildRequires: autoconf perl
AutoReq: no

# RT
Requires: %rtfullname >= 3.4.2

# Perl modules
Requires: perl(GD.pm)
Requires: perl(GD/Graph.pm)

%description
Statistics is an extension to Request Tracker (RT), from Best
Practical. It is produces statistical information based on RT data.

%prep
%setup -q -n %statsarchname-%version

%install

%__mkdir_p %buildroot%wwwroot/%rtname/

%__mkdir_p %buildroot%_libexecdir/%rtname/lib
%__cp -r lib/* %buildroot%_libexecdir/%rtname/lib/
%__cp -r html/* %buildroot%wwwroot/%rtname/

# fix permissions
find %buildroot%_libexecdir/%rtname/ -type d -print0 | xargs -r0 chmod 2755 --
find %buildroot%_libexecdir/%rtname/ -type f -print0 | xargs -r0 chmod 0644 --
find %buildroot%_libexecdir/%rtname/ -name '*.pm' -type f -print0 | xargs -r0 chmod 0755 --
find %buildroot%wwwroot/%rtname -type d -print0 |xargs -r0 chmod 2755 --
find %buildroot%wwwroot/%rtname -type f -print0 |xargs -r0 chmod 0644 --

%post

echo "Congratulations. Statistics has been installed."

%files
%doc CHANGELOG README
%attr(-,root,%webgrp) %_libexecdir/%rtname/lib/RTx/*
%attr(-,%webusr,%webgrp) %wwwroot/%rtname/%rtupname/*
%attr(-,%webusr,%webgrp) %wwwroot/%rtname/Callbacks/*

%changelog
* Wed May 31 2006 Andrew Kornilov <hiddenman@altlinux.ru> 0.1.8-alt2
- Fixed Requires (added GD/Graph.pm)

* Sat Jan 21 2006 Andrew Kornilov <hiddenman@altlinux.ru> 0.1.8-alt1
- Initial build for Sisyphus



# TODO: binary preprocessor
Name: webgrind
Version: 1.5.0
Release: alt1

Summary: Xdebug Profiling Web Frontend in PHP

License: BSD License
Group: System/Servers
Url: https://github.com/jokkedk/webgrind

# Source-url: https://github.com/jokkedk/webgrind/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildPreReq: rpm-build-apache2 rpm-macros-webserver-common

AutoReq:yes,nomingw32,nomingw64

Requires: graphviz

%description
Webgrind is a Xdebug profiling web frontend in PHP.
It implements a subset of the features of kcachegrind and installs in seconds and works on all platforms.

%package preprocessor
Summary: binary preprocessor for Xdebug Profiling Web Frontend in PHP
Group: System/Servers
Requires: %name = %EVR

%description preprocessor
Binary version of the preprocessor (for faster preprocessing)
for Xdebug Profiling Web Frontend in PHP.

%prep
%setup

%build
%if 0
# TODO arch subpackage
%make_build
%endif

%install
mkdir -p %buildroot%webserver_webappsdir
cp -a . %buildroot%webserver_webappsdir/%name

# remove unneeded
#rm -rf %buildroot%webserver_webappsdir/%name/test/

%files
%doc README.md
%dir %webserver_webappsdir/%name/
%webserver_webappsdir/%name/*
#exclude %webserver_webappsdir/%name/bin/
#config(noreplace) %webserver_webappsdir/%name/.htaccess
# yes, will notify about duplicate file
#attr(640,root,%webserver_group) %config(noreplace) %webserver_webappsdir/%name/config.inc.php

%if 0
%files preprocessor
%webserver_webappsdir/%name/bin/
%endif

%changelog
* Fri Dec 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- initial build for ALT Sisyphus

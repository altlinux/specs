Url: http://www.altlinux.org/Appliances
Name: appliance-web-mediawiki
Summary: Virtual package for MediaWiki install
BuildArch: noarch
Version: 4.0.1
Release: alt3
License: GPL
Group: System/Base

# This appliance based on appliance-ve-std
Requires: appliance-ve-std

# PHP-modules
Requires: apache-mod_php5
Requires: php5-dom
Requires: php5-mbstring
Requires: php5-mysql
Requires: php5-sockets

# ImageMagic
Requires: ImageMagick-tools
Requires: librsvg

# texvc
Requires: texvc

# diff3
#diffutils

%description
%summary

%files

%changelog
* Thu Mar 13 2014 Anton Farygin <rider@altlinux.ru> 4.0.1-alt3
- php5-eaccelerator removed from requires

* Sun Jun 16 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt2
- add Url tag

* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus


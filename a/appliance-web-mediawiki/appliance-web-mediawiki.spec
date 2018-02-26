Name: appliance-web-mediawiki
Summary: Virtual package for MediaWiki install
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

# This appliance based on appliance-ve-std
Requires: appliance-ve-std

# PHP-modules
Requires: apache-mod_php5
Requires: php5-dom
Requires: php5-eaccelerator
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
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus


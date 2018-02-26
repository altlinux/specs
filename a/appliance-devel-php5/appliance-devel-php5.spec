Name: appliance-devel-php5
Summary: Virtual package that require php5-related packages
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: Development/Other

Requires: appliance-devel-php5-modules

Requires: php5-pdo
Requires: php5-dom
Requires: php5-mhash
Requires: php5
Requires: php5-libs
Requires: php5-devel
Requires: php5-gd2
# needed at least for OpenID
Requires: php5-curl
# paranoia -- rulez!
Requires: php5-suhosin

Requires: php-manual-ru
Requires: apache-mod_php5

# Not exists for PHP5
#Requires: php5-domxml
#Requires: php5-xslt
#Requires: php5-mime_magic
#Requires: php5-xcache
#Requires: php5-imagick

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus


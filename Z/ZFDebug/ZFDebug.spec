Name: ZFDebug
Version: 1.5
Release: alt1

Summary: a debug bar for Zend Framework
License: %bsdstyle
Group: Development/Other

Url: http://code.google.com/p/zfdebug/
Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

# http://zfdebug.googlecode.com/files/ZFDebug-%version.zip
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: rpm-build-php5
Requires: ZendFramework

%description
ZFDebug is a plugin for the Zend Framework for PHP5. It provides
useful debug information displayed in a small bar at the bottom
of every page.

%prep
%setup

%install
mkdir -p %buildroot%php5_datadir/%name/library
cp -a library/%name %buildroot%php5_datadir/%name/library

mkdir -p %buildroot%php5_moddir
ln -s -- $(relative %php5_datadir/%name/library/%name %php5_moddir/%name) %buildroot%php5_moddir/%name

%files
%doc license.txt demos
%php5_datadir/%name
%php5_moddir/%name

%changelog
* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.5-alt1
- Initial build for ALT Linux Sisyphus

* Tue Oct 15 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.5-alt0.1
- Initial build

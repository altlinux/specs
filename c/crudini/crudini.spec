Name: crudini
Version: 0.7
Release: alt1
Summary: A utility for manipulating ini files
Group: Development/Python

License: GPLv2
Url: https://github.com/pixelb/%name
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: https://github.com/pixelb/%name/archive/%version.tar.gz

BuildArch: noarch
BuildRequires: python-module-iniparse
Requires: python-module-iniparse

%description
A utility for easily handling ini files from the command line and shell
scripts.

%prep
%setup

%build

%install
install -p -D -m 0755 %name %buildroot%_bindir/%name
install -p -D -m 0644 %name.1 %buildroot%_man1dir/%name.1

%check
pushd tests
./test.sh
popd

%files
%doc README COPYING TODO NEWS example.ini
%_bindir/%name
%_man1dir/%name.*

%changelog
* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 0.7-alt1
- 0.7

* Fri Jul 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.3-alt1
- First build for ALT (based on EL 0.3-2.el6)


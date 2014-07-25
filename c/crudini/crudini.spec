Name: crudini
Version: 0.3
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

%check
pushd tests
./test.sh
popd

%files
%doc README COPYING TODO example.ini
%_bindir/%name

%changelog
* Fri Jul 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.3-alt1
- First build for ALT (based on EL 0.3-2.el6)


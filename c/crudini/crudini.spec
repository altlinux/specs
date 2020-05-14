Name: crudini
Version: 0.9.3
Release: alt1
Summary: A utility for manipulating ini files
Group: Development/Python3

License: GPLv2
Url: https://github.com/pixelb/%name
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: https://github.com/pixelb/%name/archive/%version.tar.gz
Patch: crudini-py3.patch

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-iniparse

%description
A utility for easily handling ini files from the command line and shell
scripts.

%prep
%setup
%patch -p1

%build

%install
install -p -D -m 0755 %name %buildroot%_bindir/%name
install -p -D -m 0644 %name.1 %buildroot%_man1dir/%name.1

%check
pushd tests
LC_ALL=en_US.utf8 ./test.sh
popd

%files
%doc README COPYING TODO NEWS example.ini
%_bindir/%name
%_man1dir/%name.*

%changelog
* Wed May 13 2020 Alexey Shabalin <shaba@altlinux.org> 0.9.3-alt1
- 0.9.3

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 0.7-alt1
- 0.7

* Fri Jul 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.3-alt1
- First build for ALT (based on EL 0.3-2.el6)


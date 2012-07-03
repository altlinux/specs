%define modulename ipaddr

Name: python-module-%modulename
Version: 2.1.7
Release: alt1

Summary: Library for working with IP addressess, both IPv4 and IPv6
License: Apache License, Version 2.0
Group: Development/Python
Url: http://code.google.com/p/ipaddr-py/
Packager: Liudmila Butorina <lbutorina@altlinux.org>

BuildArch: noarch

Source0: %modulename-%version.tar.gz

BuildPreReq: %py_dependencies setuptools

%description
An IPv4/IPv6 manipulatin library in Python/This library is used to create/poke/manipulate IPv4 and IPv6 addresses and prefixes.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Mon Jan 30 2012 Liudmila Butorina <lbutorina@altlinux.org> 2.1.7-alt1
- Initial build


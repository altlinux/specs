%global modname iniparse

Name: python3-module-%modname
Version: 0.5
Release: alt1
Summary: Python Module for Accessing and Modifying Configuration Data in INI files
Group: Development/Python3
License: MIT and Python
Url: https://github.com/candlepin/python-iniparse
Source: %modname-%version.tar.gz

BuildRequires: python3-module-setuptools
# for tests
BuildRequires: python3-module-six python3-test

BuildArch: noarch

%description
iniparse is an INI parser for Python which is API compatible with the
standard library's ConfigParser, preserves structure of INI files
(order of sections & options, indentation, comments, and blank lines
are preserved when data is updated), and is more convenient to use.

%prep
%setup -n %modname-%version
chmod -c -x html/index.html

%build
%python3_build

%install
%python3_install
mv %buildroot%_docdir/iniparse-%version %buildroot/%_docdir/%name-%version

%check
python3 runtests.py

%files
%_docdir/%name-%version
%python3_sitelibdir/*

%changelog
* Thu May 14 2020 Alexey Shabalin <shaba@altlinux.org> 0.5-alt1
- Initial release.

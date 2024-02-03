%global modname iniparse

Name: python3-module-%modname
Version: 0.5
Release: alt2
Summary: Python Module for Accessing and Modifying Configuration Data in INI files
Group: Development/Python3
License: MIT and Python
Url: https://github.com/candlepin/python-iniparse
Source: %modname-%version.tar.gz
Patch0: fix-compatifility-issues-py311.patch
Patch1: fix-tests-with-py312.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
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
%patch0 -p1
%patch1 -p1

chmod -c -x html/index.html

%build
%pyproject_build

%install
%pyproject_install
mv %buildroot%_docdir/iniparse-%version %buildroot/%_docdir/%name-%version

%check
%pyproject_run -- %__python3 runtests.py

%files
%_docdir/%name-%version
%python3_sitelibdir/%modname
%python3_sitelibdir/%modname-%version.dist-info

%changelog
* Sat Feb 03 2024 Anton Vyatkin <toni@altlinux.org> 0.5-alt2
- Moved on modern pyproject macros.

* Thu May 14 2020 Alexey Shabalin <shaba@altlinux.org> 0.5-alt1
- Initial release.

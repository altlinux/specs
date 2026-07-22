%global modname iniparse

%def_with check

Name: python3-module-%modname
Version: 0.5.1
Release: alt2
Summary: Python Module for Accessing and Modifying Configuration Data in INI files
Group: Development/Python3
License: MIT and Python
Url: https://github.com/candlepin/python-iniparse

Source: %name-%version.tar
Patch: iniparse-0.5.1-py314-fix.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-test
%endif

BuildArch: noarch

%description
iniparse is an INI parser for Python which is API compatible with the
standard library's ConfigParser, preserves structure of INI files
(order of sections & options, indentation, comments, and blank lines
are preserved when data is updated), and is more convenient to use.

%prep
%setup
%patch -p1

# Fix version
sed -i 's/VERSION = "0.5"/VERSION = "%version"/' setup.py

chmod -c -x html/index.html

%build
%pyproject_build

%install
%pyproject_install
rm -rf %buildroot%_datadir/doc/iniparse-%version

%check
%pyproject_run -- %__python3 runtests.py

%files
%doc README.*
%python3_sitelibdir/%modname
%python3_sitelibdir/%modname-%version.dist-info

%changelog
* Wed Jul 22 2026 Anton Vyatkin <toni@altlinux.org> 0.5.1-alt2
- Fix FTBFS.

* Fri Dec 20 2024 Anton Vyatkin <toni@altlinux.org> 0.5.1-alt1
- New version 0.5.1.

* Sat Feb 03 2024 Anton Vyatkin <toni@altlinux.org> 0.5-alt2
- Moved on modern pyproject macros.

* Thu May 14 2020 Alexey Shabalin <shaba@altlinux.org> 0.5-alt1
- Initial release.

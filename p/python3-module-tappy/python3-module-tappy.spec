%define modname tap.py

Name: python3-module-tappy
Version: 3.1
Release: alt1

Summary: Test Anything Protocol (TAP) tools
Group: Development/Python3
License: BSD-2-Clause
Url: http://pypi.python.org/pypi/%modname

# VCS: https://github.com/python-tap/tappy
Source: http://pypi.io/packages/source/t/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires: python3-devel rpm-build-python3 python3-module-babel
BuildRequires: python3-module-distribute

%description
tappy python module provides a set of tools for working with the Test
Anything Protocol (TAP), a line based test protocol for recording test
data in a standard way.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%files
%_bindir/tap
%_bindir/tappy
%python3_sitelibdir_noarch/tap
%python3_sitelibdir_noarch/*.egg-info
%doc README.md LICENSE

%changelog
* Wed Dec 29 2021 Yuri N. Sedunov <aris@altlinux.org> 3.1-alt1
- 3.1

* Tue Mar 31 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt1
- 3.0 (Python3 only)
- fixed License tag

* Wed Dec 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2
- made python2 build optional

* Mon Oct 01 2018 Yuri N. Sedunov <aris@altlinux.org> 2.5-alt1
- 2.5

* Wed Jun 06 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4-alt1
- 2.4

* Wed Jan 31 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2-alt1
- first build for Sisyphus




%define modname pytest-tap

Name: python3-module-%modname
Version: 3.3
Release: alt1

Summary: Test Anything Protocol (TAP) reporting plugin for pytest
Group: Development/Python3
License: BSD-2-Clause
Url: http://pypi.python.org/pypi/%modname

# VCS: https://github.com/python-tap/pytest-tap
Source: http://pypi.io/packages/source/p/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute python3-module-babel

%description
%modname is a reporting plugin for pytest that outputs Test Anything
Protocol (TAP) data. TAP is a line based test protocol for recording test
data in a standard way.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/pytest_tap/
%python3_sitelibdir_noarch/*.egg-info
%doc README* LICENSE

%changelog
* Wed Oct 27 2021 Yuri N. Sedunov <aris@altlinux.org> 3.3-alt1
- 3.3

* Mon Nov 09 2020 Yuri N. Sedunov <aris@altlinux.org> 3.2-alt1
- 3.2

* Wed Mar 25 2020 Yuri N. Sedunov <aris@altlinux.org> 3.1-alt1
- 3.1 (python3 only)
- fixed License tag

* Wed Jan 31 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2-alt1
- first build for Sisyphus




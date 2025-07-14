%define modname tappy
%define pypi_name tap_py

%def_enable check

Name: python3-module-%modname
Version: 3.2.1
Release: alt1

Summary: Test Anything Protocol (TAP) tools
Group: Development/Python3
License: BSD-2-Clause
Url: https://pypi.python.org/pypi/%pypi_name

Vcs: https://github.com/python-tap/tappy.git

Source: http://pypi.io/packages/source/t/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

Provides: python3-module-%pypi_name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3(wheel) python3(hatchling)
BuildRequires: python3(babel)
%{?_enable_check:BuildRequires: python3(tox)}

%description
tappy python module provides a set of tools for working with the Test
Anything Protocol (TAP), a line based test protocol for recording test
data in a standard way.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%_bindir/tap
%_bindir/tappy
%python3_sitelibdir_noarch/tap
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
#%doc README.md
%doc LICENSE

%changelog
* Sun Jul 13 2025 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

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




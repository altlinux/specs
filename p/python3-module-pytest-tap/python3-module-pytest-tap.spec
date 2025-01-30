%define modname pytest-tap
%define pypi_name pytest_tap

Name: python3-module-%modname
Version: 3.5
Release: alt1

Summary: Test Anything Protocol (TAP) reporting plugin for pytest
Group: Development/Python3
License: BSD-2-Clause
Url: http://pypi.python.org/pypi/%modname

Vcs: https://github.com/python-tap/pytest-tap.git

Source: http://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch
%py3_provides %pypi_name
Provides: python3-module-%pypi_name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(hatchling)

%description
%modname is a reporting plugin for pytest that outputs Test Anything
Protocol (TAP) data. TAP is a line based test protocol for recording test
data in a standard way.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc AUTHORS LICENSE

%changelog
* Thu Jan 30 2025 Yuri N. Sedunov <aris@altlinux.org> 3.5-alt1
- 3.5

* Sun Jul 16 2023 Yuri N. Sedunov <aris@altlinux.org> 3.4-alt1
- 3.4

* Wed Oct 27 2021 Yuri N. Sedunov <aris@altlinux.org> 3.3-alt1
- 3.3

* Mon Nov 09 2020 Yuri N. Sedunov <aris@altlinux.org> 3.2-alt1
- 3.2

* Wed Mar 25 2020 Yuri N. Sedunov <aris@altlinux.org> 3.1-alt1
- 3.1 (python3 only)
- fixed License tag

* Wed Jan 31 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2-alt1
- first build for Sisyphus




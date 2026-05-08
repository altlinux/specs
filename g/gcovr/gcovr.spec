%def_disable snapshot
%def_enable check

Name: gcovr
Version: 8.6
Release: alt1

Summary: A Python script for summarizing gcov data
License: BSD-3-Clause
Group: Development/Tools
Url: https://pypi.python.org/pypi/gcovr

Vcs: https://github.com/gcovr/gcovr.git

%if_disabled snapshot
Source: https://pypi.io/packages/source/g/%name/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

BuildArch: noarch

Requires: /usr/bin/gcov
Requires: python3-module-jinja2 python3-module-Pygments

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel)
BuildRequires: python3(hatchling) python3(hatch-vcs) python3(hatch-fancy-pypi-readme)
%{?_enable_check:
BuildRequires: python3(pytest) python3(pytest_timeout) python3(pytest_cov)
BuildRequires: python3(pytest_env) python3(pytest_check) python3(xdist) python3(nox)
BuildRequires: /usr/bin/gcov gcc-c++ make cmake ninja-build
BuildRequires: python3(lxml) python3(yaxmldiff)
BuildRequires: python3(jinja2) python3(Pygments)}

%description
Gcovr provides a utility for managing the use of the GNU gcov utility
and generating summarized code coverage results. This command is inspired
by the Python coverage.py package, which provides a similar utility for
Python.

%prep
%setup
#sed -i 's/--timeout=120//' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%_bindir/%name
%python3_sitelibdir_noarch/%name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %name}

%changelog
* Fri May 08 2026 Yuri N. Sedunov <aris@altlinux.org> 8.6-alt1
- 8.6

* Sun Aug 07 2022 Yuri N. Sedunov <aris@altlinux.org> 5.2-alt1
- 5.2
- ported to %%pyproject* macros

* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 5.1-alt1
- 5.1

* Fri Jun 11 2021 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt1
- 5.0
- fixed License tag

* Sat Nov 09 2019 Yuri N. Sedunov <aris@altlinux.org> 4.2-alt1
- 4.2

* Wed Jul 04 2018 Yuri N. Sedunov <aris@altlinux.org> 4.1-alt1
- 4.1

* Mon Jun 18 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0-alt1
- 4.0

* Wed Feb 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.4-alt1
- 3.4 with Python3

* Tue Nov 01 2016 Yuri N. Sedunov <aris@altlinux.org> 3.3-alt1
- 3.3

* Fri Dec 13 2013 Igor Zubkov <icesik@altlinux.org> 3.1-alt1
- 3.1

* Sat Sep 14 2013 Igor Zubkov <icesik@altlinux.org> 3.0-alt1
- 2.4 -> 3.0

* Mon Sep 02 2013 Igor Zubkov <icesik@altlinux.org> 2.4-alt2
- Update Url

* Wed Aug 28 2013 Igor Zubkov <icesik@altlinux.org> 2.4-alt1
- build for Sisyphus


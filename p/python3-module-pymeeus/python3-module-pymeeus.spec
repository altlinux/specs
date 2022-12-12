%define pypi_name pymeeus
%define _name PyMeeus
%def_enable check

Name: python3-module-%pypi_name
Version: 0.5.12
Release: alt1

Summary: Library of astronomical algorithms in Python
Group: Development/Python3
License: GPL-3.0 and LGPL-3.0
Url: https://pypi.python.org/pypi/%_name

Source: https://pypi.io/packages/source/P/%_name/%_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute python3(wheel)
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-pytest-cov
BuildRequires: python3-module-mccabe}

%description
PyMeeus is a Python 3 implementation of the astronomical algorithms
described in the classical book "Astronomical Algorithms, 2nd Edition,
Willmann-Bell Inc. (1998)" by Jean Meeus.

%prep
%setup -n %_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir_noarch
py.test3 tests

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%_name-%version.dist-info
%doc *.rst *.md

%changelog
* Sun Dec 11 2022 Yuri N. Sedunov <aris@altlinux.org> 0.5.12-alt1
- 0.5.12
- ported to %%pyproject* macros

* Sat Jul 24 2021 Yuri N. Sedunov <aris@altlinux.org> 0.5.11-alt2
- python3-only build

* Wed Apr 14 2021 Yuri N. Sedunov <aris@altlinux.org> 0.5.11-alt1
- 0.5.11

* Sun Feb 21 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.13-alt1
- 0.3.13
- enabled %%check

* Thu Apr 02 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.7-alt1
- 0.3.7
- fixed License tag

* Wed Dec 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- first build for Sisyphus




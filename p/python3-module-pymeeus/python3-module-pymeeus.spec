%define modname pymeeus
%define _name PyMeeus
%def_enable check

Name: python3-module-%modname
Version: 0.5.11
Release: alt2

Summary: Library of astronomical algorithms in Python
Group: Development/Python3
License: GPL-3.0 and LGPL-3.0
Url: https://pypi.python.org/pypi/%_name

Source: https://pypi.io/packages/source/P/%_name/%_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%{?_enable_check:BuildRequires: python3-module-pytest}

%description
PyMeeus is a Python 3 implementation of the astronomical algorithms
described in the classical book "Astronomical Algorithms, 2nd Edition,
Willmann-Bell Inc. (1998)" by Jean Meeus.

%prep
%setup -n %_name-%version

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir_noarch
py.test3 tests

%files
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/*.egg-info
%doc *.rst

%changelog
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




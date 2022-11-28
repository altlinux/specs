%define pypi_name pymediainfo
%def_enable check

Name: python3-module-%pypi_name
Version: 6.0.1
Release: alt1

Summary: A Python 3 wrapper for the mediainfo library
Group: Development/Python3
License: MIT
Url: https://pypi.python.org/pypi/%pypi_name
Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

Requires: libmediainfo

%define python3_ver 3.5

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel >= %python3_ver python3-module-wheel python3-module-setuptools_scm
%{?_enable_check:BuildRequires: python3-module-tox python3-module-pytest-xdist libmediainfo
BuildRequires: python3(mypy) python3(pylint)}

%description
This Python3 module provides a wrapper around the MediaInfo library.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README.rst


%changelog
* Sun Nov 27 2022 Yuri N. Sedunov <aris@altlinux.org> 6.0.1-alt1
- 6.0.1
- ported to %%pyproject*/%%tox* macros

* Sun May 02 2021 Yuri N. Sedunov <aris@altlinux.org> 5.1.0-alt1
- 5.1.0

* Mon Apr 12 2021 Yuri N. Sedunov <aris@altlinux.org> 5.0.4-alt1
- 5.0.4

* Tue Nov 24 2020 Yuri N. Sedunov <aris@altlinux.org> 5.0.3-alt1
- 5.0.3
- enabled %%check

* Fri Nov 20 2020 Yuri N. Sedunov <aris@altlinux.org> 5.0.2-alt1
- 5.0.2

* Sun Nov 08 2020 Yuri N. Sedunov <aris@altlinux.org> 4.3-alt1
- 4.3

* Thu Apr 30 2020 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- 4.2.1

* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1-alt1
- 4.1
- disabled python2 module

* Sat Apr 06 2019 Yuri N. Sedunov <aris@altlinux.org> 4.0-alt1
- 4.0

* Wed Mar 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.1-alt1
- 3.1

* Sat Nov 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt1
- 3.0

* Wed May 16 2018 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sat Mar 03 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Wed Nov 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.1.9-alt1
- first build for Sisyphus



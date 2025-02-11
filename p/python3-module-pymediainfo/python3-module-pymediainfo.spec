%define pypi_name pymediainfo
%def_enable check

Name: python3-module-%pypi_name
Version: 7.0.0
Release: alt1

Summary: A Python 3 wrapper for the mediainfo library
Group: Development/Python3
License: MIT
Url: https://pypi.python.org/pypi/%pypi_name

Vcs: https://github.com/sbraz/pymediainfo.git

Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

Requires: libmediainfo

%define python3_ver 3.9

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel >= %python3_ver python3(wheel) python3(pdm.backend)
%{?_enable_check:BuildRequires: python3(tox) python3(xdist) libmediainfo
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
* Tue Feb 11 2025 Yuri N. Sedunov <aris@altlinux.org> 7.0.0-alt1
- 7.0.0

* Mon Oct 30 2023 Yuri N. Sedunov <aris@altlinux.org> 6.1.0-alt1
- 6.1.0

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



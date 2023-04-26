%def_disable snapshot
%define modname hijri-converter
%define pypi_name hijri_converter

%def_enable check

Name: python3-module-%modname
Version: 2.3.1
Release: alt1

Summary: Hijri to Gregorian dates converter
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

%if_disabled snapshot
Source: https://pypi.io/packages/source/h/%modname/%modname-%version.tar.gz
%else
Vcs: https://github.com/dralshehri/hijri-converter
Source: %modname-%version.tar
%endif

BuildArch: noarch
Provides: python3-module-%pypi_name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel >= 3.6 python3-module-setuptools python3-module-wheel
%{?_enable_check:BuildRequires: python3-module-pytest-cov}

%description
A Python package to convert accurately between Hijri and Gregorian dates
using the Umm al-Qura calendar of Saudi Arabia.

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test-3

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README* CHANGELOG*


%changelog
* Wed Apr 26 2023 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1
- ported to %%pyproject macros

* Thu May 26 2022 Yuri N. Sedunov <aris@altlinux.org> 2.2.4-alt1
- 2.2.4

* Sat Mar 05 2022 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1
- 2.2.3

* Wed Sep 29 2021 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Mon Sep 06 2021 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Mon Aug 16 2021 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Fri Jun 25 2021 Yuri N. Sedunov <aris@altlinux.org> 2.1.3-alt1
- 2.1.3

* Tue Jun 01 2021 Yuri N. Sedunov <aris@altlinux.org> 2.1.2-alt1
- 2.1.2

* Thu Nov 05 2020 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- first build for Sisyphus



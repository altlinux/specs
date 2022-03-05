%def_disable snapshot
%define modname hijri-converter
%def_enable check

Name: python3-module-%modname
Version: 2.2.3
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

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel >= 3.6
%{?_enable_check:BuildRequires: python3-module-pytest}

%description
A Python package to convert accurately between Hijri and Gregorian dates
using the Umm al-Qura calendar of Saudi Arabia.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py check

%files
%python3_sitelibdir_noarch/*
%doc README* CHANGELOG*


%changelog
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



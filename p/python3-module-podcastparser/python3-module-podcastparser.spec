%def_enable snapshot
%define pypi_name podcastparser
%def_enable check

Name: python3-module-%pypi_name
Version: 0.6.10
Release: alt2

Summary: Simple, fast and efficient podcast parser written in Python3.
Group: Development/Python3
License: ISC
Url: http://gpodder.org/%pypi_name

BuildArch: noarch

Vcs: https://github.com/gpodder/podcastparser.git
%if_disabled snapshot
Source: https://github.com/gpodder/%pypi_name/archive/%version/%pypi_name-%version.tar.gz
%else
Source: %pypi_name-%version.tar
%endif

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel rpm-build-python3 python3-module-setuptools python3(wheel)
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-pytest-cov python3-module-coverage}

%description
The podcast parser project is a library from the gPodder project to provide an
easy and reliable way of parsing RSS- and Atom-based podcast feeds in Python.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=./
py.test3

%files
%python3_sitelibdir_noarch/%{pypi_name}*
%python3_sitelibdir_noarch/__pycache__/%{pypi_name}*
%doc README.md


%changelog
* Tue Feb 13 2024 Yuri N. Sedunov <aris@altlinux.org> 0.6.10-alt2
- updated to 0.6.10-4-g03e5477 (fixed build with python-3.12)

* Tue Apr 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.10-alt1
- 0.6.10

* Wed Dec 14 2022 Yuri N. Sedunov <aris@altlinux.org> 0.6.9-alt1
- 0.6.9
- ported to %%pyproject* macros

* Fri Sep 24 2021 Yuri N. Sedunov <aris@altlinux.org> 0.6.8-alt1
- 0.6.8

* Thu Aug 12 2021 Yuri N. Sedunov <aris@altlinux.org> 0.6.7-alt1
- 0.6.7

* Tue Nov 10 2020 Yuri N. Sedunov <aris@altlinux.org> 0.6.6-alt1
- 0.6.6

* Thu Apr 09 2020 Yuri N. Sedunov <aris@altlinux.org> 0.6.5-alt1
- 0.6.5 (python3 only)
- fixed License tag

* Fri Aug 31 2018 Yuri N. Sedunov <aris@altlinux.org> 0.6.4-alt1
- 0.6.4

* Wed Jan 31 2018 Yuri N. Sedunov <aris@altlinux.org> 0.6.3-alt1
- 0.6.3

* Fri Nov 03 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt1
- 0.6.2

* Sun Jan 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- first build for Sisyphus



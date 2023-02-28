%define pypi_name toposort
%def_enable check

Name: python3-module-%pypi_name
Version: 1.10
Release: alt1

Summary: %pypi_name implements a topological sort algorithm
Group: Development/Python3
License: Apache-2.0
Url: https://pypi.org/project/%pypi_name

Vcs: https://bitbucket.org/ericvsmith/toposort.git
Source: https://pypi.io/packages/source/t/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 >= 0.1.19
BuildRequires: python3-module-setuptools >= 42 python3-module-wheel

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
%__python3 -m test.test_toposort

%files
%python3_sitelibdir_noarch/*
%doc README* CHANGES* NOTICE

%changelog
* Tue Feb 28 2023 Yuri N. Sedunov <aris@altlinux.org> 1.10-alt1
- 1.10

* Mon Jan 23 2023 Yuri N. Sedunov <aris@altlinux.org> 1.9-alt1
- 1.9

* Mon Jun 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.7-alt1
- 1.7 (deleted setup.py)

* Mon May 30 2022 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt1.1
- fixed BR

* Tue Mar 09 2021 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt1
- 1.6

* Tue Jul 21 2020 Yuri N. Sedunov <aris@altlinux.org> 1.5-alt1
- first build for Sisyphus





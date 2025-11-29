%define modname stdio-mgr
%define pypi_name stdio_mgr

%def_enable check

Name: python3-module-%modname
Version: 1.0.1.1
Release: alt1

Summary: Testing library for CLI Python applications
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/stdio-mgr/

Vcs: https://www.github.com/bskinn/stdio-mgr
Source: http://pypi.io/packages/source/s/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

Provides: pyhon3(%pypi_name) = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel python3-module-setuptools python3(attr)
%{?_enable_check:BuildRequires: python3(tox) python3(pytest) python3(flake8)}

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Sat Nov 29 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.1.1-alt1
- 1.0.1.1

* Tue Nov 15 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- first build for Sisyphus



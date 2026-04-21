%def_disable snapshot
%define pypi_name pyciede2000
%def_disable check

Name: python3-module-%pypi_name
Version: 0.0.21
Release: alt1

Summary: Python implementation of CIEDE2000 color difference calculation
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/%pypi_name

Vcs: https://github.com/shameempk/pyciede2000.git

%if_disabled snapshot
Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz
%else
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

Provides: %pypi_name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(pytest)}

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README*


%changelog
* Tue Apr 21 2026 Yuri N. Sedunov <aris@altlinux.org> 0.0.21-alt1
- first build for Sisyphus



%define modname StrEnum
%define pypi_name strenum
%def_enable check

Name: python3-module-%pypi_name
Version: 0.5.0
Release: alt1

Summary: A Python Enum that inherits from str
Group: Development/Python3
License: MIT
Url: https://pypi.python.org/pypi/%modname

Vcs: https://github.com/irgeek/StrEnum.git

Source: https://pypi.io/packages/source/S/%modname/%pypi_name-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools_scm)
%{?_enable_check:BuildRequires: python3(pytest) python3(pytest-cov)}

%description
StrEnum is a Python 'enum.Enum' that inherits from 'str' to complement
'enum.IntEnum' in the standard library.

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
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%doc README*


%changelog
* Sun Nov 01 2026 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue May 06 2025 Yuri N. Sedunov <aris@altlinux.org> 0.4.15-alt1.1
- fixed build with setuptools 75.8.1

* Fri Sep 20 2024 Yuri N. Sedunov <aris@altlinux.org> 0.4.15-alt1
- first build for Sisyphus



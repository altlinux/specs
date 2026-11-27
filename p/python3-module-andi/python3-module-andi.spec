%define pypi_name andi
%def_enable check

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt1

Summary: Library for annotation-based dependency injection
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/andi

Vcs: https://github.com/scrapinghub/andi

Source: https://pypi.io/packages/source/a/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(hatchling)
%{?_enable_check:BuildRequires: python3(pytest)
BuildRequires: python3(attrs)}

%description
andi makes it easy to implement custom dependency injection mechanisms
where dependencies are expressed using type annotations.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/
%doc README* LICENSE*

%changelog
* Fri Nov 27 2026 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- first build for Sisyphus


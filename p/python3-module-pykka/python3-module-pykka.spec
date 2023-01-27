%define _unpackaged_files_terminate_build 1
%define pypi_name pykka
%def_with check

Name: python3-module-%pypi_name
Version: 3.1.1
Release: alt1
Summary: Python implementation of the actor model
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/jodal/pykka
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(poetry.core)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest-mock)
%endif

%description
Pykka is a Python implementation of the actor model.
The actor model introduces some simple rules to control
the sharing of state and cooperation between execution units,
which makes it easier to build concurrent applications.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jan 27 2023 Alexander Makeenkov <amakeenk@altlinux.org> 3.1.1-alt1
- Updated to version 3.1.1
- Use pyproject macroses for build
- Enabled tests while build
- Don't pack tests and docs

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2.0.2-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Mon Jan 27 2020 Alexander Makeenkov <amakeenk@altlinux.org> 2.0.2-alt1
- Initial build for ALT

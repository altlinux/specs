%def_disable snapshot
%define _unpackaged_files_terminate_build 1
%define pypi_name poetry

%def_disable check

Name: python3-module-%pypi_name
Version: 1.4.2
Release: alt1

Summary: Poetry -- Python build system
License: MIT
Group: Development/Python3
Url: https://python-poetry.org/

%if_disabled snapshot
Source: https://github.com/python-poetry/poetry/archive/%version/%pypi_name-%version.tar.gz
%else
Vcs: https://github.com/python-poetry/poetry.git
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

%define core_ver 1.5.2
%define dulwich_ver 0.21.2

Requires: python3-module-poetry-core >= %core_ver
Requires: python3-module-dulwich >= %dulwich_ver
Provides: %pypi_name = %EVR
Provides: /usr/bin/%pypi_name

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(poetry-core)

%{?_enable_check:BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(pep517)
BuildRequires: python3(keyring)
BuildRequires: python3-module-pkginfo > 1.9.4
BuildRequires: python3-module-poetry-core >= %core_ver
BuildRequires: python3-module-dulwich >= %dulwich_ver
BuildRequires: python3(%{pypi_name}_plugin_export)}

%description
poetry is a tool to handle dependency installation as well as building
and packaging of Python packages. It only needs one file to do all of
that: the new, standardized pyproject.toml.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%doc README.md CHANGELOG.md 

%changelog
* Sun Apr 02 2023 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Mon Mar 20 2023 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Tue Feb 28 2023 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Jan 30 2023 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

* Tue Oct 11 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Tue Sep 27 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Mon Sep 12 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- first build for Sisyphus (1.2.0-28-gb5b78434)




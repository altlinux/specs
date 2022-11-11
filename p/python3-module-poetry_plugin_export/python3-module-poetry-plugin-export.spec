%def_disable snapshot
%define _unpackaged_files_terminate_build 1
%define modname poetry-plugin-export
%define pypi_name poetry_plugin_export

%def_disable check

Name: python3-module-%pypi_name
Version: 1.2.0
Release: alt1

Summary: Poetry plugin that allows the export of locked packages to various formats.
License: MIT
Group: Development/Python3
Url: https://python-poetry.org/

%if_disabled snapshot
Source: https://github.com/python-poetry/%modname/archive/%version/%modname-%version.tar.gz
%else
Vcs: https://github.com/python-poetry/poetry-plugin-export.git
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

%define core_ver 1.1
%define poetry_ver 1.2

Requires: python3-module-poetry-core >= %core_ver

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(poetry-core)

%{?_enable_check:BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(mypy)
BuildRequires: python3-module-poetry-core >= %core_ver
BuildRequires: python3(poetry)}

%description
This package is a plugin that allows the export of locked
packages to various formats.

Note: For now, only the requirements.txt format is available.

This plugin provides the same features as the existing export command of
Poetry which it will eventually replace.

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%doc README.md CHANGELOG.md 

%changelog
* Sat Nov 12 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Oct 10 2022 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Mon Oct 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Tue Sep 27 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- 1.0.7

* Mon Sep 12 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- first build for Sisyphus




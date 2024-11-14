%define pypi_name pytest-mypy-plugins
%define mod_name pytest_mypy_plugins

%def_with check

Name:    python3-module-%pypi_name
Version: 3.1.2
Release: alt1

Summary: pytest plugin for testing mypy types, stubs, and plugins
License: MIT
Group:   Development/Python3
URL:     https://github.com/TypedDjango/pytest-mypy-plugins

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-yaml
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-regex
BuildRequires: python3-module-decorator
BuildRequires: python3-module-tomlkit
BuildRequires: python3-module-mypy
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=$PWD
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Nov 09 2024 Alexander Burmatov <thatman@altlinux.org> 3.1.2-alt1
- Initial build for Sisyphus.

%define _unpackaged_files_terminate_build 1
%define pypi_name jupyter-events
%define mod_name jupyter_events

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt1
Summary: Configurable event system for Jupyter applications and extensions
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/jupyter-events/
Vcs: https://github.com/jupyter/jupyter_events
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-console-scripts
BuildRequires: python3-module-python-json-logger
BuildRequires: python3-module-traitlets
BuildRequires: python3-module-rich
BuildRequires: python3-module-click
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-pyaml
BuildRequires: python3-module-rfc3339-validator
%endif

%description
Jupyter Events enables Jupyter Python Applications (e.g. Jupyter Server,
JupyterLab Server, JupyterHub, etc.) to emit events-structured data describing
things happening inside the application. Other software (e.g. client applications
like JupyterLab) can listen and respond to these events.

%prep
%setup
sed -i 's/--color=yes//' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v -k 'not test_bad_validations'

%files
%doc README.*
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Tue Nov 07 2023 Anton Vyatkin <toni@altlinux.org> 0.9.0-alt1
- New version 0.9.0.

* Thu Oct 19 2023 Anton Vyatkin <toni@altlinux.org> 0.8.0-alt1
- New version 0.8.0.

* Wed Aug 02 2023 Anton Vyatkin <toni@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Tue Jun 13 2023 Anton Vyatkin <toni@altlinux.org> 0.6.3-alt1
- Initial build for Sisyphus

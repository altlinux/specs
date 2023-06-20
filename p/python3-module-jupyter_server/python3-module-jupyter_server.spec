%define _unpackaged_files_terminate_build 1
%define pypi_name jupyter_server

%def_without check

Name:    python3-module-%pypi_name
Version: 2.6.0
Release: alt1

Summary: The backend -core services, APIs, and REST endpoints-to Jupyter web applications
License: BSD-3-Clause
Group:   Development/Python3
URL: https://pypi.org/project/jupyter-server/
VCS: https://github.com/jupyter-server/jupyter_server

BuildArch: noarch

Source0: %pypi_name-%version.tar
Source1: bootstrap.min.css
Source2: bootstrap-theme.min.css

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-jupyter-builder
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-nbformat
BuildRequires: python3-module-jupyter_events
BuildRequires: python3-module-prometheus_client
BuildRequires: python3-module-jupyter_client
BuildRequires: python3-module-websocket-client
BuildRequires: python3-module-overrides
BuildRequires: python3-module-anyio
BuildRequires: python3-module-send2trash
BuildRequires: python3-module-pytest-console-scripts
BuildRequires: python3-module-pytest-timeout
%endif

%add_python3_req_skip jupyter_server_terminals
%add_python3_req_skip jupyter_server_terminals.api_handlers
%add_python3_req_skip jupyter_server_terminals.handlers
%add_python3_req_skip jupyter_server_terminals.terminalmanager

%description
The Jupyter Server provides the backend (i.e. the core services, APIs,
and REST endpoints) for Jupyter web applications like Jupyter notebook,
JupyterLab, and Voila.

%prep
%setup -n %pypi_name-%version
cp %SOURCE1 jupyter_server/static/style/
cp %SOURCE2 jupyter_server/static/style/

sed -i pyproject.toml -e 's/--color=yes//'

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v -m 'not network'

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jun 02 2023 Anton Vyatkin <toni@altlinux.org> 2.6.0-alt1
- Initial build for Sisyphus

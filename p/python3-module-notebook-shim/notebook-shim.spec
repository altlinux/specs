%define _unpackaged_files_terminate_build 1
%define pypi_name notebook-shim
%define mod_name notebook_shim

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.3
Release: alt1
Summary: A shim layer for notebook traits and config
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/notebook-shim/
VCS: https://github.com/jupyter/notebook_shim
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-jupyter
BuildRequires: python3-module-jupyter_server
%endif

%description
This project provides a way for JupyterLab and other frontends to switch
to Jupyter Server for their Python Web application backend.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %EVR

%description tests
This project provides a way for JupyterLab and other frontends to switch
to Jupyter Server for their Python Web application backend.

This package contains tests for %pypi_name.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

install -d -m 755 %buildroot%_sysconfdir/jupyter/jupyter_server_config.d
mv %buildroot/usr/etc/jupyter/jupyter_server_config.d/notebook_shim.json \
   %buildroot%_sysconfdir/jupyter/jupyter_server_config.d

%check
%pyproject_run_pytest -v

%files
%doc README.*
%dir %_sysconfdir/jupyter/
%config(noreplace) %_sysconfdir/jupyter/*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%mod_name/tests

%files tests
%python3_sitelibdir/%mod_name/tests

%changelog
* Mon Jun 19 2023 Anton Vyatkin <toni@altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus


%define _unpackaged_files_terminate_build 1
%define pypi_name jupyterlab

%def_with check

Name: python3-module-%pypi_name
Version: 4.0.3
Release: alt1
Summary: JupyterLab computational environment
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/jupyterlab/
BuildArch: noarch
Source: %pypi_name-%version.tar

Requires: python3-module-ipykernel

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-jupyter-builder
BuildRequires: npm
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-jupyter
BuildRequires: python3-module-jupyterlab-server
BuildRequires: python3-module-notebook-shim
BuildRequires: python3-module-async-lru
%endif

%description
An extensible environment for interactive and reproducible computing,
based on the Jupyter Notebook and Architecture.

JupyterLab is the next-generation user interface for Project Jupyter offering
all the familiar building blocks of the classic Jupyter Notebook
(notebook, terminal, text editor, file browser, rich outputs, etc.)
in a flexible and powerful user interface.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %EVR

%description tests
An extensible environment for interactive and reproducible computing,
based on the Jupyter Notebook and Architecture.

This package contains tests for %pypi_name.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

# Move config files to proper location
install -d -m 755 %buildroot%_sysconfdir/jupyter/jupyter_notebook_config.d
install -d -m 755 %buildroot%_sysconfdir/jupyter/jupyter_server_config.d
mv %buildroot/usr/etc/jupyter/jupyter_notebook_config.d/jupyterlab.json \
   %buildroot%_sysconfdir/jupyter/jupyter_notebook_config.d
mv %buildroot/usr/etc/jupyter/jupyter_server_config.d/jupyterlab.json \
   %buildroot%_sysconfdir/jupyter/jupyter_notebook_config.d

%check
%pyproject_run_pytest -v -k "\
not test_uninstall_core_extension \
and not test_install_and_uninstall_pinned_folder \
and not test_install_and_uninstall_pinned \
and not test_build_custom_minimal_core_config \
and not test_build_custom \
and not test_build_check \
and not test_clear \
and not test_update \
and not test_install \
and not test_uninstall \
and not test_app_dir \
and not test_list_extension \
and not test_enable_extension \
and not test_disable_extension \
and not test_link \
and not test_build"

%files
%doc README.*
%_bindir/*
%dir %_datadir/jupyter
%dir %_datadir/icons/hicolor/scalable
%dir %_datadir/icons/hicolor/scalable/apps
%_datadir/applications/jupyterlab.desktop
%_datadir/icons/hicolor/scalable/apps/jupyterlab.svg
%_datadir/jupyter/lab
%dir %_sysconfdir/jupyter/
%config(noreplace) %_sysconfdir/jupyter/*
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%pypi_name/tests
%exclude %python3_sitelibdir/%pypi_name/pytest_plugin.py

%files tests
%python3_sitelibdir/%pypi_name/tests
%python3_sitelibdir/%pypi_name/pytest_plugin.py

%changelog
* Fri Jul 14 2023 Anton Vyatkin <toni@altlinux.org> 4.0.3-alt1
- new version 4.0.3

* Mon Jun 12 2023 Anton Vyatkin <toni@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus

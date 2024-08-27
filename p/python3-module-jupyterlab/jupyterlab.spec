%define _unpackaged_files_terminate_build 1
%define pypi_name jupyterlab

%def_with check

Name: python3-module-%pypi_name
Version: 4.2.5
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
BuildRequires: python3-module-pytest-console-scripts
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-requests-cache
BuildRequires: node
BuildRequires: python3-module-httpx
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
%pyproject_run_pytest -v \
--deselect=jupyterlab/tests/test_build_api.py::TestBuildAPI::test_clear \
--deselect=jupyterlab/tests/test_build_api.py::TestBuildAPI::test_build \
--deselect=jupyterlab/tests/test_jupyterlab.py::TestExtension::test_build \
--deselect=jupyterlab/tests/test_jupyterlab.py::TestExtension::test_install_and_uninstall_pinned_folder \
--deselect=jupyterlab/tests/test_jupyterlab.py::TestExtension::test_install_and_uninstall_pinned \
--deselect=jupyterlab/tests/test_jupyterlab.py::TestExtension::test_uninstall_core_extension


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
%exclude %python3_sitelibdir/%pypi_name/browser_check.py

%files tests
%python3_sitelibdir/%pypi_name/tests
%python3_sitelibdir/%pypi_name/pytest_plugin.py
%python3_sitelibdir/%pypi_name/browser_check.py

%changelog
* Tue Aug 27 2024 Anton Vyatkin <toni@altlinux.org> 4.2.5-alt1
- new version 4.2.5

* Fri Jul 19 2024 Anton Vyatkin <toni@altlinux.org> 4.2.4-alt1
- new version 4.2.4

* Thu Jun 27 2024 Anton Vyatkin <toni@altlinux.org> 4.2.3-alt1
- new version 4.2.3

* Mon Jun 10 2024 Anton Vyatkin <toni@altlinux.org> 4.2.2-alt1
- new version 4.2.2

* Thu May 23 2024 Anton Vyatkin <toni@altlinux.org> 4.2.1-alt1
- new version 4.2.1

* Tue May 07 2024 Anton Vyatkin <toni@altlinux.org> 4.2.0-alt1
- new version 4.2.0

* Sat Apr 27 2024 Anton Vyatkin <toni@altlinux.org> 4.1.8-alt1
- new version 4.1.8

* Tue Apr 09 2024 Anton Vyatkin <toni@altlinux.org> 4.1.6-alt1
- new version 4.1.6

* Fri Mar 15 2024 Anton Vyatkin <toni@altlinux.org> 4.1.5-alt1
- new version 4.1.5

* Fri Mar 08 2024 Anton Vyatkin <toni@altlinux.org> 4.1.4-alt1
- new version 4.1.4

* Tue Mar 05 2024 Anton Vyatkin <toni@altlinux.org> 4.1.3-alt1
- new version 4.1.3

* Tue Feb 20 2024 Anton Vyatkin <toni@altlinux.org> 4.1.2-alt1
- new version 4.1.2

* Wed Feb 14 2024 Anton Vyatkin <toni@altlinux.org> 4.1.1-alt1
- new version 4.1.1

* Tue Feb 06 2024 Anton Vyatkin <toni@altlinux.org> 4.1.0-alt1
- new version 4.1.0

* Wed Jan 31 2024 Anton Vyatkin <toni@altlinux.org> 4.0.12-alt1
- new version 4.0.12

* Sun Jan 21 2024 Anton Vyatkin <toni@altlinux.org> 4.0.11-alt1
- new version 4.0.11

* Mon Jan 01 2024 Anton Vyatkin <toni@altlinux.org> 4.0.10-alt1
- new version 4.0.10

* Tue Nov 28 2023 Anton Vyatkin <toni@altlinux.org> 4.0.9-alt1
- new version 4.0.9

* Tue Nov 07 2023 Anton Vyatkin <toni@altlinux.org> 4.0.8-alt1
- new version 4.0.8

* Thu Oct 12 2023 Anton Vyatkin <toni@altlinux.org> 4.0.7-alt1
- new version 4.0.7

* Fri Sep 15 2023 Anton Vyatkin <toni@altlinux.org> 4.0.6-alt1
- new version 4.0.6

* Wed Aug 23 2023 Anton Vyatkin <toni@altlinux.org> 4.0.5-alt1
- new version 4.0.5

* Wed Aug 09 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 4.0.4-alt1.1
- NMU: moved %%python3_sitelibdir/%%pypi_name/browser_check.py to subpackage with
       tests to avoid dependency from main package on subpackage with tests.

* Fri Aug 04 2023 Anton Vyatkin <toni@altlinux.org> 4.0.4-alt1
- new version 4.0.4

* Fri Jul 14 2023 Anton Vyatkin <toni@altlinux.org> 4.0.3-alt1
- new version 4.0.3

* Mon Jun 12 2023 Anton Vyatkin <toni@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus

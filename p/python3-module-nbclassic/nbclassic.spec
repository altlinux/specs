%define _unpackaged_files_terminate_build 1
%define pypi_name nbclassic
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.0
Release: alt1
Summary: Jupyter Notebook as a Jupyter Server extension
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/nbclassic
BuildArch: noarch
Source: %pypi_name-%version.tar

Requires: python3-module-nbconvert
Requires: python3-module-jupyter-server-terminals
Requires: python3-module-ipykernel
Requires: python3-module-jupyter_client
Requires: python3-module-jupyter_core

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-jupyter-packaging
BuildRequires: python3-module-jupyter_server
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-jupyter
BuildRequires: python3-module-notebook-shim
BuildRequires: python3-module-jupyter-server-terminals
BuildRequires: python3-module-nbconvert
BuildRequires: /dev/pts
%endif

%description
NbClassic provides a backwards compatible Jupyter Notebook interface that you
can install side-by-side with the latest versions: That way, you can fearlessly
upgrade without worrying about your classic extensions and customizations breaking.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %EVR
%add_python3_req_skip playwright.sync_api
# There is wrong relative import in %python3_sitelibdir/nbclassic/tests/launchnotebook.py
%add_python3_req_skip nbclassic.utils

%description tests
NbClassic provides a backwards compatible Jupyter Notebook interface that you
can install side-by-side with the latest versions: That way, you can fearlessly
upgrade without worrying about your classic extensions and customizations breaking.

This package contains tests for %pypi_name.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

# Move config files to proper location
install -d -m 755 %buildroot%_sysconfdir/jupyter/jupyter_server_config.d
mv %buildroot/usr/etc/jupyter/jupyter_server_config.d/nbclassic.json \
   %buildroot%_sysconfdir/jupyter/jupyter_server_config.d

%check
%pyproject_run_pytest -v

%files
%doc README.*
%_bindir/*
%dir %_datadir/icons/hicolor/scalable
%dir %_datadir/icons/hicolor/scalable/apps
%_datadir/applications/jupyter-nbclassic.desktop
%_datadir/icons/hicolor/scalable/apps/nbclassic.svg
%dir %_sysconfdir/jupyter/
%config(noreplace) %_sysconfdir/jupyter/*
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%pypi_name/tests
%exclude %python3_sitelibdir/%pypi_name/*/tests

%files tests
%python3_sitelibdir/%pypi_name/tests
%python3_sitelibdir/%pypi_name/*/tests

%changelog
* Wed May 29 2024 Anton Vyatkin <toni@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Wed Aug 16 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 1.0.0-alt1.1
- NMU: ignore unmet dependency

* Fri Jun 23 2023 Anton Vyatkin <toni@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

%define _unpackaged_files_terminate_build 1
%define pypi_name glpi-api
%define module_name glpi_api

Name: python3-module-%pypi_name
Version: 0.7.0
Release: alt1
Summary: Module for interacting with GLPI using the REST API
License: GPL-3.0-or-later
Group: Development/Python3
Url: https://pypi.org/project/glpi-api
Vcs: https://github.com/unistra/python-glpi-api.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
Module for interacting with GLPI using the REST API.
This package wraps the endpoints provided by the GLPI API and manages HTTP
return codes. It provides helper functions for connection handling,
including a context manager that automatically starts and terminates sessions.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# There is no check for this module

%files
%doc README.rst LICENSE
%python3_sitelibdir/%module_name.py
%python3_sitelibdir/%{pyproject_distinfo %module_name}
%python3_sitelibdir/__pycache__/%module_name.*.pyc

%changelog
* Thu Mar 27 2025 Aleksandr A. Voyt <sobue@altlinux.org> 0.7.0-alt1
- Initial build

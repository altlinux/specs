%define _unpackaged_files_terminate_build 1
%define pypi_name python-socketio
%define mod_name socketio
%define distinfo_name python_socketio

%def_with check

Name:    python3-module-%pypi_name
Version: 5.10.0
Release: alt1

Summary: Python Socket.IO server and client
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/Flask-SocketIO
VCS:     https://github.com/miguelgrinberg/python-socketio

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-sphinx

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar
Source1: %pyproject_deps_config_name

Patch: %pypi_name-%version-alt.patch

%description
Python implementation of the Socket.IO realtime client and server.

%package docs
Summary: Documentation for %pypi_name
Group: Development/Documentation
BuildArch: noarch

%description docs
Python implementation of the Socket.IO realtime client and server.

This package contains documentation for %pypi_name.

%prep
%setup -n %pypi_name-%version
%patch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build
%make -C docs html SPHINXBUILD=sphinx-build-3

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %distinfo_name}

%files docs
%doc docs/_build/html/*
%doc examples

%changelog
* Tue Oct 24 2023 Andrey Limachko <liannnix@altlinux.org> 5.10.0-alt1
- Initial build for Sisyphus

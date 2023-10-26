%define _unpackaged_files_terminate_build 1
%define pypi_name flask-socketio
%define mod_name flask_socketio
%define distinfo_name Flask_SocketIO

%def_without check

Name:    python3-module-%pypi_name
Version: 5.3.6
Release: alt1

Summary: Socket.IO integration for Flask applications.
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/Flask-SocketIO
VCS:     https://github.com/miguelgrinberg/flask-socketio

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-pytest-cov

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar
Source1: %pyproject_deps_config_name

Patch: %pypi_name-%version-alt.patch

%description
Socket.IO integration for Flask applications.

%package docs
Summary: Documentation for %pypi_name
Group: Development/Documentation
BuildArch: noarch

%description docs
Socket.IO integration for Flask applications.

This package contains documentation for %pypi_name.

%prep
%setup -n %pypi_name-%version
%patch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

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
%python3_sitelibdir/%{distinfo_name}*

%files docs
%doc docs/_build/html/*
%doc example

%changelog
* Tue Oct 24 2023 Andrey Limachko <liannnix@altlinux.org> 5.3.6-alt1
- Initial build for Sisyphus

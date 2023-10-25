%define _unpackaged_files_terminate_build 1
%define pypi_name simple-websocket
%define mod_name simple_websocket

%def_with check

Name:    python3-module-%pypi_name
Version: 1.0.0
Release: alt1

Summary: Simple WebSocket server and client for Python.
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/simple-websocket
VCS:     https://github.com/miguelgrinberg/simple-websocket

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-sphinx

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
Simple WebSocket server and client for Python.

%package docs
Summary: Documentation for %pypi_name
Group: Development/Documentation
BuildArch: noarch

%description docs
Simple WebSocket server and client for Python.

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
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%files docs
%doc docs/_build/html/*
%doc examples

%changelog
* Tue Oct 24 2023 Andrey Limachko <liannnix@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

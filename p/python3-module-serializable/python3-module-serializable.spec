%define _unpackaged_files_terminate_build 1
%define pypi_name py-serializable

%def_with check

Name: python3-module-serializable
Version: 1.1.2
Release: alt1
Summary: Pythonic library to aid with serialisation and deserialisation to/from JSON and XML.
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/madpah/serializable

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

Provides: python3-module-%pypi_name = %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest python3-module-lxml python3-module-xmldiff
%endif

%description
This Pythonic library provides a framework for serializing/deserializing Python
classes to and from JSON and XML.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/*

%changelog
* Mon Nov 11 2024 Andrey Kovalev <ded@altlinux.org> 1.1.2-alt1
- Updated to upstream version 1.1.2.
- Terminate build if unpackaged files were found.
- Added %%check section that runs test suite by default.

* Mon Sep 16 2024 Andrey Kovalev <ded@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.

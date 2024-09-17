%define pypi_name py-serializable

Name: python3-module-serializable
Version: 1.1.0
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

%files
%python3_sitelibdir/*

%changelog
* Mon Sep 16 2024 Andrey Kovalev <ded@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.

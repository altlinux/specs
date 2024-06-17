%define _unpackaged_files_terminate_build 1
%define pypi_name lsprotocol
%define mod_name %pypi_name

%define python_path packages/python

%def_with check

Name: python3-module-%pypi_name
Version: 2023.0.1
Release: alt1
Summary: Python implementation of the Language Server Protocol
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/lsprotocol
Vcs: https://github.com/microsoft/lsprotocol
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
lsprotocol is a python implementation of object types used in the Language
Server Protocol (LSP). This repository contains the code generator and the
generated types for LSP.

LSP is used by editors to communicate with various tools to enables services
like code completion, documentation on hover, formatting, code analysis, etc.
The intent of this library is to allow you to build on top of the types used by
LSP. This repository will be kept up to date with the latest version of LSP as
it is updated.

%prep
%setup
%autopatch -p1
pushd %python_path
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
popd
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements.in
%endif

%build
pushd %python_path
%pyproject_build

%install
pushd %python_path
%pyproject_install

%check
# sys.path is patched by conftest.py
python3 -m pytest tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jun 17 2024 Stanislav Levin <slev@altlinux.org> 2023.0.1-alt1
- Initial build for Sisyphus.

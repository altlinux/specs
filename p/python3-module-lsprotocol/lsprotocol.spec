%define pypi_name lsprotocol
%define mod_name %pypi_name

%define python_path packages/python

%def_with check

Name: python3-module-%pypi_name
Version: 2025.0.0
Release: alt1
Summary: Python implementation of the Language Server Protocol
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/lsprotocol
Vcs: https://github.com/microsoft/lsprotocol
BuildArch: noarch
Patch: 7b5d4f7422bfe4c597b8124f99861e751d47f153.patch
Source: %name-%version.tar
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core
%if_with check
BuildRequires: python3-module-attrs
BuildRequires: python3-module-cattrs
BuildRequires: python3-module-importlib-resources
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-pyhamcrest
BuildRequires: python3-module-pytest
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
%patch -p1

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
* Mon Oct 13 2025 Grigory Ustinov <grenka@altlinux.org> 2025.0.0-alt1
- Automatically updated to 2025.0.0.

* Mon Jun 17 2024 Stanislav Levin <slev@altlinux.org> 2023.0.1-alt1
- Initial build for Sisyphus.

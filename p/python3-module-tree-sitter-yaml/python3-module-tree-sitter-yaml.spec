%define _unpackaged_files_terminate_build 1

%define pypi_name tree-sitter-yaml
%define mod_name tree_sitter_yaml

Name:    python3-module-%pypi_name
Version: 0.7.2
Release: alt1

Summary: YAML grammar for tree-sitter

License: MIT
Group:   Development/Python3
Url:     https://github.com/tree-sitter-grammars/tree-sitter-yaml

# Source-url: https://files.pythonhosted.org/packages/source/t/%pypi_name/%mod_name-%version.tar.gz
Source:  %name-%version.tar
# scanner.c and schema.*.c are missing from PyPI sdist, taken from upstream tag v%version
Source1: scanner-src.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
YAML grammar for tree-sitter, providing Python bindings to parse YAML files
using the Tree-sitter incremental parsing library.

%prep
%setup
tar -xvf %SOURCE1 -C src/

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Tue May 05 2026 Vitaly Lipatov <lav@altlinux.ru> 0.7.2-alt1
- initial build for ALT Sisyphus

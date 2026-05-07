%define _unpackaged_files_terminate_build 1

%define pypi_name tree-sitter
%define mod_name tree_sitter

Name:    python3-module-%pypi_name
Version: 0.25.2
Release: alt1

Summary: Python bindings to the Tree-sitter parsing library

License: MIT
Group:   Development/Python3
Url:     https://github.com/tree-sitter/py-tree-sitter

# Source-url: https://files.pythonhosted.org/packages/source/t/%pypi_name/%pypi_name-%version.tar.gz
Source:  %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Python bindings to the Tree-sitter parsing library.

Tree-sitter is a parser generator tool and an incremental parsing library.
It can build a concrete syntax tree for a source file and efficiently
update the syntax tree as the source file is edited. Tree-sitter aims to
be general enough to parse any programming language, fast enough to parse
on every keystroke in a text editor, and robust enough to provide useful
results even in the presence of syntax errors.

This package provides Python bindings built with the bundled tree-sitter
C library (compiled as a CPython extension module).

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Thu May 07 2026 Vitaly Lipatov <lav@altlinux.ru> 0.25.2-alt1
- initial build for ALT Sisyphus

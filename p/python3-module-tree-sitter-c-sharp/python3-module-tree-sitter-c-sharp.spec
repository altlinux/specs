%define _unpackaged_files_terminate_build 1

%define pypi_name tree-sitter-c-sharp
%define mod_name tree_sitter_c_sharp

Name:    python3-module-%pypi_name
Version: 0.23.5
Release: alt1

Summary: C# grammar for tree-sitter

License: MIT
Group:   Development/Python3
Url:     https://github.com/tree-sitter/tree-sitter-c-sharp

# Source-url: https://files.pythonhosted.org/packages/source/t/%pypi_name/%mod_name-%version.tar.gz
Source:  %name-%version.tar
# scanner.c is missing from PyPI sdist, taken from upstream tag v%version
Source1: scanner.c
Patch1:  setup.py-fix-queries-dirname.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
C# grammar for tree-sitter, providing Python bindings to parse C# source code
using the Tree-sitter incremental parsing library.

%prep
%setup
%patch1 -p1
cp -v %SOURCE1 src/scanner.c

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Tue May 05 2026 Vitaly Lipatov <lav@altlinux.ru> 0.23.5-alt1
- initial build for ALT Sisyphus

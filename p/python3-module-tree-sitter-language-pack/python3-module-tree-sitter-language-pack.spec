%define _unpackaged_files_terminate_build 1

%define pypi_name tree-sitter-language-pack
%define mod_name tree_sitter_language_pack

Name:    python3-module-%pypi_name
Version: 0.13.0
Release: alt1

Summary: Comprehensive collection of tree-sitter language parsers

License: MIT AND Apache-2.0
Group:   Development/Python3
Url:     https://github.com/Goldziher/tree-sitter-language-pack

# 160+ tree-sitter grammars compile into one extension; i586 runs out of memory
ExcludeArch: %ix86

# Source-url: https://files.pythonhosted.org/packages/source/t/%pypi_name/%mod_name-%version.tar.gz
Source:  %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools >= 80.9.0
BuildRequires: python3-module-wheel
BuildRequires: python3-module-typing_extensions

%description
Comprehensive collection of 160+ tree-sitter language parsers with polyglot
bindings. Provides Python access to parse source code in many programming
languages using the Tree-sitter incremental parsing library.

The package bundles tree-sitter grammars for hundreds of languages, building
them as CPython extension modules via the abi3 stable ABI.

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
* Tue May 05 2026 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- initial build for ALT Sisyphus

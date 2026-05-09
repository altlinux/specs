%define _unpackaged_files_terminate_build 1

%define pypi_name tree-sitter-embedded-template
%define mod_name tree_sitter_embedded_template

Name:    python3-module-%pypi_name
Version: 0.25.0
Release: alt1

Summary: Embedded Template (ERB, EJS) grammar for tree-sitter

License: MIT
Group:   Development/Python3
Url:     https://github.com/tree-sitter/tree-sitter-embedded-template

# Source-url: https://files.pythonhosted.org/packages/source/t/%pypi_name/%mod_name-%version.tar.gz
Source:  %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Embedded Template (ERB, EJS) grammar for tree-sitter, providing Python bindings
to parse embedded templates using the Tree-sitter incremental parsing library.

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
* Tue May 05 2026 Vitaly Lipatov <lav@altlinux.ru> 0.25.0-alt1
- initial build for ALT Sisyphus

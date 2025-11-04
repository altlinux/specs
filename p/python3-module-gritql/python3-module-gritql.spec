%define _unpackaged_files_terminate_build 1
%define pypi_name gritql
%define metadata_version 0.2.0

Name: python3-module-%pypi_name
Version: 0.1.0.alpha.1743007075
Release: alt1

Summary: GritQL is a query language for searching, linting, and modifying code
License: MIT
Group: Development/Python3

Url: https://github.com/getgrit/gritql
Vcs: https://github.com/getgrit/gritql
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(poetry)
BuildRequires: python3(poetry.core)

BuildArch: noarch

%description
GritQL is a declarative query language for searching and modifying source code.
- Start simply without learning AST details: any code snippet is a valid GritQL query
- Use Rust and query optimization to scale up to 10M+ line repositories
- Use Grit's built-in module system to reuse 200+ standard patterns or share your own
- Once you learn GritQL, you can use it to rewrite any target language:
JavaScript/TypeScript, Python, JSON, Java, Terraform, Solidity, CSS, Markdown,
YAML, Rust, Go, or SQL
- GritQL makes it easy to include auto-fix rules for faster remediation

%prep
%setup

%build
%pyproject_build python

%install
cd python
%pyproject_install

%files
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%pypi_name-%metadata_version.dist-info
%doc README.md

%changelog
* Sun Apr 13 2025 David Sultaniiazov <x1z53@altlinux.org> 0.1.0.alpha.1743007075-alt1
- Initial build

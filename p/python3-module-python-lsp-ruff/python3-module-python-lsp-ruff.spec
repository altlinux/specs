%define _unpackaged_files_terminate_build 1
%define pypi_name python-lsp-ruff
%define mod_name pylsp_ruff

%def_with check

Name: python3-module-%pypi_name
Version: 2.3.0
Release: alt1

Summary: Linter plugin for pylsp based on ruff.
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/python-lsp-ruff/
VCS: https://github.com/python-lsp/python-lsp-ruff
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-python-lsp-server
BuildRequires: python3-module-ruff
BuildRequires: python3-module-lsprotocol
BuildRequires: ruff
%endif

Requires: python3-module-ruff

%description
python-lsp-ruff is a plugin for python-lsp-server that adds
linting, code actions and formatting capabilities that are
provided by ruff, an extremely fast Python linter and formatter
written in Rust.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Mar 03 2026 Aleksandr Dovydenkov <asd@altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus.
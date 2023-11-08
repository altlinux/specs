%define _unpackaged_files_terminate_build 1
%define pypi_name pyls-spyder
%define mod_name pyls_spyder

Name: python3-module-%pypi_name
Version: 0.4.0
Release: alt1

Summary: Spyder extensions for the python language server (pyls)
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyls-spyder/
Vcs: https://github.com/spyder-ide/pyls-spyder

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
Spyder extensions for the python-lsp-server (pylsp).
This package provides Spyder-specific extras for the
Language Server Protocol (LSP) on Python, such as document
symbol searching and others.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%install
%pyproject_install

%build
%pyproject_build

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 13 2023 Anton Zhukharev <ancieg@altlinux.org> 0.4.0-alt1
- Built for ALT Sisyphus.


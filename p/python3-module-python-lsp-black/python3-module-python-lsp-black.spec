%define _unpackaged_files_terminate_build 1
%define pypi_name python-lsp-black
%define mod_name pylsp_black

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1

Summary: python-lsp-server plugin that adds support to black autoformatter
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/python-lsp-black/
Vcs: https://github.com/python-lsp/python-lsp-black

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra dev
%pyproject_builddeps_check
BuildRequires: python3-module-black
%endif

%description
Black plugin for the Python LSP Server.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE CHANGELOG.md README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Dec 21 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.0-alt1
- Updated to 2.0.0.

* Sat Oct 21 2023 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- Built for ALT Sisyphus.


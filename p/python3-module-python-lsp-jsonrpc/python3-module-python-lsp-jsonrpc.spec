%define _unpackaged_files_terminate_build 1
%define pypi_name python-lsp-jsonrpc
%define mod_name pylsp_jsonrpc

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: Fork of the python-jsonrpc-server project, maintained by the Spyder IDE team and the community
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/python-lsp-jsonrpc/
Vcs: https://github.com/python-lsp/python-lsp-jsonrpc

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check
%endif

%description
A Python 3.8+ server implementation of the JSON RPC 2.0 protocol.
This library has been pulled out of the Python LSP Server project.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
sed -i '/^addopts/d' pyproject.toml
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Sep 09 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.0-alt1
- Updated to 1.1.0.

* Tue Oct 04 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus


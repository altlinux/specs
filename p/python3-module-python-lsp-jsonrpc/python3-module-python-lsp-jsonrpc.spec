%define _unpackaged_files_terminate_build 1
%define pypi_name python-lsp-jsonrpc

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.0
Release: alt1

Summary: Fork of the python-jsonrpc-server project, maintained by the Spyder IDE team and the community
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/python-lsp-jsonrpc/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(ujson)
%endif

BuildArch: noarch

%py3_provides %pypi_name

%description
A Python 3.7+ server implementation of the JSON RPC 2.0 protocol.
This library has been pulled out of the Python LSP Server project.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%python3_sitelibdir/pylsp_jsonrpc/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 04 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus


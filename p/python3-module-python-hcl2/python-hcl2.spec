%define _unpackaged_files_terminate_build 1
%define pypi_name python-hcl2
%define mod_name hcl2

%def_with check

Name: python3-module-%pypi_name
Version: 8.2.0
Release: alt1

Summary: A parser for HCL2
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/python-hcl2
VCS: https://github.com/amplify-education/python-hcl2

BuildArch: noarch

Source0: %name-%version.tar
Source1: pyproject_deps.json

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%endif

%description
A parser for HCL2 written in Python using Lark. It can be used as a Python
library or through its CLI tools: hcl2tojson, jsontohcl2, and hq - a jq-like
query tool for HCL files.
Supports HCL2 only (not backwards compatible with HCL v1) and works with any
HCL2 config file such as Terraform.

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
%pyproject_run_pytest -vra test

%files
%doc README.md LICENSE docs
%_bindir/hcl2tojson
%_bindir/jsontohcl2
%_bindir/hq
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Nov 11 2026 Dmitry Mihalchenko <tascad@altlinux.org> 8.2.0-alt1
- Initial build for ALT Sisyphus.

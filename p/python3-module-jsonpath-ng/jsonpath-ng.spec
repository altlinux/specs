%define _unpackaged_files_terminate_build 1
%define pypi_name jsonpath-ng
%define mod_name jsonpath_ng

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.3
Release: alt1
Summary: A final implementation of JSONPath for Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/jsonpath-ng
Vcs: https://github.com/h2non/jsonpath-ng
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter coveralls
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
A final implementation of JSONPath for Python that aims to be standard
compliant, including arithmetic and binary comparison operators, as defined in
the original JSONPath proposal.

This packages merges both jsonpath-rw and jsonpath-rw-ext and provides several
AST API enhancements, such as the ability to update or removes nodes in the
tree.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# modern pytest + testscenarios don't work, fallback to unittest
%pyproject_run_unittest

%files
%doc README.*
%_bindir/%mod_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu May 11 2023 Stanislav Levin <slev@altlinux.org> 1.5.3-alt1
- Initial build for Sisyphus.

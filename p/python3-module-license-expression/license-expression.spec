%define _unpackaged_files_terminate_build 1
%define pypi_name license-expression

%def_with check

Name: python3-module-%pypi_name
Version: 30.3.1
Release: alt1
Summary: Comprehensive utility library to parse, compare, simplify and normalize license expressions
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/license-expression
VCS: https://github.com/nexB/license-expression.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# legacy provides, used by obsolete pdm-pep517
%py3_provides %pypi_name
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
license-expression is a comprehensive utility library to parse, compare,
simplify and normalize license expressions (such as SPDX license expressions)
using boolean logic.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.rst
%python3_sitelibdir/license_expression/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Sep 24 2024 Stanislav Levin <slev@altlinux.org> 30.3.1-alt1
- 30.3.0 -> 30.3.1.

* Wed Mar 20 2024 Stanislav Levin <slev@altlinux.org> 30.3.0-alt1
- 30.1.0 -> 30.3.0.

* Tue Feb 07 2023 Stanislav Levin <slev@altlinux.org> 30.1.0-alt1
- 30.0.0 -> 30.1.0.

* Wed Oct 05 2022 Stanislav Levin <slev@altlinux.org> 30.0.0-alt1
- Initial build for Sisyphus.

%define _unpackaged_files_terminate_build 1
%define pypi_name zope-browserpage
%define ns_name zope
%define mod_name browserpage

%def_with check

Name: python3-module-%pypi_name
Version: 6.0
Release: alt1
Summary: ZCML directives for configuring browser views for Zope
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope-browserpage
Vcs: https://github.com/zopefoundation/zope.browserpage
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
# switched to native namespace
Requires: python3-module-zope >= 3.3.0-alt10
# setuptools(pkg_resources) is used by namespace root which is not used in ALT
%add_pyproject_deps_runtime_filter setuptools
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
# zope.component.testing is required but subpackaged
BuildRequires: python3-module-zope.component-tests
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/

%changelog
* Fri Mar 13 2026 Stanislav Levin <slev@altlinux.org> 6.0-alt1
- 5.1 -> 6.0.

* Mon Sep 08 2025 Stanislav Levin <slev@altlinux.org> 5.1-alt1
- Initial build for Sisyphus.

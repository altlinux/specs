%define _unpackaged_files_terminate_build 1
%define pypi_name zope-untrustedpython
%define ns_name zope
%define mod_name untrustedpython

%def_with check

Name: python3-module-%pypi_name
Version: 7.0
Release: alt1
Summary: Zope Untrusted Python Library
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope-untrustedpython
Vcs: https://github.com/zopefoundation/zope.untrustedpython
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
# setuptools(pkg_resources) is used by namespace root which is not used in ALT
%add_pyproject_deps_runtime_filter setuptools
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests.py
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/tests.*

%changelog
* Fri Mar 13 2026 Stanislav Levin <slev@altlinux.org> 7.0-alt1
- 6.2 -> 7.0.

* Mon Sep 08 2025 Stanislav Levin <slev@altlinux.org> 6.2-alt1
- Initial build for Sisyphus.

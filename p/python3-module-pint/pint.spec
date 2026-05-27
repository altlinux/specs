%define _unpackaged_files_terminate_build 1
%define pypi_name pint
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.25.3
Release: alt1
Summary: Physical quantities module
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/pint
Vcs: https://github.com/hgrecco/pint
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not packaged
%add_pyproject_deps_check_filter pytest-subtests
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra test
%endif

%description
%summary.

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

# don't ship tests
rm %buildroot%python3_sitelibdir/%mod_name/testing.py
rm -r %buildroot%python3_sitelibdir/%mod_name/testsuite/

%check
%pyproject_run_pytest -vra --benchmark-skip

%files
%_bindir/pint-convert
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed May 27 2026 Stanislav Levin <slev@altlinux.org> 0.25.3-alt1
- Initial build for sisyphus.

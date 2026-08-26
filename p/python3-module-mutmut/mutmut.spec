%define _unpackaged_files_terminate_build 1
%define pypi_name mutmut
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 3.7.0
Release: alt1
Summary: mutation testing for Python 3
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/mutmut
Vcs: https://github.com/boxed/mutmut
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not packaged
%add_pyproject_deps_check_filter pyrefly
# real runtime dep
BuildRequires: python3-module-coverage
%pyproject_builddeps_metadata
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
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%_bindir/mutmut
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Aug 26 2026 Stanislav Levin <slev@altlinux.org> 3.7.0-alt1
- Initial build for sisyphus.

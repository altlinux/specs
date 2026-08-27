%define _unpackaged_files_terminate_build 1
%define pypi_name py-cpuinfo2
%define mod_name cpuinfo

%def_with check

Name: python3-module-%pypi_name
Version: 10.1.1
Release: alt1
Summary: Get CPU info with pure Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/py-cpuinfo2
Vcs: https://github.com/akx/py-cpuinfo2
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
# py-cpuinfo2 is a drop-in replacement for py-cpuinfo
Conflicts: python3-module-cpuinfo
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
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
%_bindir/cpuinfo
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Aug 27 2026 Stanislav Levin <slev@altlinux.org> 10.1.1-alt1
- Initial build for sisyphus.

%define _unpackaged_files_terminate_build 1
%define pypi_name jinxed
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1
Summary: Jinxed Terminal Library
License: MPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/jinxed
Vcs: https://github.com/Rockhopper-Technologies/jinxed
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
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
# synced to tox.ini
%pyproject_run_unittest discover -v -s tests

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jul 06 2026 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.4 -> 2.1.0

* Tue May 26 2026 Stanislav Levin <slev@altlinux.org> 2.0.4-alt1
- updated from 2.0.0 to 2.0.4

* Wed May 20 2026 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- Initial build for sisyphus.

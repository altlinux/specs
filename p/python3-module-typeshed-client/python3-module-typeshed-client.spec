%define _unpackaged_files_terminate_build 1
%define pypi_name typeshed-client
%define mod_name typeshed_client

%def_with check

Name: python3-module-%pypi_name
Version: 2.9.0
Release: alt1

Summary: Retrieve information from typeshed and other typing stubs
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/typeshed-client/
Vcs: https://github.com/JelleZijlstra/typeshed_client

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
This project provides a way to retrieve information from typeshed
and from PEP 561 stub packages.

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
%pyproject_run_unittest discover -v tests/

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 18 2026 Anton Zhukharev <ancieg@altlinux.org> 2.9.0-alt1
- Updated to 2.9.0.

* Wed Jul 16 2025 Anton Zhukharev <ancieg@altlinux.org> 2.8.2-alt1
- Updated to 2.8.2.

* Tue Jul 01 2025 Anton Zhukharev <ancieg@altlinux.org> 2.7.0-alt1
- Packaged for ALT Sisyphus.

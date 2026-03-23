%define _unpackaged_files_terminate_build 1
%define pypi_name docformatter
%define mod_name docformatter

%def_with check

Name: python3-module-%pypi_name
Version: 1.7.7
Release: alt1

Summary: Formats docstrings to follow PEP 257
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/docformatter/
Vcs: https://github.com/PyCQA/docformatter

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
%pyproject_deps_resync_check_poetry testing
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -k 'not test_detect_encoding_with_undetectable_encoding'

%files
%_bindir/docformatter
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Mar 23 2026 Anton Zhukharev <ancieg@altlinux.org> 1.7.7-alt1
- Updated to 1.7.7.

* Mon Jan 13 2025 Stanislav Levin <slev@altlinux.org> 1.7.5-alt3
- Fixed FTBFS (poetry-core 2.0).

* Thu May 23 2024 Anton Zhukharev <ancieg@altlinux.org> 1.7.5-alt2
- Fixed FTBFS.

* Thu Sep 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.7.5-alt1
- Built for ALT Sisyphus.

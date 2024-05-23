%define _unpackaged_files_terminate_build 1
%define pypi_name docformatter

%def_with check

Name: python3-module-%pypi_name
Version: 1.7.5
Release: alt2

Summary: Formats docstrings to follow PEP 257
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/docformatter/
Vcs: https://github.com/PyCQA/docformatter

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter rstcheck
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
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

# remove wrongly installed LICENSE file
rm %buildroot%python3_sitelibdir/LICENSE

%check
%pyproject_run_pytest -vra -k 'not test_no_pre_summary_space_using_pyproject'

%files
%doc LICENSE AUTHORS.rst CHANGELOG.md README.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu May 23 2024 Anton Zhukharev <ancieg@altlinux.org> 1.7.5-alt2
- Fixed FTBFS.

* Thu Sep 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.7.5-alt1
- Built for ALT Sisyphus.


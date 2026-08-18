%define _unpackaged_files_terminate_build 1
# The theme's own tests live in the gp-sphinx shared suite;
# enabling %%check here would create a circular BuildRequires on gp-sphinx.
%def_without check
%if_with check
%define pyproject_deps_check_filter %nil
%add_pyproject_deps_check_filter 'pytest-playwright$'
%add_pyproject_deps_check_filter 'typing[-_]extensions$'
%endif

%define pypi_name sphinx-gp-theme
%define module_name sphinx_gp_theme
%define version_alpha a37

%define src_dir packages/%pypi_name
%define tests_dir ../../tests

%define pyproject_distinfo() %{pep427_name: %1}-%version%{version_alpha}.dist-info/

Name: python3-module-%pypi_name
Version: 0.1.0
Release: alt1.%version_alpha

Summary: Furo child theme for git-pull project documentation
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/sphinx-gp-theme/
Vcs: https://github.com/git-pull/gp-sphinx
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Furo child theme for git-pull project documentation.

%prep
%setup
%autopatch -p1
cd %src_dir
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
cd -

%build
cd %src_dir
%pyproject_build
cd -

%install
cd %src_dir
%pyproject_install
cd -

%check
cd %src_dir
%pyproject_run_pytest %tests_dir/test_theme.py
cd -

%files
%doc LICENSE %src_dir/README.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Aug 18 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.1.0-alt1.a37
- Initial build for ALT Sisyphus.

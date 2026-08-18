%define _unpackaged_files_terminate_build 1
%def_with check
%if_with check
%define pyproject_deps_check_filter %nil
%add_pyproject_deps_check_filter 'pytest-playwright$'
%add_pyproject_deps_check_filter 'typing[-_]extensions$'
%endif

%define pypi_name gp-sphinx
%define module_name gp_sphinx
%define version_alpha a37

%define src_dir packages/%pypi_name
%define tests_dir ../../tests

%define pyproject_distinfo() %{pep427_name: %1}-%version%{version_alpha}.dist-info/

Name: python3-module-%pypi_name
Version: 0.1.0
Release: alt1.%version_alpha

Summary: Shared Sphinx documentation platform for git-pull projects
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/gp-sphinx/
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
gp-sphinx consolidates duplicated docs configuration, extensions,
theme settings, and workarounds from git-pull projects into a single
reusable package.

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
export SPHINX_VITE_BUILDER_SKIP=1
# sphinx 9 (current Sisyphus) changed autodoc signature and truncation
# rendering while the workspace targets sphinx<9; these assertion-heavy
# tests are excluded until an upstream release supports sphinx 9.
%pyproject_run_pytest %tests_dir \
    --ignore=%tests_dir/visual \
    --ignore=%tests_dir/ext/typehints_gp/test_documented_fields.py \
    -k 'not test_long_data_value_is_truncated'
cd -

%files
%doc LICENSE %src_dir/README.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Aug 18 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.1.0-alt1.a37
- Initial build for ALT Sisyphus.

%define _unpackaged_files_terminate_build 1
%define pypi_name httpx-oauth
%define mod_name httpx_oauth

%def_with check

Name: python3-module-%pypi_name
Version: 0.16.1
Release: alt1

Summary: Async OAuth client using HTTPX
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/httpx-oauth/
Vcs: https://github.com/frankie567/httpx-oauth

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_build_filter hatch-regex-commit
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter griffe-inherited-docstrings
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1

# force version to not use hatch-regex-commit
sed -i 's/^dynamic = \["version"\]$/version = "%version"/' pyproject.toml

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_hatch pyproject.toml default
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 26 2025 Anton Zhukharev <ancieg@altlinux.org> 0.16.1-alt1
- Built for ALT Sisyphus.


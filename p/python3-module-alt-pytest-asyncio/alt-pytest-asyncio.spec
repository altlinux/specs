%define _unpackaged_files_terminate_build 1
%define pypi_name alt-pytest-asyncio
%define mod_name alt_pytest_asyncio

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.5
Release: alt1
Summary: An alternative plugin for pytest to make it support async tests and fixtures
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/alt-pytest-asyncio/
Vcs: https://github.com/delfick/alt-pytest-asyncio
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
# helpers deps
%pyproject_builddeps -- helpers_pep518 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- helpers_pep517 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- helpers_metadata %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter}
%endif

%description
%summary.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
pushd helpers
%pyproject_deps_resync helpers_pep518 pep518
%pyproject_deps_resync helpers_pep517 pep517
%pyproject_deps_resync helpers_metadata metadata
popd
%endif

%build
%pyproject_build
pushd helpers
%pyproject_build
popd

%install
%pyproject_install

%check
%pyproject_run -- bash -s <<-'ENDTESTS'
set -eux
helpers_wheel=$(cat helpers/dist/.wheeltracker) ||
        { echo Make sure you built wheel for helpers ; exit 1 ; }
python -m pyproject_installer install "helpers/dist/$helpers_wheel"
python -m pytest -vra
ENDTESTS

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Feb 19 2026 Stanislav Levin <slev@altlinux.org> 0.9.5-alt1
- 0.8.2 -> 0.9.5.

* Mon Oct 14 2024 Alexander Burmatov <thatman@altlinux.org> 0.8.2-alt1
- Initial build for Sisyphus.

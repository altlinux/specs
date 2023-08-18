%define _unpackaged_files_terminate_build 1
%define pypi_name enrich
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.7
Release: alt1
Summary: Enriched extends rich library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/enrich
Vcs: https://github.com/pycontribs/enrich
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
# obsoleted by setuptools_scm
%add_pyproject_deps_build_filter setuptools-scm-git-archive
%pyproject_builddeps_build
%if_with check
# not packaged yet
%add_pyproject_deps_check_filter pytest-plus
%pyproject_builddeps_metadata_extra rich
%pyproject_builddeps_metadata_extra test
%endif

%description
Enriched extends rich library functionality with a set of changes that were not
accepted to rich itself.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
# don't ship tests
%exclude %python3_sitelibdir/%mod_name/test/

%changelog
* Wed Aug 16 2023 Stanislav Levin <slev@altlinux.org> 1.2.7-alt1
- Initial build for Sisyphus.

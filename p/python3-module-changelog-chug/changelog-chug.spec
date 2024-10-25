%define _unpackaged_files_terminate_build 1
%define pypi_name changelog-chug
%define mod_name chug

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.2
Release: alt1
Summary: Parser library for project Change Log documents
License: AGPL-3.0
Group: Development/Python3
Url: https://pypi.org/project/changelog-chug
Vcs: https://git.sr.ht/~bignose/changelog-chug
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
%pypi_name is a parser for project Change Log documents.

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
%pyproject_run_unittest -v

%files
%doc README
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Oct 25 2024 Stanislav Levin <slev@altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus.

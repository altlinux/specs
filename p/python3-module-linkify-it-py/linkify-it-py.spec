%define _unpackaged_files_terminate_build 1
%define pypi_name linkify-it-py
%define mod_name linkify_it

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.2
Release: alt1
Summary: Links recognition library with FULL unicode support
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/linkify-it-py
Vcs: https://github.com/tsutsu3/linkify-it-py.git
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
This is Python port of linkify-it.

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
%pyproject_run_pytest -ra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed May 03 2023 Stanislav Levin <slev@altlinux.org> 2.0.2-alt1
- 2.0.0 -> 2.0.2.

* Mon Apr 24 2023 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus.

%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-relaxed
%define mod_name pytest_relaxed

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1
Summary: Relaxed test discovery/organization for pytest
License: BSD-2-Clause
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/pytest-relaxed/
Vcs: https://github.com/bitprophet/pytest-relaxed
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: /dev/pts
%add_pyproject_deps_check_filter codecov
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This pytest plugin takes a page from the rest of Python, where you don't have
to explicitly note public module/class members, but only need to hint as to
which ones are private. By default, all files and objects pytest is told to
scan will be considered tests; to mark something as not-a-test, simply prefix
it with an underscore.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile dev-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- inv test

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Apr 26 2023 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.1.5 -> 2.0.0.

* Thu May 07 2020 Stanislav Levin <slev@altlinux.org> 1.1.5-alt3
- Added compatibility with Pytest 5.4.

* Fri Dec 06 2019 Stanislav Levin <slev@altlinux.org> 1.1.5-alt2
- Fixed testing against Pytest 5.3+.

* Fri Oct 18 2019 Stanislav Levin <slev@altlinux.org> 1.1.5-alt1
- Initial build for Sisyphus.

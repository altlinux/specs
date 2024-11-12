%define _unpackaged_files_terminate_build 1
%define pypi_name parso
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.8.4
Release: alt1
Summary: A Python3 Parser
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/parso/
Vcs: https://github.com/davidhalter/parso
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
Parso is a Python parser that supports error recovery and round-trip
parsing for different Python versions (in multiple Python versions).
Parso is also able to list multiple syntax errors in your python file.

Parso has been battle-tested by jedi. It was pulled out of jedi to be
useful for other projects as well.

Parso consists of a small API to parse Python and analyse the syntax tree.

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
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Nov 11 2024 Stanislav Levin <slev@altlinux.org> 0.8.4-alt1
- 0.8.3 -> 0.8.4.

* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 0.8.3-alt1
- Autobuild version bump to 0.8.3
- Introduce partial check

* Mon Feb 01 2021 Fr. Br. George <george@altlinux.ru> 0.8.1-alt1
- Autobuild version bump to 0.8.1

* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 0.5.1-alt1
- Autobuild version bump to 0.5.1

* Fri Aug 03 2018 Fr. Br. George <george@altlinux.ru> 0.3.1-alt1
- Autobuild version bump to 0.3.1


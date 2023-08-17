%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-randomly

%def_with check

Name: python3-module-%pypi_name
Version: 3.15.0
Release: alt1
Summary: Pytest plugin to randomly order tests and control random.seed
License: MIT
Group: Development/Python
Url: https://pypi.org/project/pytest-randomly/
Vcs: https://github.com/pytest-dev/pytest-randomly
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Randomness in testing can be quite powerful to discover hidden flaws in the
tests themselves, as well as giving a little more coverage to your system.

By randomly ordering the tests, the risk of surprising inter-test dependencies
is reduced - a technique used in many places.

By resetting the random seed to a repeatable number for each test, tests can
create data based on random numbers and yet remain repeatable, for example
factory boy's fuzzy values. This is good for ensuring that tests specify the
data they need and that the tested system is not affected by any data that is
filled in randomly due to not being specified.

%prep
%setup
%patch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/requirements.in
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -p no:randomly tests

%files
%doc README.rst
%python3_sitelibdir/pytest_randomly/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Aug 17 2023 Stanislav Levin <slev@altlinux.org> 3.15.0-alt1
- 3.13.0 -> 3.15.0.

* Thu Jul 20 2023 Stanislav Levin <slev@altlinux.org> 3.13.0-alt1
- 3.12.0 -> 3.13.0.

* Tue Apr 25 2023 Stanislav Levin <slev@altlinux.org> 3.12.0-alt2
- Fixed FTBFS (pytest 7.3.1).

* Wed Jul 20 2022 Stanislav Levin <slev@altlinux.org> 3.12.0-alt1
- 3.11.0 -> 3.12.0.

* Thu Feb 03 2022 Stanislav Levin <slev@altlinux.org> 3.11.0-alt1
- 3.7.0 -> 3.11.0.

* Mon Apr 19 2021 Stanislav Levin <slev@altlinux.org> 3.7.0-alt1
- 3.5.0 -> 3.7.0.

* Fri Mar 26 2021 Stanislav Levin <slev@altlinux.org> 3.5.0-alt1
- 3.4.1 -> 3.5.0.

* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 3.4.1-alt1
- 3.1.0 -> 3.4.1.

* Tue Apr 28 2020 Stanislav Levin <slev@altlinux.org> 3.1.0-alt3
- Fixed FTBFS.

* Mon Dec 02 2019 Stanislav Levin <slev@altlinux.org> 3.1.0-alt2
- Fixed testing against Pytest 5.3+.

* Sat Nov 16 2019 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- 1.2.3 -> 3.1.0.

* Wed Dec 19 2018 Stanislav Levin <slev@altlinux.org> 1.2.3-alt1
- Initial build.


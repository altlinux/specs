%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-randomly

%def_with check

Name: python3-module-%pypi_name
Version: 3.12.0
Release: alt1

Summary: Pytest plugin to randomly order tests and control random.seed
License: MIT
Group: Development/Python
# Source-git: https://github.com/pytest-dev/pytest-randomly
Url: https://pypi.org/project/pytest-randomly/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# install_requires=
BuildRequires: python3(pytest)

BuildRequires: python3(factory)
BuildRequires: python3(faker)
BuildRequires: python3(numpy)
BuildRequires: python3(pytest_xdist)
%endif

BuildArch: noarch

# PyPi name
%py3_provides %pypi_name

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

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject -- -vra

%files
%doc README.rst
%python3_sitelibdir/pytest_randomly/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
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


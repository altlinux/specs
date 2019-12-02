%define _unpackaged_files_terminate_build 1
%define oname pytest-randomly

%def_with check

Name: python3-module-%oname
Version: 3.1.0
Release: alt2

Summary: Pytest plugin to randomly order tests and control random.seed
License: BSD 3-Clause
Group: Development/Python
# Source-git: https://github.com/pytest-dev/pytest-randomly
Url: https://pypi.org/project/pytest-randomly/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(entrypoints)
BuildRequires: python3(factory)
BuildRequires: python3(numpy)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

BuildArch: noarch

# PyPi name
%py3_provides pytest-randomly

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

# relax deps
grep -qsF 'deps = -rrequirements/py37.txt' tox.ini || exit 1
sed -i 's/deps = -rrequirements\/py37\.txt/deps = /' tox.ini

%build
%python3_build

%install
%python3_install

%check
sed -i '/^\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/py.test3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -v

%files
%doc README.rst
%python3_sitelibdir/pytest_randomly.py
%python3_sitelibdir/__pycache__/pytest_randomly.*.py*
%python3_sitelibdir/pytest_randomly-*.egg-info/

%changelog
* Mon Dec 02 2019 Stanislav Levin <slev@altlinux.org> 3.1.0-alt2
- Fixed testing against Pytest 5.3+.

* Sat Nov 16 2019 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- 1.2.3 -> 3.1.0.

* Wed Dec 19 2018 Stanislav Levin <slev@altlinux.org> 1.2.3-alt1
- Initial build.


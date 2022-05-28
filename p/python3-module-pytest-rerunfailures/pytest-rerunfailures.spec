%define _unpackaged_files_terminate_build 1

%define  modulename pytest-rerunfailures

%def_with check

Name:    python3-module-%modulename
Version: 10.2
Release: alt1

Summary: a pytest plugin that re-runs failed tests up to -n times to eliminate flakey failures

License: MPL-2.0
Group:   Development/Python3
URL:     https://github.com/pytest-dev/pytest-rerunfailures

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3-module-pytest-xdist
%endif

BuildArch: noarch

Source:  %name-%version.tar
%py3_provides %modulename

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
sed -i -e '/^\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py3: _PYTEST_BIN=%_bindir\/py.test3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' \
    -e '/minversion = 3\.17\.1/d' \
    tox.ini
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%doc *.rst
%python3_sitelibdir/pytest_rerunfailures.py
%python3_sitelibdir/__pycache__/pytest_rerunfailures.*
%python3_sitelibdir/pytest_rerunfailures-%version-py%_python3_version.egg-info/

%changelog
* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 10.2-alt1
- Automatically updated to 10.2.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 10.0-alt1
- Automatically updated to 10.0.

* Mon Oct 12 2020 Stanislav Levin <slev@altlinux.org> 9.1.1-alt1
- 7.0 -> 9.1.1.
- Enabled testing.

* Tue Oct 22 2019 Grigory Ustinov <grenka@altlinux.org> 7.0-alt1
- Initial build for Sisyphus.

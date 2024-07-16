%define  modulename pytest-rerunfailures

%def_with check

Name:    python3-module-%modulename
Version: 14.0
Release: alt2

Summary: a pytest plugin that re-runs failed tests up to -n times to eliminate flakey failures

License: MPL-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/pytest-rerunfailures
VCS:     https://github.com/pytest-dev/pytest-rerunfailures

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
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
%pyproject_build

%install
%pyproject_install

%check
# https://github.com/pytest-dev/pytest-rerunfailures/issues/267
donttest="test_run_session_teardown_once_after_reruns \
and not test_exception_matches_rerun_except_query \
and not test_exception_not_match_rerun_except_query \
and not test_exception_matches_only_rerun_query \
and not test_exception_match_only_rerun_in_dual_query"
%pyproject_run_pytest -k "not $donttest"

%files
%doc *.rst
%python3_sitelibdir/pytest_rerunfailures.py
%python3_sitelibdir/__pycache__/pytest_rerunfailures.*
%python3_sitelibdir/pytest_rerunfailures-%version.dist-info/

%changelog
* Tue Jul 16 2024 Grigory Ustinov <grenka@altlinux.org> 14.0-alt2
- Fixed FTBFS.

* Wed Apr 03 2024 Grigory Ustinov <grenka@altlinux.org> 14.0-alt1
- Automatically updated to 14.0.

* Sun Jan 28 2024 Grigory Ustinov <grenka@altlinux.org> 10.2-alt2
- Moved on modern pyproject macros.

* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 10.2-alt1
- Automatically updated to 10.2.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 10.0-alt1
- Automatically updated to 10.0.

* Mon Oct 12 2020 Stanislav Levin <slev@altlinux.org> 9.1.1-alt1
- 7.0 -> 9.1.1.
- Enabled testing.

* Tue Oct 22 2019 Grigory Ustinov <grenka@altlinux.org> 7.0-alt1
- Initial build for Sisyphus.

%define pypi_name locket

%def_with check

Name:    python3-module-%pypi_name
Version: 1.0.0
Release: alt1

Summary: File-based locks for Python on Linux and Windows

License: BSD-2-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/locket
VCS:     https://github.com/mwilliamson/locket.py

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-spur
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
Locket implements a lock that can be used by multiple processes provided
they use the same path.

Locks largely behave as (non-reentrant) `Lock` instances from the `threading`
module in the standard library. Specifically, their behaviour is:

* Locks are uniquely identified by the file being locked,
  both in the same process and across different processes.
* Locks are either in a locked or unlocked state.
* When the lock is unlocked, calling `acquire()` returns immediately and changes
  the lock state to locked.
* When the lock is locked, calling `acquire()` will block until the lock state
  changes to unlocked, or until the timeout expires.
* If a process holds a lock, any thread in that process can call `release()` to
  change the state to unlocked.
* Behaviour of locks after `fork` is undefined.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 11 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.

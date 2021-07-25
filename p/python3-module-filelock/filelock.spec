%define _unpackaged_files_terminate_build 1
%define oname filelock

%def_with check

Name: python3-module-%oname
Version: 3.0.10
Release: alt2

Summary: A platform independent file lock for Python
License: Unlicense
Group: Development/Python3
# Source-git: https://github.com/benediktschmitt/py-filelock.git
Url: https://pypi.python.org/pypi/filelock

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: pytest3
%endif

BuildArch: noarch

%description
This package contains a single module, which implements a platform independent
file locking mechanism for Python.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
pytest3 -xvv test.py

%files
%doc LICENSE.rst README.rst
%python3_sitelibdir/filelock.py
%python3_sitelibdir/__pycache__/filelock.*.py*
%python3_sitelibdir/filelock-*.egg-info/

%changelog
* Sun Jul 25 2021 Grigory Ustinov <grenka@altlinux.org> 3.0.10-alt2
- Drop python2 support.

* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 3.0.10-alt1
- 3.0.9 -> 3.0.10.

* Wed Oct 10 2018 Stanislav Levin <slev@altlinux.org> 3.0.9-alt1
- Initial build.


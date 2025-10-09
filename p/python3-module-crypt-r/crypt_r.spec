%def_with check

%define srcname crypt-r

Name:    python3-module-%srcname
Version: 3.13.1
Release: alt1

Summary: A copy of the `crypt` module that was removed in Python 3.13

License: Python-2.0.1
Group:   Development/Python3
URL:     https://pypi.org/project/crypt-r
VCS:     https://github.com/fedora-python/crypt_r

Source: %name-%version.tar

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-test
BuildRequires: python3-module-pytest
%endif

%description
The crypt_r module is a renamed copy of the crypt module as it was present in
Python 3.12 before it was removed.

See PEP 594 for details of the removal.

Unlike crypt, this library always exposes the crypt_r(3) function, not crypt(3).

This module implements an interface to the crypt_r(3) routine, which is
a one-way hash function based upon a modified DES algorithm; see the Unix man
page for further details. Possible uses include storing hashed passwords so you
can check passwords without storing the actual password, or attempting to crack
Unix passwords with a dictionary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run pytest tests/test_crypt_r.py

%files
%doc *.rst
%python3_sitelibdir/__pycache__
%python3_sitelibdir/_crypt_r.cpython-*.so
%python3_sitelibdir/crypt.py
%python3_sitelibdir/crypt_r.py
%python3_sitelibdir/crypt_r-%version.dist-info

%changelog
* Wed Jul 30 2025 Grigory Ustinov <grenka@altlinux.org> 3.13.1-alt1
- Initial build for Sisyphus.

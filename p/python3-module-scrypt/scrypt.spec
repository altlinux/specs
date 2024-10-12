%define oname scrypt

%def_with check

Name: python3-module-%oname
Version: 0.8.27
Release: alt1

Summary: Bindings for the scrypt key derivation function library

License: BSD-2-Clause
Group: Development/Python3
URL: https://pypi.org/project/scrypt
VCS: https://github.com/holgern/py-scrypt

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libssl-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
This is a set of Python bindings for the scrypt key derivation
function.

Scrypt is useful when encrypting password as it is possible to specify
a *minimum* amount of time to use when encrypting and decrypting. If,
for example, a password takes 0.05 seconds to verify, a user won't
notice the slight delay when signing in, but doing a brute force
search of several billion passwords will take a considerable amount of
time. This is in contrast to more traditional hash functions such as
MD5 or the SHA family which can be implemented extremely fast on cheap
hardware.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/_scrypt.*.so
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sat Oct 12 2024 Grigory Ustinov <grenka@altlinux.org> 0.8.27-alt1
- Automatically updated to 0.8.27.

* Tue Mar 05 2024 Grigory Ustinov <grenka@altlinux.org> 0.8.24-alt1
- Automatically updated to 0.8.24.

* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 0.8.21-alt1
- Automatically updated to 0.8.21.
- Build with check.

* Mon Jul 18 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.20-alt2
- Fix license.
- Add filter for tags.

* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.20-alt1
- Build new version.

* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 0.8.6-alt2
- Drop python2 support.

* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 0.8.6-alt1
- Initial build.

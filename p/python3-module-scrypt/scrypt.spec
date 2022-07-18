%define oname scrypt

Name: python3-module-%oname
Version: 0.8.20
Release: alt2

Summary: Bindings for the scrypt key derivation function library

Url: https://pypi.org/project/scrypt
License: BSD-2-Clause
Group: Development/Python3

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libssl-devel

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
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Mon Jul 18 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.20-alt2
- Fix license.
- Add filter for tags.

* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.20-alt1
- Build new version.

* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 0.8.6-alt2
- Drop python2 support.

* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 0.8.6-alt1
- Initial build.

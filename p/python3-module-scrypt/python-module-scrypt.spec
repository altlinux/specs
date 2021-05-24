%define oname scrypt

Summary: Bindings for the scrypt key derivation function library
Name: python3-module-%oname
Version: 0.8.6
Release: alt2
Url: http://bitbucket.org/mhallin/py-scrypt
Source: https://pypi.python.org/packages/source/a/%oname/%oname-%version.tar.gz
License: BSD
Group: Development/Python3

BuildRequires(pre): rpm-build-python3
BuildRequires: libssl-devel

%description
This is a set of Python_ bindings for the scrypt_ key derivation
function.

Scrypt is useful when encrypting password as it is possible to specify
a *minimum* amount of time to use when encrypting and decrypting. If,
for example, a password takes 0.05 seconds to verify, a user won't
notice the slight delay when signing in, but doing a brute force
search of several billion passwords will take a considerable amount of
time. This is in contrast to more traditional hash functions such as
MD5 or the SHA family which can be implemented extremely fast on cheap
hardware.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/*

%changelog
* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 0.8.6-alt2
- Drop python2 support.

* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 0.8.6-alt1
- Initial build.

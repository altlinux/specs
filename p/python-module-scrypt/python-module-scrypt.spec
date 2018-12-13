%define oname scrypt

Summary: Bindings for the scrypt key derivation function library
Name: python-module-%oname
Version: 0.8.6
Release: alt1
Url: http://bitbucket.org/mhallin/py-scrypt
Source: https://pypi.python.org/packages/source/a/%oname/%oname-%version.tar.gz
License: BSD
Group: Development/Python

BuildRequires: python-devel python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
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
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Bindings for the scrypt key derivation function library
Group: Development/Python3

%description -n python3-module-%oname
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

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

cp -fR . ../python3

%build
%python_build


pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README.rst LICENSE
%python_sitelibdir/*
#%exclude %python_sitelibdir/*/tests

#%files tests
#%python_sitelibdir/*/tests

%files -n python3-module-%oname
%doc README.rst LICENSE
%python3_sitelibdir/*
#%exclude %python3_sitelibdir/*/tests

#%files -n python3-module-%oname-tests
#%python3_sitelibdir/*/tests

%changelog
* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 0.8.6-alt1
- Initial build.

%define oname crypter

%def_with python3

Name: python-module-%oname
Version: 1.0.3
Release: alt1.git20141125.1.1
Summary: Encryption daemon that listens on unix domain sockets
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/crypter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/barchart/crypter.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
Requires: openssl

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-pluggy python-module-py python-module-setuptools python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python-tools-2to3 python3 python3-base python3-module-pluggy python3-module-py python3-module-setuptools xz
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3 time

%description
Encryption/decryption daemon that handles requests via unix domain
sockets. The daemon can be run on a container host, and trusted Docker
containers can mount the socket directory to decrypt sensitive
configuration values (i.e. credentials) without requiring direct access
to the private key.

Due to the messy state of Python encryption libraries related to S/MIME
and PKCS#7, OpenSSL binaries are required.

%package -n %oname-common
Summary: Common files for Python 2 & 3 modules
Group: Development/Python

%description -n %oname-common
Encryption/decryption daemon that handles requests via unix domain
sockets. The daemon can be run on a container host, and trusted Docker
containers can mount the socket directory to decrypt sensitive
configuration values (i.e. credentials) without requiring direct access
to the private key.

This package contains common files for Python 2 & 3 modules.

%package -n python3-module-%oname
Summary: Encryption daemon that listens on unix domain sockets
Group: Development/Python3
%py3_provides %oname
Requires: openssl

%description -n python3-module-%oname
Encryption/decryption daemon that handles requests via unix domain
sockets. The daemon can be run on a container host, and trusted Docker
containers can mount the socket directory to decrypt sensitive
configuration values (i.e. credentials) without requiring direct access
to the private key.

Due to the messy state of Python encryption libraries related to S/MIME
and PKCS#7, OpenSSL binaries are required.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	2to3 -w -n $i
	mv $i $i.py3
done
popd
%endif

%python_install

install -d %buildroot/var/run/crypter

%check
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%files -n %oname-common
%_sysconfdir/*
%dir /var/run/crypter

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.3-alt1.git20141125.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1.git20141125.1
- NMU: Use buildreq for BR.

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20141125
- Initial build for Sisyphus


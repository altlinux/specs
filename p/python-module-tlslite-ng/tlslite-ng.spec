%define mname tlslite
%define oname %mname-ng

%def_without python3

Name: python-module-%oname
Version: 0.5.0
Release: alt2.beta4.git20150724
Summary: Pure python implementation of SSL and TLS
License: BSD & LGPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/tlslite-ng
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tomato42/tlslite-ng.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: graphviz python-module-coverage python-module-epydoc python-module-gmpy python-module-html5lib python-module-logilab-common python-module-m2crypto python-module-mock python-module-ndg-httpsclient python-module-pycrypto python-module-yaml /proc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-tests pylint-py3 python3-module-coverage python3-module-coveralls python3-module-pycrypto python3-module-m2crypto python3-module-gmpy python3-module-mock
%endif

%py_provides %oname
Conflicts: python-module-%mname < %EVR
Provides: python-module-%mname = %EVR

%description
tlslite-ng is a pure python implementation of SSLv3.0, TLS 1.0, TLS 1.1
and TLS 1.2 protocols.

It can use pycrypto, m2crypto and gmp for acceleration of cryptographic
operations but is not dependant upon them.

tlslite-ng aims to be a drop-in replacement for tlslite while providing
more comprehensive set of features and more secure defautls.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
tlslite-ng is a pure python implementation of SSLv3.0, TLS 1.0, TLS 1.1
and TLS 1.2 protocols.

It can use pycrypto, m2crypto and gmp for acceleration of cryptographic
operations but is not dependant upon them.

tlslite-ng aims to be a drop-in replacement for tlslite while providing
more comprehensive set of features and more secure defautls.

This package contains documentation for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Pure python implementation of SSL and TLS
Group: Development/Python3
%py3_provides %oname
Conflicts: python3-module-%mname < %EVR
Provides: python3-module-%mname = %EVR

%description -n python3-module-%oname
tlslite-ng is a pure python implementation of SSLv3.0, TLS 1.0, TLS 1.1
and TLS 1.2 protocols.

It can use pycrypto, m2crypto and gmp for acceleration of cryptographic
operations but is not dependant upon them.

tlslite-ng aims to be a drop-in replacement for tlslite while providing
more comprehensive set of features and more secure defautls.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
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
	mv $i ${i}3
done
popd
%endif

%python_install

%make docs

%check
export PYTHONPATH=$PWD
export M2CRYPTO=true PYCRYPTO=true GMPY=true
pushd tests
./httpsserver.sh &
sleep 1
python httpsclient.py
popd
killall -9 httpsserver.sh
killall -9 python
python -m unittest discover -v
%if_with python3
pushd ../python3/tests
export PYTHONPATH=$PWD/..
sed -i 's|python|python3|' httpsserver.sh
./httpsserver.sh &
sleep 1
python3 httpsclient.py
popd
killall -9 httpsserver.sh
killall -9 python3
python3 -m unittest discover -v
%endif

%files
%doc LICENSE README*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%files docs
%doc docs/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README*
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 0.5.0-alt2.beta4.git20150724
- cleanup buildreq

* Thu Aug 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.beta4.git20150724
- Initial build for Sisyphus


%define oname pysocks

%def_with python3

Name: python-module-%oname
Version: 1.5.1
Release: alt1.git20150125
Summary: A Python SOCKS module
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/PySocks/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Anorov/PySocks.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests mocks /proc
BuildPreReq: python-module-twisted-core
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-twisted-core
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname socks
%py_requires urllib2

%description
A SocksiPy fork, used in urllib3. Contains many improvements to the
original.

%package -n python3-module-%oname
Summary: A Python SOCKS module
Group: Development/Python3
%py3_provides %oname socks

%description -n python3-module-%oname
A SocksiPy fork, used in urllib3. Contains many improvements to the
original.

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
%python_install
install -p -m644 sockshandler.py %buildroot%python_sitelibdir/

%if_with python3
pushd ../python3
%python3_install
install -p -m644 sockshandler.py %buildroot%python3_sitelibdir/
popd
%endif

%check
pushd test
sed -i 's|python2|python|' test.sh
./test.sh
popd
%if_with python3
pushd ../python3/test
sed -i 's|python2|python3|' test.sh
./test.sh
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.git20150125
- Initial build for Sisyphus


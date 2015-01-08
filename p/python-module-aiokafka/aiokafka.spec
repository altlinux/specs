%define oname aiokafka

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20141230
Summary: asyncio client for kafka
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aiokafka/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aio-libs/aiokafka.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-kafka
BuildPreReq: python-module-snappy python-module-flake8
BuildPreReq: python-module-nose
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-kafka
BuildPreReq: python3-module-snappy python3-module-flake8
BuildPreReq: python3-module-nose
%endif

%py_provides %oname
%py_requires asyncio kafka snappy

%description
Kafka integration with asyncio.

%package -n python3-module-%oname
Summary: asyncio client for kafka
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio kafka snappy

%description -n python3-module-%oname
Kafka integration with asyncio.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|flake8|python3-flake8|' ../python3/Makefile
sed -i 's|nosetests|nosetests3|' ../python3/Makefile
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
%make flake
%endif
%if_with python3
pushd ../python3
python3 setup.py test
%make flake
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/tests
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141230
- Initial build for Sisyphus


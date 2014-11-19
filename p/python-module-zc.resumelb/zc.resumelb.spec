%define oname zc.resumelb

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 0.7.5
Release: alt1.git20141118
Summary: Resume-based WSGI load balancer
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zc.resumelb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zc.resumelb.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-gevent python-module-webob
BuildPreReq: python-module-llist python-module-bobo
BuildPreReq: python-module-manuel python-module-zconfig
BuildPreReq: python-module-mock python-module-webtest
BuildPreReq: python-module-zc.thread python-module-netifaces
BuildPreReq: python-module-zc.parse_addr python-module-BeautifulSoup4
BuildPreReq: python-module-zc.mappingobject python-module-waitress
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zc.zk-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-gevent python3-module-webob
BuildPreReq: python3-module-llist python3-module-bobo
BuildPreReq: python3-module-manuel python3-module-zconfig
BuildPreReq: python3-module-mock python3-module-webtest
BuildPreReq: python3-module-zc.thread python3-module-netifaces
BuildPreReq: python3-module-zc.parse_addr python3-module-BeautifulSoup4
BuildPreReq: python3-module-zc.mappingobject python3-module-waitress
BuildPreReq: python3-module-zope.testing
BuildPreReq: python3-module-zc.zk-tests
%endif

%py_provides %oname
%py_requires zc zc.thread zc.parse_addr zc.mappingobject zc.zk

%description
This package provides a load balancer for WSGI applications that sorts
requests into request classes and assigns requests of a given class to
the same workers.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zc.zk.testing

%description tests
This package provides a load balancer for WSGI applications that sorts
requests into request classes and assigns requests of a given class to
the same workers.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Resume-based WSGI load balancer
Group: Development/Python3
%py3_provides %oname
%py3_requires zc zc.thread zc.parse_addr zc.mappingobject zc.zk

%description -n python3-module-%oname
This package provides a load balancer for WSGI applications that sorts
requests into request classes and assigns requests of a given class to
the same workers.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.testing zc.zk.testing

%description -n python3-module-%oname-tests
This package provides a load balancer for WSGI applications that sorts
requests into request classes and assigns requests of a given class to
the same workers.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
export LC_ALL=en_US.UTF-8
export PYTHONPATH=$PWD/src
python setup.py test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD/src
python3 setup.py test
popd
%endif

%files
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/zc/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/zc/*/tests.*

%files tests
%python_sitelibdir/zc/*/tests.*

%if_with python3
%files -n python3-module-%oname
%_bindir/*.py3
%python3_sitelibdir/zc/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/zc/*/tests.*
%exclude %python3_sitelibdir/zc/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/zc/*/tests.*
%python3_sitelibdir/zc/*/*/tests.*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.5-alt1.git20141118
- Version 0.7.5

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt1.git20141029
- Initial build for Sisyphus


%define oname zc.isithanging

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3.0
Release: alt1
Summary: A zc.monitor plugin for testing whether function hangs
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zc.isithanging/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-manuel python-module-mock
BuildPreReq: python-module-zope.testing python-module-zc.thread
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-manuel python3-module-mock
BuildPreReq: python3-module-zope.testing python3-module-zc.thread
%endif

%py_provides %oname
%py_requires zc

%description
Somtimes, computation stops and it can be hard to find out why. Tools
like strace can be helpful, but are very low level. If a call hangs
calling external network services, all you might see is a select or poll
call and not what serveice was being called.

Isithanging provides a simple registry and a helper function for
registering and unregistering calls.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zc.thread

%description tests
Somtimes, computation stops and it can be hard to find out why. Tools
like strace can be helpful, but are very low level. If a call hangs
calling external network services, all you might see is a select or poll
call and not what serveice was being called.

Isithanging provides a simple registry and a helper function for
registering and unregistering calls.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A zc.monitor plugin for testing whether function hangs
Group: Development/Python3
%py3_provides %oname
%py3_requires zc

%description -n python3-module-%oname
Somtimes, computation stops and it can be hard to find out why. Tools
like strace can be helpful, but are very low level. If a call hangs
calling external network services, all you might see is a select or poll
call and not what serveice was being called.

Isithanging provides a simple registry and a helper function for
registering and unregistering calls.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.testing zc.thread

%description -n python3-module-%oname-tests
Somtimes, computation stops and it can be hard to find out why. Tools
like strace can be helpful, but are very low level. If a call hangs
calling external network services, all you might see is a select or poll
call and not what serveice was being called.

Isithanging provides a simple registry and a helper function for
registering and unregistering calls.

This package contains tests for %oname.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
cp README.rst src/zc/isithanging/
python setup.py test
%if_with python3
pushd ../python3
cp README.rst src/zc/isithanging/
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/zc/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/zc/*/tests.*

%files tests
%python_sitelibdir/zc/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/zc/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/zc/*/tests.*
%exclude %python3_sitelibdir/zc/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/zc/*/tests.*
%python3_sitelibdir/zc/*/*/tests.*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus


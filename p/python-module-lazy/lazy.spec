%define oname lazy

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt1.git20140420.1.1
Summary: Lazy attributes for Python objects
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/lazy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/stefanholek/lazy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
Lazy attributes are computed attributes that are evaluated only once,
the first time they are used. Subsequent uses return the results of the
first call. They come handy when code should run

* late, i.e. just before it is needed, and
* once, i.e. not twice, in the lifetime of an object.

You can think of it as deferred initialization. The possibilities are
endless.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Lazy attributes are computed attributes that are evaluated only once,
the first time they are used. Subsequent uses return the results of the
first call. They come handy when code should run

* late, i.e. just before it is needed, and
* once, i.e. not twice, in the lifetime of an object.

You can think of it as deferred initialization. The possibilities are
endless.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Lazy attributes for Python objects
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Lazy attributes are computed attributes that are evaluated only once,
the first time they are used. Subsequent uses return the results of the
first call. They come handy when code should run

* late, i.e. just before it is needed, and
* once, i.e. not twice, in the lifetime of an object.

You can think of it as deferred initialization. The possibilities are
endless.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Lazy attributes are computed attributes that are evaluated only once,
the first time they are used. Subsequent uses return the results of the
first call. They come handy when code should run

* late, i.e. just before it is needed, and
* once, i.e. not twice, in the lifetime of an object.

You can think of it as deferred initialization. The possibilities are
endless.

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.git20140420.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20140420.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20140420
- Initial build for Sisyphus


%define oname bobo

%def_with python3

Name: python-module-%oname
Version: 2.3.0
Release: alt1.git20141121
Summary: Web application framework for the impatient
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/bobo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/bobo.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-webob python-module-six
BuildPreReq: python-module-manuel-tests python-module-webtest
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-webob python3-module-six
BuildPreReq: python3-module-manuel-tests python3-module-webtest
BuildPreReq: python3-module-zope.testing
%endif

%py_provides %oname boboserver

%description
Bobo is a light-weight framework for creating WSGI web applications.

Its goal is to be easy to use and remember.

It addresses 2 problems:

* Mapping URLs to objects
* Calling objects to generate HTTP responses

%package -n python3-module-%oname
Summary: Web application framework for the impatient
Group: Development/Python3
%py3_provides %oname boboserver

%description -n python3-module-%oname
Bobo is a light-weight framework for creating WSGI web applications.

Its goal is to be easy to use and remember.

It addresses 2 problems:

* Mapping URLs to objects
* Calling objects to generate HTTP responses

%package -n python-module-bobodoctestumentation
Summary: Bobo tests and documentation
Group: Development/Python

%description -n python-module-bobodoctestumentation
Bobo is a light-weight framework for creating WSGI web applications.

Its goal is to be easy to use and remember.

It addresses 2 problems:

* Mapping URLs to objects
* Calling objects to generate HTTP responses

This package provides documentation and tests for the bobo package.

%package -n python3-module-bobodoctestumentation
Summary: Bobo tests and documentation
Group: Development/Python3

%description -n python3-module-bobodoctestumentation
Bobo is a light-weight framework for creating WSGI web applications.

Its goal is to be easy to use and remember.

It addresses 2 problems:

* Mapping URLs to objects
* Calling objects to generate HTTP responses

This package provides documentation and tests for the bobo package.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Bobo is a light-weight framework for creating WSGI web applications.

Its goal is to be easy to use and remember.

It addresses 2 problems:

* Mapping URLs to objects
* Calling objects to generate HTTP responses

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Bobo is a light-weight framework for creating WSGI web applications.

Its goal is to be easy to use and remember.

It addresses 2 problems:

* Mapping URLs to objects
* Calling objects to generate HTTP responses

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
cp objects.inv doc/

%build
pushd %oname
%python_build_debug
popd
pushd bobodoctestumentation
%python_build_debug
popd

%if_with python3
pushd ../python3/%oname
%python3_build_debug
popd
pushd ../python3/bobodoctestumentation
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3/%oname
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
pushd ../python3/bobodoctestumentation
%python3_install
popd
%endif

pushd %oname
%python_install
popd
pushd bobodoctestumentation
%python_install
popd

export PYTHONPATH=$PWD/%oname/src
%make -C doc pickle
%make -C doc html

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
pushd %oname
export PYTHONPATH=%buildroot%python_sitelibdir
python setup.py test
popd
#if_with python3
%if 0
pushd ../python3/%oname
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 setup.py test
popd
%endif

%files
%doc bobo/*.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/bobodoctestumentation*

%files -n python-module-bobodoctestumentation
%python_sitelibdir/bobodoctestumentation*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc bobo/*.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/bobodoctestumentation*

%files -n python3-module-bobodoctestumentation
%python3_sitelibdir/bobodoctestumentation*
%endif

%changelog
* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.git20141121
- Version 2.3.0

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20140710
- Initial build for Sisyphus


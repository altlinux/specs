%define oname hamcrest

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt1.a1.git20141030
Summary: Hamcrest framework for matcher objects
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/PyHamcrest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hamcrest/PyHamcrest.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-tox
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-tox
%endif

%py_provides %oname

%description
PyHamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations
where matchers are invaluable, such as UI validation, or data filtering,
but it is in the area of writing flexible tests that matchers are most
commonly used.

%package -n python3-module-%oname
Summary: Hamcrest framework for matcher objects
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
PyHamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations
where matchers are invaluable, such as UI validation, or data filtering,
but it is in the area of writing flexible tests that matchers are most
commonly used.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
PyHamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations
where matchers are invaluable, such as UI validation, or data filtering,
but it is in the area of writing flexible tests that matchers are most
commonly used.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
PyHamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations
where matchers are invaluable, such as UI validation, or data filtering,
but it is in the area of writing flexible tests that matchers are most
commonly used.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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

export PYTHONPATH=$PWD/src
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

rm -f *requirements.txt

%check
python setup.py test
export PYTHONPATH=$PWD/src
py.test
%if_with python3
pushd ../python3
python3 setup.py test
#export PYTHONPATH=$PWD/src
#py.test-%_python3_version
popd
%endif

%files
%doc *.txt *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1.git20141030
- Initial build for Sisyphus


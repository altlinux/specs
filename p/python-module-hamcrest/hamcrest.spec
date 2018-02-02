# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.a1.git20150729.1.1.1
%define oname hamcrest

%def_with python3

Name: python-module-%oname
Version: 2.0.0
#Release: alt2.a1.git20150729.1
Summary: Hamcrest framework for matcher objects
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/PyHamcrest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hamcrest/PyHamcrest.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-mock python-module-objects.inv python-module-pytest-cov python-module-setuptools
BuildRequires: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-pbr python3-module-pytest-cov python3-module-setuptools python3-module-tox python3-module-unittest2
%endif

%py_provides %oname

# optimized out: -=FIXES: python2.7(sphinx_rtd_theme)
BuildRequires: python2.7(sphinx_rtd_theme)

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt2.a1.git20150729.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.a1.git20150729.1.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.a1.git20150729.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 05 2016 Sergey Alembekov <rt@altlinux.ru> 2.0.0-alt2.a1.git20150729
- cleanup buildreq

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1.git20150729
- New snapshot

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1.git20141030
- Initial build for Sisyphus


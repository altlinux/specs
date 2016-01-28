%define oname datarray

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0.7
Release: alt1.git20111119.1
Summary: NumPy arrays with named axes and named indices
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/datarray/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/fperez/datarray.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-numpy python-module-matplotlib
#BuildPreReq: python-module-networkx python-module-nose
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-numpy python3-module-matplotlib
#BuildPreReq: python3-module-networkx python-module-nose
%endif

%py_provides %oname
%py_requires numpy matplotlib

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mpmath python-module-numpy python-module-pyparsing python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-numpy
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-matplotlib python-module-nose python-module-numpy-testing python-module-objects.inv python-module-pydot python-module-pygraphviz python-module-scipy python-module-yaml python3-module-numpy-testing rpm-build-python3 time

%description
Scientists, engineers, mathematicians and statisticians don't just work
with matrices; they often work with structured data, just like you'd
find in a table. However, functionality for this is missing from Numpy,
and there are efforts to create something to fill the void. This is one
of those efforts.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Scientists, engineers, mathematicians and statisticians don't just work
with matrices; they often work with structured data, just like you'd
find in a table. However, functionality for this is missing from Numpy,
and there are efforts to create something to fill the void. This is one
of those efforts.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: NumPy arrays with named axes and named indices
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy matplotlib

%description -n python3-module-%oname
Scientists, engineers, mathematicians and statisticians don't just work
with matrices; they often work with structured data, just like you'd
find in a table. However, functionality for this is missing from Numpy,
and there are efforts to create something to fill the void. This is one
of those efforts.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Scientists, engineers, mathematicians and statisticians don't just work
with matrices; they often work with structured data, just like you'd
find in a table. However, functionality for this is missing from Numpy,
and there are efforts to create something to fill the void. This is one
of those efforts.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Scientists, engineers, mathematicians and statisticians don't just work
with matrices; they often work with structured data, just like you'd
find in a table. However, functionality for this is missing from Numpy,
and there are efforts to create something to fill the void. This is one
of those efforts.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Scientists, engineers, mathematicians and statisticians don't just work
with matrices; they often work with structured data, just like you'd
find in a table. However, functionality for this is missing from Numpy,
and there are efforts to create something to fill the void. This is one
of those efforts.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.7-alt1.git20111119.1
- NMU: Use buildreq for BR.

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20111119
- Initial build for Sisyphus


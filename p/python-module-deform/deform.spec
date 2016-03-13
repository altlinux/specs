%define oname deform

%def_with python3

Name: python-module-%oname
Version: 2.0
Release: alt2.a2.git20141001.1.1
Summary: Another form generation library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/deform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pylons/deform.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
#BuildPreReq: python-module-colander python-module-peppercorn
#BuildPreReq: python-module-chameleon.core
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires colander peppercorn chameleon.utils zope.deprecation

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-iso8601 python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-translationstring python-module-zope python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: pylons_sphinx_theme python-module-alabaster python-module-chameleon.core python-module-colander python-module-docutils python-module-html5lib python-module-objects.inv python-module-peppercorn python3-module-setuptools rpm-build-python3 time

%description
A Python HTML form library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A Python HTML form library.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Another form generation library
Group: Development/Python3
%py3_provides %oname
%py3_requires colander peppercorn chameleon.utils zope.deprecation

%description -n python3-module-%oname
A Python HTML form library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A Python HTML form library.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A Python HTML form library.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A Python HTML form library.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/
cp -fR %_datadir/pylons_sphinx_theme docs/_themes

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
cp -fR %oname/templates %oname/static \
	%buildroot%python_sitelibdir/%oname/

%if_with python3
pushd ../python3
%python3_install
cp -fR %oname/templates %oname/static \
	%buildroot%python3_sitelibdir/%oname/
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt2.a2.git20141001.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0-alt2.a2.git20141001.1
- NMU: Use buildreq for BR.

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2.a2.git20141001
- Added necessary files

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.a2.git20141001
- Initial build for Sisyphus


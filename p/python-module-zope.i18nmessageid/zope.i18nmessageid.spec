%define oname zope.i18nmessageid

%def_with python3

Name: python-module-%oname
Version: 4.0.4
Release: alt1.dev0.git20150309.1.1.1.1
Summary: Message Identifiers for internationalization
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.i18nmessageid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zope.i18nmessageid.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-nose python-module-coverage
#BuildPreReq: python-module-nosexcover
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-nose python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-nose python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-nosexcover python-module-objects.inv python-module-setuptools python3-devel python3-module-coverage python3-module-nosexcover python3-module-setuptools rpm-build-python3 time

#BuildRequires: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-nose python3-module-coverage
#BuildPreReq: python3-module-nosexcover
#BuildPreReq: python-tools-2to3
%endif

%py_provides zope.i18nmessageid

%py_requires zope

%description
This package provides facilities for *declaring* messages within
program source text;  translation of the messages is the responsiblitiy
of the 'zope.i18n' package.

%if_with python3
%package -n python3-module-%oname
Summary: Message Identifiers for internationalization (Python 3)
Group: Development/Python3
%py3_provides zope.i18nmessageid
%py3_requires zope

%description -n python3-module-%oname
This package provides facilities for *declaring* messages within
program source text;  translation of the messages is the responsiblitiy
of the 'zope.i18n' package.

%package -n python3-module-%oname-tests
Summary: Tests for zope.i18nmessageid (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides facilities for *declaring* messages within
program source text;  translation of the messages is the responsiblitiy
of the 'zope.i18n' package.

This package contains tests for zope.i18nmessageid
%endif

%package pickles
Summary: Pickles for zope.i18nmessageid
Group: Development/Python

%description pickles
This package provides facilities for *declaring* messages within
program source text;  translation of the messages is the responsiblitiy
of the 'zope.i18n' package.

This package contains pickles for zope.i18nmessageid

%package tests
Summary: Tests for zope.i18nmessageid
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides facilities for *declaring* messages within
program source text;  translation of the messages is the responsiblitiy
of the 'zope.i18n' package.

This package contains tests for zope.i18nmessageid

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
%python_build
%if_with python3
pushd ../python3
%python3_build
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
%make -C docs pickle
%make -C docs html
install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=$PWD/src
python setup.py test -v
nosetests -vv --with-xunit --with-xcoverage
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD/src
python3 setup.py test -v
nosetests3 -vv --with-xunit --with-xcoverage
popd
%endif

%files
%doc *.txt *.rst docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.4-alt1.dev0.git20150309.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150309.1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150309.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt1.dev0.git20150309.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev0.git20150309
- Version 4.0.4.dev0
- Added documentation
- Enabled check

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-3.3

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.3-alt4.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt4
- Added necessary requirements
- Excluded *.pth

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt3
- Added %%py_provides zope.i18nmessageid

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt2
- Don't build python-module-zope.arch

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt1
- Initial build for Sisyphus


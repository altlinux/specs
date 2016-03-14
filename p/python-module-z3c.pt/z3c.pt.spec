%define oname z3c.pt

%def_with python3

Name: python-module-%oname
Version: 3.0.0
Release: alt2.a2.dev0.git20130313.1.1
Summary: Python template compiler which supports ZPT
License: ZPLv2.1
Group: Development/Python
Url: http://chameleon.repoze.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/zopefoundation/z3c.pt.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-zope.interface
#BuildPreReq: python-module-zope.i18n python-module-zope.component
#BuildPreReq: python-module-zope.event python-module-zope.i18nmessageid
#BuildPreReq: python-module-texttemplate python-module-zope.schema
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c zope.interface zope.component zope.i18n zope.traversing
%py_requires zope.contentprovider chameleon

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-persistent python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-z3c python-module-zope.component python-module-zope.event python-module-zope.hookable python-module-zope.i18nmessageid python-module-zope.interface python-module-zope.schema python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-texttemplate python-module-zope.i18n python3-module-setuptools rpm-build-python3 time

%description
This is a fast implementation of the ZPT template engine for Zope 3
which uses Chameleon to compile templates to byte-code.

The package provides application support equivalent to
``zope.app.pagetemplate``.

%package -n python3-module-%oname
Summary: Python template compiler which supports ZPT
Group: Development/Python3
%py3_requires z3c zope.interface zope.component zope.i18n zope.traversing
%py3_requires zope.contentprovider chameleon

%description -n python3-module-%oname
This is a fast implementation of the ZPT template engine for Zope 3
which uses Chameleon to compile templates to byte-code.

The package provides application support equivalent to
``zope.app.pagetemplate``.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.pt
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This is a fast implementation of the ZPT template engine for Zope 3
which uses Chameleon to compile templates to byte-code.

The package provides application support equivalent to
``zope.app.pagetemplate``.

This package contains tests for z3c.pt

%package -n python-module-z3c
Summary: z3c core package
Group: Development/Python
%py_provides z3c

%description -n python-module-z3c
z3c core package.

%package -n python3-module-z3c
Summary: z3c core package (Python 3)
Group: Development/Python3
%py3_provides z3c

%description -n python3-module-z3c
z3c core package.

%package tests
Summary: Tests for z3c.pt
Group: Development/Python
Requires: %name = %version-%release

%description tests
This is a fast implementation of the ZPT template engine for Zope 3
which uses Chameleon to compile templates to byte-code.

The package provides application support equivalent to
``zope.app.pagetemplate``.

This package contains tests for z3c.pt

%package pickles
Summary: Pickles for z3c.pt
Group: Development/Python

%description pickles
This is a fast implementation of the ZPT template engine for Zope 3
which uses Chameleon to compile templates to byte-code.

The package provides application support equivalent to
``zope.app.pagetemplate``.

This package contains pickles for z3c.pt

%package docs
Summary: Documentation for z3c.pt
Group: Development/Documentation
BuildArch: noarch

%description docs
This is a fast implementation of the ZPT template engine for Zope 3
which uses Chameleon to compile templates to byte-code.

The package provides application support equivalent to
``zope.app.pagetemplate``.

This package contains documentation for z3c.pt

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
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

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
%make pickle
%make html
popd

install -d %buildroot%python_sitelibdir/z3c
install -d %buildroot%python_sitelibdir/%oname
install -p -m644 src/z3c/__init__.py %buildroot%python_sitelibdir/z3c/

install -d %buildroot%python3_sitelibdir/z3c
install -p -m644 src/z3c/__init__.py %buildroot%python3_sitelibdir/z3c/

%ifarch x86_64
mv %buildroot%python_sitelibdir_noarch/z3c/* \
	%buildroot%python_sitelibdir/z3c/
%if_with python3
mv %buildroot%python3_sitelibdir_noarch/z3c/* \
	%buildroot%python3_sitelibdir/z3c/
%endif
%endif
cp -fR docs/.build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%python_sitelibdir/*
%ifnarch x86_64
%exclude %python_sitelibdir/*.pth
%endif
%exclude %python_sitelibdir/z3c/__init__.py*
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/*/*/tests

%files -n python-module-z3c
%dir %python_sitelibdir/z3c
%python_sitelibdir/z3c/__init__.py*

%files -n python3-module-z3c
%dir %python3_sitelibdir/z3c
%python3_sitelibdir/z3c/__init__.py*
%python3_sitelibdir/z3c/__pycache__

%files tests
%python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/.build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%ifnarch x86_64
%exclude %python3_sitelibdir/*.pth
%endif
%exclude %python3_sitelibdir/z3c/__init__.py*
%exclude %python3_sitelibdir/z3c/__pycache__/__init__.*
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.0-alt2.a2.dev0.git20130313.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.0.0-alt2.a2.dev0.git20130313.1
- NMU: Use buildreq for BR.

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt2.a2.dev0.git20130313
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.a2.dev0.git20130313
- Version 3.0.0a2.dev0

* Sat Mar 02 2013 Aleksey Avdeev <solo@altlinux.ru> 3.0.0-alt1.a1
- Version 3.0.0a1

* Wed Apr 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.bzr20120215
- Version 2.2.1
- Added python3-module-z3c

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.5-alt1.bzr20111124
- Version 2.1.5

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.rc2-alt1.bzr20110511.2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.rc2-alt1.bzr20110511.2
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.rc2-alt1.bzr20110511.1
- Set as archdep package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.rc2-alt1.bzr20110511
- Initial build for Sisyphus


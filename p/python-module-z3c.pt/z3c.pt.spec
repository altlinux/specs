%define oname z3c.pt
Name: python-module-%oname
Version: 2.2.1
Release: alt1.bzr20120215
Summary: Python template compiler which supports ZPT
License: ZPLv2.1
Group: Development/Python
Url: http://chameleon.repoze.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# bzr branch lp:z3c.pt
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel python-module-zope.interface
BuildPreReq: python-module-zope.i18n python-module-zope.component
BuildPreReq: python-module-zope.event python-module-zope.i18nmessageid
BuildPreReq: python-module-texttemplate python-module-zope.schema

%py_requires z3c zope.interface zope.component zope.i18n zope.traversing
%py_requires zope.contentprovider chameleon

%description
This is a fast implementation of the ZPT template engine for Zope 3
which uses Chameleon to compile templates to byte-code.

The package provides application support equivalent to
``zope.app.pagetemplate``.

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

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%install
%python_install

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

%changelog
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


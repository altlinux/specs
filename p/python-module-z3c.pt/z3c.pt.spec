%define oname z3c.pt

%def_with python3
%def_with check
%def_with docs

Name: python-module-%oname
Version: 3.2.0
Release: alt1
Summary: Python template compiler which supports ZPT
License: ZPLv2.1
Group: Development/Python
Url: https://github.com/zopefoundation/z3c.pt

# git://github.com/zopefoundation/z3c.pt.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools
%if_with check
BuildRequires: python-module-six
BuildRequires: python-module-zope.interface
BuildRequires: python-module-zope.component
BuildRequires: python-module-zope.component-tests
BuildRequires: python-module-zope.i18n >= 3.5
BuildRequires: python-module-zope.traversing
BuildRequires: python-module-zope.contentprovider
BuildRequires: python-module-chameleon.core >= 2.4
BuildRequires: python-module-zope.pagetemplate
BuildRequires: python-module-zope.testing
BuildRequires: python-module-zope.testrunner
%endif

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%if_with check
BuildRequires: python3-module-six
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.component-tests
BuildRequires: python3-module-zope.i18n >= 3.5
BuildRequires: python3-module-zope.traversing
BuildRequires: python3-module-zope.contentprovider
BuildRequires: python3-module-chameleon.core >= 2.4
BuildRequires: python3-module-zope.pagetemplate
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
%endif
%endif

%if_with docs
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-docutils python-module-objects.inv
%endif

%py_requires z3c zope.interface zope.component
%py_requires zope.i18n zope.traversing zope.contentprovider

%description
This is a fast implementation of the ZPT template engine for Zope 3
which uses Chameleon to compile templates to byte-code.

The package provides application support equivalent to
``zope.app.pagetemplate``.

%if_with python3
%package -n python3-module-%oname
Summary: Python template compiler which supports ZPT
Group: Development/Python3
%py3_requires z3c

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
%endif

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

%if_with docs
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
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%if_with docs
%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
        %buildroot%python3_sitelibdir/
%endif
%endif

%if_with docs
export PYTHONPATH="$(pwd)/src"
pushd docs
%make pickle
%make html
install -d %buildroot%python_sitelibdir/%oname/
cp -va .build/pickle %buildroot%python_sitelibdir/%oname/
popd
%endif


%if_with check
%check
PYTHONPATH="$(pwd)/src" zope-testrunner --test-path=./src/

%if_with python3
pushd ../python3
PYTHONPATH="$(pwd)/src" zope-testrunner3 --test-path=./src/
popd
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%ifnarch x86_64
%exclude %python_sitelibdir/*.pth
%endif
%if_with docs
%exclude %python_sitelibdir/%oname/pickle
%endif
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with docs
%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/.build/html/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%ifnarch x86_64
%exclude %python3_sitelibdir/*.pth
%endif
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sat Feb 02 2019 Ivan A. Melnikov <iv@altlinux.org> 3.2.0-alt1
- 3.2.0
- add %%check
- add toggles for %%check and building docs, on by default
- build 'z3c' namespace module separately, remove it from here
- minor spec cleanups

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.0-alt2.a2.dev0.git20130313.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

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


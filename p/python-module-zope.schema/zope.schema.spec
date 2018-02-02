# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev0.git20150128.1.1.1.1
%define oname zope.schema

%def_with python3

Name: python-module-%oname
Version: 4.4.3
#Release: alt1.dev0.git20150128.1.1
Summary: zope.interface extension for defining data schemas
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.schema/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zope.schema.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-zope.event
#BuildPreReq: python-module-zope.testing
#BuildPreReq: python-module-nose python-module-coverage
#BuildPreReq: python-module-nosexcover
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-repoze.sphinx.autointerface
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-nose python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-zope python-module-zope.exceptions python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-nose python3-module-pytest python3-module-setuptools python3-module-zope python3-module-zope.exceptions python3-module-zope.interface
BuildRequires: python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-nosexcover python-module-objects.inv python-module-repoze.sphinx.autointerface python-module-setuptools python-module-zope.event python-module-zope.testing python3-module-coverage python3-module-nosexcover python3-module-setuptools python3-module-zope.event python3-module-zope.testing rpm-build-python3 time

#BuildRequires: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-zope.event
#BuildPreReq: python3-module-zope.testing
#BuildPreReq: python3-module-nose python3-module-coverage
#BuildPreReq: python3-module-nosexcover
%endif

%py_requires zope.interface zope.event

%description
This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

Schemas extend the notion of interfaces to detailed descriptions of
Attributes (but not methods). Every schema is an interface and specifies
the public fields of an object. A field roughly corresponds to an
attribute of a python object. But a Field provides space for at least a
title and a description. It can also constrain its value and provide a
validation method. Besides you can optionally specify characteristics
such as its value being read-only or not required.

%if_with python3
%package -n python3-module-%oname
Summary: zope.interface extension for defining data schemas (Python 3)
Group: Development/Python3
%py3_requires zope.interface zope.event

%description -n python3-module-%oname
This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

Schemas extend the notion of interfaces to detailed descriptions of
Attributes (but not methods). Every schema is an interface and specifies
the public fields of an object. A field roughly corresponds to an
attribute of a python object. But a Field provides space for at least a
title and a description. It can also constrain its value and provide a
validation method. Besides you can optionally specify characteristics
such as its value being read-only or not required.

%package -n python3-module-%oname-tests
Summary: Tests for zope.schema (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

Schemas extend the notion of interfaces to detailed descriptions of
Attributes (but not methods). Every schema is an interface and specifies
the public fields of an object. A field roughly corresponds to an
attribute of a python object. But a Field provides space for at least a
title and a description. It can also constrain its value and provide a
validation method. Besides you can optionally specify characteristics
such as its value being read-only or not required.

This package contains tests for zope.schema
%endif

%package pickles
Summary: Pickles for zope.schema
Group: Development/Python

%description pickles
This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

Schemas extend the notion of interfaces to detailed descriptions of
Attributes (but not methods). Every schema is an interface and specifies
the public fields of an object. A field roughly corresponds to an
attribute of a python object. But a Field provides space for at least a
title and a description. It can also constrain its value and provide a
validation method. Besides you can optionally specify characteristics
such as its value being read-only or not required.

This package contains pickles for zope.schema

%package tests
Summary: Tests for zope.schema
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

Schemas extend the notion of interfaces to detailed descriptions of
Attributes (but not methods). Every schema is an interface and specifies
the public fields of an object. A field roughly corresponds to an
attribute of a python object. But a Field provides space for at least a
title and a description. It can also constrain its value and provide a
validation method. Besides you can optionally specify characteristics
such as its value being read-only or not required.

This package contains tests for zope.schema

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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

%make -C docs pickle
%make -C docs html
install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
nosetests -vv --with-xunit --with-xcoverage
%if_with python3
pushd ../python3
python3 setup.py test -v
#nosetests3 -vv --with-xunit --with-xcoverage
popd
%endif

%files
%doc *.txt *.rst docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.4.3-alt1.dev0.git20150128.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.3-alt1.dev0.git20150128.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.3-alt1.dev0.git20150128.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.4.3-alt1.dev0.git20150128.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.3-alt1.dev0.git20150128
- Version 4.4.3.dev0
- Added documentation
- Enabled check

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.1-alt1
- Version 4.4.1

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt1
- Version 4.3.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 4.1.1-alt1.1
- Rebuild with Python-3.3

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.0-alt4.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt2
- Set as archdep package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt1
- Initial build for Sisyphus


%define oname zope.container

%def_with python3

Name: python-module-%oname
Version: 4.1.1
Release: alt1.dev0.git20150608.1
Summary: Zope Container
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.container/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zope.container.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-zope.dottedname python-module-zope.schema
#BuildPreReq: python-module-zope.location python-module-zope.event
#BuildPreReq: python-module-zope.lifecycleevent python-module-zope.size
#BuildPreReq: python-module-zope.filerepresentation
#BuildPreReq: python-module-zope.traversing-tests
#BuildPreReq: python-module-zope.component-tests
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-repoze.sphinx.autointerface
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-zope.dottedname python3-module-zope.schema
#BuildPreReq: python3-module-zope.location python3-module-zope.event
#BuildPreReq: python3-module-zope.lifecycleevent python3-module-zope.size
#BuildPreReq: python3-module-zope.filerepresentation
#BuildPreReq: python3-module-zope.traversing-tests
#BuildPreReq: python3-module-zope.component-tests
%endif

Requires: python-module-zope.i18nmessageid
%py_requires zope.interface zope.dottedname zope.schema zope.traversing
%py_requires zope.component zope.event zope.location zope.security
%py_requires zope.lifecycleevent zope.size zope.filerepresentation
#BuildPreReq: python3-module-zope.traversing-tests

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-BTrees python-module-PyStemmer python-module-Pygments python-module-ZEO python-module-ZODB python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mimeparse python-module-numpy python-module-pbr python-module-persistent python-module-pyasn1 python-module-pytz python-module-repoze python-module-repoze.sphinx python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-transaction python-module-twisted-core python-module-unittest2 python-module-zc.lockfile python-module-zdaemon python-module-zope python-module-zope.annotation python-module-zope.browser python-module-zope.component python-module-zope.configuration python-module-zope.container python-module-zope.contenttype python-module-zope.dottedname python-module-zope.event python-module-zope.exceptions python-module-zope.filerepresentation python-module-zope.hookable python-module-zope.i18n python-module-zope.i18nmessageid python-module-zope.interface python-module-zope.lifecycleevent python-module-zope.location python-module-zope.pagetemplate python-module-zope.proxy python-module-zope.publisher python-module-zope.schema python-module-zope.security python-module-zope.size python-module-zope.tal python-module-zope.tales python-module-zope.testing python-module-zope.traversing python-module-zope.untrustedpython python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-dev python3-module-BTrees python3-module-ZEO python3-module-ZODB python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-persistent python3-module-pip python3-module-pycparser python3-module-pytz python3-module-setuptools python3-module-transaction python3-module-unittest2 python3-module-zc.lockfile python3-module-zdaemon python3-module-zope python3-module-zope.annotation python3-module-zope.browser python3-module-zope.component python3-module-zope.configuration python3-module-zope.container python3-module-zope.contenttype python3-module-zope.dottedname python3-module-zope.event python3-module-zope.exceptions python3-module-zope.i18n python3-module-zope.i18nmessageid python3-module-zope.interface python3-module-zope.lifecycleevent python3-module-zope.location python3-module-zope.proxy python3-module-zope.publisher python3-module-zope.schema python3-module-zope.security python3-module-zope.tal python3-module-zope.tales python3-module-zope.testing python3-module-zope.traversing
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-pytest python-module-repoze.sphinx.autointerface python-module-zope.browserpage python-module-zope.site python-module-zope.testrunner python3-module-html5lib python3-module-pytest python3-module-zope.filerepresentation python3-module-zope.pagetemplate python3-module-zope.site python3-module-zope.size python3-module-zope.testrunner rpm-build-python3 time

%description
This package define interfaces of container components, and provides
container implementations such as a BTreeContainer and OrderedContainer,
as well as the base class used by zope.site.folder for the Folder
implementation.

%package -n python3-module-%oname
Summary: Zope Container
Group: Development/Python3
Requires: python3-module-zope.i18nmessageid
%py3_requires zope.interface zope.dottedname zope.schema 
%py3_requires zope.component zope.event zope.location zope.security
%py3_requires zope.lifecycleevent

%description -n python3-module-%oname
This package define interfaces of container components, and provides
container implementations such as a BTreeContainer and OrderedContainer,
as well as the base class used by zope.site.folder for the Folder
implementation.

%package -n python3-module-%oname-tests
Summary: Tests for Zope Container
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package define interfaces of container components, and provides
container implementations such as a BTreeContainer and OrderedContainer,
as well as the base class used by zope.site.folder for the Folder
implementation.

This package contains tests for Zope Container.

%package pickles
Summary: Pickles for Zope Container
Group: Development/Python

%description pickles
This package define interfaces of container components, and provides
container implementations such as a BTreeContainer and OrderedContainer,
as well as the base class used by zope.site.folder for the Folder
implementation.

This package contains pickles for Zope Container.

%package tests
Summary: Tests for Zope Container
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package define interfaces of container components, and provides
container implementations such as a BTreeContainer and OrderedContainer,
as well as the base class used by zope.site.folder for the Folder
implementation.

This package contains tests for Zope Container.

%prep
%setup

rm -fR src/*.egg-info

%if_with python3
cp -fR . ../python3
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

%make -C docs pickle
%make -C docs html
install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
rm -fR build
#py.test -vv
#if_with python3
%if 0
pushd ../python3
rm -fR build
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.txt *.rst docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.1.1-alt1.dev0.git20150608.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150608
- Version 4.1.1.dev0
- Added documentation

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0
- Enabled check

* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Added necessary requirements

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Version 4.0.0
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a3
- Version 4.0.0a3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.12.0-alt3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.12.0-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt2
- Added necessary requirements
- Excluded *.th

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt1
- Initial build for Sisyphus


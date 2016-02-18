%define oname zope.pytest

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt4.1
Summary: zope pytest integration
License: ZPL
Group: Development/Python
Url: http://packages.python.org/zope.pytest
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-zope.browserpage
#BuildPreReq: python-module-zope.app.appsetup python-module-docutils
#BuildPreReq: python-module-zope.app.zcmlfiles python-module-zope.schema
#BuildPreReq: python-module-zope.securitypolicy python-module-simplejson
#BuildPreReq: python-module-infrae.testbrowser
#BuildPreReq: python-module-zope.configuration
#BuildPreReq: python-module-zope.component python-module-zope.testing
#BuildPreReq: python-module-zope.event python-module-zope.processlifetime
#BuildPreReq: python-module-zope.app.publication python-module-zope.app.wsgi
#BuildPreReq: python-module-ZODB3 python-module-webob
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.configuration zope.component zope.testing
%py_requires zope.event zope.processlifetime zope.app.publication
%py_requires zope.app.wsgi webob simplejson zope.app.appsetup
%py_requires zope.app.zcmlfiles zope.browserpage zope.securitypolicy
%py_requires infrae.testbrowser ZODB3

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-BTrees python-module-PyStemmer python-module-Pygments python-module-WSGIProxy2 python-module-ZEO python-module-ZODB python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-dns python-module-docutils python-module-enum34 python-module-genshi python-module-greenlet python-module-html5lib python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-persistent python-module-psycopg2 python-module-pyasn1 python-module-pytz python-module-restkit python-module-roman python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-transaction python-module-waitress python-module-webtest python-module-zc.lockfile python-module-zconfig python-module-zdaemon python-module-zodbpickle python-module-zope python-module-zope.annotation python-module-zope.app python-module-zope.app.applicationcontrol python-module-zope.app.appsetup python-module-zope.app.authentication python-module-zope.app.basicskin python-module-zope.app.broken python-module-zope.app.component python-module-zope.app.container python-module-zope.app.content python-module-zope.app.dependable python-module-zope.app.error python-module-zope.app.exception python-module-zope.app.folder python-module-zope.app.form python-module-zope.app.generations python-module-zope.app.http python-module-zope.app.i18n python-module-zope.app.locales python-module-zope.app.localpermission python-module-zope.app.pagetemplate python-module-zope.app.principalannotation python-module-zope.app.publication python-module-zope.app.publisher python-module-zope.app.renderer python-module-zope.app.rotterdam python-module-zope.app.schema python-module-zope.app.security python-module-zope.app.wsgi python-module-zope.app.zopeappgenerations python-module-zope.applicationcontrol python-module-zope.authentication python-module-zope.broken python-module-zope.browser python-module-zope.browsermenu python-module-zope.browserpage python-module-zope.browserresource python-module-zope.cachedescriptors python-module-zope.component python-module-zope.componentvocabulary python-module-zope.configuration python-module-zope.container python-module-zope.contenttype python-module-zope.copy python-module-zope.copypastemove python-module-zope.datetime python-module-zope.deprecation python-module-zope.dottedname python-module-zope.dublincore python-module-zope.error python-module-zope.event python-module-zope.exceptions python-module-zope.filerepresentation python-module-zope.formlib python-module-zope.generations python-module-zope.hookable python-module-zope.i18n python-module-zope.i18nmessageid python-module-zope.interface python-module-zope.lifecycleevent python-module-zope.location python-module-zope.login python-module-zope.minmax python-module-zope.pagetemplate python-module-zope.password python-module-zope.pluggableauth python-module-zope.principalannotation python-module-zope.principalregistry python-module-zope.processlifetime python-module-zope.proxy python-module-zope.ptresource python-module-zope.publisher python-module-zope.schema python-module-zope.security python-module-zope.securitypolicy python-module-zope.session python-module-zope.site python-module-zope.size python-module-zope.structuredtext python-module-zope.tal python-module-zope.tales python-module-zope.testbrowser python-module-zope.testing python-module-zope.traversing python-module-zope.untrustedpython python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base
BuildRequires: python-module-alabaster python-module-infrae.testbrowser python-module-objects.inv python-module-zope.app.zcmlfiles python3-module-setuptools rpm-build-python3 time

%description
This package contains a set of helper functions to test Zope/Grok
using pytest. It currently lacks special support for doctesting.

%package -n python3-module-%oname
Summary: zope pytest integration
Group: Development/Python3
%py3_requires zope.configuration zope.component zope.testing
%py3_requires zope.event zope.processlifetime zope.app.publication
%py3_requires zope.app.wsgi webob simplejson zope.app.appsetup
%py3_requires zope.app.zcmlfiles zope.browserpage zope.securitypolicy
%py3_requires infrae.testbrowser ZODB3

%description -n python3-module-%oname
This package contains a set of helper functions to test Zope/Grok
using pytest. It currently lacks special support for doctesting.

%package pickles
Summary: Pickles for zope.pytest
Group: Development/Python

%description pickles
This package contains a set of helper functions to test Zope/Grok
using pytest. It currently lacks special support for doctesting.

This package contains pickles for zope.pytest.

%package docs
Summary: Documentation for zope.pytest
Group: Development/Documentation
BuildArch: noarch

%description docs
This package contains a set of helper functions to test Zope/Grok
using pytest. It currently lacks special support for doctesting.

This package contains documentation for zope.pytest.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

export PYTHONPATH=$PWD/src
pushd doc
%make html
%make pickle

popd
%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

mkdir -p %buildroot%python_sitelibdir/%name
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%name/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/%name/pickle

%files pickles
%python_sitelibdir/%name/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt4.1
- NMU: Use buildreq for BR.

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added documentation and pickles

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus


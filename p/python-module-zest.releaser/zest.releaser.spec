%define oname zest.releaser

%def_with python3

Name: python-module-%oname
Version: 3.55
Release: alt1.dev0.git20141229.1

Summary: Software releasing made easy and repeatable
License: GPLv2+
Group: Development/Python

Url: https://pypi.python.org/pypi/zest.releaser

# https://github.com/zestsoftware/zest.releaser.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-module-setuptools-tests
#BuildPreReq: python-module-z3c.testsetup
#BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-z3c.testsetup
#BuildPreReq: python3-module-nose
#BuildPreReq: python-tools-2to3
%endif

%setup_python_module %oname

Requires: python-module-zest = %EVR

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-BTrees python-module-PyStemmer python-module-Pygments python-module-WSGIProxy2 python-module-ZEO python-module-ZODB python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-dns python-module-docutils python-module-enum34 python-module-genshi python-module-greenlet python-module-html5lib python-module-jinja2 python-module-ndg-httpsclient python-module-ntlm python-module-persistent python-module-psycopg2 python-module-pyasn1 python-module-pytest python-module-pytz python-module-restkit python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-transaction python-module-waitress python-module-webtest python-module-zc.lockfile python-module-zdaemon python-module-zope.annotation python-module-zope.app.applicationcontrol python-module-zope.app.appsetup python-module-zope.app.authentication python-module-zope.app.basicskin python-module-zope.app.broken python-module-zope.app.component python-module-zope.app.container python-module-zope.app.content python-module-zope.app.debug python-module-zope.app.dependable python-module-zope.app.error python-module-zope.app.exception python-module-zope.app.folder python-module-zope.app.form python-module-zope.app.generations python-module-zope.app.http python-module-zope.app.i18n python-module-zope.app.locales python-module-zope.app.localpermission python-module-zope.app.pagetemplate python-module-zope.app.principalannotation python-module-zope.app.publication python-module-zope.app.publisher python-module-zope.app.renderer python-module-zope.app.rotterdam python-module-zope.app.schema python-module-zope.app.security python-module-zope.app.testing python-module-zope.app.wsgi python-module-zope.app.zcmlfiles python-module-zope.app.zopeappgenerations python-module-zope.applicationcontrol python-module-zope.authentication python-module-zope.broken python-module-zope.browser python-module-zope.browsermenu python-module-zope.browserpage python-module-zope.browserresource python-module-zope.cachedescriptors python-module-zope.component python-module-zope.componentvocabulary python-module-zope.configuration python-module-zope.container python-module-zope.contenttype python-module-zope.copy python-module-zope.copypastemove python-module-zope.datetime python-module-zope.deprecation python-module-zope.dottedname python-module-zope.dublincore python-module-zope.error python-module-zope.event python-module-zope.exceptions python-module-zope.filerepresentation python-module-zope.formlib python-module-zope.generations python-module-zope.hookable python-module-zope.i18n python-module-zope.i18nmessageid python-module-zope.interface python-module-zope.lifecycleevent python-module-zope.location python-module-zope.login python-module-zope.minmax python-module-zope.pagetemplate python-module-zope.password python-module-zope.pluggableauth python-module-zope.principalannotation python-module-zope.principalregistry python-module-zope.processlifetime python-module-zope.proxy python-module-zope.ptresource python-module-zope.publisher python-module-zope.schema python-module-zope.security python-module-zope.securitypolicy python-module-zope.session python-module-zope.site python-module-zope.size python-module-zope.structuredtext python-module-zope.tal python-module-zope.tales python-module-zope.testbrowser python-module-zope.testing python-module-zope.traversing python-module-zope.untrustedpython python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base python3-module-BTrees python3-module-Pygments python3-module-ZEO python3-module-ZODB python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-html5lib python3-module-jinja2 python3-module-paste python3-module-persistent python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-transaction python3-module-waitress python3-module-webtest python3-module-wsgiproxy python3-module-zc.lockfile python3-module-zdaemon python3-module-zope python3-module-zope.annotation python3-module-zope.app.applicationcontrol python3-module-zope.app.appsetup python3-module-zope.app.authentication python3-module-zope.app.basicskin python3-module-zope.app.broken python3-module-zope.app.component python3-module-zope.app.container python3-module-zope.app.content python3-module-zope.app.debug python3-module-zope.app.dependable python3-module-zope.app.error python3-module-zope.app.exception python3-module-zope.app.folder python3-module-zope.app.form python3-module-zope.app.generations python3-module-zope.app.http python3-module-zope.app.i18n python3-module-zope.app.locales python3-module-zope.app.localpermission python3-module-zope.app.pagetemplate python3-module-zope.app.principalannotation python3-module-zope.app.publication python3-module-zope.app.publisher python3-module-zope.app.renderer python3-module-zope.app.rotterdam python3-module-zope.app.schema python3-module-zope.app.security python3-module-zope.app.testing python3-module-zope.app.wsgi python3-module-zope.app.zcmlfiles python3-module-zope.app.zopeappgenerations python3-module-zope.applicationcontrol python3-module-zope.authentication python3-module-zope.broken python3-module-zope.browser python3-module-zope.browsermenu python3-module-zope.browserpage python3-module-zope.browserresource python3-module-zope.cachedescriptors python3-module-zope.component python3-module-zope.componentvocabulary python3-module-zope.configuration python3-module-zope.container python3-module-zope.contenttype python3-module-zope.copy python3-module-zope.copypastemove python3-module-zope.datetime python3-module-zope.deprecation python3-module-zope.dottedname python3-module-zope.dublincore python3-module-zope.error python3-module-zope.event python3-module-zope.exceptions python3-module-zope.filerepresentation python3-module-zope.formlib python3-module-zope.generations python3-module-zope.i18n python3-module-zope.i18nmessageid python3-module-zope.interface python3-module-zope.lifecycleevent python3-module-zope.location python3-module-zope.login python3-module-zope.minmax python3-module-zope.pagetemplate python3-module-zope.password python3-module-zope.pluggableauth python3-module-zope.principalannotation python3-module-zope.principalregistry python3-module-zope.processlifetime python3-module-zope.proxy python3-module-zope.ptresource python3-module-zope.publisher python3-module-zope.schema python3-module-zope.security python3-module-zope.securitypolicy python3-module-zope.session python3-module-zope.site python3-module-zope.size python3-module-zope.structuredtext python3-module-zope.tal python3-module-zope.tales python3-module-zope.testbrowser python3-module-zope.testing python3-module-zope.traversing
BuildRequires: python-module-nose python-module-setuptools-tests python-module-z3c.testsetup python3-module-nose python3-module-setuptools-tests python3-module-sphinx python3-module-z3c.testsetup rpm-build-python3 time

%description
zest.releaser is collection of command-line programs to help you
automate the task of releasing a Python project.

%package -n python3-module-%oname
Summary: Software releasing made easy and repeatable
Group: Development/Python3
Requires: python3-module-zest = %EVR

%description -n python3-module-%oname
zest.releaser is collection of command-line programs to help you
automate the task of releasing a Python project.

%package -n python3-module-%oname-tests
Summary: Tests for zest.releaser
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires z3c.testsetup

%description -n python3-module-%oname-tests
zest.releaser is collection of command-line programs to help you
automate the task of releasing a Python project.

This package contains tests for zest.releaser.

%package tests
Summary: Tests for zest.releaser
Group: Development/Python
Requires: %name = %EVR
%py_requires z3c.testsetup

%description tests
zest.releaser is collection of command-line programs to help you
automate the task of releasing a Python project.

This package contains tests for zest.releaser.

%package -n python-module-zest
Summary: Core package of zest
Group: Development/Python

%description -n python-module-zest
This package contains core package of zest.

%package -n python3-module-zest
Summary: Core package of zest
Group: Development/Python3

%description -n python3-module-zest
This package contains core package of zest.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

touch %buildroot%python_sitelibdir/zest/__init__.py
%if_with python3
touch %buildroot%python3_sitelibdir/zest/__init__.py
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%doc doc/source/*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/zest/__init__.py*

%files tests
%python_sitelibdir/*/*/tests

%files -n python-module-zest
%dir %python_sitelibdir/zest
%python_sitelibdir/zest/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%doc doc/source/*
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/zest/__init__.py
%exclude %python3_sitelibdir/zest/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests

%files -n python3-module-zest
%dir %python3_sitelibdir/zest
%python3_sitelibdir/zest/__init__.py
%dir %python3_sitelibdir/zest/__pycache__
%python3_sitelibdir/zest/__pycache__/__init__.*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.55-alt1.dev0.git20141229.1
- NMU: Use buildreq for BR.

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.55-alt1.dev0.git20141229
- Version 3.55.dev0

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.54-alt1.dev0.git20141121
- New snapshot

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.54-alt1.dev0.git20141110
- Version 3.54.dev0

* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.53-alt1.dev0.git20140717
- Version 3.53.dev0

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.50-alt1
- Version 3.50
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.48-alt1
- Version 3.48

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.46-alt1
- Version 3.46

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.44-alt1
- Initial build for Sisyphus


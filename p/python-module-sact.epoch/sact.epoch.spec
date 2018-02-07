# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1.1.1
%define mname sact
%define oname %mname.epoch

%def_with python3

Name: python-module-%oname
Version: 1.3.0
#Release: alt1.1.1
Summary: Time object subclassing datetime allowing diverting local clock mecanism
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sact.epoch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-dateutil python-module-zope.interface
#BuildPreReq: python-module-zope.component python-module-pytz
#BuildPreReq: python-module-zope.testing python-module-zope.testrunner
#BuildPreReq: python-module-z3c.testsetup python-module-nose
#BuildPreReq: python-module-coverage
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-dateutil python3-module-zope.interface
#BuildPreReq: python3-module-zope.component python3-module-pytz
#BuildPreReq: python3-module-zope.testing python3-module-zope.testrunner
#BuildPreReq: python3-module-z3c.testsetup python3-module-nose
#BuildPreReq: python3-module-coverage
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires dateutil zope.interface zope.component pytz

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-BTrees python-module-PyStemmer python-module-Pygments python-module-WSGIProxy2 python-module-ZEO python-module-ZODB python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-dns python-module-docutils python-module-enum34 python-module-genshi python-module-greenlet python-module-html5lib python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mimeparse python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pbr python-module-persistent python-module-psycopg2 python-module-pyasn1 python-module-pytest python-module-pytz python-module-restkit python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-transaction python-module-twisted-core python-module-unittest2 python-module-waitress python-module-webtest python-module-zc.lockfile python-module-zdaemon python-module-zope python-module-zope.annotation python-module-zope.app.applicationcontrol python-module-zope.app.appsetup python-module-zope.app.authentication python-module-zope.app.basicskin python-module-zope.app.broken python-module-zope.app.component python-module-zope.app.container python-module-zope.app.content python-module-zope.app.debug python-module-zope.app.dependable python-module-zope.app.error python-module-zope.app.exception python-module-zope.app.folder python-module-zope.app.form python-module-zope.app.generations python-module-zope.app.http python-module-zope.app.i18n python-module-zope.app.locales python-module-zope.app.localpermission python-module-zope.app.pagetemplate python-module-zope.app.principalannotation python-module-zope.app.publication python-module-zope.app.publisher python-module-zope.app.renderer python-module-zope.app.rotterdam python-module-zope.app.schema python-module-zope.app.security python-module-zope.app.testing python-module-zope.app.wsgi python-module-zope.app.zcmlfiles python-module-zope.app.zopeappgenerations python-module-zope.applicationcontrol python-module-zope.authentication python-module-zope.broken python-module-zope.browser python-module-zope.browsermenu python-module-zope.browserpage python-module-zope.browserresource python-module-zope.cachedescriptors python-module-zope.component python-module-zope.componentvocabulary python-module-zope.configuration python-module-zope.container python-module-zope.contenttype python-module-zope.copy python-module-zope.copypastemove python-module-zope.datetime python-module-zope.deprecation python-module-zope.dottedname python-module-zope.dublincore python-module-zope.error python-module-zope.event python-module-zope.exceptions python-module-zope.filerepresentation python-module-zope.formlib python-module-zope.generations python-module-zope.hookable python-module-zope.i18n python-module-zope.i18nmessageid python-module-zope.interface python-module-zope.lifecycleevent python-module-zope.location python-module-zope.login python-module-zope.minmax python-module-zope.pagetemplate python-module-zope.password python-module-zope.pluggableauth python-module-zope.principalannotation python-module-zope.principalregistry python-module-zope.processlifetime python-module-zope.proxy python-module-zope.ptresource python-module-zope.publisher python-module-zope.schema python-module-zope.security python-module-zope.securitypolicy python-module-zope.session python-module-zope.site python-module-zope.size python-module-zope.structuredtext python-module-zope.tal python-module-zope.tales python-module-zope.testbrowser python-module-zope.testing python-module-zope.traversing python-module-zope.untrustedpython python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-module-BTrees python3-module-Pygments python3-module-ZEO python3-module-ZODB python3-module-babel python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-genshi python3-module-html5lib python3-module-jinja2 python3-module-mimeparse python3-module-ntlm python3-module-paste python3-module-pbr python3-module-persistent python3-module-pip python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-transaction python3-module-unittest2 python3-module-waitress python3-module-webtest python3-module-wsgiproxy python3-module-zc.lockfile python3-module-zdaemon python3-module-zope python3-module-zope.annotation python3-module-zope.app.applicationcontrol python3-module-zope.app.appsetup python3-module-zope.app.authentication python3-module-zope.app.basicskin python3-module-zope.app.broken python3-module-zope.app.component python3-module-zope.app.container python3-module-zope.app.content python3-module-zope.app.debug python3-module-zope.app.dependable python3-module-zope.app.error python3-module-zope.app.exception python3-module-zope.app.folder python3-module-zope.app.form python3-module-zope.app.generations python3-module-zope.app.http python3-module-zope.app.i18n python3-module-zope.app.locales python3-module-zope.app.localpermission python3-module-zope.app.pagetemplate python3-module-zope.app.principalannotation python3-module-zope.app.publication python3-module-zope.app.publisher python3-module-zope.app.renderer python3-module-zope.app.rotterdam python3-module-zope.app.schema python3-module-zope.app.security python3-module-zope.app.testing python3-module-zope.app.wsgi python3-module-zope.app.zcmlfiles python3-module-zope.app.zopeappgenerations python3-module-zope.applicationcontrol python3-module-zope.authentication python3-module-zope.broken python3-module-zope.browser python3-module-zope.browsermenu python3-module-zope.browserpage python3-module-zope.browserresource python3-module-zope.cachedescriptors python3-module-zope.component python3-module-zope.componentvocabulary python3-module-zope.configuration python3-module-zope.container python3-module-zope.contenttype python3-module-zope.copy python3-module-zope.copypastemove python3-module-zope.datetime python3-module-zope.deprecation python3-module-zope.dottedname python3-module-zope.dublincore python3-module-zope.error python3-module-zope.event python3-module-zope.exceptions python3-module-zope.filerepresentation python3-module-zope.formlib python3-module-zope.generations python3-module-zope.i18n python3-module-zope.i18nmessageid python3-module-zope.interface python3-module-zope.lifecycleevent python3-module-zope.location python3-module-zope.login python3-module-zope.minmax python3-module-zope.pagetemplate python3-module-zope.password python3-module-zope.pluggableauth python3-module-zope.principalannotation python3-module-zope.principalregistry python3-module-zope.processlifetime python3-module-zope.proxy python3-module-zope.ptresource python3-module-zope.publisher python3-module-zope.schema python3-module-zope.security python3-module-zope.securitypolicy python3-module-zope.session python3-module-zope.site python3-module-zope.size python3-module-zope.structuredtext python3-module-zope.tal python3-module-zope.tales python3-module-zope.testbrowser python3-module-zope.testing python3-module-zope.traversing xz
BuildRequires: python-module-alabaster python-module-coverage python-module-dateutil python-module-nose python-module-objects.inv python-module-setuptools python-module-z3c.testsetup python-module-zope.testrunner python3-module-coverage python3-module-dateutil python3-module-nose python3-module-setuptools python3-module-sphinx python3-module-z3c.testsetup python3-module-zope.testrunner rpm-build-python3 time

%description
This packages provides a time abstraction mecanism, allowing code that
would use it as reference to be diverted both on the local time zone and
the real time.

This allows clock-dependent code to be tested. Additionnaly, as an
abstraction of the legacy datetime object, Time object provided in
sact.epoch.Time provides some common helpers and force this object to
always provide a timezone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.testrunner z3c.testsetup

%description tests
This packages provides a time abstraction mecanism, allowing code that
would use it as reference to be diverted both on the local time zone and
the real time.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Time object subclassing datetime allowing diverting local clock mecanism
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires dateutil zope.interface zope.component pytz

%description -n python3-module-%oname
This packages provides a time abstraction mecanism, allowing code that
would use it as reference to be diverted both on the local time zone and
the real time.

This allows clock-dependent code to be tested. Additionnaly, as an
abstraction of the legacy datetime object, Time object provided in
sact.epoch.Time provides some common helpers and force this object to
always provide a timezone.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.testing zope.testrunner z3c.testsetup

%description -n python3-module-%oname-tests
This packages provides a time abstraction mecanism, allowing code that
would use it as reference to be diverted both on the local time zone and
the real time.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This packages provides a time abstraction mecanism, allowing code that
would use it as reference to be diverted both on the local time zone and
the real time.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This packages provides a time abstraction mecanism, allowing code that
would use it as reference to be diverted both on the local time zone and
the real time.

This package contains documentation for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/%mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/
%if_with python3
pushd ../python3
install -p -m644 src/%mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/
popd
%endif

export PYTHONPATH=$PWD/src
pushd docs
sphinx-build -b pickle -d _build/doctrees source _build/pickle
sphinx-build -b html -d _build/doctrees source _build/html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__/__init__.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus


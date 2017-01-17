%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zope.traversing

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 4.1.0
#Release: alt2.dev0.git20150613.1.1
Summary: Resolving paths in the object hierarchy
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.traversing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zope.traversing.git
Source0: https://pypi.python.org/packages/5a/59/61da8ee69088c06fec5c2efc6163d56860856a7afb3c91903eb58aadc610/%{oname}-%{version}.tar.gz

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-%oname-tests
#BuildPreReq: python-module-nose
#BuildPreReq: python-module-zope.i18nmessageid python-module-zope.i18n
#BuildPreReq: python-module-zope.proxy 
#python-module-zope.publisher-tests
#BuildPreReq: python-module-zope.security python-module-zope.location
#BuildPreReq: python-module-six python-module-transaction
#BuildPreReq: python-module-zope.annotation
#BuildPreReq: python-module-zope.browserresource
#BuildPreReq: python-module-zope.security
#BuildPreReq: python-module-zope.tales
#BuildPreReq: python-module-zope.testing
#BuildPreReq: python-module-zope.testrunner
#BuildPreReq: python-module-zope.browser
#python-module-zope.component-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-module-%oname-tests 
#BuildPreReq: python3-module-nose
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-zope.i18nmessageid python3-module-zope.i18n
#BuildPreReq: python3-module-zope.proxy
#python3-module-zope.publisher-tests
#BuildPreReq: python3-module-zope.security python3-module-zope.location
#BuildPreReq: python3-module-six python3-module-transaction
#BuildPreReq: python3-module-zope.annotation
#BuildPreReq: python3-module-zope.browser
#BuildPreReq: python3-module-zope.browserresource
#BuildPreReq: python3-module-zope.security
#BuildPreReq: python3-module-zope.tales
#BuildPreReq: python3-module-zope.testing
#BuildPreReq: python3-module-zope.testrunner
#BuildPreReq: python3-module-zope.component-tests
%endif

#Requires: python-module-zope.i18nmessageid
#%py_requires zope.component zope.i18n zope.interface zope.proxy six
#%py_requires zope.publisher zope.security zope.location transaction

%py_requires zope.event zope.component pytz zope.schema zope.i18nmessageid zope.i18n zope.proxy zope.location zope.browser zope.configuration zope.contenttype zope.security zope.publisher zope.traversing zope.exceptions

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-BTrees python-module-ZEO python-module-ZODB python-module-cffi python-module-cryptography python-module-enum34 python-module-mimeparse python-module-numpy python-module-pbr python-module-persistent python-module-pyasn1 python-module-pytz python-module-serial python-module-setuptools python-module-transaction python-module-twisted-core python-module-unittest2 python-module-zc.lockfile python-module-zdaemon python-module-zope.component python-module-zope.configuration python-module-zope.event python-module-zope.exceptions python-module-zope.hookable python-module-zope.i18nmessageid python-module-zope.interface python-module-zope.location python-module-zope.proxy python-module-zope.schema python-module-zope.tal python-module-zope.testing python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-BTrees python3-module-ZEO python3-module-ZODB python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-persistent python3-module-pip python3-module-pycparser python3-module-pytz python3-module-setuptools python3-module-transaction python3-module-unittest2 python3-module-zc.lockfile python3-module-zdaemon python3-module-zope python3-module-zope.component python3-module-zope.configuration python3-module-zope.event python3-module-zope.exceptions python3-module-zope.i18nmessageid python3-module-zope.interface python3-module-zope.location python3-module-zope.proxy python3-module-zope.schema python3-module-zope.tal python3-module-zope.testing
BuildRequires: python-module-nose python-module-pytest python-module-zope.annotation python-module-zope.browser python-module-zope.i18n python-module-zope.security python-module-zope.tales python-module-zope.testrunner python3-module-html5lib python3-module-nose python3-module-pytest python3-module-zope.annotation python3-module-zope.browser python3-module-zope.i18n python3-module-zope.security python3-module-zope.tales python3-module-zope.testrunner rpm-build-python3

%description
The zope.traversing package provides adapteres for resolving object
paths by traversing an object hierarchy. This also includes support for
traversal namespaces (e.g. ++view++, ++skin++, etc.) as well as
computing URLs via the @@absolute_url view.

%package -n python3-module-%oname
Summary: Resolving paths in the object hierarchy
Group: Development/Python3
Requires: python3-module-zope.i18nmessageid
%py3_requires zope.component zope.i18n zope.interface zope.proxy six
%py3_requires zope.publisher zope.security zope.location transaction

%description -n python3-module-%oname
The zope.traversing package provides adapteres for resolving object
paths by traversing an object hierarchy. This also includes support for
traversal namespaces (e.g. ++view++, ++skin++, etc.) as well as
computing URLs via the @@absolute_url view.

%package -n python3-module-%oname-tests
Summary: Tests for zope.traversing
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.browser zope.configuration
%py3_requires zope.container zope.pagetemplate zope.site zope.tal
%py3_requires zope.testing ZODB3

%description -n python3-module-%oname-tests
The zope.traversing package provides adapteres for resolving object
paths by traversing an object hierarchy. This also includes support for
traversal namespaces (e.g. ++view++, ++skin++, etc.) as well as
computing URLs via the @@absolute_url view.

This package contains tests for zope.traversing.

%package tests
Summary: Tests for zope.traversing
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.browserpage zope.browser zope.configuration
%py_requires zope.container zope.pagetemplate zope.site zope.tal
%py_requires zope.testing ZODB3

%description tests
The zope.traversing package provides adapteres for resolving object
paths by traversing an object hierarchy. This also includes support for
traversal namespaces (e.g. ++view++, ++skin++, etc.) as well as
computing URLs via the @@absolute_url view.

This package contains tests for zope.traversing.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
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

%check
cd ~
export PYTHONPATH=%buildroot%python_sitelibdir
nosetests -vv %oname
#if_with python3
%if 0
export PYTHONPATH=%buildroot%python3_sitelibdir
nosetests3 -vv %oname
%endif

%files
%doc *.txt CHANGES.rst PKG-INFO README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt CHANGES.rst PKG-INFO README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1
- automated PyPI update

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt2.dev0.git20150613.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt2.dev0.git20150613.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.1-alt2.dev0.git20150613.1
- NMU: Use buildreq for BR.

* Tue Jan 19 2016 Sergey Alembekov <rt@altlinux.ru> 4.0.1-alt2.dev0.git20150613
- disable check, remove some build requires to break cyclic dependency

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev0.git20150613
- Version 4.0.1.dev0
- Enabled check

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Version 4.0.0
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a3
- Version 4.0.0a3

* Thu Dec 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14.0-alt1
- Version 3.14.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.13.2-alt4.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.2-alt4
- Added necessary requirements for tests

* Mon Jun 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.2-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.2-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.2-alt1
- Initial build for Sisyphus


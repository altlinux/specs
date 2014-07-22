%define oname grokcore.message

%def_with python3

Name: python-module-%oname
Version: 0.4.2
Release: alt3
Summary: Grok messaging machinery
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.message/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires grokcore grokcore.component z3c.flashmessage zope.component
%py_requires zope.traversing

%description
This package provides integration of z3c.flashmessage for a grok setup.
This means taking care of:

* Registering a global message receiver with the component
  architechture.
* Registering by default a global session-based message source named
  session.
* Optionally (if including ram.zcml) registering a global RAM stored
  message source named ram.
* Providing components to make use of global message receivers and
  sources.

%package -n python3-module-%oname
Summary: Grok messaging machinery
Group: Development/Python3
%py3_requires grokcore grokcore.component z3c.flashmessage zope.component
%py3_requires zope.traversing

%description -n python3-module-%oname
This package provides integration of z3c.flashmessage for a grok setup.
This means taking care of:

* Registering a global message receiver with the component
  architechture.
* Registering by default a global session-based message source named
  session.
* Optionally (if including ram.zcml) registering a global RAM stored
  message source named ram.
* Providing components to make use of global message receivers and
  sources.

%package -n python3-module-%oname-tests
Summary: Tests for grokcore.message
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.publisher zope.security zope.session

%description -n python3-module-%oname-tests
This package provides integration of z3c.flashmessage for a grok setup.
This means taking care of:

* Registering a global message receiver with the component
  architechture.
* Registering by default a global session-based message source named
  session.
* Optionally (if including ram.zcml) registering a global RAM stored
  message source named ram.
* Providing components to make use of global message receivers and
  sources.

This package contains tests for grokcore.message.

%package tests
Summary: Tests for grokcore.message
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.publisher zope.security zope.session

%description tests
This package provides integration of z3c.flashmessage for a grok setup.
This means taking care of:

* Registering a global message receiver with the component
  architechture.
* Registering by default a global session-based message source named
  session.
* Optionally (if including ram.zcml) registering a global RAM stored
  message source named ram.
* Providing components to make use of global message receivers and
  sources.

This package contains tests for grokcore.message.

%prep
%setup

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

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*test*
%python3_sitelibdir/*/*/*/*test*
%endif

%changelog
* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus


%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zc.zservertracelog

%def_with python3

Name: python-module-%oname
Version: 1.4.0
#Release: alt2.1
Summary: Zope 3 tracelog implementation for zserver
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.zservertracelog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/36/fd/a54f70a9db463f714b7f9d21f1c60178f2ebe9804914605d02732849b54a/%{oname}-%{version}.zip

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.app.appsetup zope.app.server zope.app.wsgi zope.server
%py_requires zc

%description
This package implements a Zope2-style (extended) tracelog. A tracelog is
a kind of access log that records several low-level events for each
request. Each log entry starts with a record type, a request identifier
and the time. Some log records have additional data.

%package -n python3-module-%oname
Summary: Zope 3 tracelog implementation for zserver
Group: Development/Python3
%py3_requires zope.app.appsetup zope.app.server zope.app.wsgi zope.server
%py3_requires zc

%description -n python3-module-%oname
This package implements a Zope2-style (extended) tracelog. A tracelog is
a kind of access log that records several low-level events for each
request. Each log entry starts with a record type, a request identifier
and the time. Some log records have additional data.

%package -n python3-module-%oname-tests
Summary: Tests for Zope 3 tracelog implementation for zserver
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package implements a Zope2-style (extended) tracelog. A tracelog is
a kind of access log that records several low-level events for each
request. Each log entry starts with a record type, a request identifier
and the time. Some log records have additional data.

This package contains tests for Zope 3 tracelog implementation for
zserver.

%package tests
Summary: Tests for Zope 3 tracelog implementation for zserver
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package implements a Zope2-style (extended) tracelog. A tracelog is
a kind of access log that records several low-level events for each
request. Each log entry starts with a record type, a request identifier
and the time. Some log records have additional data.

This package contains tests for Zope 3 tracelog implementation for
zserver.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc README.rst CHANGES.rst PKG-INFO COPYRIGHT.rst LICENSE.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc README.rst CHANGES.rst PKG-INFO COPYRIGHT.rst LICENSE.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.2-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt2
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1
- Version 1.3.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus


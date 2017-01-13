%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname repoze.filesafe

%def_with python3

Name: python-module-%oname
Version: 2.2
#Release: alt2.gi20140506.1
Summary: Transaction-aware file creation
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.filesafe
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.filesafe.git
Source0: https://pypi.python.org/packages/55/7a/de63694ea21de0f5e5f50d692e5cfaa6071a531af212b57bcb7de5080378/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze transaction zope.interface

%description
repoze.filesafe provides utilities methods to handle creation
of files on the filesystem safely by integrating with the ZODB package's
transaction manager.  It can be used in combination with repoze.tm (or
repoze.tm2) for use in WSGI environments.

%package -n python3-module-%oname
Summary: Transaction-aware file creation
Group: Development/Python3
%py3_requires repoze transaction zope.interface

%description -n python3-module-%oname
repoze.filesafe provides utilities methods to handle creation
of files on the filesystem safely by integrating with the ZODB package's
transaction manager.  It can be used in combination with repoze.tm (or
repoze.tm2) for use in WSGI environments.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.filesafe
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
repoze.filesafe provides utilities methods to handle creation
of files on the filesystem safely by integrating with the ZODB package's
transaction manager.  It can be used in combination with repoze.tm (or
repoze.tm2) for use in WSGI environments.

This package contains tests for repoze.filesafe.

%package tests
Summary: Tests for repoze.filesafe
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.filesafe provides utilities methods to handle creation
of files on the filesystem safely by integrating with the ZODB package's
transaction manager.  It can be used in combination with repoze.tm (or
repoze.tm2) for use in WSGI environments.

This package contains tests for repoze.filesafe.

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

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1-alt2.gi20140506.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1-alt2.gi20140506.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt2.gi20140506
- Added module for Python 3

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.gi20140506
- Version 2.1

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0b2-alt1.gi20130320
- New snapshot

* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0b2-alt1.gi20110831
- Version 2.0b2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.gi20110322.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.gi20110322.1
- Added necessary requirements
- Excluded *.pth

* Thu Jun 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.gi20110322
- Initial build for Sisyphus


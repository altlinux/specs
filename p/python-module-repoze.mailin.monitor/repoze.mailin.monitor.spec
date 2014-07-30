%define oname repoze.mailin.monitor

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt2.git20110817
Summary: WSGI app which allows users to view data about a mailin store using repoze.mailin
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.mailin.monitor
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.mailin.monitor.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze.mailin repoze.bfg webob

%description
This package provides a WSGI user interface that can be used to view data
about a mailin store using repoze.mailin.  Currently only data about the
quarantined messages is available and is intended help detect and troubleshoot
problems with mailin.

repoze.mailin.monitor is implemented as a very simple repoze.bfg application
and as such should be pretty extensible.  This will need to be extended in
order to have much of a security story.

%package -n python3-module-%oname
Summary: WSGI app which allows users to view data about a mailin store using repoze.mailin
Group: Development/Python3
%py3_requires repoze.mailin repoze.bfg webob

%description -n python3-module-%oname
This package provides a WSGI user interface that can be used to view data
about a mailin store using repoze.mailin.  Currently only data about the
quarantined messages is available and is intended help detect and troubleshoot
problems with mailin.

repoze.mailin.monitor is implemented as a very simple repoze.bfg application
and as such should be pretty extensible.  This will need to be extended in
order to have much of a security story.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.mailin.monitor
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides a WSGI user interface that can be used to view data
about a mailin store using repoze.mailin.  Currently only data about the
quarantined messages is available and is intended help detect and troubleshoot
problems with mailin.

repoze.mailin.monitor is implemented as a very simple repoze.bfg application
and as such should be pretty extensible.  This will need to be extended in
order to have much of a security story.

This package contains tests for repoze.mailin.monitor.

%package tests
Summary: Tests for repoze.mailin.monitor
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a WSGI user interface that can be used to view data
about a mailin store using repoze.mailin.  Currently only data about the
quarantined messages is available and is intended help detect and troubleshoot
problems with mailin.

repoze.mailin.monitor is implemented as a very simple repoze.bfg application
and as such should be pretty extensible.  This will need to be extended in
order to have much of a security story.

This package contains tests for repoze.mailin.monitor.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2.git20110817
- Added module for Python 3

* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20110817
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.git20110227.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20110227.1
- Added necessary requirements
- Excluded *.pth

* Sun Jun 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20110227
- Initial build for Sisyphus


%define oname repoze.mailin.monitor
Name: python-module-%oname
Version: 0.2
Release: alt1.git20110817
Summary: WSGI app which allows users to view data about a mailin store using repoze.mailin
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.mailin.monitor
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.mailin.monitor.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.mailin repoze.bfg webob

%description
This package provides a WSGI user interface that can be used to view data
about a mailin store using repoze.mailin.  Currently only data about the
quarantined messages is available and is intended help detect and troubleshoot
problems with mailin.

repoze.mailin.monitor is implemented as a very simple repoze.bfg application
and as such should be pretty extensible.  This will need to be extended in
order to have much of a security story.

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

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20110817
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.git20110227.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20110227.1
- Added necessary requirements
- Excluded *.pth

* Sun Jun 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20110227
- Initial build for Sisyphus


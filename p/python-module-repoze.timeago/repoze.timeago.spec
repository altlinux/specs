%define oname repoze.timeago
Name: python-module-%oname
Version: 0.5
Release: alt1.1
Summary: Compute human-friendly elapsed time messages
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.timeago/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze

%description
This package provides library function for rendering a human-friendly
message describing elapsed time since an event.

%package tests
Summary: Tests for repoze.timeago
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides library function for rendering a human-friendly
message describing elapsed time since an event.

This package contains tests for repoze.timeago.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus


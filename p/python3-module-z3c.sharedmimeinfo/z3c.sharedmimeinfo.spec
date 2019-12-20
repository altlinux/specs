%define oname z3c.sharedmimeinfo

Name: python3-module-%oname
Version: 0.1.0
Release: alt4

Summary: MIME type guessing framework for Zope, based on shared-mime-info
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/z3c.sharedmimeinfo/

Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
%py3_requires zope.i18n zope.i18nmessageid zope.interface zope.schema


%description
This package provides an utility for guessing MIME type from file name
and/or actual contents. It's based on freedesktop.org's shared-mime-info
database.

%package tests
Summary: Tests for z3c.sharedmimeinfo
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.component

%description tests
This package provides an utility for guessing MIME type from file name
and/or actual contents. It's based on freedesktop.org's shared-mime-info
database.

This package contains tests for z3c.sharedmimeinfo.

%prep
%setup
%patch0 -p2

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt4
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.1.0-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus


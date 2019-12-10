%define _unpackaged_files_terminate_build 1

%define oname z3c.schema

Name: python3-module-%oname
Version: 1.1.0
Release: alt2

Summary: Additional schema fields for Zope 3
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/z3c.schema/

Source0: https://pypi.python.org/packages/97/b4/e2975b847ac8471f878a1660423d3e97b77ea554aaffd9b48f59f5732188/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
%py3_requires zope.i18nmessageid zope.interface zope.schema


%description
This package provides different additional Zope 3 schema fields.

%package tests
Summary: Tests for z3c.schema
Group: Development/Python3
Requires: %name = %version-%release
%py3_requires zope.testing

%description tests
This package provides different additional Zope 3 schema fields.

This package contains tests for z3c.schema.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build

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
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt2
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1
- Initial build for Sisyphus


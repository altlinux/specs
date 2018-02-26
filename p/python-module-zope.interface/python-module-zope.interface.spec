%define version 3.8.0
#define subver c1
%define release alt2
%define oname zope.interface
%setup_python_module %oname

%def_with python3

Summary: Zope interfaces package
Name: %packagename
Version: %version
Url: http://www.python.org/pypi/zope.interface
%ifdef subver
Release: %release.%subver
Source0: zope.interface-%version%subver.tar.gz
%else
Release: %release
Source0: zope.interface-%version.tar.gz
%endif
License: ZPL
Group: Development/Python
Packager: Python Development Team <python@packages.altlinux.org>

BuildPreReq: python-module-distribute python-module-zope.fixers
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python3-module-zope.fixers
%endif

%description
This is a separate distribution of the zope.interface package used in
Zope 3, along with the packages it depends on.

%if_with python3
%package -n python3-module-%oname
Summary: Zope interfaces package (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
This is a separate distribution of the zope.interface package used in
Zope 3, along with the packages it depends on.

%package -n python3-module-%oname-tests
Summary: Tests for zope.interface (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This is a separate distribution of the zope.interface package used in
Zope 3, along with the packages it depends on.

This package contains tests for zope.interface.
%endif

%package tests
Summary: Tests for zope.interface
Group: Development/Python
Requires: %name = %version-%release

%description tests
This is a separate distribution of the zope.interface package used in
Zope 3, along with the packages it depends on.

This package contains tests for zope.interface.

%prep
%ifdef subver
%setup -n zope.interface-%version%subver
%else
%setup -n zope.interface-%version
%endif
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug build_ext
%if_with python3
pushd ../python3
%python3_build build_ext
popd
%endif

%install
%python_module_declare %python_sitelibdir/zope
%python_install --optimize=2 --record=INSTALLED_FILES
rm -fR %buildroot%python_sitelibdir/zope/__init__.py*

%if_with python3
pushd ../python3
%python3_install
popd
rm -fR %buildroot%python3_sitelibdir/zope/__init__.py*
%endif
 
%files
%python_sitelibdir/*
%exclude %python_sitelibdir/zope/interface/tests
%exclude %python_sitelibdir/zope/interface/common/tests
%ifnarch x86_64
%exclude %python_sitelibdir/zope*egg-info
%endif
%doc *.txt

%files tests
%python_sitelibdir/zope/interface/tests
%python_sitelibdir/zope/interface/common/tests

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/zope/interface/tests
%exclude %python3_sitelibdir/zope/interface/common/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/zope/interface/tests
%python3_sitelibdir/zope/interface/common/tests
%endif

%changelog
* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt2
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt1
- Version 3.8.0

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.3-alt2.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt2
- Don't pack zope*egg-info

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt1
- Version 3.6.3

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt1
- Version 3.6.2

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Set as archdep package

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt2
- Rebuilt with python 2.6

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.1.2
- Fixed file conflict with python-module-zope

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.1.1
- Fixed file conflict with python-module-zope (ALT #21981)

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 3.3.0-alt1.1
- Rebuilt with python-2.5.

* Sun Feb 18 2007 Ivan Fedorov <ns@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Mon Nov 20 2006 Ivan Fedorov <ns@altlinux.ru> 3.1.0-alt1.c1
- 3.1.0c1

* Mon Oct 03 2005 Ivan Fedorov <ns@altlinux.ru> 3.0.1-alt1
- Initial build for ALT Linux.

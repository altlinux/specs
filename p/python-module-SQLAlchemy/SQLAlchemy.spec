%define oname SQLAlchemy

%def_with python3

Name: python-module-%oname
Version: 1.0.8
Release: alt1.1

Summary: Python SQL toolkit and Object Relational Mapper
License: MIT
Group: Development/Python
Url: http://www.sqlalchemy.org/

Source: SQLAlchemy-%version.tar
%py_provides SQLAlchemy

#BuildArch: noarch
#BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-devel python3-module-setuptools rpm-build-python3

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
%endif

%description
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives
application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns,
designed for efficient and high-performing database access, adapted into a
simple and Pythonic domain language.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 SQL toolkit and Object Relational Mapper
Group: Development/Python3
%py3_provides SQLAlchemy

%description -n python3-module-%oname
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives
application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns,
designed for efficient and high-performing database access, adapted into a
simple and Pythonic domain language.

%package -n python3-module-%oname-tests
Summary: Tests for SQLAlchemy (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives
application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns,
designed for efficient and high-performing database access, adapted into a
simple and Pythonic domain language.

This package contains tests for SQLAlchemy.
%endif

%package tests
Summary: Tests for SQLAlchemy
Group: Development/Python
#BuildArch: noarch
Requires: %name = %version-%release

%description tests
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives
application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns,
designed for efficient and high-performing database access, adapted into a
simple and Pythonic domain language.

This package contains tests for SQLAlchemy.

%prep
%setup -n SQLAlchemy-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
CFLAGS="%optflags" python setup.py install --optimize=2 --root=buildroot \
	--record INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
mkdir -p %buildroot
cp -r buildroot/* %buildroot/

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES
%exclude %python_sitelibdir/*/testing

%files tests
%python_sitelibdir/*/testing

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/testing

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/testing
%endif

%changelog
* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.0.8-alt1.1
- NMU: Use buildreq for BR.

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1
- Version 1.0.8

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Version 1.0.2

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.b3
- Version 1.0.0b3

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.b1
- Version 1.0.0b1

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1
- Version 0.9.8

* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1
- Version 0.9.7

* Thu Dec 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt2
- Extracted tests into separated packages

* Wed Dec 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1
- Version 0.8.3

* Thu Mar 21 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7.10-alt1.1
- Rebuild with Python-3.3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.10-alt1
- Version 0.7.10

* Sat Sep 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.8-alt1
- Version 0.7.8

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt3
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt2
- Added provides of SQLAlchemy

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1
- Version 0.6.2 (ALT #23768)
- Moved tests into separate package

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.1
- Rebuilt with python 2.6

* Mon Feb 23 2009 Gennady Kovalev <gik@altlinux.ru> 0.5.2-alt1
- 0.5.2 release

* Sun Jan 11 2009 Gennady Kovalev <gik@altlinux.ru> 0.5.0-alt1
- 0.5.0 release

* Mon Jan 05 2009 Gennady Kovalev <gik@altlinux.ru> 0.5.0rc4-alt1
- 0.5.0rc4

* Sun Oct 12 2008 Gennady Kovalev <gik@altlinux.ru> 0.5.0rc1-alt1
- 0.5.0rc1

* Fri Aug 01 2008 Gennady Kovalev <gik@altlinux.ru> 0.4.7p1-alt1
- 0.4.7p1 release 

* Sun May 04 2008 Gennady Kovalev <gik@altlinux.ru> 0.4.5-alt1
- 0.4.5 release

* Wed Jan 09 2008 Gennady Kovalev <gik@altlinux.ru> 0.4.2b-alt1
- 0.4.2b release

* Mon Jan 07 2008 Gennady Kovalev <gik@altlinux.ru> 0.4.2a-alt1
- 0.4.2a release

* Wed Jan 02 2008 Gennady Kovalev <gik@altlinux.ru> 0.4.2-alt1
- 0.4.2 release

* Sat Jan 2 2008 Gennady Kovalev <gik@altlinux.ru> 0.4.1-alt1
- 0.4.1 release

* Thu Nov 15 2007 Gennady Kovalev <gik@altlinux.ru> 0.4.0-alt1
- 0.4 release

* Sun Jun 18 2006 Alex V. Myltsev <avm@altlinux.ru> 0.2.3-alt1
- Initial build for Sisyphus.


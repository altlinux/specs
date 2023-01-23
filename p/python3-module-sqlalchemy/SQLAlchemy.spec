Name: python3-module-sqlalchemy
Version: 1.4.44
Release: alt1

Summary: Python SQL toolkit and Object Relational Mapper
License: MIT
Group: Development/Python3
Url: http://www.sqlalchemy.org/

Source: SQLAlchemy-%version.tar

Provides: python3-module-SQLAlchemy = %EVR
Obsoletes: python3-module-SQLAlchemy

%py3_provides SQLAlchemy

BuildRequires: rpm-build-python3 python3-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

# Make sure that at least the Python built-in sqlite driver
# is present (and can be used by SQLAlchemy--among other things--
# in various tests, like in the tests for sphinx).
Requires: python3-modules-sqlite3

%description
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives
application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns,
designed for efficient and high-performing database access, adapted into a
simple and Pythonic domain language.

%package tests
Summary: Tests for SQLAlchemy (Python 3)
Group: Development/Python3
Requires: %name = %EVR

%description tests
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives
application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns,
designed for efficient and high-performing database access, adapted into a
simple and Pythonic domain language.

This package contains tests for SQLAlchemy.

%prep
%setup -n SQLAlchemy-%version

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/testing

%files tests
%python3_sitelibdir/*/testing

%changelog
* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.44-alt1
- 1.4.44 released

* Mon Nov  7 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.43-alt1
- 1.4.43 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.40-alt1
- 1.4.40 released

* Fri Jul 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.39-alt1
- 1.4.39

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.36-alt1
- 1.4.36

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.31-alt1
- 1.4.31

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.25-alt1
- 1.4.25

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.22-alt1
- 1.4.22 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.13-alt1
- 1.4.13

* Fri Feb 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.23-alt1
- 1.3.23

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.3.20-alt2
- build python3 package separately

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.20-alt1
- 1.3.20

* Mon Sep 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.19-alt1
- 1.3.19

* Tue Jul 07 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.18-alt1
- 1.3.18

* Mon Sep 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.8-alt1
- Version updated to 1.3.8

* Thu Jan 10 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.15-alt1
- 1.2.15

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.12-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.12-alt1
- 1.0.12

* Fri Apr 15 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.8-alt2
- Make sure that at least the Python built-in sqlite driver is present
  (and can be used by SQLAlchemy whenever SQLAlchemy is installed;
  among other things, it's useful for tests, like in sphinx).

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.8-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

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

* Thu Nov 15 2007 Gennady Kovalev <gik@altlinux.ru> 0.4.0-alt1
- 0.4 release

* Sun Jun 18 2006 Alex V. Myltsev <avm@altlinux.ru> 0.2.3-alt1
- Initial build for Sisyphus.


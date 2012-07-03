%define oname psycopg2
%def_with python3

Version: 2.4.5
Release: alt1.git20120328
%setup_python_module %oname

Summary: psycopg2 is a PostgreSQL database adapter for Python
Name: %packagename
# git://dndg.it/public/psycopg2.git
Source0: psycopg2.tar
License: GPL
Group: Development/Python
URL: http://www.initd.org/software/psycopg/
BuildRequires: postgresql-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python-tools-2to3
%endif
Packager: Python Development Team <python@packages.altlinux.org>

%description
psycopg is a PostgreSQL database adapter for the Python programming
language (just like pygresql and popy.) It was written from scratch with
the aim of being very small and fast, and stable as a rock. The main
advantages of psycopg are that it supports the full Python DBAPI-2.0 and
being thread safe at level 2.

%if_with python3
%package -n python3-module-%oname
Summary: psycopg2 is a PostgreSQL database adapter for Python 3
Group: Development/Python3

%description -n python3-module-%oname
psycopg is a PostgreSQL database adapter for the Python 3 programming
language (just like pygresql and popy.) It was written from scratch with
the aim of being very small and fast, and stable as a rock. The main
advantages of psycopg are that it supports the full Python DBAPI-2.0 and
being thread safe at level 2.

%package -n python3-module-%oname-tests
Summary: Tests for psycopg2 python 3 PostgreSQL database adapter
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Tests for the psycopg2 python 3 PostgreSQL database adapter.

%package -n python3-module-psycopg2da
Summary: PostgreSQL Database Adapter for Zope 3
Group: Development/Python3

%description -n python3-module-psycopg2da
PostgreSQL Database Adapter for Zope 3
%endif

%package tests
Summary: Tests for psycopg2 python PostgreSQL database adapter
Group: Development/Python
Requires: %name = %version-%release

%description tests
Tests for the psycopg2 python PostgreSQL database adapter.

%package doc
Summary: Documentation for psycopg2 python PostgreSQL database adapter
Group: Development/Python
BuildArch: noarch

%description doc
Documenation and example files for the psycopg2 python PostgreSQL
database adapter.

%package -n python-module-psycopg2da
Summary: PostgreSQL Database Adapter for Zope 3
Group: Development/Python

%description -n python-module-psycopg2da
PostgreSQL Database Adapter for Zope 3

%prep
%setup

echo "include_dirs=.:/usr/include/pgsql" >> setup.cfg

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w $i
done
%python3_build
popd
%endif

%install
mkdir -p %buildroot/%python_sitelibdir/psycopg2da/
%python_install --optimize=2 --record=INSTALLED_FILES
%if_with python3
pushd ../python3
mkdir -p %buildroot/%python3_sitelibdir/psycopg2da/
%python3_install
sed -i 's|_psycopg|%oname._psycopg|' \
	%buildroot%python3_sitelibdir/%oname/psycopg1.py
install -m644 psycopg2da/__init__.py %buildroot/%python3_sitelibdir/psycopg2da/
install -m644 psycopg2da/adapter.py %buildroot/%python3_sitelibdir/psycopg2da/
install -m644 psycopg2da/*.zcml %buildroot/%python3_sitelibdir/psycopg2da/
popd
%endif

install -m644 psycopg2da/__init__.py %buildroot/%python_sitelibdir/psycopg2da/
install -m644 psycopg2da/adapter.py %buildroot/%python_sitelibdir/psycopg2da/
install -m644 psycopg2da/*.zcml %buildroot/%python_sitelibdir/psycopg2da/

%files -f INSTALLED_FILES
%dir %python_sitelibdir/psycopg2
%exclude %python_sitelibdir/psycopg2/tests

%files tests
%python_sitelibdir/psycopg2/tests

%files doc
%doc AUTHORS INSTALL README doc examples

%files -n python-module-psycopg2da
%dir %python_sitelibdir/psycopg2da
%python_sitelibdir/psycopg2da/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/psycopg2da
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files -n python3-module-psycopg2da
%python3_sitelibdir/psycopg2da
%endif

%changelog
* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.5-alt1.git20120328
- Version 2.4.5
- Added module for Python 3

* Mon Jan 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.4-alt1.git20111219
- Version 2.4.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.1-alt2.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt2
- Rebuilt for debuginfo

* Wed Dec 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1
- Version 2.3.1 (ALT #24712)
- Extracted tests into separate package

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt3
- Fixed underlinking

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt2
- Set docs package as noarch

* Fri Jul 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1
- Version 2.2.2

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.8-alt1.1
- Rebuilt with python 2.6

* Sat Nov 01 2008 Ivan Fedorov <ns@altlinux.org> 2.0.8-alt1
- new version

* Thu Jan 03 2008 Ivan Fedorov <ns@altlinux.org> 2.0.6-alt3
- fix building

* Sun Jul 15 2007 Ivan Fedorov <ns@altlinux.org> 2.0.6-alt2
- 2.0.6
- fixed bug in type casting. (uninitialized pointer)

* Wed Mar 21 2007 Ivan Fedorov <ns@altlinux.ru> 2.0.6-alt1.svn876
- rebuild with libpq5 from postgresql8.2
- update to svn

* Sat Mar 03 2007 Ivan Fedorov <ns@altlinux.ru> 2.0.6-alt1.b1
- 2.0.6b1

* Sun Feb 18 2007 Ivan Fedorov <ns@altlinux.ru> 2.0.5.1-alt1
- 2.0.5.1

* Sat Jul 01 2006 Ivan Fedorov <ns@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Sun Feb 12 2006 Ivan Fedorov <ns@altlinux.ru> 2.0-alt0.b8
- 2.0b8

* Wed Feb 01 2006 Ivan Fedorov <ns@altlinux.ru> 2.0-alt0.b6
- 2.0b6

* Thu Nov 10 2005 Ivan Fedorov <ns@altlinux.ru> 2.0-alt0.b5
- 2.0b5

* Mon Oct 03 2005 Ivan Fedorov <ns@altlinux.ru> 2.0-alt0.b4
- switch to 2.0 branch
- 2.0b4

* Tue Jan 11 2005 Andrey Orlov <cray@altlinux.ru> 1.1.18-alt1
- New Version

* Fri Jul 02 2004 Andrey Orlov <cray@altlinux.ru> 1.1.11-alt9
- Requires for egenix-mx-base added;

* Wed May 19 2004 Andrey Orlov <cray@altlinux.ru> 1.1.11-alt8
- Obsoleting of previous packages added

* Tue May 18 2004 Andrey Orlov <cray@altlinux.ru> 1.1.11-alt7
- Conditional operators excluded from spec

* Mon May 10 2004 Andrey Orlov <cray@altlinux.ru> 1.1.11-alt6.d
- Fix egenix-mx-base dependence

* Thu Apr 22 2004 Andrey Orlov <cray@altlinux.ru> 1.1.11-alt5.d
- Remove BuildArchitecture: noarch clause

* Tue Apr 13 2004 Andrey Orlov <cray@altlinux.ru> 1.1.11-alt4.d
- Rebuild with new rpm/python macros
- Insert BuildArchitecture: noarch clause

* Fri Mar 26 2004 Andrey Orlov <cray@altlinux.ru> 1.1.11-alt3.d
- New version
- Fix new python policy compatibility

* Wed Dec 10 2003 Andrey Orlov <cray@altlinux.ru> 1.1.9-alt4
- Fix permissions
- Try eliminate libpq2
- Try to use with py23

* Sun Sep 14 2003 Andrey Orlov <cray@altlinux.ru> 1.1.9-alt1
- New release

* Sat Dec 14 2002 Andrey Orlov <cray@altlinux.ru> 1.0.12-alt3
- Declaration of requirements are enhanced

* Mon Dec 02 2002 Andrey Orlov <cray@altlinux.ru> 1.0.12-alt2
- Logging of all queries in debug mode (STUPID_LOG_SEVERITY=DEBUG) was added

* Tue Oct 29 2002 Andrey Orlov <cray@altlinux.ru> 1.0.12-alt1
- Recompile with gcc 3.2.1

* Fri Sep 13 2002 Federico Di Gregorio  <fog@debian.org>
- Release 1.0.12.

- Removed code to support COPY FROM/TO, will be added to new 1.1
  branch to be released next week.

- cursor.c (_mogrify_seq): Fixed memory leak reported by Menno
  Smits (values obtained by calling PySequence_GetItem are *new*
  references!)

* Sun Sep  9 2002 Federico Di Gregorio  <fog@debian.org>

- cursor.c (_psyco_curs_execute): Added skeleton to support COPY
  FROM/TO.

* Fri Sep  6 2002  Federico Di Gregorio  <fog@debian.org>

- configure.in: if libcrypt can't be found we probably are on
  MacOS X: check for libcrypto, as suggested by Aparajita Fishman.

* Tue Sep 3 2002 Federico Di Gregorio  <fog@debian.org>

- ZPsycopgDA/db.py (DB.columns): Applied patch from Dieter Maurer
  to allow the DA-browser to work with mixed case table names.

* Fri Aug 30 2002 Federico Di Gregorio  <fog@debian.org>

- ZPsycopgDA/DA.py (cast_DateTime): Applied patch from Yury to fix
  timestamps (before they were returned with time always set to 0.)

* Mon Aug 26 2002  Federico Di Gregorio  <fog@debian.org>

- Release 1.0.11.1 (to fix a %%&£$"! bug in ZPsycopgDA not
   accepting psycopg 1.0.11 as a valid version.

- Release 1.0.11.

* Thu Aug 22 2002  Federico Di Gregorio  <fog@debian.org>

- Release 1.0.11pre2.

- cursor.c (_psyco_curs_execute): fixed IntegrityError as reported
  by Andy Dustman. (psyco_curs_execute): converting TypeError to
  ProgrammingError on wrong number of %% and/or aeguments.

- doc/examples/integrity.py: added example and check for
  IntegrityError.

* Thu Aug  08 2002  Federico Di Gregorio  <fog@debian.org>

- Release 1.0.11pre1.

* Tue Aug 06 2002  Federico Di Gregorio  <fog@debian.org>

- ZPsycopgDA/DA.py (cast_DateTime): patched as suggested by Tom
  Jenkins; now it shouldwork with time zones too.

* Thu Aug 01 2002  Federico Di Gregorio  <fog@debian.org>

- ZPsycopgDA/DA.py (cast_DateTime): fixed problem with missing
  AM/PM, as reported by Tom Jenkins.

* Tue Jul  23 2002  Federico Di Gregorio  <fog@debian.org>

- Fixed buglets reported by Mike Coleman.

* Mon Jul  22 2002  Federico Di Gregorio  <fog@debian.org>

- Release 1.0.10.

* Sat Jul  14 2002  Federico Di Gregorio  <fog@debian.org>

- Release 1.0.10pre2.

- typeobj.c (psyco_LONGINTEGER_cast): fixed bad segfault by
  INCREFfing Py_None when it is the result of a NULL conversion.

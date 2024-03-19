%define        _unpackaged_files_terminate_build 1
%define        pypiname psycopg
%define        modname psycopg
%define        distname psycopg
%def_disable   doc

Name:          python3-module-%pypiname
Version:       3.1.10
Release:       alt1.1
Summary:       psycopg is a PostgreSQL database adapter for Python
License:       LGPL-3.0
Group:         Development/Python3
Url:           https://www.psycopg.org/psycopg3/
Vcs:           https://github.com/psycopg/psycopg.git
Packager:      Python Development Team <python@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-python3
BuildRequires: postgresql-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
%if_enabled doc
BuildRequires: python3(typing_extensions)
BuildRequires: python3(sphinx_autodoc_typehints)
BuildRequires: python3(furo)
BuildRequires: python3-module-sphinx-sphinx-build-symlink
%endif
Obsoletes:     psycopg <= 1.1.9-alt4

%description
psycopg is a PostgreSQL database adapter for the Python programming
language (just like pygresql and popy.) It was written from scratch with
the aim of being very small and fast, and stable as a rock. The main
advantages of psycopg are that it supports the full Python DBAPI-2.0 and
being thread safe at level 2.

Psycopg 3 design emerges from the experience of more than 10 years of
development and support of psycopg2. It embraces the new possibilities offered
by the more modern generations of the Python language and the PostgreSQL
database and addresses the challenges offered by the current patterns in
software development and deployment.


%package       doc
Summary:       Documentation for psycopg python PostgreSQL database adapter
Group:         Development/Documentation

%description   doc
Documenation and example files for the psycopg python PostgreSQL
database adapter.


%prep
%setup

%build
pushd psycopg
%pyproject_build
popd
export PYTHONPATH=$(pwd)/psycopg
%{?!_disable_doc:%make -C docs html SPHINXBUILD=sphinx-build-3}

%install
pushd psycopg
%pyproject_install
popd

%files
%doc *.rst
%{?!_disable_doc:%doc docs/build/html/*}
%python3_sitelibdir/%{distname}
%python3_sitelibdir/%{modname}*/METADATA


%files         doc
%doc *.rst docs


%changelog
* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 3.1.10-alt1.1
- NMU: added missing build dependency on setuptools.

* Tue Aug 15 2023 Pavel Skrylev <majioa@altlinux.org> 3.1.10-alt1
- * renamed to python3-module-psycopg, and restored in Sisyphus
- ^ 1.1.21 -> 3.1.10

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.21-alt3.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.21-alt3
- Rebuilt for debuginfo

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.21-alt2.1.1
- Rebuilt with python 2.6

* Mon Jan 28 2008 Grigory Batalov <bga@altlinux.ru> 1.1.21-alt2.1
- Rebuilt with python-2.5.

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.1.21-alt2
- Use __python_version macro while building.

* Mon Apr 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.1.21-alt1.1
- Fixed python-module-psycopg x86-64 packaging (#11655).
- Disabled python-module-psycopg-ZPsycopgDA packaging.

* Fri Mar 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.1.21-alt1.0
- Rebuilt due to libpq.so.4 -> libpq.so.5 soname change.

* Mon Oct 03 2005 Ivan Fedorov <ns@altlinux.ru> 1.1.21-alt1
- 1.1.21

* Fri Aug 12 2005 Ivan Fedorov <ns@altlinux.ru> 1.1.19-alt1
- 1.1.19

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


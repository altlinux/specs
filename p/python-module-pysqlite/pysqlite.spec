%define version 1.0
%define release alt3

%setup_python_module pysqlite

Name: %packagename
Version: %version
Release: %release.1
Summary: Python interface to SQLite
License: LICENSE
Group: Development/Python
Url: http://pysqlite.org
Packager: Konstantin Klimchev <koka@altlinux.ru>

Source: %modulename-%version.tar.gz

Requires: sqlite
BuildRequires: sqlite-devel
Obsoletes: python-sqlite
%py_provides pysqlite

%description
Pysqlite is an interface to the SQLite database server for Python.
It aims to be fully compliant with Python database API version 2.0
while also exploiting the unique features of SQLite.

%prep
%setup -n %modulename

%build
%python_build_debug

%install
%python_build_install \
	--optimize=2 \
	--record=INSTALLED_FILES

chmod -x doc/rest/manual.txt

%files -f INSTALLED_FILES
%doc README LICENSE doc/rest/manual.txt
%doc test examples misc

%changelog
* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt3.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Added %%py_provides pysqlite

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Rebuilt for debuginfo

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1.1.1.0.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.0-alt1.1.1.0.1
- Rebuilt with python-2.5.

* Sun Jul 29 2007 Slava Semushin <php-coder@altlinux.ru> 1.0-alt1.1.1.0
- NMU
- Fixed Url tag (#7596)
- Spec cleanup:
  + s/Source0/Source/
  + s/Copyright/License/
  + Set Packager tag to previous maintainer
  + Removed trailing space in %%description
  + s/%%setup -q/%%setup/
  + s/$RPM_OPT_FLAGS/%%optflags/
  + s/%%__chmod/chmod
  + Don't try remove executed bit from files without this bit
  + Removed unneded %%defattr(-,root,root) from %%files section
  + More strict names in %%files section

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-alt1.1.0
- Automated rebuild.

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-alt1.1
- Rebuilt with python-2.4.

* Tue Nov 23 2004 Konstantin Klimchev <koka@altlinux.ru> 1.0-alt1
- new 1.0

* Fri May 21 2004 Konstantin Klimchev <koka@altlinux.ru> 0.5.0-alt2
- new python policy

* Wed Mar 31 2004 Konstantin Klimchev <koka@altlinux.ru> 0.5.0-alt1
- Initial build for Sisyphus

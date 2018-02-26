Name: emdros
Version: 3.1.1
Release: alt1.2

Summary: The database engine for analyzed or annotated text
License: GPL
Group: Databases

Packager: Kirill Maslinsky <kirill@altlinux.org>
URL: http://emdros.org
Source: emdros-%version.tar
Patch0: emdros-%version-alt-locallib.patch
Patch1: emdros-3.1.1-alt-python.patch

BuildRequires(pre): rpm-build-python
# Automatically added by buildreq on Wed Sep 24 2008 (-bi)
BuildRequires: gcc-c++ libMySQL-devel libpango-devel libpcre-devel libsqlite3-devel postgresql-devel python-devel wxGTK-devel zlib-devel
# not added automatically by buildreq
BuildRequires: swig

Requires: lib%name = %version-%release, %name-gui = %version-%release, %name-utils = %version-%release, %name-doc = %version-%release

%description
Emdros is a text database engine for storage and retrieval of annotated
or analyzed text. Application domains include linguistics, publishing,
and text processing. Emdros has a powerful query-language for
query/create/update/delete operations.

%package -n lib%name
Summary: The database engine for analyzed or annotated text: shared libraries
Group: Databases

%description -n lib%name
Emdros is a text database engine for storage and retrieval of annotated
or analyzed text. Application domains include linguistics, publishing,
and text processing. Emdros has a powerful query-language for
query/create/update/delete operations.

This package contains shared librares used by emdros tools.

%package gui
Summary: The database engine for analyzed or anotated text: GUI programs
Group: Databases
Requires: %name-utils = %version-%release

%description gui
Emdros is a text database engine for storage and retrieval of
annotated or analyzed text. Application domains include linguistics,
publishing, and text processing, with corpus linguistics being the
main target domain. Emdros has a powerful query-language for
query/create/update/delete operations.

This package contains end-user GUI-programs distributed with emdros:
tools for database creation amd querying.

%package utils
Summary: The database engine for analyzed or annotated text: utilities
Group: Databases

%description utils

Emdros is a text database engine for storage and retrieval of
annotated or analyzed text. Application domains include linguistics,
publishing, and text processing, with corpus linguistics being the
main target domain. Emdros has a powerful query-language for
query/create/update/delete operations.

This package contains various utils distributed with emdros: commandline
tools for database creation amd querying, utils for importing data from popular
linguistic annotation formats.

%package doc
Summary: The database engine for analyzed or annotated text: documentation
Group: Databases
BuildArch: noarch

%description doc

Emdros is a text database engine for storage and retrieval of
annotated or analyzed text. Application domains include linguistics,
publishing, and text processing, with corpus linguistics being the
main target domain. Emdros has a powerful query-language for
query/create/update/delete operations.

This package contains emdros documentation.

%package -n lib%name-devel
Summary: The database engine for analyzed or annotated text: development files
Group: Development/Databases
Provides: emdros-devel = %version-%release
Obsoletes: emdros-devel <= 3.0.0-alt1

%description -n lib%name-devel

Emdros is a text database engine for storage and retrieval of
annotated or analyzed text. Application domains include linguistics,
publishing, and text processing, with corpus linguistics being the
main target domain. Emdros has a powerful query-language for
query/create/update/delete operations.

This package contains the development files needed for building
applications with Emdros.

%package -n python-module-EmdrosPy
Summary: The database engine for analyzed or annotated text: python interface
Group: Development/Python

%description -n python-module-EmdrosPy

Emdros is a text database engine for storage and retrieval of
annotated or analyzed text. Application domains include linguistics,
publishing, and text processing, with corpus linguistics being the
main target domain. Emdros has a powerful query-language for
query/create/update/delete operations.

This package contains python interface to EMdF and MQL.

%prep
%setup -q -n emdros-%version
rm -rv pcre sqlite sqlite3
%patch0 -p2
%patch1 -p2
sed -i 's,-lpython2.5,-lpython%_python_version,' SWIG/python/Makefile.am

%build
autoreconf -fisv
export lt_prog_compiler_static_works=no
%configure --with-swig-language-python=yes --with-swig-language-perl=no --with-swig-language-ruby=no \
--disable-debug --with-sqlite3=system --with-sqlite=no --with-default-backend=sqlite3 --enable-utf8 --disable-static
%make_build
bzip2 ChangeLog

%install
%make_install install DESTDIR=%buildroot
mkdir -p %buildroot/%python_sitelibdir/
mv %buildroot/%_libdir/%name/* %buildroot/%python_sitelibdir/

for i in wx/*.png ; do \
	size=$(basename "${i##*blue-E-}" .png) ; \
	install -D "$i" %buildroot/%_iconsdir/hicolor/$size/apps/emergence-blue-E.png ; \
	done
mkdir -p %buildroot%_desktopdir
find -name "*.desktop" -exec sed -i '/Encoding/d' {} \;
find -name "*.desktop" -exec cp -t %buildroot%_desktopdir {} \;

%check
tests/emdftry -b SQLite3
tests/mqltry -b SQLite3
tests/mqllingtry -b SQLite3

%files

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/libemdrosguiu*.so.*

%files -n lib%name-devel
%_includedir/emdros/
%_libdir/*.so

%files gui
%_bindir/chunkingtoolu
%_bindir/eqtu
%_bindir/htmlcanvastestu
%_bindir/htreetestu
%_bindir/importtoolu
%_man1dir/eqtu.1.gz
%_libdir/libemdrosguiu*.so.*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*

%files utils
%doc AUTHORS COPYING NEWS README ChangeLog.bz2 INSTALL
%_bindir/TECkit_Compile
%_bindir/TxtConv
%_bindir/agexport
%_bindir/emdftry
%_bindir/eqtc
%_bindir/hal_build_db
%_bindir/manage_indices
%_bindir/mql
%_bindir/mqldump
%_bindir/mqlhal
%_bindir/mqllingtry
%_bindir/mqltry
%_bindir/negraimport
%_bindir/pennimport
%_bindir/plaintextimport
%_bindir/sfmimport
%_bindir/slashedtextimport
%_bindir/tigerxmlimport
%_bindir/ubimport
%_bindir/upgrade_db
%_bindir/jsontry
%_bindir/renderobjects
%_man1dir/agexport.1.gz
%_man1dir/emdftry.1.gz
%_man1dir/emdros.1.gz
%_man1dir/eqt.1.gz
%_man1dir/eqtc.1.gz
%_man1dir/hal_build_db.1.gz
%_man1dir/manage_indices.1.gz
%_man1dir/mql.1.gz
%_man1dir/mqldump.1.gz
%_man1dir/mqlhal.1.gz
%_man1dir/mqllingtry.1.gz
%_man1dir/mqltry.1.gz
%_man1dir/negraimport.1.gz
%_man1dir/pennimport.1.gz
%_man1dir/plaintextimport.1.gz
%_man1dir/sfmimport.1.gz
%_man1dir/slashedtextimport.1.gz
%_man1dir/tigerxmlimport.1.gz
%_man1dir/ubimport.1.gz
%_man1dir/upgrade_db.1.gz
%_man1dir/jsontry.1.gz
%_man1dir/renderobjects.1.gz
%_datadir/emdros/
%exclude %_datadir/emdros/*.png

%files doc
%doc doc/*
%doc examples/ChunkingTool/doc/ChunkingToolGuide.pdf
%doc src/qrytool/doc/EQTUsersGuide.pdf
%doc doc/progref/EmdrosProgRefGuide.pdf
%doc examples/HAL/doc/HALGuide.pdf
%doc src/importtool/doc/ImportToolUsersGuide.pdf
%doc SWIG/java/README-Java
%doc SWIG/java/TestEmdros.java
%doc SWIG/ruby/README-Ruby
%doc SWIG/ruby/test.rb
%doc SWIG/ruby/dir.sh
%doc SWIG/perl/README-Perl
%doc SWIG/perl/test.pl

%files -n python-module-EmdrosPy
%python_sitelibdir/*
%doc SWIG/python/README-Python
%doc SWIG/python/test.py
%doc SWIG/python/dir.py

%changelog
* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.2
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.1-alt1.1.1.1
- Rebuild with Python-2.7

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1.1.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.1
- Rebuilt with python 2.6

* Fri Sep 11 2009 Kirill Maslinsky <kirill@altlinux.org> 3.1.1-alt1
- 3.1.1
  + built with wxGTK 2.8
  + run tests during build
  + remove deprecated Encoding key from .desktop files

* Tue Jul 28 2009 Andrey Rahmatullin <wrar@altlinux.ru> 3.1.0-alt2
- fix hardcoded libpython version

* Thu May 07 2009 Kirill Maslinsky <kirill@altlinux.org> 3.1.0-alt1
- version up
- fixed build with gcc 4.4
- emdros-gui: menu entries and icons added

* Mon Oct 27 2008 Kirill Maslinsky <kirill@altlinux.org> 3.0.0-alt3
- fixed build with gcc 4.3
- new subpackage emdros-gui for end user GUI tools, emdros-utils
  now has no dependencies on graphical libs

* Wed Sep 24 2008 Kirill Maslinsky <kirill@altlinux.org> 3.0.0-alt2
- package splitted into lib, utils, doc (noarch), devel
- build with python SWIG interface as a separate package
  python-module-EmdrosPy


* Mon Jan 28 2008 Kirill Maslinsky <kirill@altlinux.ru> 3.0.0-alt1
- version up (3.0.0 release, see NEWS and ChangeLog)
- spec:
  	+ updated packaged docs list in %%files
	+ rename -alt-locallib.patch (needs no rediffing)

* Mon Jul 16 2007 Kirill Maslinsky <kirill@altlinux.org> 1.2.0.pre262-alt1
- version up (pre262, see NEWS and ChangeLog for details)
	+ rediff locallib patch
- packaging enhancements:
	+ split emdros and emdros-devel packages (following upstream spec template)
	+ cleanup %%files sections
	+ bzip ChangeLog
	+ use %%version macro properly in .gear-rules and spec

* Thu Jun 07 2007 Kirill Maslinsky <kirill@altlinux.org> 1.2.0-alt0.4
- version up (pre242, see NEWS and ChangeLog for details)
  + includes security-related fixes
- build options:
  + default database backend: SQLite3

* Sun Jan 14 2007 Kirill Maslinsky <kirill@altlinux.ru> 1.2.0-alt0.3
- rebuilt with wx GUI frontend enabled

* Mon Jan 08 2007 Kirill Maslinsky <kirill@altlinux.ru> 1.2.0-alt0.2
- bugfix release (1.2.0.pre231), see NEWS and ChangeLog for details
- added Packager tag in spec
- build options:
  + database backends: SQLite2, MySQL, PostgreSQL
  + default backend: SQLite2
  + without any SWIG languages
  + --enable-utf8
  + docs included in package

* Sat Jul 08 2006 Alexey Tourbin <at@altlinux.ru> 1.2.0-alt0.1
- initial revision (1.2.0.pre206)

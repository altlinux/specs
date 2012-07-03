Name: libdb1
Version: 1.85
Release: alt7

Summary: Berkeley database library version %version
License: BSD
Group: System/Libraries
Url: http://www.sleepycat.com/
Packager: Dmitry V. Levin <ldv@altlinux.org>

Provides: libdb1.so.2, db1 = %version
Obsoletes: db1
Conflicts: glibc < 2.1.90

# ftp://ftp.sleepycat.com/releases/db.%version.tar.gz
Source: db.%version.tar
Source1: db_dump185.c
Patch1: db.%version.patch
Patch2: db.%version.s390.patch
Patch3: db.%version.nodebug.patch

%package -n db1-utils
Summary: Command line tools for managing Berkeley DB databases
Group: Databases
Requires: %name = %version-%release
Conflicts: db4-utils < 0:4.3.29-alt3

%package devel
Summary: Development environment for Berkeley database library version %version
Group: Development/C
Requires: %name = %version-%release, db1-utils = %version-%release
Provides: db1-devel = %version
Obsoletes: db1-devel
Conflicts: glibc-devel < 2.1.90

%package devel-static
Summary: Static libraries for Berkeley database library version %version
Group: Development/C
Provides: db1-devel-static = %version
Obsoletes: db1-devel-static
Requires: %name-devel = %version-%release
Requires: glibc-devel-static

%package doc
Summary: Documentation for Berkeley database library version %version
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
It should be installed if compatibility is needed with databases created
with db1.

This library used to be part of the glibc package.
Since glibc-2.1.90, it is independent package.

%description -n db1-utils
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.

This package contains command line tools for managing Berkeley DB databases.

%description devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.

This package contains the header files, libraries for building programs
which use Berkeley DB.

%description devel-static
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.

This package contains the static library required for building statically linked
programs which use Berkeley DB.

%description doc
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.

This package contains documentation for Berkeley DB version %version.

%prep
%setup -q -n db.%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
install -pm644 %_sourcedir/db_dump185.c PORT/linux/

%build
%add_optflags -fno-strict-aliasing
%make_build -C PORT/linux OORG="%optflags"
bzip2 -9 docs/*.ps

sed -i 's/<db\.h>/<db1\/db.h>/' PORT/include/ndbm.h

%install
mkdir -p %buildroot{/%_lib,%_bindir,%_libdir,%_includedir/db1}

sed -n '/^\/\*-/,/^ \*\//s/^.\*.\?//p' include/db.h |grep -v '^@.*db\.h' >LICENSE

pushd PORT/linux
	install -p -m755 db_dump185 %buildroot%_bindir/db1_dump185
	ln -s db1_dump185 %buildroot%_bindir/db_dump185
	sover=`echo libdb.so.* |sed -e 's/libdb\.so\.//'`
	install -pm755 libdb.so.$sover %buildroot%_libdir/%name.so.$sover
	install -pm644 libdb.a %buildroot%_libdir/%name.a
	ln -s %name.so.$sover %buildroot%_libdir/libdb.so.$sover
	ln -s %name.so.$sover %buildroot%_libdir/%name.so
popd
install -pm644 PORT/include/ndbm.h include/{db,mpool}.h \
	%buildroot%_includedir/db1/

%define docdir %_docdir/%name-%version
install -pDm644 changelog %buildroot%docdir/ChangeLog
install -pm644 README LICENSE docs/*usenix*.ps.* %buildroot%docdir/

%files
%_libdir/*.so.*
%dir %docdir
%docdir/[A-Z]*

%files -n db1-utils
%_bindir/*

%files devel
%_libdir/*.so
%_includedir/*

%files devel-static
%_libdir/*.a

%files doc
%dir %docdir
%docdir/*.ps.*

%changelog
* Fri Nov 05 2010 Dmitry V. Levin <ldv@altlinux.org> 1.85-alt7
- Rebuilt for soname set-versions.

* Mon Dec 15 2008 Dmitry V. Levin <ldv@altlinux.org> 1.85-alt6
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- Packaged -doc subpackage as noarch.

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 1.85-alt5
- Disabled gcc optimization based on strict aliasing rules.

* Mon Mar 13 2006 Dmitry V. Levin <ldv@altlinux.org> 1.85-alt4
- Updated db_dump185 source from db-4.3.29 package.
- Relocated library from /%_lib/ to %_libdir/.

* Thu Feb 10 2005 Dmitry V. Levin <ldv@altlinux.org> 1.85-alt3
- Fixed multilib (closes #4884).

* Tue Sep 03 2002 Dmitry V. Levin <ldv@altlinux.org> 1.85-alt2
- Moved documentation to %name-doc subpackage.
- Updated %post/%postun scripts.
- Updated devel-static requirements.

* Wed Sep 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.85-alt1
- Moved db1_dump185 utility to utils subpackage.
- Renamed library subpackages.
- Added explicit provides for libdb1.so.2
- Built without explicit "-g" option (rh).

* Wed Jun 20 2001 Mikhail Zabaluev <mhz@altlinux.ru> 1.85-ipl3mdk
- Synced with Redhat 1.85-5, include path in ndbm.h fixed
- Turned optimizations really on
- devel-static subpackage

* Sun Oct 01 2000 Dmitry V. Levin <ldv@fandra.org> 1.85-ipl2mdk
- Rebuilt with glibc-2.1.94 & gcc-2.96.
- Defined _noVersionedDependencies.
- Automatically added BuildRequires.

* Fri Aug 18 2000 Dmitry V. Levin <ldv@fandra.org> 1.85-ipl1mdk
- RE and Fandra adaptions.

* Sun May 28 2000 Jeff Johnson <jbj@redhat.com>
- rename db_dump185 to db1_dump185 to avoid file conflict with db3.

* Thu Apr 20 2000 Jakub Jelinek <jakub@redhat.com>
- Include db_dump185 program from db2 here (as it is linked
  against this shared library).

* Wed Apr 19 2000 Jakub Jelinek <jakub@redhat.com>
- Create.

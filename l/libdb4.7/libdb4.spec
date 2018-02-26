%define _sover 4.7
Name: libdb%_sover
Version: %_sover.25
Release: alt7
%define srcname db-%version

Summary: Berkeley database library
License: BSD-style
Group: System/Libraries
Url: http://www.oracle.com/technology/products/berkeley-db/db/index.html

# http://download.oracle.com/berkeley-db/db-%srcname.tar.gz
Source:  %srcname.tar
Source1: man.tar

# http://www.oracle.com/technetwork/database/berkeleydb/patch-088170.html
# http://download.oracle.com/berkeley-db/patches/db/4.7.25/patch.4.7.25.1
Patch1: db-4.7.25.1.patch
# http://download.oracle.com/berkeley-db/patches/db/4.7.25/patch.4.7.25.2
Patch2: db-4.7.25.2.patch
# http://download.oracle.com/berkeley-db/patches/db/4.7.25/patch.4.7.25.3
Patch3: db-4.7.25.3.patch
# http://download.oracle.com/berkeley-db/patches/db/4.7.25/patch.4.7.25.4
Patch4: db-4.7.25.4.patch

Patch100: db-4.7.25-alt-build.patch
Patch101: db-4.7.25-alt-bound.patch
Patch102: db-4.7.25-alt-glibc.patch

Provides: libdb4 = %version-%release, db4 = %version-%release
Conflicts: glibc <= 6:2.1.3

%def_enable compat185
%def_enable cxx
%def_disable debug
%{?_enable_debug:%def_enable debug_rop}
%{!?_enable_debug:%def_disable debug_rop}
%{?_enable_debug:%def_enable debug_wop}
%{!?_enable_debug:%def_disable debug_wop}
%{?_enable_debug:%def_enable diagnostic}
%{!?_enable_debug:%def_disable diagnostic}
%def_disable dump185
%ifarch %ix86 x86_64
%def_enable java
%else
%def_disable java
%endif
%def_disable posixmutexes
%def_enable rpc
%def_enable tcl
%def_disable test
%def_disable uimutexes
%def_disable umrw

BuildConflicts: %name-devel, libdb4.0-devel, libdb4.1-devel, libdb4.2-devel, libdb4.3-devel, libdb4.4-devel, libdb4.6-devel, libdb4-devel
BuildPreReq: rpm-build >= 4.0.4-alt1
%{?_enable_cxx:BuildPreReq: gcc-c++}
%{?_enable_dump185:BuildPreReq: libdb1-devel}
%{?_enable_java:BuildPreReq: jdkgcj, sharutils, /proc}
%{?_enable_tcl:BuildPreReq: tcl-devel >= 8.4.0-alt1}

%package -n db%_sover-utils
Summary: Command line tools for managing Berkeley DB databases
Group: Databases
Provides: db4-utils = %version-%release
Requires: %{name}_int = %version-%release
Conflicts: db3-utils, db4.0-utils, db4.1-utils, db4.2-utils, db4.3-utils, db4.4-utils

%package devel
Summary: Development environment for Berkeley database library
Group: Development/C
Provides: libdb4-devel = %version-%release, db4-devel = %version-%release
Requires: %name = %version-%release
Conflicts: libdb3-devel, libdb4.0-devel, libdb4.1-devel, libdb4.2-devel, libdb4.3-devel, libdb4.4-devel, libdb4.6-devel, libdb2-devel < 0:2.4.14-alt3

%package devel-static
Summary: Static version of Berkeley database library
Group: Development/C
Provides: libdb4-devel-static = %version-%release, db4-devel-static = %version-%release
Requires: %name-devel = %version-%release

%package -n %{name}_int
Summary: Berkeley database library with exported internal API
Group: System/Libraries
Provides: libdb4_int = %version-%release
Requires: %name = %version-%release

%package -n %{name}_int-devel
Summary: Development files for Berkeley database library with exported internal API
Group: Development/C
Provides: libdb4_int-devel = %version-%release
Requires: %name-devel = %version-%release
Requires: %{name}_int = %version-%release

%package -n %{name}_cxx
Summary: C++ bindings for Berkeley database library
Group: System/Libraries
Provides: libdb4_cxx = %version-%release
Requires: %{name}_int = %version-%release

%package -n %{name}_cxx-devel
Summary: C++ development bindings for Berkeley database library
Group: Development/C++
Provides: libdb4_cxx-devel = %version-%release
Requires: %name-devel = %version-%release
Requires: %{name}_cxx = %version-%release
Conflicts: libdb4.0_cxx-devel, libdb4.1_cxx-devel, libdb4.2_cxx-devel, libdb4.3_cxx-devel, libdb4.4_cxx-devel, libdb4.6_cxx-devel

%package -n %{name}_cxx-devel-static
Summary: C++ development bindings for Berkeley database library
Group: Development/C++
Provides: libdb4_cxx-devel-static = %version-%release
Requires: %name-devel-static = %version-%release
Requires: %{name}_cxx-devel = %version-%release

%package -n %{name}_tcl
Summary: Tcl bindings for Berkeley database library
Group: System/Libraries
Provides: libdb4_tcl = %version-%release
Requires: %{name}_int = %version-%release
Conflicts: libdb3_tcl, libdb4.0_tcl, libdb4.1_tcl, libdb4.2_tcl, libdb4.3_tcl, libdb4.4_tcl, libdb4.6_tcl

%package -n %{name}_tcl-devel
Summary: Tcl development bindings for Berkeley database library
Group: Development/Tcl
Provides: libdb4_tcl-devel = %version-%release
Requires: %name-devel = %version-%release
Requires: %{name}_tcl = %version-%release
Conflicts: libdb4.0_tcl-devel, libdb4.1_tcl-devel, libdb4.2_tcl-devel, libdb4.3_tcl-devel, libdb4.4_tcl-devel, libdb4.6_tcl-devel

%package -n %{name}_tcl-devel-static
Summary: Tcl development bindings for Berkeley database library
Group: Development/Tcl
Provides: libdb4_tcl-devel-static = %version-%release
Requires: %name-devel-static = %version-%release
Requires: %{name}_tcl-devel = %version-%release

%package -n %{name}_java
Summary: Java bindings for Berkeley database library
Group: System/Libraries
Provides: libdb4_java = %version-%release
Requires: %{name}_int = %version-%release
Conflicts: libdb4.0_java, libdb4.1_java, libdb4.2_java, libdb4.3_java, libdb4.4_java, libdb4.6_java

%package -n %{name}_java-devel
Summary: Java development bindings for Berkeley database library
Group: Development/Java
Provides: libdb4_java-devel = %version-%release
Requires: %name-devel = %version-%release
Requires: %{name}_java = %version-%release

%package -n %{name}_java-devel-static
Summary: Java development bindings for Berkeley database library
Group: Development/Java
Provides: libdb4_java-devel-static = %version-%release
Requires: %name-devel-static = %version-%release
Requires: %{name}_java-devel = %version-%release

%package doc
Summary: Documentation for Berkeley database library
Group: Development/Other
BuildArch: noarch
Provides: libdb4-doc = %version-%release

%description
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB is used by many applications, including Python and Perl, so this
should be installed on all systems.

%description -n db%_sover-utils
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains command line tools for managing Berkeley DB databases.

%description devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains the header files and libraries for
building programs which use Berkeley DB.

%description devel-static
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains static libraries for building statically linked programs
which use Berkeley DB.

%description -n %{name}_int
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains Berkeley DB library with exported internal API.

%description -n %{name}_int-devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains development files for Berkeley database library
with exported internal API.

%description -n %{name}_cxx
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains C++ API library.

%description -n %{name}_cxx-devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains libraries and header files for building programs using C++ API.

%description -n %{name}_cxx-devel-static
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains static libraries for C++ API.

%description -n %{name}_tcl
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains Tcl API library.

%description -n %{name}_tcl-devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains libraries for building programs using Tcl API.

%description -n %{name}_tcl-devel-static
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains static libraries for Tcl API.

%description -n %{name}_java
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains Java API library.

%description -n %{name}_java-devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains libraries and header files for building programs using
Java API.

%description -n %{name}_java-devel-static
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains static libraries for Java API.

%description doc
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains documentation for developers.

%prep
%setup -n %srcname -a1
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1

%build
%add_optflags -fno-strict-aliasing
%define _configure_script ../dist/configure

pushd build_unix
	%configure \
		%{subst_enable compat185} \
		%{subst_enable cxx} \
		%{subst_enable debug} \
		%{subst_enable debug_rop} \
		%{subst_enable debug_wop} \
	        %{subst_enable dump185} \
		%{subst_enable diagnostic} \
		%{subst_enable java} \
		%{subst_enable posixmutexes} \
		%{subst_enable rpc} \
		%{subst_enable tcl} \
		%{subst_enable test} \
		%{subst_enable uimutexes} \
		%{subst_enable umrw} \
		%{?_enable_tcl:--with-tcl=%_libdir} \
		#
	# Remove libtool predep_objects and postdep_objects wonkiness
	sed -i 's/-shared -nostdlib/-shared/' libtool
	sed -i 's/^\(predep_objects="\|postdep_objects="\).*$/\1"/' libtool
	# Edit libtool files by hand until autoreconf can be used here
	find -type f -name libtool -print0 |
		xargs -r0 grep -lZ '^sys_lib_dlsearch_path_spec="' -- |
		xargs -r0 sed -i 's|^\(sys_lib_dlsearch_path_spec="\).*|\1/%_lib %_libdir"|' --
	# SMP-incompatible build.
	make LDFLAGS=--no-allow-shlib-undefined
popd

rm -f examples_*/tags

%install
mkdir -p %buildroot{/%_lib,%_libdir,%_includedir/db4}
%{?_enable_tcl:mkdir -p %buildroot{%_tcllibdir,%_tcldatadir/Db_tcl}}

%define docdir %_docdir/%srcname
%makeinstall -C build_unix docdir=%buildroot%docdir

mkdir -p %buildroot%_man1dir
install -pm644 man/*.1 %buildroot%_man1dir/

install -pm644 README LICENSE %buildroot%docdir/
cp -pRL examples_* %buildroot%docdir/

%define _libdb_a	libdb-%_sover.a
%define _libdb_so	libdb-%_sover.so

pushd %buildroot
	# Relocate main shared library from %_libdir/ to /%_lib/.
	mv .%_libdir/%_libdb_so ./%_lib/
	for f in .%_libdir/libdb{,-*}.so; do
		ln -snf ../../%_lib/%_libdb_so "$f"
	done
	ln -s ../../%_lib/%_libdb_so .%_libdir/

	# Correct static libraries.
	pushd .%_libdir
	for f in libdb*.a; do
		[ -n "${f%%%%*-%_sover.a}" ] || continue
		ln -snf "${f%%.a}-%_sover.a" "$f"
	done
	popd
	rm .%_libdir/libdb_int-*.a

%if_enabled tcl
	mv .%_libdir/libdb_tcl* .%_tcllibdir/
	rm .%_tcllibdir/*.la
%endif

	mv .%_includedir/*.h .%_includedir/db4/
	ln -s db4/db.h db4/db_185.h .%_includedir/
popd

%{?_enable_tcl:%tea_makeindex -f libdb_tcl-%_sover.so -C %buildroot%_tcldatadir/Db_tcl}

%if_enabled java
# Move java jar file to the correct place.
mkdir -p %buildroot%_datadir/java
mv %buildroot%_libdir/*.jar %buildroot%_datadir/java/
%endif

mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
for n in db%_sover-utils \
	 %name{,-devel{,-static}} \
	 %{name}_cxx{,-devel{,-static}} \
	 %{?_enable_tcl:%{name}_tcl{,-devel{,-static}}} \
	 %{?_enable_java:%{name}_java{,-devel{,-static}}} \
	 ; do
	echo "${n/%_sover/4}" >"%buildroot%_sysconfdir/buildreqs/packages/substitute.d/$n"
done

%files
%config %_sysconfdir/buildreqs/packages/substitute.d/%name
/%_lib/*.so
%dir %docdir
%doc %docdir/[A-Z]*


%if_enabled cxx
%files -n %{name}_cxx
%config %_sysconfdir/buildreqs/packages/substitute.d/%{name}_cxx
%_libdir/*_cxx-[0-9].[0-9].so

%files -n %{name}_cxx-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/%{name}_cxx-devel
%_libdir/*_cxx.so
%_libdir/*_cxx-[0-9].so
%_includedir/*/*cxx*

%files -n %{name}_cxx-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/%{name}_cxx-devel-static
%_libdir/*_cxx*.a
%endif #cxx

%if_enabled tcl
%files -n %{name}_tcl
%config %_sysconfdir/buildreqs/packages/substitute.d/%{name}_tcl
%_tcllibdir/*_tcl-[0-9].[0-9].so
%_tcldatadir/Db_tcl

%files -n %{name}_tcl-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/%{name}_tcl-devel
%_tcllibdir/*_tcl.so
%_tcllibdir/*_tcl-[0-9].so

%files -n %{name}_tcl-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/%{name}_tcl-devel-static
%_tcllibdir/*_tcl*.a
%endif #tcl

%if_enabled java
%files -n %{name}_java
%config %_sysconfdir/buildreqs/packages/substitute.d/%{name}_java
%_libdir/*_java-[0-9].[0-9].so
%_datadir/java/*.jar

%files -n %{name}_java-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/%{name}_java-devel
%_libdir/*_java.so
%_libdir/*_java-[0-9].so
%_libdir/*_java-[0-9].[0-9]_g.so

%files -n %{name}_java-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/%{name}_java-devel-static
%_libdir/*_java*.a
%endif #java

%files -n db%_sover-utils
%config %_sysconfdir/buildreqs/packages/substitute.d/db%_sover-utils
%_bindir/*
%_man1dir/*

%files doc
%dir %docdir
%doc %docdir/[a-z]*

%files devel
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-devel
%_libdir/libdb.so
%_libdir/libdb-*.so
%_includedir/*
%if_enabled cxx
%exclude %_includedir/*/*cxx*
%endif

%files -n %{name}_int
%_libdir/*_int-[0-9].[0-9].so

%files -n %{name}_int-devel
%_libdir/*_int.so
%_libdir/*_int-[0-9].so

%files devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-devel-static
%_libdir/libdb.a
%_libdir/libdb-[0-9]*.a

%changelog
* Tue Feb 15 2011 Dmitry V. Levin <ldv@altlinux.org> 4.7.25-alt7
- Rebuilt for debuginfo.

* Tue Oct 12 2010 Dmitry V. Levin <ldv@altlinux.org> 4.7.25-alt6
- Backported RPATH fix from libtool package.
- Rebuilt for soname set-versions.

* Tue May 19 2009 Dmitry V. Levin <ldv@altlinux.org> 4.7.25-alt5
- Imported official patch #4.
- devel: Packaged symlink to the main shared library.
- Disabled compiler optimization based on strict-aliasing rules.

* Wed Dec 17 2008 Dmitry V. Levin <ldv@altlinux.org> 4.7.25-alt4
- Imported official patches #2,#3.

* Fri Nov 28 2008 Dmitry V. Levin <ldv@altlinux.org> 4.7.25-alt3
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- Packaged -doc subpackage as noarch.
- Applied upstream fix for multi-partition lock manager.

* Wed Oct 29 2008 Dmitry V. Levin <ldv@altlinux.org> 4.7.25-alt2
- Applied upstream fix to allow replication clients to open a sequence.
- Enabled java bindings again, thanks to gcc4.3-java.

* Sat May 31 2008 Dmitry V. Levin <ldv@altlinux.org> 4.7.25-alt1
- Updated to 4.7.25.
- Disabled java bindings for a while.

* Fri May 09 2008 Dmitry V. Levin <ldv@altlinux.org> 4.6.21-alt2
- Resurrected linkage fixes lost in previous release.
- Imported FC fix for build with fresh glibc.
- libdb_tcl: Fixed strncat(3) usage.

* Mon May 05 2008 Stanislav Ievlev <inger@altlinux.org> 4.6.21-alt1
- Updated to 4.6.21 + official patch #1.

* Sun Oct 22 2006 Dmitry V. Levin <ldv@altlinux.org> 4.4.20-alt2
- Applied official patches #3,#4.
- db4.4-utils: Added manual pages from Debian db4.4-util package.

* Mon Mar 13 2006 Dmitry V. Levin <ldv@altlinux.org> 4.4.20-alt1
- Updated to 4.4.20 + official patches #1,#2.
- Updated build patch.
- Linked tcl bindings with -ltcl.

* Mon Mar 13 2006 Dmitry V. Levin <ldv@altlinux.org> 4.3.29-alt3
- Fixed build without tcl support (#8626).
- Removed -utils from -devel dependencies (#9235).
- Added %{name}_int-devel subpackage.
- Disabled build of db_dump185 utility for -utils subpackage,
  because db1-utils package already contains it.

* Thu Oct 13 2005 Dmitry V. Levin <ldv@altlinux.org> 4.3.29-alt2
- Build java bindings with -fno-strict-aliasing.

* Sun Aug 21 2005 Dmitry V. Levin <ldv@altlinux.org> 4.3.29-alt1
- Updated to 4.3.29.
- Cloned libdb library to libdb_int.
- Linked shared bindings with libdb_int library.
- Restricted list of global symbols exported by the libdb library.

* Wed Jun 15 2005 Dmitry V. Levin <ldv@altlinux.org> 4.3.28-alt1
- Updated to 4.3.28.
- Corrected license tag (closes #6679).

* Fri Mar 25 2005 Kachalov Anton <mouse@altlinux.ru> 4.3.27-alt2
- Reenabled java bindings.

* Wed Feb 09 2005 Dmitry V. Levin <ldv@altlinux.org> 4.3.27-alt1
- Updated to 4.3.27 + official patches #1,#2,#3.
- Added buildreq substitution rules.

* Wed Feb 09 2005 Kachalov Anton <mouse@altlinux.ru> 4.3.27-alt0.1
- 4.3.27
- Fixed multilib (closes #4885).
- Disabled build of java bindings for a while.

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 4.2.52-alt4.1
- Rebuilt with libstdc++.so.6.

* Wed May 26 2004 Dmitry V. Levin <ldv@altlinux.org> 4.2.52-alt4
- %name-devel: removed %_libdir/%_libdb_so symlink.

* Fri May 07 2004 Dmitry V. Levin <ldv@altlinux.org> 4.2.52-alt3
- %name-devel: package %_includedir/db_185.h symlink.

* Tue Apr 27 2004 Dmitry V. Levin <ldv@altlinux.org> 4.2.52-alt2
- Rebuilt with glibc-2.3.x.

* Thu Feb 12 2004 Dmitry V. Levin <ldv@altlinux.org> 4.2.52-alt1
- Updated to 4.2.52 + official patches #1,#2.

* Wed Nov 26 2003 Dmitry V. Levin <ldv@altlinux.org> 4.1.25-alt2
- Do not package .la files.
- Temporarily removed -v option from %%tea_makeindex call (Sergey Bolshakov).

* Fri Mar 07 2003 Dmitry V. Levin <ldv@altlinux.org> 4.1.25-alt1
- Updated to 4.1.25 + official patch #1.
- Updated patches:
  + alt-makefile
  + alt-configure
- Removed patches:
  + rh-recover (merged upstream)
  + rh-ham_dirty_meta ((merged upstream)
  + alt-gcc296 (no longer needed)
- Cleaned up library relocation.

* Thu Mar 06 2003 Dmitry V. Levin <ldv@altlinux.org> 4.0.14-alt9
- Renamed to libdb4.0.

* Wed Nov 13 2002 Dmitry V. Levin <ldv@altlinux.org> 4.0.14-alt8
- Relocated db.jar from %_libdir/ to %_datadir/java/.

* Mon Nov 11 2002 Dmitry V. Levin <ldv@altlinux.org> 4.0.14-alt7
- Added patch from Sleepycat to avoid db_recover (rh #70362).
- Fixed includedir problem (rh).
- Enabled java support.

* Sat Oct 12 2002 Dmitry V. Levin <ldv@altlinux.org> 4.0.14-alt6
- Fixed docs installation due to coreutils-4.5.2-alt1.

* Wed Oct  2 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 4.0.14-alt5
- rebuilt with tcl 8.4
- tcl package index added

* Tue Sep 03 2002 Stanislav Ievlev <inger@altlinux.ru> 4.0.14-alt4
- super split. New subpackages:
    * for c++
    * for tcl
    * documentation

* Mon Aug 12 2002 Stanislav Ievlev <inger@altlinux.ru> 4.0.14-alt3
- Rebuild with new tcl layout

* Sat Mar 30 2002 Dmitry V. Levin <ldv@alt-linux.org> 4.0.14-alt2
- Implemented new %%def_enable/%%_def_disable specfile logic.
- Build with diagnostic disabled by default.
- Use postun_ldconfig.

* Wed Mar 13 2002 Dmitry V. Levin <ldv@alt-linux.org> 4.0.14-alt1
- 4.0.14
- Fixed permissions on shared libraries (0000543).
- Dropped db_chroot_prefix hack.
- Conflicts: db3-utils, libdb3-devel, libdb3-devel-static.

* Mon Dec 10 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.3.11-alt4
- Fixed db_chroot_prefix hack (jbj).

* Wed Dec 05 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.3.11-alt3
- Added db_chroot_prefix hack.
- Added compatibility symlink to shared library.
- Dropped compatibility symlink to static library.

* Thu Oct 25 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.3.11-alt2
- Added ham_dirty_meta patch from Sleepycat.
- Added compatibility symlink to static library.

* Tue Sep 25 2001 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.3.11-alt1
- 3.3.11 release.
- Renamed library subpackages.
- Corrected interpackage requires.
- Moved static libraries to devel-static subpackage.
- Moved %_includedir/db_185.h symlink to libdb2-devel package.

* Fri Feb 02 2001 Dmitry V. Levin <ldv@fandra.org> 3.2.9-ipl2mdk
- Added noticecall callback interface
  (by Alexander Bokovoy <ab@avilink.net>).

* Fri Feb 02 2001 Dmitry V. Levin <ldv@fandra.org> 3.2.9-ipl1mdk
- 3.2.9 release.
- Enabled LFS support.
- Explicitly set strip methods.

* Mon Jan 15 2001 Dmitry V. Levin <ldv@fandra.org> 3.2.3e-ipl2mdk
- Fixed db_185.h

* Thu Jan 04 2001 Dmitry V. Levin <ldv@fandra.org> 3.2.3e-ipl1mdk
- New version for MaxSQL's transactions support.
- Disabled posixmutexes again.

* Sat Nov 11 2000 Dmitry V. Levin <ldv@fandra.org> 3.1.17-ipl3mdk
- Rebuild with glibc-2.2 and for glibc-2.2.
- Docs cleanup.
- Enabled C++ api.
- Enabled posixmutexes.
- Fixed static/shared build.

* Sun Oct 01 2000 Dmitry V. Levin <ldv@fandra.org> 3.1.17-ipl2mdk
- Rebuilt with glibc-2.1.94 & gcc-2.96.
- Defined _noVersionedDependencies.
- Automatically added BuildRequires.

* Mon Aug 21 2000 Dmitry V. Levin <ldv@fandra.org> 3.1.17-ipl1mdk
- 3.1.17.

* Fri Aug 18 2000 Dmitry V. Levin <ldv@fandra.org> 3.1.14-ipl1mdk
- RE and Fandra adaptions.

* Sun Jun 11 2000 Jeff Johnson <jbj@redhat.com>
- upgrade to 3.1.14.
- create db3-utils sub-package to hide tcl dependency, enable tcl Yet Again.
- FHS packaging.

* Mon Jun  5 2000 Jeff Johnson <jbj@redhat.com>
- disable tcl Yet Again, base packages cannot depend on libtcl.so.

* Sat Jun  3 2000 Jeff Johnson <jbj@redhat.com>
- enable tcl, rebuild against tcltk 8.3.1 (w/o pthreads).

* Tue May 30 2000 Matt Wilson <msw@redhat.com>
- include /lib/libdb.so in the devel package

* Wed May 10 2000 Jeff Johnson <jbj@redhat.com>
- put in "System Environment/Libraries" per msw instructions.

* Tue May  9 2000 Jeff Johnson <jbj@redhat.com>
- install shared library in /lib, not /usr/lib.
- move API docs to db3-devel.

* Mon May  8 2000 Jeff Johnson <jbj@redhat.com>
- don't rename db_* to db3_*.

* Tue May  2 2000 Jeff Johnson <jbj@redhat.com>
- disable --enable-test --enable-debug_rop --enable-debug_wop.
- disable --enable-posixmutexes --enable-tcl as well, to avoid glibc-2.1.3
  problems.

* Mon Apr 24 2000 Jeff Johnson <jbj@redhat.com>
- add 3.0.55.1 alignment patch.
- add --enable-posixmutexes (linux threads has not pthread_*attr_setpshared).
- add --enable-tcl (needed -lpthreads).

* Sat Apr  1 2000 Jeff Johnson <jbj@redhat.com>
- add --enable-debug_{r,w}op for now.
- add variable to set shm perms.

* Sat Mar 25 2000 Jeff Johnson <jbj@redhat.com>
- update to 3.0.55

* Tue Dec 29 1998 Jeff Johnson <jbj@redhat.com>
- Add --enable-cxx to configure.

* Thu Jun 18 1998 Jeff Johnson <jbj@redhat.com>
- Create.

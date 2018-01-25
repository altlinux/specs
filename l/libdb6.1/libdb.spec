%define _sover 6.1
Name: libdb%_sover
Version: %_sover.19
Release: alt6
%define srcname db-%version

Summary: Berkeley database library
License: GNU AFFERO GPLv3
Group: System/Libraries
Url: http://www.oracle.com/us/products/database/berkeley-db/overview/

Source:  %srcname.tar.gz
Patch1: java8-fix.patch

%def_enable compat185
%def_enable cxx
%def_enable debug
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
%def_enable tcl
%def_enable test
%def_disable uimutexes
%def_disable umrw

%{?_enable_cxx:BuildPreReq: gcc-c++}
%{?_enable_dump185:BuildPreReq: libdb1-devel}
%{?_enable_java:BuildPreReq: java-devel-default, sharutils, /proc}
%{?_enable_tcl:BuildPreReq: tcl-devel >= 8.4.0-alt1}

BuildRequires: libsocket-devel

%package -n db%_sover-utils
Summary: Command line tools for managing Berkeley DB databases
Group: Databases
Conflicts: db3-utils, db4.0-utils, db4.1-utils, db4.2-utils
Conflicts: db4.3-utils, db4.4-utils, db4.7-utils, db4.8-utils
Provides: db6-utils = %version-%release

%package devel
Summary: Development environment for Berkeley database library
Group: Development/C
Requires: %name = %version-%release
Conflicts: libdb3-devel, libdb4.0-devel, libdb4.1-devel, libdb4.2-devel
Conflicts: libdb4.3-devel, libdb4.4-devel, libdb4.6-devel
Conflicts: libdb4.7-devel, libdb4.8-devel, libdb2-devel < 0:2.4.14-alt3
Provides: libdb6-devel = %version-%release

%package -n %{name}_cxx
Summary: C++ bindings for Berkeley database library
Group: System/Libraries
Provides: libdb6_cxx = %version-%release

%package -n %{name}_sql
Summary: SQL API for Berkeley database library
Group: System/Libraries
Provides: libdb6_sql = %version-%release

%package -n %{name}_cxx-devel
Summary: C++ development bindings for Berkeley database library
Group: Development/C++
#Provides: libdb4_cxx-devel = %version-%release
Requires: %name-devel = %version-%release
Requires: %{name}_cxx = %version-%release
Conflicts: libdb4.0_cxx-devel, libdb4.1_cxx-devel, libdb4.2_cxx-devel
Conflicts: libdb4.3_cxx-devel, libdb4.4_cxx-devel, libdb4.6_cxx-devel
Conflicts: libdb4.7_cxx-devel libdb4.8_cxx-devel
Provides: libdb6_cxx-devel = %version-%release

%package -n %{name}_sql-devel
Summary: SQL API development files for Berkeley database library
Group: Development/Databases
Requires: %name-devel = %version-%release
Requires: %{name}_sql = %version-%release
Provides: libdb6_sql-devel = %version-%release

%package -n %{name}_tcl
Summary: Tcl bindings for Berkeley database library
Group: System/Libraries
Conflicts: libdb3_tcl, libdb4.0_tcl, libdb4.1_tcl, libdb4.2_tcl
Conflicts: libdb4.3_tcl, libdb4.4_tcl, libdb4.6_tcl, libdb4.7_tcl
Conflicts: libdb4.8_tcl
Provides: libdb6_tcl = %version-%release

%package -n %{name}_tcl-devel
Summary: Tcl development bindings for Berkeley database library
Group: Development/Tcl
Requires: %name-devel = %version-%release
Requires: %{name}_tcl = %version-%release
Conflicts: libdb4.0_tcl-devel, libdb4.1_tcl-devel, libdb4.2_tcl-devel
Conflicts: libdb4.3_tcl-devel, libdb4.4_tcl-devel, libdb4.6_tcl-devel
Conflicts: libdb4.7_tcl-devel libdb4.8_tcl-devel
Provides: libdb6_tcl-devel = %version-%release

%package -n %{name}_java
Summary: Java bindings for Berkeley database library
Group: System/Libraries
Conflicts: libdb4.0_java, libdb4.1_java, libdb4.2_java, libdb4.3_java
Conflicts: libdb4.4_java, libdb4.6_java, libdb4.7_java, libdb4.8_java
Provides: libdb6_java = %version-%release

%package -n %{name}_java-devel
Summary: Java development bindings for Berkeley database library
Group: Development/Java
Requires: %name-devel = %version-%release
Requires: %{name}_java = %version-%release
Provides: libdb6_java-devel = %version-%release

%package doc
Summary: Documentation for Berkeley database library
Group: Development/Other
BuildArch: noarch

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

%description -n %{name}_cxx
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains C++ API library.

%description -n %{name}_sql
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains SQL API library.

%description -n %{name}_cxx-devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains libraries and header files for building programs using C++ API.

%description -n %{name}_sql-devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains libraries and header files for building programs using SQL API.

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

%description doc
The Berkeley Database (Berkeley DB) is a programmatic toolkit that provides
embedded database support for both traditional and client/server applications.
Berkeley DB includes B+tree, Extended Linear Hashing, Fixed and Variable-length
record access methods, transactions, locking, logging, shared memory caching
and database recovery.  DB supports C, C++, Java and Perl APIs.

This package contains documentation for developers.

%prep
%setup -n %srcname
%patch1 -p1
cp -pvf /usr/share/gnu-config/config.{sub,guess} lang/sql/sqlite/

%build
%add_optflags -fno-strict-aliasing -DBDBSQL_FILE_PER_TABLE=1
%add_optflags -DSQLITE_ENABLE_FTS3=1 -DSQLITE_ENABLE_RTREE=1
%define _configure_script ../dist/configure

pushd dist
	%autoreconf
	./s_config
popd
pushd build_unix
	ln -s ../dist/configure ./
	%configure \
		--enable-static=no \
		--enable-sql \
		--with-cryptography \
		--enable-load-extension \
		--enable-o_direct \
		--enable-sql_codegen \
		--enable-localization \
		--enable-amalgamation \
		%{subst_enable compat185} \
		%{subst_enable cxx} \
		%{subst_enable debug} \
		%{subst_enable debug_rop} \
		%{subst_enable debug_wop} \
	        %{subst_enable dump185} \
		%{subst_enable diagnostic} \
		%{subst_enable java} \
		%{subst_enable posixmutexes} \
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
	%make
popd

%install
mkdir -p %buildroot{/%_lib,%_libdir,%_includedir/db4}
%{?_enable_tcl:mkdir -p %buildroot{%_tcllibdir,%_tcldatadir/Db_tcl}}

%define docdir %_docdir/%srcname
%makeinstall -C build_unix docdir=%buildroot%docdir

#mkdir -p %buildroot%_man1dir
#install -pm644 man/*.1 %buildroot%_man1dir/

install -pm644 README LICENSE %buildroot%docdir/
cp -pRL examples %buildroot%docdir/

%define _libdb_a	libdb-%_sover.a
%define _libdb_so	libdb-%_sover.so

pushd %buildroot
	# Relocate main shared library from %_libdir/ to /%_lib/.
	mv .%_libdir/%_libdb_so ./%_lib/
	for f in .%_libdir/libdb{,-*}.so; do
		ln -snf ../../%_lib/%_libdb_so "$f"
	done
	ln -s ../../%_lib/%_libdb_so .%_libdir/

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
	 %name{,-devel} \
	 %{name}_cxx{,-devel} \
	 %{?_enable_tcl:%{name}_tcl{,-devel}} \
	 %{?_enable_java:%{name}_java{,-devel}} \
	 %{name}_sql{,-devel} \
	 ; do
	echo "${n/%_sover/6}" >"%buildroot%_sysconfdir/buildreqs/packages/substitute.d/$n"
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
%_libdir/*_cxx-[0-9].so

%files -n %{name}_cxx-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/%{name}_cxx-devel
%_libdir/*_cxx.so
%_includedir/*/*cxx*
%endif #cxx

%files -n %{name}_sql
%config %_sysconfdir/buildreqs/packages/substitute.d/%{name}_sql
%_libdir/*_sql-[0-9].[0-9].so
%_libdir/*_sql-[0-9].so

%files -n %{name}_sql-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/%{name}_sql-devel
%_libdir/*_sql.so
%_includedir/*/dbsql.h

%if_enabled tcl
%files -n %{name}_tcl
%config %_sysconfdir/buildreqs/packages/substitute.d/%{name}_tcl
%_tcllibdir/*_tcl-[0-9].[0-9].so
%_tcldatadir/Db_tcl

%files -n %{name}_tcl-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/%{name}_tcl-devel
%_tcllibdir/*_tcl.so
%_tcllibdir/*_tcl-[0-9].so
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
%endif #java

%files -n db%_sover-utils
%config %_sysconfdir/buildreqs/packages/substitute.d/db%_sover-utils
%_bindir/*
#_man1dir/*

%files doc
%dir %docdir
%doc %docdir/[a-z]*

%files devel
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-devel
%_libdir/libdb.so
%_libdir/libdb-*.so
%_includedir/*
%exclude %_includedir/*/dbsql.h
%if_enabled cxx
%exclude %_includedir/*/*cxx*
%endif

%changelog
* Thu Jan 25 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.19-alt6
- fixed build on armh

* Wed Jan 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.19-alt5
- Updated java build dependencies.

* Tue Oct 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.19-alt4
- Fixed provides.

* Thu Aug 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.19-alt3
- Rebuilt with gcc-6.

* Sun Apr 17 2016 Igor Vlasenko <viy@altlinux.ru> 6.1.19-alt2
- NMU: fixed substitute.d files

* Wed Sep 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.19-alt1
- Initial build for Sisyphus


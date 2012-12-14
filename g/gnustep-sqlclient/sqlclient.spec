%set_verify_elf_method unresolved=strict

Name: gnustep-sqlclient
Version: 1.6.0
Release: alt2.git20121129
Summary: Provide a simple interface to SQL databases for GNUstep applications
License: LGPLv3+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-sqlclient.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-performance-devel /proc
BuildPreReq: java-devel-default postgresql9.1-devel libsqlite3-devel
BuildPreReq: libMySQL-devel

Requires: lib%name = %version-%release

%description
The SQLClient library is designed to provide a simple interface to SQL
databases for GNUstep applications. It does not attempt the sort of
abstraction provided by the much more sophisticated GDL2 library but
rather allows applications to directly execute SQL queries and
statements.

%package -n lib%name
Summary: Shared libraries of GNUstep SQLClient
Group: System/Libraries

%description -n lib%name
The SQLClient library is designed to provide a simple interface to SQL
databases for GNUstep applications. It does not attempt the sort of
abstraction provided by the much more sophisticated GDL2 library but
rather allows applications to directly execute SQL queries and
statements.

This package contains shared libraries of SQLClient.

%package -n lib%name-devel
Summary: Development files of GNUstep SQLClient
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release
Requires: %name = %version-%release

%description -n lib%name-devel
The SQLClient library is designed to provide a simple interface to SQL
databases for GNUstep applications. It does not attempt the sort of
abstraction provided by the much more sophisticated GDL2 library but
rather allows applications to directly execute SQL queries and
statements.

This package contains shared libraries of SQLClient.

%package doc
Summary: Documentation for GNUstep SQLClient
Group: Development/Documentation
BuildArch: noarch

%description doc
The SQLClient library is designed to provide a simple interface to SQL
databases for GNUstep applications. It does not attempt the sort of
abstraction provided by the much more sophisticated GDL2 library but
rather allows applications to directly execute SQL queries and
statements.

This package contains documentation for SQLClient.

%prep
%setup

%build
export LD_LIBRARY_PATH=$(dirname $(find %_jvmdir -name libjvm.so) \
	|egrep server)
%autoreconf
%configure \
	--libexecdir=%_libdir \
	--with-postgres-dir=%prefix \
	--with-additional-include=-I%_includedir/pgsql \
%ifarch x86_64
	--with-jre-architecture=amd64 \
%else
	--with-jre-architecture=i386 \
%endif
	--with-installation-domain=SYSTEM

libSQLClient=$PWD/obj/libSQLClient.so

buildIt() {
	%make_build \
		messages=yes \
		debug=yes \
		strip=no \
		shared=yes \
		AUXILIARY_CPPFLAGS='-O2' \
		CONFIG_SYSTEM_LIBS="$1 -lPerformance -lgnustep-base -lobjc"
}

buildIt
for i in SQLite MySQL JDBC_libs JDBC Postgres ECPG
do
	rm -f $(find ./ -name $i -type f)
done
buildIt $libSQLClient
 
%install
%makeinstall_std messages=yes GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc ChangeLog README
%_libdir/GNUstep

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files doc
%_docdir/GNUstep

%changelog
* Fri Dec 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt2.git20121129
- Rebuild with updated gnustep-mak

* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20121129
- Initial build for Sisyphus


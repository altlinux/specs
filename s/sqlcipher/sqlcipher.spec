# bcond default logic is nicely backwards...
%def_without static

Summary: AES encryption for SQLite databases
Name: sqlcipher
Version: 3.2.0
Release: alt1
License: BSD
Group: Databases
Url: http://sqlcipher.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: https://github.com/sqlcipher/sqlcipher/archive/v%version.tar.gz
# Shut up stupid tests depending on system settings of allowed open fd's
#Patch1: sqlite-3.7.7.1-stupid-openfiles-test.patch
# Shut up pagecache overflow test whose expected result depends on compile
# options and whatnot. Dunno why this started failing in 3.7.10 but
# doesn't seem particularly critical...
#Patch2: sqlite-3.7.10-pagecache-overflow-test.patch
# sqlite >= 3.7.10 is buggy if malloc_usable_size() is detected, disable it:
# https://bugzilla.redhat.com/show_bug.cgi?id=801981
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=665363
#Patch3: sqlcipher-3.7.15-no-malloc-usable-size.patch
BuildRequires: ncurses-devel readline-devel glibc-devel
BuildRequires: libssl-devel
BuildRequires: %_bindir/tclsh
BuildRequires: tcl-devel

Requires: lib%name = %EVR

%description
SQLCipher is an open source library that provides transparent, secure
256-bit AES encryption of SQLite database files.

SQLCipher has been adopted as a secure database solution by many
commercial and open source products, making it one of the most popular
encrypted database platforms for Mobile, Embedded, and Desktop
applications.

%package -n lib%name
Summary: Shared libraries of the sqlite3 embeddable SQL database engine
Group: System/Libraries

%description -n lib%name
SQLCipher is an open source library that provides transparent, secure
256-bit AES encryption of SQLite database files.

SQLCipher has been adopted as a secure database solution by many
commercial and open source products, making it one of the most popular
encrypted database platforms for Mobile, Embedded, and Desktop
applications.

This package contains shared libraries of %name.

%package -n lib%name-devel
Summary: Development tools for the sqlite3 embeddable SQL database engine
Group: Development/Other
Requires: lib%name = %EVR

%description -n lib%name-devel
This package contains the header files and development documentation
for %name. If you like to develop programs using %name, you will need
to install lib%name-devel.

%prep
%setup

%build
%autoreconf
%add_optflags -DSQLITE_HAS_CODEC -DSQLITE_ENABLE_COLUMN_METADATA=1
%add_optflags -DSQLITE_DISABLE_DIRSYNC=1 -DSQLITE_ENABLE_FTS3=3
%add_optflags -DSQLITE_ENABLE_RTREE=1 -DSQLITE_SECURE_DELETE=1
%add_optflags -DSQLITE_ENABLE_UNLOCK_NOTIFY=1 -Wall -fno-strict-aliasing
%add_optflags -I$PWD/ext/fts3
%configure \
	--enable-threadsafe \
	--enable-threads-override-locks \
	--enable-load-extension \
	--enable-cross-thread-connections \
	--enable-tempstore=yes \

# rpath removal
subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%makeinstall_std

install -D -m0644 sqlcipher.1 %buildroot%_man1dir/sqlcipher.1

%if ! %{with static}
rm -f %buildroot%_libdir/*.{la,a}
%endif

rm -fR %buildroot%_tcldatadir

%check
make testfixture
%ifarch s390 s390x ppc ppc64 %sparc %arm
./testfixture test/crypto.test || :
%else
./testfixture test/crypto.test
%endif

%files
%doc *.md LICENSE doc/*
%_bindir/sqlcipher
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/sqlcipher
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1
- Version 3.2.0

* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus

* Tue Aug 13 2013 Abel Luck <abel@outcomedubious.im> - 2.2.1-1
- Initial SQLCipher package based on SQLite 3.7.17


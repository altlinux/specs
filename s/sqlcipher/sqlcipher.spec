# bcond default logic is nicely backwards...
%def_without static

Summary: AES encryption for SQLite databases
Name:    sqlcipher
Version: 4.6.1
Release: alt1
License: BSD
Group:   Databases
Url:     http://sqlcipher.net/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: https://github.com/sqlcipher/sqlcipher/archive/v%version.tar.gz
BuildRequires: ncurses-devel readline-devel glibc-devel
BuildRequires: libssl-devel
BuildRequires: %_bindir/tclsh
BuildRequires: tcl-devel
BuildRequires: zlib-devel

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

%package tcl
Summary: Tcl module for the sqlite3 embeddable SQL database engine
Group: Development/Tcl
Requires: %name = %EVR
Conflicts: sqlite3-tcl

%description tcl
This package contains the tcl modules for %name.

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
	TCLLIBDIR=%_tcllibdir

# rpath removal
subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%makeinstall_std

install -d %buildroot%_tcllibdir/sqlite3
mv %buildroot%_tcllibdir/pkgIndex.tcl \
	%buildroot%_tcllibdir/sqlite3/

install -D -m0644 sqlcipher.1 %buildroot%_man1dir/sqlcipher.1

%if ! %{with static}
rm -f %buildroot%_libdir/*.{la,a}
%endif

%check
#make testfixture
#./testfixture test/all.test

%files
%doc *.md doc/*
%_bindir/sqlcipher
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/sqlcipher
%_libdir/*.so
%_pkgconfigdir/*.pc

%files tcl
%_tcllibdir/*

%changelog
* Wed Aug 21 2024 Andrey Cherepanov <cas@altlinux.org> 4.6.1-alt1
- New version.

* Tue May 21 2024 Andrey Cherepanov <cas@altlinux.org> 4.6.0-alt1
- New version.

* Thu Apr 25 2024 Andrey Cherepanov <cas@altlinux.org> 4.5.7-alt1
- New version.

* Thu Jan 18 2024 Andrey Cherepanov <cas@altlinux.org> 4.5.6-alt1
- New version.

* Thu Aug 31 2023 Andrey Cherepanov <cas@altlinux.org> 4.5.5-alt1
- New version.

* Fri Apr 28 2023 Andrey Cherepanov <cas@altlinux.org> 4.5.4-alt1
- New version.

* Wed Dec 21 2022 Andrey Cherepanov <cas@altlinux.org> 4.5.3-alt1
- New version.

* Thu Aug 04 2022 Andrey Cherepanov <cas@altlinux.org> 4.5.2-alt1
- New version.

* Fri Mar 04 2022 Andrey Cherepanov <cas@altlinux.org> 4.5.1-alt1
- New version.

* Fri Oct 29 2021 Andrey Cherepanov <cas@altlinux.org> 4.5.0-alt1
- New version.

* Wed Mar 03 2021 Andrey Cherepanov <cas@altlinux.org> 4.4.3-alt1
- New version.

* Thu Nov 26 2020 Andrey Cherepanov <cas@altlinux.org> 4.4.2-alt1
- New version.

* Sat Nov 07 2020 Andrey Cherepanov <cas@altlinux.org> 4.4.1-alt1
- New version.

* Thu May 14 2020 Andrey Cherepanov <cas@altlinux.org> 4.4.0-alt1
- New version.

* Mon Dec 23 2019 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version.

* Sat Jun 01 2019 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- New version.

* Tue Mar 19 2019 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1
- New version.

* Wed Dec 19 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.1-alt1
- New version.

* Tue Dec 04 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version.
- Disable tests.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 3.4.2-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Mon Dec 25 2017 Andrey Cherepanov <cas@altlinux.org> 3.4.2-alt1
- New version.

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1
- New version
- Remove obsoleted patches

* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt2
- Added tcl subpackage

* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1
- Version 3.2.0

* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus

* Tue Aug 13 2013 Abel Luck <abel@outcomedubious.im> - 2.2.1-1
- Initial SQLCipher package based on SQLite 3.7.17


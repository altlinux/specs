Name: ustr
Version: 1.0.4
Release: alt2
Summary: String library, very low memory overhead, simple to import
Group: System/Libraries
License: MIT or LGPLv2+ or BSD
Url: http://www.and.org/ustr/
Source0: http://www.and.org/ustr/%version/%name-%version.tar.gz
%description
 Micro string library, very low overhead from plain strdup() (Ave. 44%% for
0-20B strings). Very easy to use in existing C code. At it's simplest you can
just include a single header file into your .c and start using it.
 This package also distributes pre-built shared libraries.


%package -n lib%name
Summary: String library, very low memory overhead, simple to import
Group: System/Libraries

%description -n lib%name
 Micro string library, very low overhead from plain strdup() (Ave. 44%% for
0-20B strings). Very easy to use in existing C code. At it's simplest you can
just include a single header file into your .c and start using it.
 This package also distributes pre-built shared libraries.

%description -n lib%name
 Micro string library, very low overhead from plain strdup() (Ave. 44%% for
0-20B strings). Very easy to use in existing C code. At it's simplest you can
just include a single header file into your .c and start using it.
 This package also distributes pre-built shared libraries.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: pkg-config >= 0.14
Requires: lib%name = %version-%release

%description -n lib%name-devel
 Header files for the Ustr string library, and the .so to link with.
 Also includes a %name.pc file for pkg-config usage.
 Includes the ustr-import tool, for if you jsut want to include
the code in your projects ... you don't have to link to the shared lib.

%package -n lib%name-devel-static
Summary: Static development files for %name
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
 Static library for the Ustr string library.

%package -n lib%name-devel-debug
Summary: Development files for %name, with debugging options turned on
Group: Development/C
Requires: pkg-config >= 0.14
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-debug
 Header files and dynamic libraries for a debug build of the Ustr string
library.
 Also includes a %name-debug.pc file for pkg-config usage.

%package -n lib%name-devel-debug-static
Summary: Static development files for %name, with debugging options turned on
Group: Development/C
Requires: lib%name-devel-debug = %version-%release

%description -n lib%name-devel-debug-static
 Static library for the debug build of the Ustr string library.

%prep
%setup -q

%build
%make_build CFLAGS="${CFLAGS:-%optflags}"


%install
%makeinstall

%files -n lib%name
%_libdir/libustr-1.0.so.*
%doc ChangeLog LICENSE* README NEWS

%files -n lib%name-devel
%_datadir/ustr-%version
%_bindir/ustr-import
%_includedir/ustr.h
%_includedir/ustr-*.h
%exclude %_includedir/ustr*debug*.h
%_libdir/pkgconfig/ustr.pc
%_libdir/libustr.so
%_datadir/doc/ustr-devel-%version
%_mandir/man1/*
%_mandir/man3/*

%files -n lib%name-devel-static
%_libdir/libustr.a

%files -n lib%name-devel-debug
%_libdir/libustr-debug-1.0.so.*
%_libdir/libustr-debug.so
%_includedir/ustr*debug*.h
%_libdir/pkgconfig/ustr-debug.pc

%files -n lib%name-devel-debug-static
%_libdir/libustr-debug.a

%changelog
* Sat Dec 20 2008 Anton Farygin <rider@altlinux.ru> 1.0.4-alt2
- requires fixed

* Sat Dec 20 2008 Anton Farygin <rider@altlinux.ru> 1.0.4-alt1
- first build for Sisyphus, based on specfile from Fedora

Name: libwinevbs
Version: 0.10.4
Release: alt1

Summary: Native Wine VBScript engine as a C library

License: LGPL-2.1-or-later
Group: System/Libraries
URL: https://github.com/vpinball/libwinevbs
# Source-url: https://github.com/vpinball/libwinevbs/archive/bcc790e58d394b282c327feca2a7c921ca022e8d.tar.gz
Source: %name-%version.tar

Patch0: libdir.patch
Patch1: test-32bit.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake gcc bison

%description
A cross-platform VBScript engine extracted from Wine and packaged as a
standalone native C library with COM and OLE automation support.

%package -n libwinevbs0
Summary: Native Wine VBScript runtime library
Group: System/Libraries

%description -n libwinevbs0
Shared library implementing native Wine VBScript and COM/OLE functionality.

%package devel
Summary: Development files for libwinevbs
Group: Development/C

%description devel
Headers, ATL/Wine compatibility headers and pkg-config metadata for
building applications against libwinevbs.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%cmake \
    -DPLATFORM=linux \
    -DARCH=x64 \
    -DBUILD_SHARED=ON \
    -DBUILD_STATIC=OFF \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DCMAKE_INSTALL_LIBEXECDIR=%_libexecdir
%cmake_build

%install
%cmake_install
install -Dpm0644 /dev/null %buildroot%_libdir/pkgconfig/winevbs.pc
cat > %buildroot%_libdir/pkgconfig/winevbs.pc <<'EOF_PC'
prefix=%_prefix
exec_prefix=${prefix}
libdir=%_libdir
includedir=${prefix}/include

Name: winevbs
Description: Native Wine VBScript engine
Version: %version
Libs: -L${libdir} -lwinevbs
Cflags: -I${includedir}/libwinevbs/atl -I${includedir}/libwinevbs/atlmfc -I${includedir}/libwinevbs/wine -I${includedir}/libwinevbs -I${includedir}/wine/windows
EOF_PC

%files -n libwinevbs0
%_libdir/libwinevbs.so.0
%_libdir/libwinevbs.so.0.*

%files devel
%_includedir/libwinevbs/
%_libdir/libwinevbs.so
%_libdir/pkgconfig/winevbs.pc
%_libexecdir/libwinevbs/

%changelog
* Fri Nov 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.10.4-alt1
- new version (0.10.4)


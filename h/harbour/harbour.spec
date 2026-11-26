%define abi 3.2

Name: harbour
Version: 3.2.0
Release: alt1
Summary: Clipper-compatible xBase compiler and runtime

License: GPL-2.0-or-later AND GPL-2.0-or-later WITH harbour-exception AND CC-BY-SA-4.0
Group: Development/Other
URL: https://github.com/harbour/core
# Source-url: https://github.com/harbour/core/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

# hbmk2 needs a real compiler; /usr/bin/gcc alone only pulls gcc-common.
Requires: gcc
Requires: libharbour-devel = %EVR

BuildRequires: gcc-c++ pkgconfig(libpcre) pkgconfig(zlib) pkgconfig(ncurses)

%description
Harbour is a portable compiler for the xBase language, compatible with Clipper.
This package provides the compiler, hbpp preprocessor, hbmk2 build tool,
hbrun script runner, message compiler and regression test utility.
Contributed libraries are built separately from the core distribution.

%package -n libharbour%abi
Summary: Harbour shared runtime library
License: GPL-2.0-or-later WITH harbour-exception
Group: System/Libraries

%description -n libharbour%abi
Shared virtual machine, xBase runtime, DBF/NTX/CDX database drivers and
terminal backends for Harbour programs.

%package -n libharbour-devel
Summary: Headers and libraries for Harbour development
License: GPL-2.0-or-later WITH harbour-exception
Group: Development/Other
Requires: libharbour%abi = %EVR
# hbmk2 needs the Harbour compiler as well as these development files.
Requires: %name = %EVR
# hbmk2 static links need the system libraries' development linker names.
Requires: pkgconfig(libpcre) pkgconfig(zlib) pkgconfig(ncurses)

%description -n libharbour-devel
Public C and Harbour headers, extern symbol lists, shared-library linker name
and core static archives for hbmk2. The archives are required for explicit
static builds and for compiler and startup support in shared builds.
These files also support building the separate Harbour contrib distribution.

%prep
%setup
# The core uses system PCRE 1 and zlib. Other hosted libraries belong to
# contribs, which are deliberately excluded from this source package build.
rm -rf src/3rd/pcre src/3rd/zlib src/3rd/png src/3rd/jpeg

%build
# Upstream README.md: Build Options. Explicit paths prevent bundled fallback;
# disable dependency autodetection so optional backends cannot change the build.
export HB_INSTALL_PREFIX=%_prefix HB_SYSLOC=yes
export HB_BUILD_CONTRIBS=no HB_BUILD_3RDEXT=no
export HB_BUILD_DYN=yes HB_BUILD_SHARED=yes HB_BUILD_STRIP=no
export HB_WITH_PCRE=%_includedir/pcre HB_WITH_ZLIB=%_includedir
export HB_WITH_CURSES=%_includedir HB_WITH_SLANG=no HB_WITH_GPM=no HB_WITH_X11=no
export HB_WITH_BZIP2=no HB_WITH_EXPAT=no HB_WITH_JPEG=no HB_WITH_PNG=no
export HB_WITH_SQLITE3=no HB_WITH_MINIZIP=no
# hbmk2 consumes the static archives directly; preserve native code with LTO.
export HB_USER_CFLAGS="%optflags -ffat-lto-objects"
export HB_USER_LDFLAGS="%optflags %{?build_ldflags}"
export HB_USER_DFLAGS="%optflags %{?build_ldflags}"
%make_build

%install
export HB_INSTALL_PREFIX=%_prefix HB_SYSLOC=yes
export HB_BUILD_CONTRIBS=no HB_BUILD_3RDEXT=no
export HB_BUILD_DYN=yes HB_BUILD_SHARED=yes HB_BUILD_STRIP=no
export HB_WITH_PCRE=%_includedir/pcre HB_WITH_ZLIB=%_includedir
export HB_WITH_CURSES=%_includedir HB_WITH_SLANG=no HB_WITH_GPM=no HB_WITH_X11=no
export HB_WITH_BZIP2=no HB_WITH_EXPAT=no HB_WITH_JPEG=no HB_WITH_PNG=no
export HB_WITH_SQLITE3=no HB_WITH_MINIZIP=no
export HB_USER_CFLAGS="%optflags -ffat-lto-objects"
export HB_USER_LDFLAGS="%optflags %{?build_ldflags}"
export HB_USER_DFLAGS="%optflags %{?build_ldflags}"
export HB_INSTALL_PKG_ROOT=%buildroot
export HB_INSTALL_BIN=%buildroot%_bindir
export HB_INSTALL_INC=%buildroot%_includedir/harbour
export HB_INSTALL_LIB=%buildroot%_libdir/harbour
export HB_INSTALL_DYN=%buildroot%_libdir
export HB_INSTALL_ETC=%buildroot%_sysconfdir/harbour
export HB_INSTALL_MAN=%buildroot%_mandir
export HB_INSTALL_DOC=%buildroot%_docdir/%name-%version
%makeinstall_std
# hbmk2 implements the documented hbrun alias itself; no contrib extensions.
ln -s hbmk2 %buildroot%_bindir/hbrun
# Compiler-only bootstrap archive, unused by installed hbmk2.
rm -f %buildroot%_libdir/harbour/libhbnortl.a
# The shared library is installed into the standard loader search directory.
rm -f %buildroot%_sysconfdir/ld.so.conf.d/harbour.conf
# Upstream development scripts are not installed compiler tools.
rm -f %buildroot%_bindir/{3rdpatch.hb,check.hb,commit.hb,harbour.ucf}

%files
%_bindir/*
%_mandir/man1/*
%dir %_sysconfdir/harbour
%config(noreplace) %_sysconfdir/harbour/hb-charmap.def
%docdir %_docdir/%name-%version
%_docdir/%name-%version

%files -n libharbour%abi
%_libdir/libharbour.so.%{abi}*

%files -n libharbour-devel
%_includedir/harbour
%_libdir/harbour
%_libdir/libharbour.so

%changelog
* Thu Nov 26 2026 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- initial build for ALT Linux.

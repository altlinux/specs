%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define abiversion 1

Name: tbox
Version: 1.8.0
Release: alt1

Summary: A glib-like multi-platform c library
License: Apache-2.0
Group: System/Libraries
Url: https://tboox.top
VCS: https://github.com/tboox/tbox

Source: %name-%version.tar
Patch: %name-%version-alt-fix-DESTDIR-configure.patch
Patch1: %name-%version-alt-add-relwithdebinfo-mode.patch

BuildRequires: gcc-c++
BuildRequires: chrpath

%description
TBOX is a glib-like cross-platform C library that is simple to use yet
powerful in nature.

The project focuses on making C development easier and provides many
modules (.e.g stream, coroutine, regex, container, algorithm ...), so
that any developer can quickly pick it up and enjoy the productivity
boost when developing in C language.

It supports the following platforms: Windows, Macosx, Linux, Android,
iOS, *BSD and etc.

And it provides many compiling options using xmake:
- Release: Disable debug information, assertion, memory checking and
enable optimization.
- Debug: Enable debug information, assertion, memory checking and
disable optimization.
- Small: Disable all extensional modules and enable space optimization.
- Micro: compiling micro library (~64K) for the embed system.

%package -n lib%name%abiversion
Summary: Shared library for %name
Group: System/Libraries

%description -n lib%name%abiversion
This package contains shared library for software that requires %name.

%package -n lib%name-demo
Summary: Demo for %name
Group: Development/C
Requires: lib%name%abiversion = %EVR

%description -n lib%name-demo
This package contains demo for %name.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name%abiversion = %EVR

%description -n lib%name-devel
This package contains headers and libraries for building software that
uses %name.

# skip platform-dependent requires
%add_findreq_skiplist %_includedir/*/platform/android/*
%add_findreq_skiplist %_includedir/*/platform/windows/*

%prep
%setup
%autopatch -p1
cat > %name.pc << EOF
prefix=%_prefix
exec_prefix=\${prefix}
libdir=%_libdir
includedir=%_includedir

Name: %name
Description: %summary
Version: %version
Libs: -Ltbox
Cflags: -I\${includedir}/%name
EOF

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%configure \
    --mode=relwithdebinfo \
    --kind=shared \
    --force_utf8=yes \
    --hash=yes \
    --charset=yes
%make_build

%install
%makeinstall_std
chrpath -d %buildroot%_bindir/demo
mv %buildroot%_bindir/demo %buildroot%_bindir/%name-demo
install -Dm 644 %name.pc %buildroot%_pkgconfigdir/%name.pc

%files -n lib%name%abiversion
%doc LICENSE.md
%_libdir/*.so.%abiversion
%_libdir/*.so.%abiversion.*

%files -n lib%name-demo
%_bindir/%name-demo

%files -n lib%name-devel
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/%name.pc

%changelog
* Tue Apr 14 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 1.8.0-alt1
- Initial build for ALT.


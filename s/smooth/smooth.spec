%ifarch %ix86 x86_64
%define systemlibcpuid config=systemlibcpuid
%else
%define systemlibcpuid %nil
%endif

Name: smooth
Version: 0.9.10
Release: alt1.gita7e64e52

Summary: The smooth Class Library

License: Artistic-2.0
Group: System/Libraries
URL: http://www.smooth-project.org
VCS: https://github.com/enzo1982/smooth

Packager: Alexander Kovalev <alexvk@altlinux.org>

Source: %name-%version.tar

Patch: %name-%version-%release.patch
Patch1: alt-fix-underlinked-libX11.patch

BuildRequires: gcc-c++
BuildRequires: bzlib-devel
%ifarch %ix86 x86_64
BuildRequires: libcpuid-devel
%endif
BuildRequires: libcurl-devel
BuildRequires: libfribidi-devel
BuildRequires: libgtk+3-devel
BuildRequires: libjpeg-devel
BuildRequires: libxml2-devel

%description
smooth is an object oriented C++ class library for Windows, macOS,
Linux and most Unix-like operating systems. It provides basic
functionality and platform support for applications and libraries.

%package -n lib%name
Summary: Library of %name
Group: System/Libraries

%description -n lib%name
This package contains library for %name.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C++

%description -n lib%name-devel
This package contains header files for lib%name.

%prep
%setup
%autopatch -p1
sed -i 's|/usr/lib|%_libdir|g' classes/system/dynamicloader.cpp
find . -type f -exec sed -i 's|/usr/local|%_prefix|g' {} \;
sed -i 's|^LIBDIR = lib$|LIBDIR = %_lib|;
	s|(prefix)/lib$|(prefix)/%_lib|' Makefile-options

%build
export CFLAGS="%optflags"
export CXXFLAGS="$CFLAGS"
export OBJCFLAGS="$CFLAGS"
export OBJCXXFLAGS="$CFLAGS"
%make_build %systemlibcpuid

%install
%makeinstall_std

%files
%doc *.md ChangeLog Copying doc/reference/
%_bindir/%name-*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Tue Oct 14 2025 Alexander Kovalev <alexvk@altlinux.org> 0.9.10-alt1.gita7e64e52
- Initial build for ALT.

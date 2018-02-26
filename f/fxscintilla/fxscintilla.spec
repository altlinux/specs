# vim: set ft=spec: -*- rpm-spec -*-

%define soversion 20

Name: fxscintilla
Version: 1.78.0
Release: alt1

Summary: Scintilla widget for the FOX GUI toolkit
Group: System/Libraries
License: LGPL
Url: http://www.nongnu.org/fxscintilla/

BuildRequires: gcc-c++ libfox-devel

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
FXScintilla is an implementation of the Scintilla widget for the
FOX GUI toolkit.

%package -n lib%name%soversion
Summary: Scintilla widget for the FOX GUI toolkit
Group: System/Libraries

%description -n lib%name%soversion
FXScintilla is an implementation of the Scintilla widget for the
FOX GUI toolkit.

%package -n lib%name-devel
Summary: Scintilla widget for the FOX GUI toolkit - development files.
Group: Development/C++
Requires: lib%name%soversion = %version-%release

%description -n lib%name-devel
FXScintilla is an implementation of the Scintilla widget for the
FOX GUI toolkit.

This package contains development files.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--enable-shared \
	--disable-static
%make_build

%install
%makeinstall_std
bzip -9 ChangeLog

%files -n lib%name%soversion
%doc README ChangeLog*
%_libdir/lib%name.so.%soversion
%_libdir/lib%name.so.%soversion.*

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/*
%_pkgconfigdir/*

%changelog
* Tue Jul 07 2009 Alexey I. Froloff <raorn@altlinux.org> 1.78.0-alt1
- Built for Sisyphus


Name:    libSDL2_Pango
Version: 2.1.5
Release: alt1

Summary: SDL2 port of SDL_Pango

License: LGPL-2.1
Group:   System/Libraries
Url:     https://github.com/markuskimius/SDL2_Pango

Packager: Grigory Ustinov <grenka@altlinux.org>

Source: %name-%version.tar

BuildRequires: libSDL2-devel
BuildRequires: libpango-devel

%description
SDL2_Pango is a library for graphically rendering
internationalized and tagged text in SDL2 using TrueType fonts.

%package devel
Summary: Development files for SDL2_pango
Group: Development/C
Requires: %name = %EVR

%description devel
Development files for SDL2_pango.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc COPYING AUTHORS ChangeLog NEWS README
%_libdir/*.so.4*

%files devel
%doc docs/html/*
%_includedir/SDL2_Pango.h
%_libdir/pkgconfig/SDL2_Pango.pc
%_libdir/*.so

%changelog
* Tue Apr 02 2024 Grigory Ustinov <grenka@altlinux.org> 2.1.5-alt1
- Initial build for Sisyphus.

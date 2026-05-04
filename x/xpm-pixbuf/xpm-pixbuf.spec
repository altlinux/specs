%define sover 0

Name: xpm-pixbuf
Version: 1.0.0
Release: alt1.d290a0c8.1
Summary: xpm-pixbuf library
License: LGPL-2.1
Group: System/Libraries
URL: https://gitlab.gnome.org/ZanderBrown/xpm-pixbuf
VCS: https://gitlab.gnome.org/ZanderBrown/xpm-pixbuf

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)

%description
xpm-pixbuf library.

%package -n lib%name%sover
Summary: xpm-pixbuf library
Group: Development/C

%description -n lib%name%sover
xpm-pixbuf library.

%package devel
Summary: xpm-pixbuf development files
Group: Development/C

%description devel
xpm-pixbuf development files.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files -n lib%name%sover
%_libdir/libxpm-pixbuf.so.%sover

%files devel
%_includedir/xpm-pixbuf.h
%_libdir/libxpm-pixbuf.so
%_libdir/pkgconfig/xpm-pixbuf.pc

%changelog
* Sun Jul 13 2025 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1.d290a0c8.1
- initial build

Name: surf-geometry
Version: 1.0.6
Release: alt1

Summary: Tool to visualize some real algebraic geometry

License: GPL-2.0-or-later
Group: Sciences/Mathematics
Url: https://surf.sourceforge.net/

Source: https://downloads.sourceforge.net/surf/surf-%version.tar.gz
Source1: %name.module.in

Patch: %name-min-max.patch
# Update from gtk+ 1.2 to 2.0
Patch1: %name-gtk2.patch
Patch2: surf-geometry-configure-c99.patch
Patch3: surf-geometry-c99.patch

BuildRequires: gcc-c++
BuildRequires: flex
BuildRequires: libcups-devel
BuildRequires: pkgconfig(gmp)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(zlib)
BuildRequires: environment(modules)
Requires: environment(modules)

%description
surf is a tool to visualize some real algebraic geometry:
plane algebraic curves, algebraic surfaces and hyperplane sections of surfaces.
surf is script driven and has (optionally) a nifty GUI using the Gtk widget set.

%prep
%setup -n surf-%version
%autopatch -p1

# Regenerate the configure script due to patch 1
%autoreconf

# Avoid extra directory and install binary and xpm file in same directory
sed -i 's|^\(pkgdatadir = $(datadir)\)/@PACKAGE@|\1|' Makefile.in
sed -i 's|/surf\(/surf\.xpm\)|\1|' gtkgui/showAbout.cc
chmod -x gtkgui/PrintImageDialog.{cc,h}

%build
export CFLAGS="${CFLAGS:-%optflags -fPIC}"
export CXXFLAGS="${CXXFLAGS:-%optflags -fPIC -std=c++14}"

%configure \
    --bindir=%_libdir/%name \
    --datadir=%_libdir/%name \
    --with-gmp=%prefix \
    --with-gtk=%prefix \
    --with-x
%make_build

%install
%makeinstall_std

# Based on 4ti2.spec
mkdir -p %buildroot%_datadir/modulefiles
sed 's#@BINDIR@#'%_libdir/%name'#g;' < %SOURCE1 > \
%buildroot%_datadir/modulefiles/%name-%_arch

mv %buildroot%_man1dir/surf.1 \
%buildroot%_man1dir/%name.1

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_libdir/%name
%_man1dir/%name.1*
%_datadir/modulefiles/%name-%_arch

%changelog
* Fri Nov 08 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.6-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
- Needed for Singular.

Name: grass
Version: 6.4.0
Release: alt2.3

%def_with mysql
%def_with postgres
%def_with sqlite

Summary: Geographic Resources Analysis Support System
License: %gpl2plus
Group: Sciences/Geosciences
URL: http://grass.itc.it/

Packager: Egor Vyscrebentsov <evyscr@altlinux.org>

Source: %name-%version.tar

Patch0: %name-6.4.0-alt-destdir.patch
Patch1: %name-6.4.0-alt-rpath.patch

%define grassfix 64
#define grassdir grass%grassfix
%define grassdir grass-6.4.0
%define grassdatadir /var/lib/grass%grassfix/data

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Mon Feb 19 2007
BuildRequires: flex gcc-c++ python-dev
BuildRequires: libfftw-devel libjpeg-devel libpng-devel libtiff-devel zlib-devel
BuildRequires: libncurses-devel libtinfo-devel
BuildRequires: libpq-devel postgresql-devel libMySQL-devel libsqlite3-devel
BuildRequires: libqt4-core libXmu-devel swig libfreetype-devel readline-devel libGLU-devel
BuildRequires: proj-devel libgdal-devel libproj-nad proj
BuildRequires: tcl-devel tk-devel
BuildRequires: libICE-devel, libSM-devel, libX11-devel, libXau-devel, libXaw-devel, libXrandr-devel, libXdmcp-devel, libXext-devel, libXfixes-devel, libXfont-devel, libXft-devel, libXi-devel, libXmu-devel, libXpm-devel, libXrender-devel, libXres-devel, libXScrnSaver-devel, libXinerama-devel, libXt-devel, libXtst-devel, libXxf86dga-devel, libXcomposite-devel, libXxf86vm-devel, libdmx-devel, libfontenc-devel, libGLU-devel, libXdamage-devel, libxkbfile-devel, xcursorgen, xorg-font-utils, libXvMC-devel, libXcursor-devel, libXevie-devel, libXv-devel, xorg-xtrans-devel, xorg-util-macros, xorg-sgml-doctools, xorg-compat-devel

%description
GRASS (Geographic Resources Analysis Support System) is an
open source, Free Software Geographical Information System (GIS)
with raster, topological vector, image processing, and graphics
production functionality that operates on various platforms
through a graphical user interface and shell in X-Window.

%package devel
Summary: Development files for GRASS
Group: Development/C
Requires: grass

%description devel
This package contains development headers for GRASS.

%package doc
Summary: Documentation for GRASS
Group: Documentation
BuildArch: noarch

%description doc
This package contains documentation for GRASS GIS.


%prep
%setup
%patch0 -p2
%patch1 -p2

%build
%configure \
	--prefix=%_libdir \
	--with-nls \
	--with-cxx \
	%{subst_with mysql} \
	--with-mysql-includes=/usr/include/mysql \
	%{subst_with postgres} \
	--with-postgres-includes=/usr/include/pgsql \
	%{subst_with sqlite} \
	--with-proj-share=/usr/share/proj \
	--with-python \
	--with-readline \
	--with-freetype \
	--with-freetype-includes=/usr/include/freetype2 \
	--enable-largefile

%make

%install
%makeinstall_std
#mkdir -p %buildroot%_menudir
#subst 's#GISBASE=.*#GISBASE=%_libdir/%{grassdir}#' \
#        %buildroot/usr/bin/grass%grassfix
#subst 's#mozilla-firefox#firefox#' %buildroot%_libdir/%grassdir/etc/Init.sh

#sed -i '/export GISBASE/ a \[ -z "$GISDBASE" ] && export GISDBASE=%grassdatadir' %buildroot%_bindir/grass%grassfix

#mkdir -p %buildroot%grassdatadir

#subst 's#GISDBASE=.*#GISDBASE=%{grassdatadir}#' \
#        %buildroot%grassdatadir/demolocation/.grassrc%grassfix

# Add makefiles to includes:
#cp -a include/Make %buildroot%_libdir/grass%grassfix/include/

mkdir -p %buildroot%_lockdir/grass%grassfix/

mkdir -p %buildroot/usr/share/doc/%grassdir
mv %buildroot%_libdir/%grassdir/docs/* %buildroot/usr/share/doc/%grassdir/
rm -fr %buildroot%_libdir/%grassdir/docs/
cd %buildroot%_libdir/%grassdir/
ln -s ../../share/doc/%grassdir/ docs
#Menu support:
#cat << EOF > $RPM_BUILD_ROOT%_menudir/%name
#?package(%name):command="%_bindir/grass%grassfix" \
#icon="%name.png" \
#needs="text" \
#section="Applications/Sciences/Geosciences" \
#title="Grass%grassfix" \
#longtitle="Geographic Resources Analysis Support System"
#EOF

%post
[ ! -L %_lockdir/grass62/locks ] || rm -f %_lockdir/grass62/locks
[ $1 -ne 1 ] || ln -s %_lockdir/grass%grassfix %_libdir/%grassdir/locks

%preun
rm -f  %_libdir/%grassdir/locks

%add_findreq_skiplist %_libdir/%grassdir/etc/*

%files
%_bindir/*
%dir %_libdir/%grassdir
%_libdir/%grassdir/AUTHORS
%_libdir/%grassdir/COPYING
%_libdir/%grassdir/CHANGES
%_libdir/%grassdir/docs
%_libdir/%grassdir/bin
%dir %_libdir/%grassdir/lib
#_libdir/%grassdir/lib/*.%{version}*.so
%_libdir/%grassdir/bwidget
%_libdir/%grassdir/driver
%_libdir/%grassdir/etc
%_libdir/%grassdir/fonts
%_libdir/%grassdir/locale
%_libdir/%grassdir/man
%_libdir/%grassdir/scripts
#_menudir/%name
%_libdir/%grassdir/lib/*.so
%_libdir/%grassdir/lib/*.a
%_libdir/%grassdir/tools
#_miconsdir/*.png
#_liconsdir/*.png
#_iconsdir/*.png
%attr(1777,root,root) %_lockdir/grass%grassfix/

%files devel
%_libdir/%grassdir/include

%files doc
%dir /usr/share/doc/%grassdir
/usr/share/doc/%grassdir

%changelog
* Fri Apr 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.4.0-alt2.3
- build fixed

* Fri Nov 19 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.4.0-alt2.2
- build fixed
- BuildRequires structured

* Mon Sep 20 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.4.0-alt2.1
- rebuild with MySQL 5.1

* Tue Sep 14 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.4.0-alt2
- 6.4.0 release
- docs moved to /usr/share (may cause problems) for fixing build

* Fri Sep 03 2010 Egor Vyscrebentsov <evyscr@altlinux.org> 6.4.0-alt1.rc6
- new version: 6.4.0 RC6
- enabled install section of spec with corresponding checks
- built with mysql,sqlite
- fixed lockdir symlinking
- doc subpackage
- devel subpackage

* Thu Dec 04 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.2.3-alt2
- build fixed 

* Mon Apr 07 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.2.3-alt1
- new upstream version: advanced vectors, new GUI

* Thu Aug 23 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.2.2-alt1
- first try by me

* Wed Feb 14 2007 Dmitri Kuzishchin <dim@altlinux.ru> 6.2.1-alt1
- Initial package.

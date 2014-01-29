
Name:    grass
Version: 6.4.3
Release: alt1

%def_with mysql
%def_with postgres
%def_with sqlite

Summary: Geographic Resources Analysis Support System
License: %gpl2plus
Group:   Sciences/Geosciences
URL:     http://grass.itc.it/

Packager: Egor Vyscrebentsov <evyscr@altlinux.org>

Source: %name-%version.tar

Patch0: %name-6.4.0-alt-destdir.patch
Patch1: %name-6.4.0-alt-rpath.patch
Patch2: %name-6.4.2-docfiles.patch 
Patch3: %name-6.4.3-platform_name_encoding.patch
Patch4: %name-pkgconf.patch
Patch5: %name-shlib-soname.patch

%define grassfix 64
#define grassdir grass%grassfix
%define grassdir grass-%version
%define grassdatadir /var/lib/grass%grassfix/data

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Mon Feb 19 2007
BuildRequires: flex gcc-c++ python-devel
BuildRequires: libfftw-devel libjpeg-devel libpng-devel libtiff-devel zlib-devel
BuildRequires: libncurses-devel libtinfo-devel
BuildRequires: libpq-devel postgresql-devel libMySQL-devel libsqlite3-devel
BuildRequires: libqt4-core libXmu-devel swig libfreetype-devel readline-devel libGLU-devel
BuildRequires: proj-devel libgdal-devel libproj-nad proj
BuildRequires: tcl-devel tk-devel
BuildRequires: libICE-devel, libSM-devel, libX11-devel, libXau-devel, libXaw-devel, libXrandr-devel, libXdmcp-devel, libXext-devel, libXfixes-devel, libXfont-devel, libXft-devel, libXi-devel, libXmu-devel, libXpm-devel, libXrender-devel, libXres-devel, libXScrnSaver-devel, libXinerama-devel, libXt-devel, libXtst-devel, libXxf86dga-devel, libXcomposite-devel, libXxf86vm-devel, libdmx-devel, libfontenc-devel, libGLU-devel, libXdamage-devel, libxkbfile-devel, xcursorgen, xorg-font-utils, libXvMC-devel, libXcursor-devel, libXevie-devel, libXv-devel, xorg-xtrans-devel, xorg-util-macros, xorg-sgml-doctools
BuildRequires: gccmakedep, imake, lndir, makedepend, rman, xorg-cf-files
BuildRequires: libcairo-devel
BuildRequires: libblas-devel
BuildRequires: libgeos-devel
BuildRequires: liblapack-devel
BuildRequires: lesstif-devel
BuildRequires: libGLw-devel
BuildRequires: libunixODBC-devel
BuildRequires: libwxGTK-devel
BuildRequires: python-module-wx-devel
BuildRequires: xorg-glproto-devel

%description
GRASS (Geographic Resources Analysis Support System) is an
open source, Free Software Geographical Information System (GIS)
with raster, topological vector, image processing, and graphics
production functionality that operates on various platforms
through a graphical user interface and shell in X-Window.

%package -n lib%name
Summary: GRASS (Geographic Resources Analysis Support System) runtime libraries
Group: Sciences/Geosciences
Provides: %name-docs = %version-%release
Obsoletes: %name-docs < %version-%release

%description -n lib%name
GRASS (Geographic Resources Analysis Support System) runtime libraries.

%package devel
Summary: Development files for GRASS
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development headers for GRASS.

%prep
%setup
#%patch0 -p2
%patch1 -p2
%patch2 -p1
%patch3 -p4
%patch4 -p0
%patch5 -p1

%build
%configure \
	--prefix=%_libdir \
	--with-nls \
	--with-cxx \
	--enable-largefile \
	--enable-shared \
	--with-blas \
	--with-cairo \
	--with-cxx \
	--with-fftw \
	--with-freetype-includes=%{_includedir}/freetype2 \
	--with-freetype=yes \
	--with-gdal \
	--with-geos \
	--with-glw \
	--with-lapack \
	--with-motif \
	%{subst_with mysql} \
	--with-mysql-includes=%{_includedir}/mysql \
	--with-nls \
	--with-odbc \
	--with-opengl \
	%{subst_with postgres} \
	--with-postgres-includes=/usr/include/pgsql \
	--with-proj \
	--with-proj-share=%{_datadir}/proj \
	--with-python \
	--with-readline \
	%{subst_with sqlite} \
	--with-wxwidgets=wx-config \
	--with-x

%make

%install
#%make_install install INST_DIR=%buildroot BINDIR=%buildroot%_bindir
%makeinstall BINDIR=%buildroot%_bindir PREFIX=%buildroot%_prefix install

# Change GISBASE in startup script to point to systems %{_libdir}/%{name}-%{version}
#TODO: Still necessary? Version-less?
sed -i -e "1,\$s&^GISBASE.*&GISBASE=%_libdir/%grassdir&"  \
	%buildroot%_bindir/%name%grassfix

# Sadly, parts of the following can't be done safely in prep,
# hence they're done here
# Replace GISBASE environment variable with paths that match our documentation file layout
sed -i -e 's|$env(GISBASE)/docs/|%_docdir/%grassdir/docs/|' \
    %buildroot%_prefix/%grassdir/etc/gis_set.tcl \
    %buildroot%_prefix/%grassdir/etc/gui.tcl \
    %buildroot%_prefix/%grassdir/etc/nviz2.2/scripts/nviz2.2_script
sed -i -e 's|C_BASE="$GISBASE"|C_BASE=\"%_docdir/%grassdir/docs"|g' \
    %buildroot%_prefix/%grassdir/scripts/g.manual
sed -i -e 's|%grassdir/docs|%grassdir|g' \
    %buildroot%_prefix/%grassdir/scripts/g.manual
sed -i -e 's|(\"GISBASE\"), \"docs\", \"html\", \"icons\", \"silk\")|(\"GISBASE\"), \"icons\", \"silk\")|g' \
    %buildroot%_prefix/%grassdir/etc/wxpython/icons/icon.py
sed -i -e 's|self.fspath = os.path.join(gisbase|self.fspath = os.path.join("%_docdir/%grassdir\"|' \
    %buildroot%_prefix/%grassdir/etc/wxpython/gui_core/ghelp.py
sed -i 's|file://$env(GISBASE)|file://%_docdir/%grassdir|' %buildroot%_prefix/%grassdir/etc/r.li.setup/r.li.setup.main
sed -i 's|GRASS_DOC_BASE=`check_docbase "$GISBASE"`|GRASS_DOC_BASE=%_docdir/%grassdir|' %buildroot%_prefix/%grassdir/scripts/g.manual

# Exceptional path for files used in the GUI as well
#TODO: Could include them in the main package too
sed -i -e 's|os\.getenv("GISBASE")|\"%_docdir/%name-libs-%version\"|' \
    %buildroot%_prefix/%grassdir/etc/wxpython/gui_core/ghelp.py

#TODO: Quotes and linebreaks in sed calls
# Replace GISBASE environment variable with paths that match our locale file layout
sed -i -e 's|os.path.join(os.getenv("GISBASE"), '\''locale'\''|os.path.join('\''%_datadir'\'', '\''locale'\''|' -e 's|os.path.join(os.getenv("GISBASE"), "etc"|os.path.join(\"%_libdir/%grassdir\", "etc"|' -e 's|self.gisbase  = os.getenv("GISBASE")|self.gisbase = "%_docdir/%grassdir"|' %buildroot%_prefix/%grassdir/etc/wxpython/*.py %buildroot%_prefix/%grassdir/etc/python/grass/script/*.py

# Make grass headers and libraries available on the system
mv %buildroot%_prefix/%grassdir/lib/ %buildroot%_libdir
mv %buildroot%_prefix/%grassdir/include %buildroot%_prefix/
rm -rf %buildroot%_includedir/Make

# Create universal multilib header bz#341391
#install -p -m 644 %%buildroot%%_includedir/%%name/config.h \
#           %%buildroot%%_includedir/%%name/config-%%cpuarch.h
#install -p -m 644 %%SOURCE2 %%buildroot%%_includedir/%%name/config.h

#TODO: Do we still need this?
# Fix prelink issue bz#458427
#mkdir -p %%buildroot%%_sysconfdir/prelink.conf.d
#cat > %%buildroot%%_sysconfdir/prelink.conf.d/%%name-%%cpuarch.conf <<EOF
#-b %%_libdir/libgrass_gproj.so.6.4.0
#-b %%_libdir/libgrass_sim.so.6.4
#EOF

# Make man pages available on system, convert to utf8 and avoid name conflict with "parallel" manpage
mkdir -p %buildroot%_mandir/man1
for manpage in `find  %buildroot%_prefix/%grassdir/man/man1 -type f` ; do
   iconv -f iso8859-1 -t utf8 \
        $manpage > %buildroot%_mandir/man1/`basename $manpage`"grass"
done
sed -i -e 's/^.TH \(.*\) 1/.TH \1 1grass/' %buildroot%_mandir/man1/*
rm -rf %buildroot%_prefix/%grassdir/man

# Make locales available on system, correct case for pt_br locale
mkdir -p %buildroot%_datadir/locale/
mv %buildroot%_prefix/%grassdir/locale %buildroot%_datadir/
mv %buildroot%_datadir/locale/pt_br %buildroot%_datadir/locale/pt_BR

# Create versionless symlinks for binary and libdir
# The libdir symlink is handy for QGIS. QGIS asks the user for gisbase
# and then stores it. See Fedora BZ 711860
# Ubuntu does it the same way
#
# The binary symlink may keeps us from creating the desktop file
# And we will can just pack it
ln -s %_bindir/%name%grassfix %buildroot%_bindir/%name
ln -s %_libdir/%grassdir %buildroot%_libdir/%name

%find_lang %{name}mods
%find_lang %{name}libs
%find_lang %{name}wxpy

mkdir -p %buildroot%_libdir/pkgconfig
install -p -m 644 %name.pc %buildroot%_libdir/pkgconfig/

for res in 48x48 64x64; do
  mkdir -p %buildroot%_datadir/icons/hicolor/$res/apps
  install -p -m 644 gui/icons/%name-$res.png %buildroot%_datadir/icons/hicolor/$res/apps/%name.png
done

# Correct permissions
#TODO: Still necessary; create a ticket and/or change in prep
#TODO: Why are the permissions right in Ubuntu?
find %buildroot -name "*.tcl" -exec chmod +r-x '{}' \;
chmod -x %buildroot%_prefix/%grassdir/etc/nviz2.2/scripts/configIndex
chmod -x %buildroot%_prefix/%grassdir/etc/nviz2.2/scripts/nviz_params
chmod -x %buildroot%_prefix/%grassdir/etc/nviz2.2/scripts/tclIndex
chmod -x %buildroot%_prefix/%grassdir/etc/nviz2.2/scripts/panelIndex
chmod +x %buildroot%_prefix/%grassdir/etc/g.mapsets.tcl
chmod +x %buildroot%_prefix/%grassdir/etc/dm/tksys.tcl
chmod +x %buildroot%_prefix/%grassdir/etc/gm/tksys.tcl
chmod +x %buildroot%_prefix/%grassdir/etc/gm/animate.tcl

# fixup few nviz script header, it will anyway always be executed by nviz
for nviz in {script_play,nviz2.2_script,script_tools,script_file_tools,script_get_line}; do
 cat %buildroot%_prefix/%grassdir/etc/nviz2.2/scripts/$nviz \
  | grep -v '#!nviz' > %buildroot%_prefix/%grassdir/etc/nviz2.2/scripts/$nviz.tmp 
 mv  %buildroot%_prefix/%grassdir/etc/nviz2.2/scripts/$nviz.tmp \
     %buildroot%_prefix/%grassdir/etc/nviz2.2/scripts/$nviz
done

# Move icon folder in GISBASE and set its path to be FHS compliant
mv %buildroot%_prefix/%grassdir/docs/html/icons %buildroot%_prefix/%grassdir/

# Switch to the system wide docs, to be FHS compliant
rm -rf %buildroot%_prefix/%grassdir/docs

# Hide GISBASE into system's %_libdir instead, to be FHS compliant
mv %buildroot%_prefix/%grassdir %buildroot%_libdir/

# Correct font path
sed -i -e 's|%buildroot%_prefix/%grassdir|%_libdir/%grassdir|' \
%buildroot%_libdir/%grassdir/etc/fontcap

# Remove service scripts
rm -rf %buildroot%_libdir/%grassdir/tools

%post
[ ! -L %_lockdir/grass62/locks ] || rm -f %_lockdir/grass62/locks
[ $1 -ne 1 ] || ln -s %_lockdir/grass%grassfix %_libdir/%grassdir/locks

%preun
rm -f %_libdir/%grassdir/locks

%add_findreq_skiplist %_libdir/%grassdir/etc/*

%files -f %{name}mods.lang -f %{name}libs.lang -f %{name}wxpy.lang
%_bindir/*
%dir %_libdir/%grassdir
%_libdir/%grassdir/*
%_iconsdir/hicolor/*/apps/%name.png

%files -n lib%name
%doc AUTHORS COPYING GPL.TXT CHANGES ChangeLog_%version.gz translators.csv contributors.csv contributors_extra.csv doc
%_libdir/lib%{name}_*.so.*
%_libdir/%grassdir/etc/*.table
%_libdir/%grassdir/driver/db/*

%files devel
%doc TODO doc SUBMITTING*
%_pkgconfigdir/%name.pc
%_includedir/%name
%_libdir/lib%{name}_*.so

%changelog
* Tue Jan 28 2014 Andrey Cherepanov <cas@altlinux.org> 6.4.3-alt1
- New version
- Add support of useful bindings
- Move libraries to libgrass (ALT #15725)

* Fri Jun 07 2013 Ivan Ovcherenko <asdus@altlinux.org> 6.4.2-alt1.2
- Create versionless symlinks

* Thu Mar 28 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.4.2-alt1.1
- build fixed

* Fri Feb 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.4.2-alt1
- 6.4.2
- build fixed

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

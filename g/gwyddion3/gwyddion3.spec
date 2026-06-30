%def_disable with_gtk_devel

# sorry 64bit only!
ExcludeArch: i586

Name: gwyddion3
Version: 3.11
Release: alt1

Summary: An SPM data visualization and analysis tool
Summary(ru_RU.UTF-8):  Программа для визуализации и анализа данных АСМ

Group: Sciences/Other
License: GPLv2+
Url: http://gwyddion.net/

Source: %name-%version.tar.gz


BuildRequires(pre): libGConf-devel
BuildRequires: gcc-c++
BuildRequires: gtk-doc
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: libgtk+3-gir-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: zlib-devel
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(OpenEXR)
BuildRequires: pkgconfig(cfitsio)
BuildRequires: pkgconfig(libpng)
BuildRequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: findutils
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(gtksourceview-3.0)
BuildRequires: pkgconfig(libzip)
#BuildRequires: pkgconfig(jansson)
BuildRequires: pkgconfig(hdf5)
BuildRequires: hdf5-tools
BuildRequires: sed
BuildRequires: python3
BuildRequires: pkgconfig(fftw3)
BuildRequires: gobject-introspection-devel
BuildRequires: pkgconfig(epoxy)
BuildRequires: /proc



%define _gtkdocdir %_datadir/gtk-doc/html/%name
%define pkglibdir %_libdir/%name
%define pkglibexecdir %_libexecdir/%name
%define pkgdatadir %_datadir/%name
%define pkgincludedir %_includedir/%name
%define libname lib%{name}


%description
Gwyddion is a modular SPM (Scanning Probe Microsopy) data visualization and
analysis tool written with Gtk+.

It can be used for all most frequently used data processing operations
including: leveling, false color plotting, shading, filtering, denoising, data
editing, integral transforms, grain analysis, profile extraction, fractal
analysis, and many more.  The program is primarily focused on SPM data analysis
(e.g. data obtained from AFM, STM, NSOM, and similar microscopes).  However, it
can also be used for analysis of SEM (Scanning Electron Microscopy) data or any
other 2D data.


%package -n %libname
Summary: Libraries and tools for %name
Group: System/Libraries
%description -n %libname
Libraries for %name.


%package -n lib%name-devel
Summary: Headers, libraries and tools for %name module development
Group: Development/C
Requires: %libname = %EVR
%description -n lib%name-devel
Header files, libraries and tools for %name module and plug-in development.

%if_enabled with_gtk_devel
%package -n %libname-gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %libname = %EVR
%description -n %libname-gir
GObject introspection data for %name

%package -n %libname-gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
Requires: %libname-devel = %EVR
Requires: %libname-gir = %EVR
BuildArch: noarch
%description -n %libname-gir-devel
GObject introspection devel data for %name
%endif

%package -n lib%name-doc
Summary: Docs for Gwyddion module development
Group: Development/C
BuildArch: noarch
Conflicts: lib%name-devel < %version-%release
%description -n lib%name-doc
This package contains the API docmentation.


%prep
%setup
%autopatch


%build
%autoreconf
%configure \
	CFLAGS='%optflags' CXXFLAGS='%optflags' \
	--disable-rpath \
	--with-html-dir=%_gtkdocdir
#	--enable-library-bloat 
	
# fix build errors. Unstable?
sed -i 's|#include "preview.h"|#include "../preview.h"|' modules/synth/*.c
# __hack__ to fix l18n file names not to conflict with gwyddion2
sed -i 's|PACKAGE = gwyddion|PACKAGE = gwyddion3|' po/Makefile


%make_build

%install
%makeinstall_std

# Install the icon to the hicolor theme *and* to %%_pixmapsdir because
# some distros expect it in one place, some in another.
mkdir -p %buildroot%_pixmapsdir
install pixmaps/60x60/apps/gwyddion.png %buildroot%_pixmapsdir/%name.png
%find_lang %name

# Get rid of .la files 
find %buildroot -name \*.la -print0 | xargs -0 rm -f

%files -f %name.lang
%_bindir/%name
%_bindir/%name-thumbnailer

%doc AUTHORS NEWS README THANKS
%dir %pkgdatadir
%dir %pkgdatadir/pixmaps
%pkgdatadir/pixmaps/*.png
%pkgdatadir/pixmaps/*.ico
%pkgdatadir/gradients/
%pkgdatadir/glmaterials/
%pkgdatadir/ui/
%pkgdatadir/user-guide-modules
%pkgdatadir/icons/
%pkgdatadir/drawings/
%_man1dir/*
#%_liconsdir/%name.png
%_pixmapsdir/%name.png
%pkglibdir/modules/cmap/*.so
%pkglibdir/modules/file/*.so
%pkglibdir/modules/graph/*.so
%pkglibdir/modules/image/*.so
%pkglibdir/modules/synth/*.so
%pkglibdir/modules/tool/*.so
%pkglibdir/modules/volume/*.so
%pkglibdir/modules/xyz/*.so

%dir %pkglibdir/modules/cmap
%dir %pkglibdir/modules/file
%dir %pkglibdir/modules/graph
%dir %pkglibdir/modules/image
%dir %pkglibdir/modules/synth
%dir %pkglibdir/modules/tool
%dir %pkglibdir/modules/volume
%dir %pkglibdir/modules/xyz
%dir %pkglibdir/modules
%dir %pkglibdir
%_desktopdir/%name.desktop
%_datadir/mime/packages/%name.xml
%_datadir/metainfo/*.xml
%_datadir/thumbnailers/*


%files -n %libname
%_libdir/*.so

%files -n lib%name-devel
%doc devel-docs/CODING-STANDARDS
%doc data/%name.vim
%pkgincludedir/*.h
%pkgincludedir/libgwyapp/*.h
%pkgincludedir/libgwyddion/*.h
%pkgincludedir/libgwyui/*.h
%dir %pkgincludedir/libgwyapp
%dir %pkgincludedir/libgwyddion
%dir %pkgincludedir/libgwyui
%dir %pkgincludedir
#%_libdir/*.so
%_pkgconfigdir/libgwyapp3.pc
%_pkgconfigdir/libgwyddion3.pc
%_pkgconfigdir/libgwyui3.pc
%pkglibdir/include/gwyconfig3.h
%dir %pkglibdir/include


%if_enabled with_gtk_devel
%files -n lib%name-gir
%_typelibdir/Gwy*.typelib

%files -n lib%name-gir-devel
%_girdir/Gwy*.gir
%endif


%files -n lib%name-doc
# Documentation
%doc %_gtkdocdir/libgwyapp/*
%doc %_gtkdocdir/libgwyddion/*
%doc %_gtkdocdir/libgwyui/*
%doc %dir %_datadir/gtk-doc
%doc %dir %_datadir/gtk-doc/html
%doc %dir %_gtkdocdir
%doc %dir %_gtkdocdir/libgwyapp
%doc %dir %_gtkdocdir/libgwyddion
%doc %dir %_gtkdocdir/libgwyui




%changelog
* Tue Jun 30 2026 Alexei Mezin <alexvm@altlinux.org> 3.11-alt1
- Initial build of officialy UNSTABLE version



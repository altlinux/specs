
Name: gwyddion
Version: 2.49
Release: alt1

Summary: An SPM data visualization and analysis tool
Summary(ru_RU.UTF-8):  Программа для визуализации и анализа данных АСМ

Group: Sciences/Other
License: GNU GPL
Url: http://gwyddion.net/

# Source-url: http://sourceforge.net/projects/gwyddion/files/gwyddion/%version/gwyddion-%version.tar.xz/download
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro libGConf-devel

BuildRequires: GConf gcc-c++ imake kde4libs-devel libfftw3-devel libgtkglext-devel libgtksourceview-devel libicu-devel
BuildRequires: libxml2-devel perl-Pod-Usage python-module-distribute python-module-pygtk-devel
BuildRequires: libgtk+2-devel pkg-config libgtkglext-devel libfftw3-devel chrpath kde4libs-devel libruby-devel

# File Format and some features support
BuildRequires: libminizip-devel libwebp-devel openexr-devel libcfitsio-devel libunique-devel

BuildPreReq: perl-podlators libpng-devel

%define _gtkdocdir %_datadir/gtk-doc/html
%define pkglibdir %_libdir/%name
%define pkglibexecdir %_libexecdir/%name
%define pkgdatadir %_datadir/%name
%define pkgincludedir %_includedir/%name
%define libname lib%{name}2
%add_python_req_skip %pkglibdir
%add_python_req_skip %pkgdatadir

# Stop auto picking wrong deps!
%add_findreq_skiplist %pkglibexecdir/plugins/process/*


%package -n %libname
Summary: Libraries and tools for Gwyddion
Group: System/Libraries

%package -n lib%name-devel
Summary: Headers, libraries and tools for Gwyddion module development
Group: Development/C
Requires: %libname = %version-%release

%package -n lib%name-doc
Summary: Docs for Gwyddion module development
Group: Development/C
BuildArch: noarch

%package thumbnailer-gconf
Summary: GConf schemas for gwyddion-thumbnailer integration
Group: Graphical desktop/GNOME
Requires: %name = %version-%release
Requires(pre):   GConf2
Requires(post):  GConf2
Requires(preun): GConf2

%package thumbnailer-kde4
Summary: KDE4 gwyddion thumbnailer module
Group: Graphical desktop/KDE
Requires: %name = %version-%release
# We do not actually link with them, but they own the module directory.
Requires: kde4libs >= 4.0

%package -n python-module-pygwy
Summary: Python tools for Gwyddion module development
Group: Development/Python
Requires: %libname = %version-%release


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

%description -n %libname
Libraries for %name.

%description -n lib%name-devel
Header files, libraries and tools for Gwyddion module and plug-in development.
This package also contains sample plug-ins in various programming languages.

%description -n lib%name-doc
This package contains the API docmentation.

%description thumbnailer-gconf
GConf schemas that register gwyddion-thumbnailer as thumbnailer for SPM files
in GNOME and XFce.

%description thumbnailer-kde4
Gwyddion-thumbnailer based KDE thumbnail creator extension module for SPM
files.

%description  -n python-module-pygwy
Python tools for Gwyddion module development

%prep
%setup

# Don't install .la files.
%__subst '/# Install the pseudo-library/,/^$/d' ltmain.sh
# Replace universal %_bindir/env shbang with the real thing.
%__subst '1s/env *//' plugins/process/*.{py,rb,pl}

%__subst 's|#include <pygtk-2.0/pygobject.h>|#include <pygtk/pygobject.h>|' modules/pygwy/pygwy.c
%__subst 's|#include <pygtk-2.0/pygobject.h>|#include <pygtk/pygobject.h>|' modules/pygwy/gwy.c

# Fix libpython linking
%__subst 's|--ldflags|--libs|' m4/gwy-python.m4

%build
autoconf -f
%configure \
	CFLAGS='%optflags -I%_K4includedir'  \
	CXXFLAGS='%optflags -I%_K4includedir'  \
	--with-kde4-thumbnailer \
	--disable-rpath \
	--with-gconf-schema-file-dir=%_sysconfdir/gconf/schemas \
	--enable-library-bloat 
%make_build

%install
%makeinstall_std
# Install the icon to the hicolor theme *and* to %_pixmapsdir because
# some distros expect it in one place, some in another.
mkdir -p %buildroot%_pixmapsdir
install pixmaps/%name.png %buildroot%_pixmapsdir
%find_lang %name

# Get rid of .la files if some silly distros (hello Mandriva) overwrote our
# fixed libtool with some crap.
find %buildroot -name \*.la -print0 | xargs -0 rm -f

# I cannot express this as %%files in a sensible manner, especially not when
# python byte-compilation kicks in.  Set permissions in the filesystem.
find %buildroot%pkglibexecdir -type f -print0 | xargs -0 chmod 755
find %buildroot%pkglibexecdir -type f -name \*.rgi -print0 | xargs -0 chmod 644

# Perl, Python, and Ruby modules are private, remove the Perl man page.
rm -f %buildroot%_man3dir/Gwyddion::dump.*

mkdir -p %buildroot%python_sitelibdir
mv %buildroot%pkglibdir/modules/pygwy.so %buildroot%python_sitelibdir/gwy.so

%pre thumbnailer-gconf
%gconf2_uninstall

%post thumbnailer-gconf
%gconf2_install

%preun thumbnailer-gconf
%gconf2_uninstall

%files -f %name.lang
%_bindir/%name
%_bindir/%name-thumbnailer

%doc AUTHORS COPYING INSTALL NEWS README THANKS
%dir %pkgdatadir
%dir %pkgdatadir/pixmaps
%pkgdatadir/pixmaps/*.png
%pkgdatadir/pixmaps/*.ico
%pkgdatadir/gradients/
%pkgdatadir/glmaterials/
%pkgdatadir/pygwy/
%pkgdatadir/ui/
%pkgdatadir/user-guide-modules/
%_man1dir/%name.1*
%_man1dir/%name-thumbnailer.1*
%_liconsdir/%name.png
%_pixmapsdir/%name.png
%pkglibdir/modules/file/*.so
%pkglibdir/modules/graph/*.so
%pkglibdir/modules/layer/*.so
%pkglibdir/modules/process/*.so
%pkglibdir/modules/tool/*.so
%pkglibdir/modules/volume/*.so
%pkglibdir/modules/xyz/*.so
%pkglibdir/modules/*.so
%dir %pkglibdir/modules/file
%dir %pkglibdir/modules/graph
%dir %pkglibdir/modules/layer
%dir %pkglibdir/modules/process
%dir %pkglibdir/modules/tool
%dir %pkglibdir/modules/volume
%dir %pkglibdir/modules/xyz
%dir %pkglibdir/modules
%dir %pkglibdir
%_desktopdir/%name.desktop
%_datadir/mime/packages/%name.xml
%dir %_datadir/thumbnailers
%_datadir/thumbnailers/%name.thumbnailer

%files -n %libname
%_libdir/*.so.*

%files -n lib%name-devel
%doc devel-docs/CODING-STANDARDS
%doc data/%name.vim
%pkgincludedir/app/*.h
%pkgincludedir/libdraw/*.h
%pkgincludedir/libprocess/*.h
%pkgincludedir/libgwyddion/*.h
%pkgincludedir/libgwydgets/*.h
%pkgincludedir/libgwymodule/*.h
%dir %pkgincludedir/app
%dir %pkgincludedir/libdraw
%dir %pkgincludedir/libprocess
%dir %pkgincludedir/libgwyddion
%dir %pkgincludedir/libgwydgets
%dir %pkgincludedir/libgwymodule
%dir %pkgincludedir
%_libdir/*.so
%_pkgconfigdir/gwyddion.pc
%pkglibdir/include/gwyconfig.h
%dir %pkglibdir/include
# Plug-ins and plug-in devel stuff
%pkglibdir/perl/Gwyddion/*
%dir %pkglibdir/perl/Gwyddion
%dir %pkglibdir/perl
%pkglibdir/python/Gwyddion/*
%dir %pkglibdir/python/Gwyddion
%dir %pkglibdir/python
%pkglibdir/ruby/gwyddion/*
%dir %pkglibdir/ruby/gwyddion
%dir %pkglibdir/ruby
# Use filesystem permissions here.
%pkglibexecdir/plugins/file/*
%pkglibexecdir/plugins/process/*
%dir %pkglibexecdir/plugins/file
%dir %pkglibexecdir/plugins/process
%dir %pkglibexecdir/plugins
%dir %pkglibexecdir

%files -n lib%name-doc
# Documentation
%doc %_gtkdocdir/libgwyapp/*
%doc %_gtkdocdir/libgwydraw/*
%doc %_gtkdocdir/libgwyprocess/*
%doc %_gtkdocdir/libgwyddion/*
%doc %_gtkdocdir/libgwydgets/*
%doc %_gtkdocdir/libgwymodule/*
%doc %dir %_gtkdocdir/libgwyapp
%doc %dir %_gtkdocdir/libgwydraw
%doc %dir %_gtkdocdir/libgwyprocess
%doc %dir %_gtkdocdir/libgwyddion
%doc %dir %_gtkdocdir/libgwydgets
%doc %dir %_gtkdocdir/libgwymodule
%doc %dir %_gtkdocdir
%doc %dir %_datadir/gtk-doc

%files thumbnailer-gconf
%_sysconfdir/gconf/schemas/*.schemas

%files thumbnailer-kde4
%_libdir/kde4/gwythumbcreator.so

%files -n python-module-pygwy
%python_sitelibdir/*
%_datadir/gtksourceview-2.0/language-specs/*.lang

%changelog
* Sun Dec 24 2017 Alexei Mezin <alexvm@altlinux.org> 2.49-alt1
- new version

* Wed Jan 18 2017 Alexei Mezin <alexvm@altlinux.org> 2.47-alt2
- spec cleanups

* Tue Jan 17 2017 Alexei Mezin <alexvm@altlinux.org> 2.47-alt1
- new version

* Sat Apr 23 2016 Vitaly Lipatov <lav@altlinux.ru> 2.44-alt1
- new version 2.44 (with rpmrb script) (ALT bug #31603)

* Thu Feb 13 2014 Evgeny Sinelnikov <sin@altlinux.ru> 2.34-alt1
- update to new version

* Wed Apr 03 2013 Boris Savelev <boris@altlinux.org> 2.31-alt1
- new version. closes: #28780

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.25-alt1.3
- Rebuilt with libpng15

* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.25-alt1.2
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.25-alt1.1
- Rebuild with Python-2.7

* Thu Jun 16 2011 Boris Savelev <boris@altlinux.org> 2.25-alt1
- up to 2.25

* Fri Feb 18 2011 Boris Savelev <boris@altlinux.org> 2.22-alt1
- up to 2.22

* Tue Dec 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18-alt2.2
- Rebuilt for soname set-versions
- Fixed linking

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18-alt2.1
- Fixed build

* Mon Nov 30 2009 Boris Savelev <boris@altlinux.org> 2.18-alt2
- add noarch doc package
- fix mime xml
- fix exec with --remote-new

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18-alt1.1
- Rebuilt with python 2.6

* Thu Nov 12 2009 Boris Savelev <boris@altlinux.org> 2.18-alt1
- new version

* Fri Jul 03 2009 Boris Savelev <boris@altlinux.org> 2.16-alt1
- initial build for Sisyphus


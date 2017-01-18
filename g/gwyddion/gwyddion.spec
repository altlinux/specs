
Name: gwyddion
Version: 2.47
Release: alt2

Summary: An SPM data visualization and analysis tool
Summary(ru_RU.UTF-8):  Программа для визуализации и анализа данных АСМ

Group: Sciences/Other
License: GNU GPL
Url: http://gwyddion.net/

# Source-url: http://sourceforge.net/projects/gwyddion/files/gwyddion/%version/gwyddion-%version.tar.xz/download
Source: %name-%version.tar
#Patch0: fix-rpath-issue.patch
#Patch1: gwyddion-2.25-alt-glib2.patch
#Patch2: gwyddion-2.25-alt-libpng15.patch

BuildRequires(pre): rpm-build-intro libGConf-devel
# Automatically added by buildreq on Sat Apr 23 2016
# optimized out: GConf ORBit2-devel aalib at-spi2-atk boost-context-devel boost-devel bzlib-devel cmake cppunit cracklib desktop-file-utils efl-libs elfutils flite fontconfig fontconfig-devel fpc-compiler fpc-units-rtl gamin gcc-c++ gcr-libs glib2-devel glibc-devel-static glusterfs3-server gnome-vfs gnome-vfs-devel gnu-config gnustep-base-devel gobject-introspection gobject-introspection-devel gst-plugins-bad1.0 gst-plugins-devel gst-plugins1.0-devel gstreamer-devel gstreamer1.0-devel guile18 hornetq i586-binutils i586-fontconfig i586-fontconfig-devel i586-gettext-tools i586-glib2 i586-glibc-devel i586-libEGL i586-libGL i586-libGL-devel i586-libGLU i586-libICE i586-libICE-devel i586-libSM i586-libSM-devel i586-libX11 i586-libX11-devel i586-libXScrnSaver i586-libXau i586-libXau-devel i586-libXaw i586-libXcomposite i586-libXcursor i586-libXdamage i586-libXdmcp i586-libXevie i586-libXext i586-libXext-devel i586-libXfixes i586-libXfixes-devel i586-libXfont i586-libXft i586-libXi i586-libXinerama i586-libXmu i586-libXmu-devel i586-libXpm i586-libXrandr i586-libXrender i586-libXrender-devel i586-libXres i586-libXt i586-libXt-devel i586-libXv i586-libXv-devel i586-libXvMC i586-libXxf86dga i586-libXxf86misc i586-libXxf86vm i586-libalsa i586-libasyncns i586-libatk i586-libavahi i586-libcairo i586-libclucene-core i586-libclucene-shared i586-libcom_err-devel i586-libcroco i586-libcups i586-libdatrie i586-libdrm i586-libelf i586-libexif i586-libffi6 i586-libflac8 i586-libfontenc i586-libfreetype i586-libfreetype-devel i586-libgbm i586-libgd2 i586-libgdk-pixbuf i586-libgio i586-libgmp10 i586-libgnutls30 i586-libgphoto2-6 i586-libgphoto2_port-12 i586-libgpm i586-libgraphite2 i586-libgsm i586-libgstreamer i586-libgstreamer1.0 i586-libgtk+2 i586-libhalf11 i586-libhalf12 i586-libhalf6 i586-libharfbuzz i586-libhogweed4 i586-libhunspell i586-libidn i586-libieee1284 i586-libiex11 i586-libiex12 i586-libiex6 i586-libilmthread11 i586-libilmthread12 i586-libilmthread6 i586-libjasper i586-libjpeg i586-libjson-c i586-libkrb5 i586-libkrb5-devel i586-libkrb5-ldap i586-liblcms i586-libldap i586-liblockdev i586-libltdl7 i586-libmm i586-libmng i586-libmpg123 i586-libncurses i586-libnet-snmp30 i586-libnettle6 i586-libnl3 i586-libnspr i586-libnss i586-libogg i586-libopenal1 i586-liborc i586-libp11-kit i586-libpango i586-libpciaccess i586-libpixman i586-libpng15 i586-libpolkit i586-libpulseaudio i586-libqt4-core i586-libqt4-dbus i586-libqt4-declarative i586-libqt4-gui i586-libqt4-network i586-libqt4-opengl i586-libqt4-script i586-libqt4-sql i586-libqt4-xml i586-libqt4-xmlpatterns i586-libqtsoap i586-libsane i586-libsensors3 i586-libsndfile i586-libsqlite3 i586-libstdc++6 i586-libtasn1 i586-libthai i586-libtiff5 i586-libtinfo-devel i586-libunistring2 i586-libv4l i586-libverto i586-libverto-devel i586-libvorbis i586-libwayland-client i586-libwayland-server i586-libxcb i586-libxcb-devel i586-libxml2 i586-libxshmfence i586-perl-base i586-zlib-devel icon-naming-utils id3lib jack-audio-connection-kit kde4libs kdevplatform-libs libEGL-devel libGConf-devel libGL-devel libGLU-devel libICE-devel libIDL-devel libSDL-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXaw-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXevie-devel libXext-devel libXfixes-devel libXfont-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXres-devel libXt-devel libXtst-devel libXv-devel libXvMC-devel libXxf86dga-devel libXxf86misc-devel libXxf86vm-devel libacl-devel libakonadi4-contact libakonadi4-kde libakonadi4-kmime libalsa-devel libarchive-devel libart_lgpl-devel libat-spi2-core libatk-devel libatkmm-devel libaudiofile-devel libavahi-devel libavahi-glib libavahi-qt3 libavahi-qt4 libavcodec-devel libavutil-devel libbonobo-devel libbonoboui-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcairomm-devel libcanberra-devel libcanberra-gtk3 libcdio-devel libcdio-paranoia libclucene-core libclucene-shared libclutter-gst3.0 libclutter-gtk3 libcom_err-devel libcomedi-devel libcommoncpp2-devel libconfig-c++ libcups-devel libcurl-devel libcxx-gtk-utils libdb4-devel libdbus-devel libdbus-glib libdbus-glib-devel libdbusmenu-qt2 libdc1394-22 libdevmapper-devel libdevmapper-event libdrm-devel libdvdread-devel libebml-devel libenchant-devel libevent-devel libexif-devel libexpat-devel libffi-devel libfontenc-devel libfreetds-unixodbc libfreetype-devel libgail-devel libgamin-fam libgarcon-devel libgarcon-gtk2 libgcj-common libgcrypt-devel libgdk-pixbuf libgdk-pixbuf-devel libgdk-pixbuf-xlib libgeocode-glib libggadget-js libggadget-xdg libgif-devel libgio-devel libglade-devel libglibmm-devel libglusterfs3-api libglusterfs3-devel libgmp-devel libgnome-devel libgnome-keyring libgnome-keyring-devel libgnome-online-accounts libgnomecanvas-devel libgnomeoffice-light0.8 libgnustep-BioCocoa libgnustep-base libgnustep-corebase libgnustep-gui libgnustep-objc2 libgnustep-objc2-devel libgnutls-devel libgpg-error libgpg-error-devel libgpgmexx4-pthread libgphoto2-6 libgphoto2-devel libgphoto2_port-12 libgraphite2-devel libgsl-devel libgsm-devel libgst-plugins libgst-plugins1.0 libgtk+2-devel libgtk+3-devel libgtk-sharp2 libgtkmm2-devel libgtkmm3-devel libgtksourceview3-devel libgtkspell3-devel libgupnp-igd libharfbuzz-devel libharfbuzz-icu libhdf5-8-seq libibverbs-devel libicu-devel libieee1284-devel libjack-devel libjansson-devel libjavascriptcoregtk2-devel libjavascriptcoregtk3-devel libjpeg-devel libjson-c libjson-glib libkate-devel libkrb5-devel libkrb5-ldap liblcms-devel libldap-devel libleptonica-devel libltdl7-devel libmenu-cache libmm-glib libmowgli-devel libmpg123-devel libmysqlclient-devel libncurses-devel libnet-snmp30 libnet-snmp30-snmptrapd libnetcdf7-seq libnl-devel libnl3-utils libnm-glib4 libnm-util2 libnumpy-devel libnumpy-py3 libogg-devel libomniORB-devel libopenal-devel libopencore-amrnb0 libopencore-amrwb0 libopus-devel liborc-test libossp-uuid libp11-kit libpango-devel libpangomm-devel libpangox-compat libpangox-compat-devel libpcre-devel libpilot-link libpng-devel libpolkit-qt-core-1 libpoppler-devel libpoppler1-qt5 libpoppler4-qt4 libpoppler8-glib libpopt-devel libportaudio2-devel libprojectM-qt libprotobuf-c1 libpurple-client libqscintilla2-12-qt4 libqt4-clucene libqt4-core libqt4-dbus libqt4-declarative libqt4-designer libqt4-devel libqt4-gui libqt4-help libqt4-location libqt4-multimedia libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-scripttools libqt4-sensors libqt4-sql libqt4-svg libqt4-test libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libqt5-bluetooth libqt5-clucene libqt5-compositor libqt5-concurrent libqt5-core libqt5-dbus libqt5-declarative libqt5-designer libqt5-designercomponents libqt5-egldeviceintegration libqt5-gui libqt5-help libqt5-location libqt5-multimedia libqt5-network libqt5-nfc libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickparticles libqt5-quicktest libqt5-quickwidgets libqt5-script libqt5-sensors libqt5-serialport libqt5-sql libqt5-svg libqt5-test libqt5-waylandclient libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-websockets libqt5-widgets libqt5-xcbqpa libqt5-xml libqt5-xmlpatterns libqtspell-qt4 libqtspell-qt5 libquicktime111-core libradiusclient-ng libraw1394-11 libraw1394-devel librevenge-devel librrd-devel libsane-devel libsearpc-devel libsensors3-devel libsigc++2-devel libsndfile-devel libsodium-devel libsoup-devel libsoup-gnome libspeex-devel libspeexdsp-devel libspice-server libsqlite3-devel libsrtp-devel libss-devel libssl-devel libstartup-notification libstdc++-devel libstrigi-devel libsysfs-devel libtelepathy-glib libtheora-devel libtiff-devel libtinfo-devel libudev-devel libuniset-devel libuniset-extensions libunixODBC-devel libunixODBC-devel-compat libusb-devel libuserspace-rcu libutempter-devel libuuid-devel libv4l-devel libv8-chromium libvdpau-devel libverto-devel libvo-aacenc libvo-amrwbenc libvorbis-devel libvpx-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl libwayland-server libwayland-server-devel libwrap-devel libxbase-devel libxcb-devel libxcb-render-util libxcbutil-icccm libxcbutil-image libxcbutil-keysyms libxerces-c libxfce4ui-devel libxfce4util-devel libxfconf-devel libxkbcommon-x11 libxkbfile-devel libxml++2-devel libxml2-devel libxslt-devel libyajl-devel llvm mono pam0_userpass perl perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-Pod-Usage perl-podlators phonon-devel php5-libs pkg-config python-base python-devel python-module-distribute python-module-google python-module-pygobject python-module-pygobject-devel python-modules python-modules-compiler python3 python3-base python3-dev qt4-serialport qt5-base-devel qt5-declarative-devel qt5-gstreamer1 qt5-script-devel ruby ruby-stdlibs samba-client-libs sendmail-common setproctitle shared-mime-info sipgateway svgalib t1lib tcl-devel tesseract ucommon-devel vala w3c-libwww w3c-libwww-devel wine-etersoft wireshark-base xorg-xproto-devel xsltproc zlib-devel zlib-devel-static

BuildRequires: GConf gcc-c++ imake kde4libs-devel libfftw3-devel libgtkglext-devel libgtksourceview-devel libicu-devel
BuildRequires: libminizip-devel libxml2-devel perl-Pod-Usage python-module-distribute python-module-pygtk-devel

BuildRequires: libgtk+2-devel pkg-config libgtkglext-devel libfftw3-devel chrpath kde4libs-devel libruby-devel
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
#patch0 -p1
#patch1 -p2
#patch2 -p2

# Don't install .la files.
%__subst '/# Install the pseudo-library/,/^$/d' ltmain.sh
# Replace universal %_bindir/env shbang with the real thing.
%__subst '1s/env *//' plugins/process/*.{py,rb,pl}

%__subst 's|#include <pygtk-2.0/pygobject.h>|#include <pygtk/pygobject.h>|' modules/pygwy/pygwy.c
%__subst 's|#include <pygtk-2.0/pygobject.h>|#include <pygtk/pygobject.h>|' modules/pygwy/gwy.c

%build
%configure \
	CFLAGS='%optflags -I%_K4includedir' \
	CXXFLAGS='%optflags -I%_K4includedir' \
	--with-kde4-thumbnailer \
	--disable-rpath \
	--with-gconf-schema-file-dir=%_sysconfdir/gconf/schemas \
	--enable-library-bloat \
	--enable-pygwy
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

%doc AUTHORS COPYING INSTALL.%name NEWS README THANKS
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
%pkglibdir/modules/*.so
%dir %pkglibdir/modules/file
%dir %pkglibdir/modules/graph
%dir %pkglibdir/modules/layer
%dir %pkglibdir/modules/process
%dir %pkglibdir/modules/tool
%dir %pkglibdir/modules/volume
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


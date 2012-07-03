# Copyright (c) 2006-2008 oc2pus
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to toni@links2linux.de
#
#Tue Dec 23 2008: get from SuSE 11.X's srpm ( ftp://ftp.pbone.net/mirror/packman.iu-bremen.de/suse/11.1/SRPMS/buzztard-0.4.0-0.pm.1.src.rpm ) and reformed for ALT Linux

%define _gst_branch	0.10
%define buzz_enable_doc enable
%define prerel alt4

Name: buzztard
License: GPLv2+
Group: Sound
Summary: A free replacement of closed source software Buzz
Version: 0.6.0
Release: %prerel.svn20100715
Url: http://www.buzztard.org
Packager: Egor Glukhov <kaman@altlinux.org>

Source: %name-%version.tar

Requires: lib%name-gst = %version-%release
Requires: lib%name-core = %version-%release
Requires: lib%name-ic = %version-%release
Requires: libbsl = %version-%release
Obsoletes: buzztard-full
BuildRequires(pre): rpm-build-gnome rpm-build-licenses rpm-build-buzztard
BuildRequires(pre): rpm-build-compat shared-mime-info
BuildPreReq: libstdc++-devel libhal-devel libdbus-glib-devel
BuildPreReq: libGL-devel gtk-doc ImageMagick-tools liboil-devel gstreamer-devel

# Automatically added by buildreq on Fri Jan 02 2009
BuildRequires: GConf aspell libX11-devel

BuildRequires: gcc-c++ glibc-devel
BuildRequires: cvs desktop-file-utils gnome-vfs-devel gst-plugins-devel intltool
BuildRequires: libgnomecanvas-devel librarian librsvg-devel
BuildRequires: gst-ffmpeg gst-plugins-bad gst-plugins-devel
BuildRequires: gst-plugins-gio gst-plugins-gnomevfs gst-plugins-good
BuildRequires: gst-plugins-libvisual gst-plugins-pango gst-plugins-ugly
BuildRequires: gtk-doc libfluidsynth-devel
%ifarch %ix86
BuildPreReq: libwine-devel
%endif
#if %buzz_enable_doc == enable
#BuildPreReq: libbuzztard-core-devel >= %version-%prerel
#BuildPreReq: libbuzztard-ic-devel >= %version-%prerel
#endif

%description
The Buzztard project aims to provide a free replacement (or clone)
of the currently windows only and closed source software Buzz.
The buzz software is not really further developed, as the main
developer has lost his source code.
We want to provide a music production environment, that is based on
a very modular approach (following some of the ideas behind buzz),
to allow many people to get involved. We hope that our software will
have a better usabillity than buzz has although. We don't want to
make this a 1:1 copy though.

The Buzztard project itself has no direct link to buzz (apart from
concepts). To allow migration for buzz users, we will provide
song-file import and buzz-machine reuse.

%package -n lib%name-core0
Group: System/Libraries
Summary: Core library for buzztard
Provides: lib%name-core = %version-%release
Requires: lib%name-ic = %version-%release

%description -n lib%name-core0
Core library for buzztard.

%package -n lib%name-ic0
Group: System/Libraries
Summary: Input control library for buzztard
Provides: lib%name-ic = %version-%release

%description -n lib%name-ic0
Input control library for buzztard.

%package -n lib%name-core-devel
Group: Development/C++
Summary: Development package for buzztard core library
Requires: lib%name-core = %version-%release
Requires: lib%name-gst-devel = %version-%release

%description -n lib%name-core-devel
Development package for buzztard core library.

%package -n lib%name-core-devel-static
Group: Development/C++
Summary: Static development files for buzztard core library
Requires: lib%name-core-devel = %version-%release
Requires: lib%name-gst-devel-static = %version-%release

%description -n lib%name-core-devel-static
Static development files for buzztard core library.

%package -n lib%name-ic-devel
Group: Development/C++
Summary: Development package for buzztard input control library
Requires: lib%name-ic = %version-%release
Requires: lib%name-core-devel = %version-%release
Requires: lib%name-gst-devel = %version-%release

%description -n lib%name-ic-devel
Development package for buzztard input control library.

%package -n lib%name-ic-devel-static
Group: Development/C++
Summary: Static development files for buzztard input control library
Requires: lib%name-ic-devel = %version-%release
Requires: lib%name-core-devel-static = %version-%release
Requires: lib%name-gst-devel-static = %version-%release

%description -n lib%name-ic-devel-static
Static development files for buzztard input control library.

%package -n lib%name-devel-doc
Group: Development/Documentation
Summary: Development documentation for buzztard
BuildArch: noarch

%description -n lib%name-devel-doc
Development documentation for buzztard.

# libbml

%package -n libbml
Summary: The library that loads buzz machines from the Buzz
Group: System/Libraries

%description -n libbml
The libbml is a library that loads buzz machines from the windows music
composer Buzz, so that Linux apps can use them.
This lib is either using the libavifile wrapper or the libfst one.
See original README in README.libfst for the latter.

The emulation of windows machines uses some parts of wine at runtime. It
needs kernel32.dll, e.g. /usr/lib/wine/kernel32.dll.so, MFC42.DLL,
MSVCRT.DLL. The original windows dll should also work.

Then you need to copy the all *.dll libraries from a windows buzz
installation to your LD_LIBARY_PATH. We recommend to copy them to
/usr/lib.

Next copy the machines. You can e.g. just copy the whole Gear folder's
content to /usr/lib/Gear as well.
You might need to fix some machine names (e.g. names with '?' in them).

%package -n libbml-devel
Summary: Include and object files required for C++ development of buzztard
Group: Development/C++
Requires: libbml = %version-%release

%description -n libbml-devel
Include and object files required for C++ development of buzztard.

%package -n libbml-devel-static
Summary: Buzztard static devel libraries
Group: Development/C++
Requires: libbml-devel = %version-%release

%description -n libbml-devel-static
Buzztard static devel libraries.

# buzzmachines

%package -n buzzmachines
Summary: This module provide a set of opensource buzzmachines
Group: Sound
Requires: libbml = %version-%release

%description -n buzzmachines
This module provide a set of buzzmachines that have been released as open source.
They can be used via bml library or in all gstreamer app via bml+gstbml.

# gst-buzztard

%package -n lib%name-gst
Summary: This module contains experimental code that extends gstreamer
Group: System/Libraries
Provides: gstreamer-buzztard = %version-%release
Provides: gst-buzztard = %version-%release
Obsoletes: gst-buzztard < %version-%release
Requires: buzzmachines = %version-%release

%description -n lib%name-gst
This package contains code that eventualy will be move to gstreamer
and right now is needed to build all other buzztard-modules.

Author: Stefan Kost <ensonic@users.sourceforge.net>

%package -n lib%name-gst-devel
Summary: Development files for gst-buzztard
Group: Development/C++
Requires: lib%name-gst = %version-%release
Requires: libbml-devel = %version-%release
Provides: gst-buzztard-devel = %version-%release
Obsoletes: gst-buzztard-devel < %version-%release

%description -n lib%name-gst-devel
Development headers for gst-buzztard.

Author: Stefan Kost <ensonic@users.sourceforge.net>

%package -n lib%name-gst-devel-doc
Summary: gtk documentation for buzztard
Group: Development/Documentation
BuildArch: noarch
Provides: gst-buzztard-devel-doc = %version-%release
Obsoletes: gst-buzztard-devel-doc < %version-%release

%description -n lib%name-gst-devel-doc
GTK documentation for buzztard.

%package -n lib%name-gst-devel-static
Summary: Static development files for gst-buzztard
Group: Development/C++
Requires: lib%name-gst-devel = %version-%release
Requires: libbml-devel-static = %version-%release
Provides: gst-buzztard-devel-static = %version-%release
Obsoletes: gst-buzztard-devel-static < %version-%release

%description -n lib%name-gst-devel-static
Static files for buzztard.

# libbsl

%package -n libbsl
Summary: Buzz song loader for Buzztard
Group: Sound

%description -n libbsl
The bsl package provides an import plugin for buzztard to load
buzz song files.

Author: Stefan Kost <ensonic@users.sourceforge.net>

%prep
%setup

%build
%ifarch %ix86
BML_PATH=%buzz_gear_dir:%buzz_gear_dir/Effects:%buzz_gear_dir/Generators
%else
BML_PATH=%buzz_gear_dir
%endif
export BML_PATH
rm -fR CVSROOT

# libbml

pushd bml
./autogen.sh
%configure --with-gnu-ld
%make_build
%make check
popd

# buzzmachines

pushd buzzmachines
./autogen.sh
%configure --with-gnu-ld
%make_build
%make check
popd

# gst-buzztard

pushd gst-buzztard
#sed -i -e '3s/docs//' Makefile.am
./autogen.sh
%configure \
	--with-gnu-ld \
	--disable-deprecated \
	--disable-debug \
	--%buzz_enable_doc-gtk-doc
%make_build
popd

# buzztard

pushd buzztard
./autogen.sh
%configure \
	--disable-rpath \
	--disable-deprecated \
	--disable-debug \
	--with-gnu-ld \
	--%buzz_enable_doc-gtk-doc
%make_build
#glib-genmarshal --header --prefix=bt_marshal \
#	src/ui/edit/marshal.list > src/lib/core/libbuzztard-core/marshal.h
popd

# libbsl

pushd bsl
./autogen.sh
%configure \
	--enable-static \
	--disable-rpath \
	--with-gnu-ld
%make_build
%make check
popd

%install

# libbml

pushd bml
install -d %buildroot%buzz_gear_dir
%ifarch %ix86
install -d %buildroot%buzz_gear_dir/Effects
install -d %buildroot%buzz_gear_dir/Generators
%endif
%makeinstall_std
rm -f %buildroot%_includedir/BuzzMachineLoader.h
install -d %buildroot%_bindir
install -m755 src/.libs/bmltest_info src/.libs/bmltest_process \
	%buildroot%_bindir
popd

# buzzmachines

pushd buzzmachines
%makeinstall_std
popd

# gst-buzztard

pushd gst-buzztard
%makeinstall_std
popd

# buzztard

pushd buzztard
%makeinstall_std

update-mime-database %buildroot/usr/share/mime
bzip2 ChangeLog
popd

install -d %buildroot%_niconsdir
pushd %buildroot%_liconsdir
convert %name.png -resize "32x32" %buildroot%_niconsdir/%name.png
popd

# libbsl

pushd bsl
%makeinstall_std
%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/buzztard-songio %buildroot%_libdir/
%endif
popd

%find_lang --with-gnome %name

%files -f %name.lang
%doc buzztard/AUTHORS buzztard/ChangeLog.bz2 buzztard/COPYING* buzztard/NEWS
%doc buzztard/README buzztard/NEWSLETTER buzztard/TODO
%_bindir/*
%gconf_schemasdir/%name.schemas
%_datadir/%name
%_desktopdir/%name-edit.desktop
%_liconsdir/%name.png
%_miconsdir/*.png
%_niconsdir/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/24x24/apps/*.png
%_iconsdir/gnome/*/apps/*.svg
%_iconsdir/gnome/*/apps/*.png
%_omfdir/%name-edit/%name-edit-C.omf
%_xdgmimedir/packages/%name.xml
%_xdgmimedir/audio/x-bzt*.xml
%gnome_helpdir/%name-edit

%files -n lib%name-core0
%_libdir/lib%name-core.so.*

%files -n lib%name-ic0
%_libdir/lib%name-ic.so.*

%files -n lib%name-core-devel
%_includedir/lib%name-core
%_libdir/lib%name-core.so
%_pkgconfigdir/lib%name-core.pc

%files -n lib%name-ic-devel
%_includedir/lib%name-ic
%_libdir/lib%name-ic.so
%_pkgconfigdir/lib%name-ic.pc

%if %buzz_enable_static == enable
%files -n lib%name-core-devel-static
%_libdir/lib%name-core.a

%files -n lib%name-ic-devel-static
%_libdir/lib%name-ic.a
%endif

%if %buzz_enable_doc == enable
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/%name-cmd
%_datadir/gtk-doc/html/%name-core
%_datadir/gtk-doc/html/%name-edit
%_datadir/gtk-doc/html/%name-ic
%endif

# libbml

%files -n libbml
%_libdir/libbml.so.*
%_libdir/bml/libbuzzmachineloader.so.*
%ifarch %ix86
%_libdir/win32/*.dll
%endif

%files -n libbml-devel
%_libdir/libbml.so
%_libdir/bml/libbuzzmachineloader.so
%_pkgconfigdir/libbml.pc
%_includedir/libbml

%if %buzz_enable_static == enable
%files -n libbml-devel-static
%_libdir/libbml.a
%endif

# buzzmachines

%files -n buzzmachines
%buzz_gear_dir
%_datadir/Gear

# gst-buzztard

%files -n lib%name-gst
%doc gst-buzztard/AUTHORS gst-buzztard/ChangeLog gst-buzztard/COPYING
%doc gst-buzztard/NEWS gst-buzztard/README gst-buzztard/TODO
%_libdir/libgstbuzztard.so.*
%_libdir/gstreamer-%_gst_branch/*.so

%files -n lib%name-gst-devel
%_libdir/libgstbuzztard.so
%_libdir/pkgconfig/libgstbuzztard.pc
%_includedir/libgstbuzztard

%if %buzz_enable_doc == enable
%files -n lib%name-gst-devel-doc
%_datadir/gtk-doc/html/gst-buzztard
%endif

%if %buzz_enable_static == enable
%files -n lib%name-gst-devel-static
%_libdir/libgstbuzztard.a
%endif

# libbsl

%files -n libbsl
%doc bsl/AUTHORS bsl/ChangeLog bsl/COPYING bsl/NEWS bsl/README bsl/TODO
%_libdir/buzztard-songio
%exclude %_desktopdir/buzztard-songio-buzz.desktop
%_xdgmimedir/packages/buzztard-songio-buzz.xml
%_xdgmimedir/audio/x-bm?.xml

%changelog
* Sat Aug 20 2011 Egor Glukhov <kaman@altlinux.org> 0.6.0-alt4.svn20100715
- Rebuilt with new fluidsynth

* Sun Oct 24 2010 Egor Glukhov <kaman@altlinux.org> 0.6.0-alt3.svn20100715
- Fixed specfile for rebuilding

* Sun Aug 01 2010 Egor Glukhov <kaman@altlinux.org> 0.6.0-alt2.svn20100715
- Cleanup

* Sun Aug 01 2010 Egor Glukhov <kaman@altlinux.org> 0.6.0-alt1.svn20100715
- Snapshot 20100715

* Thu Jan 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.svn20091224
- Version 0.6.0
- Restored Buzz Gear dir (ALT #22592)

* Fri Jul 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt3.svn20090724
- Snapshot 20090724

* Sun May 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt3.svn20090509
- New trunk
- Remove dependence on gstreamer-pitfdll
- Enable gtk-doc

* Mon Apr 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2
- New trunk (fixed unmets of 3 machines by upstream)
- Changed directory with Buzz machines

* Tue Mar 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.svn20090331
- Version 0.5.0 (unstable, without gtk-doc)
- Build all packages from one source repository

* Sun Feb 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2.svn20081222
- rebuild for reformed gst-buzztard with enabled gtk-doc

* Sun Feb 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2
- rebuild for reformed gst-buzztard: bootstrap

* Sat Jan 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.svn20081222
- Enable gtk-doc

* Fri Jan 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus (without gtk-doc)


Name: darktable
Version: 1.0.4
Release: alt1

Summary: Darktable is a virtual lighttable and darkroom for photographer
License: GPLv3
Group: Graphics

Url: http://darktable.sourceforge.net/
Source: http://downloads.sourceforge.net/darktable/darktable-%version.tar.gz

# For gconf_schemasdir definition:
BuildPreReq: rpm-build-gnome

# Automatically added by buildreq on Thu Mar 15 2012
# optimized out: cmake-modules fontconfig glib2-devel ilmbase-devel libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXrender-devel libatk-devel libcairo-devel libcurl-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgnome-keyring libgpg-error libpango-devel libstdc++-devel libwayland-client libwayland-server libxml2-devel perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators pkg-config xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
BuildRequires: cmake gcc-c++ libSDL-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-glib-devel libexiv2-devel libflickcurl-devel libgnome-keyring-devel libgomp-devel libgphoto2-devel libgtk+2-devel libjpeg-devel liblcms2-devel liblensfun-devel libpng-devel librsvg-devel libsqlite3-devel libtiff-devel libxkbfile-devel lsb-release openexr-devel perl-Pod-Parser

%description
darktable is a virtual light table and darkroom for photographers. It manages
your digital negatives in a database and lets you view them through a zoomable
light table. It also enables you to develop raw images and enhance them.

%prep
%setup

%build
subst 's/-Werror//' src/CMakeLists.txt
%cmake
cd BUILD
%make_build VERBOSE=1

%install
pushd BUILD
export DESTDIR=%buildroot
%makeinstall
popd
# Upstream switched to cmake-based build system. This change
# resulted in missed rpath, so we have to fix it:
mv %buildroot%_libdir/darktable/libdarktable.so %buildroot%_libdir/

install -pD -m644 data/pixmaps/16x16/darktable.png %buildroot%_miconsdir/darktable.png
install -pD -m644 data/pixmaps/32x32/darktable.png %buildroot%_niconsdir/darktable.png
install -pD -m644 data/pixmaps/48x48/darktable.png %buildroot%_liconsdir/darktable.png

%find_lang %name

%set_verify_elf_method unresolved=relaxed

%files -f %name.lang
%_bindir/*
%_datadir/darktable
%_libdir/libdarktable.so
%_libdir/darktable/
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
#%gconf_schemasdir/*
%_man1dir/*
%exclude /usr/share/doc/darktable/

%changelog
* Sat Jun 16 2012 Victor Forsiuk <force@altlinux.org> 1.0.4-alt1
- 1.0.4

* Tue May 15 2012 Victor Forsiuk <force@altlinux.org> 1.0.3-alt1
- 1.0.3

* Thu Mar 15 2012 Victor Forsiuk <force@altlinux.org> 1.0-alt1
- 1.0

* Sat Nov 12 2011 Victor Forsiuk <force@altlinux.org> 0.9.3-alt1
- 0.9.3

* Wed Nov 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt2
- rebuilt against libexiv2.so.11

* Sun Aug 28 2011 Victor Forsiuk <force@altlinux.org> 0.9.2-alt1
- 0.9.2

* Wed Jul 27 2011 Victor Forsiuk <force@altlinux.org> 0.9.1-alt1
- 0.9.1

* Sun Jul 03 2011 Victor Forsiuk <force@altlinux.org> 0.9-alt1
- 0.9

* Wed Mar 09 2011 Victor Forsiuk <force@altlinux.org> 0.8-alt3
- Refresh BuildRequires.

* Thu Feb 17 2011 Victor Forsiuk <force@altlinux.org> 0.8-alt2
- Fix build mistake, now darktable will work correctly (closes: #25102).

* Wed Feb 16 2011 Victor Forsiuk <force@altlinux.org> 0.8-alt1
- 0.8

* Tue Dec 14 2010 Victor Forsiuk <force@altlinux.org> 0.7.1-alt1
- 0.7.1

* Fri Dec 03 2010 Victor Forsiuk <force@altlinux.org> 0.7-alt1
- 0.7

* Wed Sep 08 2010 Victor Forsiuk <force@altlinux.org> 0.6-alt1
- 0.6

* Tue Jun 01 2010 Victor Forsiuk <force@altlinux.org> 0.5-alt2
- Rebuild with libexiv2.so.9.

* Wed Mar 31 2010 Victor Forsiuk <force@altlinux.org> 0.5-alt1
- 0.5

* Wed Feb 10 2010 Victor Forsiuk <force@altlinux.org> 0.4-alt1.git20100210
- Git snapshot from 2010-02-10.

* Tue Aug 18 2009 Victor Forsyuk <force@altlinux.org> 0.2-alt1
- Initial build.

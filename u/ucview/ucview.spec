Summary: Image and video capture application using unicap toolkit
Name: ucview
Version: 0.31
Release: alt1.1
License: GPLv2+
Group: Video
Url: http://www.unicap-imaging.org/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: http://www.unicap-imaging.org/downloads/%name-%version.tar.gz
Source1: %name.desktop
Patch: %name-0.31-alt-DSO.patch
# Automatically added by buildreq on Sun Aug 16 2009
BuildRequires: GConf intltool libGConf-devel libglade-devel libunicap-devel libunicapgtk-devel libucil-devel

%description
UCView is a video image capture application using the unicap toolkit.
It provides a simple way to parametrise the video device, can capture
still images from the video stream or record the stream as mpeg file.
By using unicap, it can access many different video capture devices
like webcams, video grabber boards, IEEE-1394 (FireWire) cameras and
others.

%package devel
Summary: Development files for the ucview
Group: Development/C
Requires: %name = %version-%release

%description devel
The ucvie-devel package includes header files necessary for building
ucview plugins

%prep
%setup -q
%patch -p2
%autoreconf

%build
%configure
%make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

# Install a working ucview.desktop file
mkdir -p %buildroot%_desktopdir
cp -a %SOURCE1 %buildroot%_desktopdir

# Don't install any static .a and libtool .la files
rm -f %buildroot%_libdir/%name/plugins/*.{a,la}

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog
%_sysconfdir/gconf/schemas/%name.schemas
%_bindir/%name
%_pkgconfigdir/%name.pc
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_man1dir/%name.1*

%files devel
%_includedir/*

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.31-alt1.1
- Fixed build

* Wed May 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.31-alt1
- 0.31

* Wed Oct 14 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.30-alt2
- rebuild with libunicap-0.9.7
- build devel subpackage

* Sun Aug 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.30-alt1
- 0.30

* Tue Apr 21 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.23-alt1
- 0.23

* Wed Mar 11 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.22-alt1
- initial

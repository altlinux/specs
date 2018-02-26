%set_automake_version 1.9
%set_libtool_version 1.5

%define tname     LibVNCServer
Name: libvncserver
%define libname %name
Version: 0.9.8.2
Release: alt1.1

Group: System/Libraries
Summary: An easy API to write one's own VNC server
Url: http://sourceforge.net/projects/libvncserver/
License: GPL
Packager: Sergey V Turchin <zerg@altlinux.org>

Source: http://downloads.sourceforge.net/libvncserver/%tname-%version.tar.gz
# SuSE
Patch1: LibVNCServer-LINUX.diff
Patch2: filetransfer-overflow.diff
Patch3: redef-keysym.patch
Patch4: dont-build-x11vnc.patch
Patch5: LibVNCServer-system-lzo.patch

# Automatically added by buildreq on Thu Apr 21 2011 (-bi)
# optimized out: elfutils libX11-devel libgfortran-devel libstdc++-devel xorg-xproto-devel
#BuildRequires: gcc-c++ gcc-fortran glibc-devel-static imake libICE-devel libSDL-devel libjpeg-devel xorg-cf-files zlib-devel
BuildRequires: gcc-c++ gcc-fortran libICE-devel libSDL-devel libjpeg-devel zlib-devel
BuildRequires: libssl-devel liblzo2-devel

%description
LibVNCServer makes writing a VNC server (or more correctly, a program
exporting a framebuffer via the Remote Frame Buffer protocol) easy.

It is based on OSXvnc, which in turn is based on the original Xvnc by
ORL, later AT&T research labs in UK.

It hides the programmer from the tedious task of managing clients and
compression schema.

LibVNCServer was put together and is (actively ;-) maintained by
Johannes Schindelin <Johannes.Schindelin@gmx.de>


%package devel
Summary: Headers for developing programs that will use %tname
Group: Development/C
Requires: %name = %version-%release
%description devel
Headers for developing programs that will use %tname

%package devel-static
Summary: Static libraries for developing programs that will use %tname
Group: Development/C
Requires: %name-devel = %version-%release
%description devel-static
Static libraries for developing programs that will use %tname

%package -n linuxvnc
Summary: VNC server to monitor a text session
Group: Networking/Remote access
Requires: %name = %version-%release
%description -n linuxvnc
With linuxvnc you can export your currently running text sessions to any VNC
client. So it can be useful, if you want to move to another computer without
having to log out and if you've forgotten to attach a 'screen' session to it,
or to help a distant colleague to solve a problem.

Based on the ideas of x0rfbserver and on LibVNCServer, it has evolved
into a versatile and performant while still easy to use program.

%prep
%setup -q -n %tname-%version
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p1

mkdir -p x11vnc
%autoreconf


%build
%configure --disable-static --enable-shared --without-x11vnc
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build


%install
%make DESTDIR=%buildroot install


%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%_libdir/*.so.*

%files devel
%_pkgconfigdir/libvnc*.pc
%_includedir/rfb
%_libdir/*.so
%_bindir/libvncserver-config

%files -n linuxvnc
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%_bindir/LinuxVNC

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.2-alt1.1
- Removed bad RPATH

* Tue Dec 13 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.8.2-alt1
- new version

* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.7-alt3
- fix build requires

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt2.1
- Rebuilt for soname set-versions

* Thu Mar 11 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.7-alt1.M51.1
- built for M51

* Wed Mar 03 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.7-alt2
- add patches from SuSE
- don't build static library

* Wed Apr 29 2009 Sergey V Turchin <zerg@altlinux.org> 0.9.7-alt1
- new version
- remove deprecated macroses from specfile

* Tue Mar 18 2008 Sergey V Turchin <zerg at altlinux dot org> 0.9.1-alt1
- initial specfile
- force detect linux

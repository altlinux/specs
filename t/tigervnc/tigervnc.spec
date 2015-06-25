%define _deffontdir catalogue:%_sysconfdir/X11/fontpath.d

Name: tigervnc
Version: 1.3.1
Release: alt1
Summary: A TigerVNC remote display system

Group: Networking/Remote access
License: GPLv2+
URL: http://www.tigervnc.com

Requires: xauth xkeyboard-config fonts-bitmap-misc xorg-dri-swrast
Provides: tightvnc = 1.7.6
Obsoletes: tightvnc < 1.7.6

Source0: %name-%version.tar.gz
Source1: vncserver.init
Source6: vncviewer.desktop

# XXX buildreq

Source100: xorg-server-source-1.15.1.tar.bz2
Source101: tightpasswd.tar.gz
Source200: repatch_spec.sh
source201: repatch_spec.unused

## FC patches
Patch1: FC-cookie.patch
Patch2: FC-tigervnc11-ldnow.patch
Patch3: FC-tigervnc11-gethomedir.patch
Patch4: FC-tigervnc11-rh692048.patch
Patch5: FC-0001-tigervnc-xserver-1.14-patch.patch
Patch6: FC-inetd-nowait.patch
Patch7: FC-setcursor-crash.patch
Patch8: FC-manpages.patch
Patch9: FC-getmaster.patch
Patch10: FC-shebang.patch
Patch11: FC-1.3.0-xserver-1.15.patch
Patch12: FC-format-security.patch
Patch13: FC-zrle-crash.patch
Patch14: FC-cursor.patch
Patch15: FC-xstartup.patch
Patch16: FC-ppc64le.patch
Patch17: FC-1.3.1-xserver-1.16.patch
Patch18: FC-pointersync.patch

## Ubuntu patches

## ALT patches
Patch501: tigervnc-1.3.1-stdinpasswd.patch

# TODO (if any)
Patch601: tigervnc-viewer-reparent.patch

# Automatically added by buildreq on Wed Jun 25 2014
# optimized out: cmake-modules fontconfig libGL-devel libICE-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libcloog-isl4 libdrm-devel libgpg-error libgpg-error-devel libp11-kit libstdc++-devel pkg-config xorg-fixesproto-devel xorg-fontsproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-recordproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: ImageMagick-tools cmake doxygen flex gcc-c++ libSM-devel libXdmcp-devel libXfont-devel libXtst-devel libfltk-devel libgcrypt-devel libgnutls-devel libjpeg-devel libpam-devel libpixman-devel libssl-devel libxkbfile-devel libxshmfence-devel xorg-bigreqsproto-devel xorg-damageproto-devel xorg-dri2proto-devel xorg-dri3proto-devel xorg-glproto-devel xorg-presentproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-resourceproto-devel xorg-scrnsaverproto-devel xorg-videoproto-devel xorg-xcmiscproto-devel xorg-xineramaproto-devel xorg-xtrans-devel zlib-devel

BuildRequires: xorg-sdk xorg-font-utils

%ifarch %ix86 x86_64
BuildRequires: nasm
%endif

%description
Virtual Network Computing (VNC) is a remote display system which
allows you to view a computing 'desktop' environment not only on the
machine where it is running, but from anywhere on the Internet and
from a wide variety of machine architectures.  This package contains a
client which will allow you to connect to other desktops running a VNC
server.

%package server
Summary: A TigerVNC server
Group: Networking/Remote access
Provides: tightvnc-server = 1.7.6
Obsoletes: tightvnc-server < 1.7.6

%description server
The VNC system allows you to access the same desktop from a wide
variety of platforms.  This package is a TigerVNC server, allowing
others to access the desktop on your machine.

%package -n xorg-extension-vnc
Summary: VNC extension for Xorg
Group: Networking/Remote access

%description -n xorg-extension-vnc
TigerVNC extension for Xorg server

%prep
#setup -q -n %name-%version
%setup -a101
tar -xjf %SOURCE100 -C unix/xserver
pushd unix
patch -p0 < xserver114.patch
popd

## FC apply patches
%patch1 -p1 -b .cookie
%patch2 -p1 -b .ldnow
%patch3 -p1 -b .gethomedir
%patch4 -p1 -b .rh692048
#patch5 -p1 -b .vnc
%patch6 -p1 -b .inetd-nowait
%patch7 -p1 -b .setcursor-crash
%patch8 -p1 -b .manpages
%patch9 -p1 -b .getmaster
%patch10 -p1 -b .shebang
%patch11 -p1 -b .115
%patch12 -p1 -b .format-security
%patch13 -p1 -b .zrle-crash
%patch14 -p1 -b .cursor
%patch15 -p1 -b .xstartup
%patch16 -p1 -b .ppc64le
#patch17 -p1 -b .116
%patch18 -p1 -b .pointersync

## Ubuntu apply patches

## ALT apply patches
%patch501 -p1

%build
%add_optflags -fPIC
%cmake_insource
%make_build

pushd unix/xserver
%autoreconf
%configure \
	--disable-composite \
	--disable-config-dbus \
	--disable-config-hal \
	--disable-config-udev \
	--disable-devel-docs \
	--disable-dmx \
	--disable-dri \
	--disable-kdrive \
	--disable-selective-werror \
	--disable-static \
	--disable-unit-tests \
	--disable-wayland \
	--disable-xephyr \
	--disable-xinerama \
	--disable-xnest \
	--disable-xorg \
	--disable-xvfb \
	--disable-xwayland \
	--disable-xwin \
	--enable-dri2 \
	--enable-dri3 \
	--enable-glx \
	--enable-install-libxf86config \
	--enable-ipv6 \
	--with-default-font-path=%_deffontdir \
	--with-dri-driver-path=%_libdir/dri \
	--with-module-dir="%_xorgmoduledir" \
	--with-pic \
	--with-xkb-output=%_localstatedir/xkb

%make_build
popd

# Build icons
pushd media
%cmake_insource -DDATA_DIR:PATH=%_datadir
%make
popd

# Build tightvnc compatible vncpasswd
pushd tightpasswd
cc %optflags *.c -o tightpasswd
popd

%install
%makeinstall_std

pushd unix/xserver/hw/vnc
%make DESTDIR=%buildroot install
popd

# Install Xvnc as service
install -pD -m755 %SOURCE1 %buildroot%_initddir/vncserver

mkdir -p %buildroot%_sysconfdir/sysconfig
cat << __EOF__ > %buildroot%_sysconfdir/sysconfig/vncservers
# The VNCSERVERS variable is a list of display:user pairs.
#
# Uncomment the line below to start a VNC server on display :1
# as my 'myusername' (adjust this to your own).  You will also
# need to set a VNC password; run 'man vncpasswd' to see how
# to do that.
#
# DO NOT RUN THIS SERVICE if your local area network is
# untrusted!  For a secure way of using VNC, see
# <URL:http://www.uk.research.att.com/vnc/sshvnc.html>.

# VNCSERVERS="1:myusername"
__EOF__

install -D %SOURCE6 %buildroot%_desktopdir/vncviewer.desktop

# Build tightvnc compatible vncpasswd
pushd tightpasswd
install tightpasswd %buildroot%_bindir/tightpasswd
install vncpasswd.man %buildroot%_man1dir/tightpasswd.1
popd

%find_lang %name

%files -f %name.lang
%doc LICENCE.TXT
%_bindir/vncviewer
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_man1dir/vncviewer.1*

%files server
%_initddir/vncserver
%config(noreplace) %_sysconfdir/sysconfig/vncservers
%_bindir/vncconfig
%_bindir/vncpasswd
%_bindir/tightpasswd
%_bindir/x0vncserver
%_bindir/Xvnc
%_bindir/vncserver
%_man1dir/Xvnc.1*
%_man1dir/vncpasswd.1*
%_man1dir/tightpasswd.1*
%_man1dir/vncconfig.1*
%_man1dir/vncserver.1*
%_man1dir/x0vncserver.1*

%files -n xorg-extension-vnc
%_xorgmoduledir/extensions/*.so

%changelog
* Wed Jun 25 2015 Fr. Br. George <george@altlinux.ru> 1.3.1-alt1
- Version update
- FC patches import
- Old vncpasswd binary renamed to tightpasswd

* Tue Apr 22 2015 Fr. Br. George <george@altlinux.ru> 1.3.0-alt1
- Massive submajor version update

* Wed Oct 22 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt2
- disabled vnc extension

* Wed May 02 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sun Jul 24 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.90-alt6
- enabled VeNCrypt

* Tue Jun 21 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.90-alt5
- updated xorg-server-source to 1.10.2
- enabled ipv6
- fixed CVE-2011-1775

* Tue Apr 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.90-alt4
- updated build dependencies
- updated xorg-server-source to 1.9.5

* Sun Nov 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.90-alt3
- SVN snapshot 2010-08-13 (4123)

* Mon Oct 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.90-alt2
- rebuild with libcrypto.so.10

* Wed Apr 14 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.90-alt1
- vncpasswd compatibility to tightvnc

* Tue Mar 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.90-alt0.20100219svn3993
- initial release

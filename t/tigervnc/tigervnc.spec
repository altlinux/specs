%define _deffontdir catalogue:%_sysconfdir/X11/fontpath.d

Name: tigervnc
Version: 1.1.0
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
Source7: xserver110.patch

Source100: xorg-server-source-1.12.1.tar.bz2

Patch0: tigervnc-102434.patch
Patch4: tigervnc-cookie.patch
Patch8: tigervnc-viewer-reparent.patch
Patch10: tigervnc11-ldnow.patch
Patch11: tigervnc11-gethomedir.patch
Patch13: tigervnc11-rh692048.patch
Patch14: tigervnc11-xorg111.patch
Patch15: tigervnc11-xorg112.patch

Patch100: tigervnc-1.1.0-tightvnc-passwd.patch
Patch101: tigervnc-1.0.90-vncviewer-iso10646-1.patch
Patch102: tigervnc-1.1.0-alt-xor.patch

# Automatically added by buildreq on Tue Mar 30 2010
BuildRequires: ImageMagick-tools doxygen flex gcc-c++ libGL-devel libSM-devel libX11-devel libXau-devel libXdmcp-devel libXext-devel libXfont-devel
BuildRequires: libXi-devel libXtst-devel libpciaccess-devel libpixman-devel libssl-devel libxkbfile-devel xorg-bigreqsproto-devel xorg-damageproto-devel
BuildRequires: xorg-fixesproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-resourceproto-devel xorg-scrnsaverproto-devel xorg-videoproto-devel
BuildRequires: xorg-xcmiscproto-devel xorg-xf86driproto-devel xorg-xtrans-devel zlib-devel libjpeg-devel desktop-file-utils intltool xorg-util-macros
BuildRequires: xorg-font-utils libfontenc-devel xorg-compositeproto-devel xorg-sdk libturbojpeg-devel xorg-glproto-devel
BuildRequires: libgnutls-devel libgcrypt-devel libgpg-error-devel libpam-devel
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
%setup -q -n %name-%version

mkdir -p m4
touch config.rpath

%patch0 -p1 -b .102434
%patch4 -p1 -b .cookie
%patch8 -p1 -b .viewer-reparent
%patch10 -p1 -b .ldnow
%patch11 -p1 -b .gethomedir
%patch13 -p1 -b .rh692048
%patch101 -p1 -b .iso10646-1
%patch102 -p1 -b .xor

tar -xjf %SOURCE100 -C unix/xserver
%patch14 -p1
pushd unix/xserver
patch -p1 -b --suffix .vnc < %{SOURCE7}
%patch15 -p1
popd

%patch100 -p1

# Use newer gettext
sed -i "s|AM_GNU_GETTEXT_VERSION.*|GETTEXT_PACKAGE=%name\nAC_SUBST(GETTEXT_PACKAGE)\nIT_PROG_INTLTOOL|" configure.ac
sed -i "s|^\(.*\)|\1 ru|" po/LINGUAS

#install -m0644 %_includedir/xorg/xf86Module.h unix/xserver/hw/xfree86/common/xf86Module.h

%build
%autoreconf
%configure \
	--with-system-jpeg \
	--disable-static
%make_build

pushd unix/xserver
%autoreconf
%configure \
	--enable-ipv6 \
	--disable-xorg \
	--disable-xnest \
	--disable-xvfb \
	--disable-dmx \
	--disable-xwin \
	--disable-xephyr \
	--disable-kdrive \
	--disable-static \
	--disable-xinerama \
	--disable-composite \
	--with-default-font-path=%_deffontdir \
	--with-xkb-output=%_localstatedir/xkb \
	--enable-glx \
	--disable-dri \
	--enable-dri2 \
	--disable-config-dbus \
	--disable-config-hal \
	--with-module-dir="%_xorgmoduledir" \
	--disable-unit-tests

%make_build
popd

# Build icons
pushd media
%make
popd

%install
%make DESTDIR=%buildroot install

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

# Install desktop stuff
mkdir -p %buildroot%_datadir/icons/hicolor/{16x16,24x24,48x48}/apps

pushd media/icons

convert +antialias -background transparent tigervnc.svg tigervnc_48.png
convert +antialias -background transparent ../tigervnc_16.svg tigervnc_16.png
for s in 16 48; do
install -m644 tigervnc_$s.png %buildroot%_datadir/icons/hicolor/${s}x$s/apps/tigervnc.png
done
popd

mkdir -p %buildroot%_datadir/applications
desktop-file-install --dir %buildroot%_datadir/applications %SOURCE6

#find_lang %name

%files
%doc LICENCE.TXT
%_bindir/vncviewer
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_man1dir/vncviewer.1*

%files server
%_initddir/vncserver
%config(noreplace) %_sysconfdir/sysconfig/vncservers
%_bindir/vncconfig
%_bindir/vncpasswd
%_bindir/x0vncserver
%_bindir/Xvnc
%_bindir/vncserver
%_man1dir/Xvnc.1*
%_man1dir/vncpasswd.1*
%_man1dir/vncconfig.1*
%_man1dir/vncserver.1*
%_man1dir/x0vncserver.1*

%files -n xorg-extension-vnc
%_xorgmoduledir/extensions/*.so

%changelog
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

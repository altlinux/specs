%define _unpackaged_files_terminate_build 1
%define _deffontdir catalogue:%_sysconfdir/X11/fontpath.d
%define _xorgmoduledir %_libdir/X11/modules

Name: tigervnc
Version: 1.15.0
Release: alt1

Summary: A TigerVNC remote display system
License: GPL-2.0-or-later
Group: Networking/Remote access
Url: https://tigervnc.org
VCS: https://github.com/TigerVNC/tigervnc.git

BuildRequires(pre): rpm-macros-cmake
Provides: tightvnc
Requires: fonts-bitmap-misc
Requires: xauth
Requires: xkeyboard-config
Requires: xorg-dri-swrast
Obsoletes: tightvnc

Source0: %name-%version.tar
Source1: vncserver.init
Source2: vncserver.service
Source3: vncserver.pl
Source4: vncserver.man

Source100: xorg-server-21.1.8.tar
Source200: repatch_spec.sh

## FC patches
Patch1: FC-vncsession-restore-script-systemd-service.patch
Patch2: FC-xserver120.patch

## Ubuntu patches
Patch103: Ubuntu-0002-fix-linking.patch
Patch109: Ubuntu-0205-defined-CMAKE_INSTALL_FULL_BINDIR.patch

## ALT patches
Patch501: tigervnc-stdinpasswd.patch

BuildRequires: ImageMagick-tools
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: libGL-devel
BuildRequires: libXaw-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXfont2-devel
BuildRequires: libXinerama-devel
BuildRequires: libXpm-devel
BuildRequires: libXrandr-devel
BuildRequires: libXres-devel
BuildRequires: libXtst-devel
BuildRequires: libXv-devel
BuildRequires: libaudit-devel
BuildRequires: libavcodec-devel
BuildRequires: libdrm-devel
BuildRequires: libfltk-devel
BuildRequires: libgbm-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgnutls-devel
BuildRequires: libjpeg-devel
BuildRequires: libnettle-devel
BuildRequires: libpam-devel
BuildRequires: libpciaccess-devel
BuildRequires: libpixman-devel
BuildRequires: libselinux-devel
BuildRequires: libssl-devel
BuildRequires: libswscale-devel
BuildRequires: libtasn1-devel
BuildRequires: libudev-devel
BuildRequires: libxcb-render-util-devel
BuildRequires: libxcbutil-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: libxcbutil-image-devel
BuildRequires: libxcbutil-keysyms-devel
BuildRequires: libxkbfile-devel
BuildRequires: libxshmfence-devel
BuildRequires: perl-parent
BuildRequires: xmlto
BuildRequires: xorg-xtrans-devel
BuildRequires: zlib-devel

BuildRequires: libfltk-devel >= 1.3.3

BuildRequires: xorg-sdk xorg-font-utils

BuildRequires: libXrender-devel libxcvt-devel

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
Provides: tightvnc-server
Requires: tigervnc-common = %EVR
Requires: tigervnc-pam = %EVR
Obsoletes: tightvnc-server

%description server
The VNC system allows you to access the same desktop from a wide
variety of platforms.  This package is a TigerVNC server, allowing
others to access the desktop on your machine.

%package common
Summary: A TigerVNC password utility
Group: Networking/Remote access
Conflicts: turbovnc-server

%description common
A TigerVNC password utility

%package -n xorg-extension-vnc
Summary: VNC extension for Xorg
Group: Networking/Remote access
Requires: %name-common = %version-%release, %name-pam = %version-%release

%description -n xorg-extension-vnc
TigerVNC extension for Xorg server

%package pam
Summary: PAM module for TigerVNC servers
Group: Networking/Remote access

%description pam
PAM module for TigerVNC servers

%prep
%setup -a100
cp %SOURCE3 %SOURCE4 .

## FC apply patches
%patch1 -p1 -b .vncsession-restore-script-systemd-service

## Ubuntu apply patches
%patch103 -p1
%patch109 -p1

## ALT apply patches
%patch501 -p1

%build

%add_optflags -fPIC
%cmake -DCMAKE_INSTALL_UNITDIR:PATH=%_unitdir
%cmake_build

cp -a unix/xserver  %_cmake__builddir/unix/
cp -a xorg-server-*/* %_cmake__builddir/unix/xserver/

patch -p1 -i `pwd`/unix/xserver21.patch -d %_cmake__builddir/unix/xserver

%autoreconf %_cmake__builddir/unix/xserver
( cd %_cmake__builddir/unix/xserver
  %configure \
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
	--disable-xephyr \
	--disable-xnest \
	--disable-xorg \
	--disable-xvfb \
	--disable-wayland \
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
	--with-xkb-output=%_localstatedir/xkb \
        || exit 1
)

%make_build -C %_cmake__builddir/unix/xserver \
	    LIBS="-ljpeg -lpam -lz -lgnutls -lm" \
	    CPPFLAGS="-I/usr/include/libdrm" \
	    TIGERVNC_SRCDIR=`pwd` \
	    #

%install
%cmakeinstall_std
%makeinstall_std -C %_cmake__builddir/unix/xserver/hw/vnc

# Install Xvnc as service
install -pD -m755 %SOURCE1 %buildroot%_initddir/vncserver

mkdir -p %buildroot%_sysconfdir/sysconfig
cat << __EOF__ > %buildroot%_sysconfdir/sysconfig/vncservers
# The VNCSERVERS variable is a list of display:user pairs.
# The VNCSERVERARGS[N] variable is a list of display's (N) parameters.
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
# VNCSERVERARGS[1]="-geometry 800x600 -localhost"
__EOF__

install -D contrib/packages/rpm/el7/SOURCES/10-libvnc.conf \
	%buildroot%_sysconfdir/X11/xorg.conf.d/vnc.conf

install vncserver.pl %buildroot/%_bindir/vncserver
install vncserver.man %buildroot/%_man1dir/vncserver.1

%find_lang %name

%files -f %name.lang
%doc LICENCE.TXT *.rst
%_bindir/vncviewer
%_desktopdir/*.desktop
%_docdir/tigervnc/
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_libdir/X11/modules/extensions/libvnc.la
%_man1dir/vncviewer.1*
%_datadir/metainfo/org.tigervnc.vncviewer.metainfo.xml


%files server
%_initddir/vncserver
%_unitdir/vncserver@.service
%config(noreplace) %_sysconfdir/sysconfig/vncservers
%config(noreplace) %_sysconfdir/tigervnc
%_bindir/vncconfig
%_bindir/x0vncserver
%_bindir/Xvnc
%_bindir/vncserver
%_sbindir/*
%_prefix/libexec/*
%_man1dir/Xvnc.1*
%_man1dir/vncconfig.1*
%_man8dir/*.8*
%_man1dir/x0vncserver.1*
%_man1dir/vncserver.1*

%files common
%_bindir/vncpasswd
%_man1dir/vncpasswd.1*

%files pam
%_sysconfdir/pam.d/*

%files -n xorg-extension-vnc
%config(noreplace) %_sysconfdir/X11/xorg.conf.d/vnc.conf
%_xorgmoduledir/extensions/*.so

%changelog
* Mon Feb 24 2025 Constantin Sunzow <protvin@altlinux.org> 1.15.0-alt1
- Removed obsoleted tightpasswd.
- Change license to SPDX format.
- Update Url tag.
- Add VCS tag.
- New version.

* Tue Dec 19 2023 Fr. Br. George <george@altlinux.org> 1.13.1-alt2
- Eliminate missing -rfbwait option

* Fri Oct 13 2023 Fr. Br. George <george@altlinux.org> 1.13.1-alt1
- Udate to 1.13.1
- Update patches

* Fri Aug 06 2021 Fr. Br. George <george@altlinux.ru> 1.11.0-alt1
- Udate to 1.11.0
- Update patches

* Mon Jan 25 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10.1-alt5
- Fixed desktop file (Closes: 39595).

* Tue Nov 17 2020 Fr. Br. George <george@altlinux.ru> 1.10.1-alt4
- Fix CVE-2020-26117

* Thu Sep 17 2020 Fr. Br. George <george@altlinux.ru> 1.10.1-alt3
- Update patches, fix vncviwewer "invalid resolution" bug

* Sat Jun 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.1-alt2
- add explicit libGL-devel buildreq

* Thu Jun 04 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.10.1-alt1
- New version
- Update FC-passwd-crash-with-malloc-checks.patch

* Thu Dec 19 2019 Fr. Br. George <george@altlinux.ru> 1.10.0-alt1
- Version up
- Update to XServer 1.20.6
- Update patches

* Wed Jul 24 2019 Fr. Br. George <george@altlinux.ru> 1.9.0-alt4
- Update to XServer 1.20 (ALT: #37059)

* Thu May 30 2019 Pavel Moseev <mars@altlinux.org> 1.9.0-alt3
- fix tooltip translation

* Tue May 07 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.9.0-alt2
- Spec cleanup
- Fix repocop's test 'rpm-filesystem-conflict-file'

* Mon Mar 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.9.0-alt1
- New version (ALT #36339)
- Update FC-getmaster.patch and tigervnc-stdinpasswd.patch

* Wed Aug 02 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.8.0-alt2
- Rebuild with new xorg-server (1.19.3) - fix discrepancy of ABI vnc-module and server
- Update FC-xserver116-rebased.patch

* Wed Aug 02 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.8.0-alt1
- New version
- Removed FC patch (.libvnc-os)
- Updated buildrequires

* Fri Jan 27 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.7.0-alt2
- vncserver.init: added ability to specify the display settings
- default "xstartup": added exporting environment variable LANG

* Tue Jan 10 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.7.0-alt1
- New version (ALT #32741, #32898)

* Mon Apr 25 2016 Fr. Br. George <george@altlinux.ru> 1.6.0-alt1
- Update FC patches, fix one
- (cas@) New version (ALT #30662)
- (cas@) Rebuild with xorg-server 1.18.2
- (cas@) Package vncserver@.service file
- (cas@) Return missing xorg-extension-vnc configuration file

* Thu Jun 25 2015 Fr. Br. George <george@altlinux.ru> 1.3.1-alt1
- Version update
- FC patches import
- Old vncpasswd binary renamed to tightpasswd

* Wed Apr 22 2015 Fr. Br. George <george@altlinux.ru> 1.3.0-alt1
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

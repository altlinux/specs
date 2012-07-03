Name: xbmc
Version: 11.0
Release: alt2

Summary: XBMC Media Center
License: GPL
Group: Video
Url: http://xbmc.org

Requires: xbmc-data = %version-%release

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++ gperf nasm
BuildRequires: boost-devel bzlib-devel libmysqlclient-devel libSDL_image-devel libSDL_mixer-devel
BuildRequires: libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel
BuildRequires: libXdmcp-devel libXext-devel libXft-devel libXinerama-devel libXmu-devel
BuildRequires: libXpm-devel libXrandr-devel libXt-devel libXtst-devel libSM-devel libxkbfile-devel
BuildRequires: libX11-devel libXfixes-devel libXrender-devel xorg-xproto-devel
BuildRequires: libalsa-devel libass-devel libavahi-devel libcdio-devel libcurl-devel
BuildRequires: libenca-devel libexpat-devel libfaad-devel libflac-devel libfribidi-devel
BuildRequires: libglew-devel libjasper-devel libjpeg-devel liblzo2-devel libyajl-devel
BuildRequires: libmad-devel libmicrohttpd-devel libmms-devel libmodplug-devel libmpeg2-devel
BuildRequires: libpcrecpp-devel libpng-devel libsamplerate-devel libsmbclient-devel
BuildRequires: libsqlite3-devel libtiff-devel libvorbis-devel libwavpack-devel
BuildRequires: libavfilter-devel libavformat-devel libpostproc-devel libswscale-devel libva-devel libvdpau-devel
BuildRequires: libdbus-devel libplist-devel libssh-devel librtmp-devel python-devel unzip zip
BuildRequires: libbluray-devel libpulseaudio-devel fontconfig-devel libfreetype-devel
BuildRequires: libbluez-devel libudev-devel

%package data
Summary: XBMC architecture-independent data
Group: Video
BuildArch: noarch

%description
XBMC Media Center is an media-player and entertainment hub for all your digital media.

%description data
XBMC Media Center is an media-player and entertainment hub for all your digital media.
This package contains all architecture-independent data requried for XBMC.

%define docdir %_defaultdocdir/%name-%version

%prep
%setup

%build
[ ! -x bootstrap ] || sh bootstrap
GIT_REV='20120322-14feb09' \
%configure --disable-non-free
%make_build

%install
make \
    DESTDIR=%buildroot \
    bindir=%_bindir \
    libdir=%_libdir \
    datadir=%_datadir install

rm -rf \
    %buildroot%_datadir/xbmc/addons/library.xbmc.* \
    %buildroot%_datadir/xbmc/system/players/dvdplayer/etc \
    %buildroot%_datadir/xbmc/system/players/paplayer

mv %buildroot%_datadir/doc/xbmc %buildroot%docdir

mkdir -p \
    %buildroot%_sysconfdir/sysconfig \
    %buildroot%_sysconfdir/X11/wmsession.d \
    %buildroot%_libdir/xbmc/system/players/paplayer/timidity

cat >%buildroot%_libdir/xbmc/system/players/paplayer/timidity/timidity.cfg << 'E_O_F'
dir /usr/share/timidity
source midia.cfg
E_O_F

cat >%buildroot%_sysconfdir/X11/wmsession.d/20XBMC << 'E_O_F'
NAME=XBMC
ICON=/usr/share/xbmc/media/icon32x32.png
DESC=XBMC Media Center
EXEC=/usr/bin/xbmc-standalone
SCRIPT:
exec /usr/bin/xbmc-standalone
E_O_F

cat >%buildroot%_bindir/xbmc << 'E_O_F'
#!/bin/sh
FEH="%_datadir/xbmc/FEH.py"

[ ! -f "$FEX" ] || {
    python "$FEH" "$@"
    [ $? -eq 0 ] || exit $?
}

exec %_libdir/xbmc/xbmc.bin "$@"
E_O_F

cat >%buildroot%_bindir/xbmc-standalone << 'E_O_F'
#!/bin/sh
while ! %_libdir/xbmc/xbmc.bin -fs --standalone; do :; done
E_O_F

%add_python_req_skip xbmc
%add_python_req_skip xbmcgui
%add_python_req_skip xbmcaddon

%files
%docdir

%config(noreplace) %_sysconfdir/X11/wmsession.d/20XBMC

%_bindir/xbmc
%_bindir/xbmc-standalone

%_datadir/xsessions/XBMC.desktop
%_desktopdir/xbmc.desktop
%_iconsdir/hicolor/*/apps/xbmc.png

%dir %_libdir/xbmc

%_libdir/xbmc/system
%_libdir/xbmc/addons

%_libdir/xbmc/xbmc.bin
%_libdir/xbmc/xbmc-xrandr

%files data
%dir %_datadir/xbmc
%_datadir/xbmc/FEH.py
%_datadir/xbmc/addons
%_datadir/xbmc/language
%_datadir/xbmc/media
%_datadir/xbmc/sounds
%_datadir/xbmc/system
%_datadir/xbmc/userdata

%changelog
* Tue May 08 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0-alt2
- 11.0 Eden-r2 released

* Sun Mar 25 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0-alt1
- 11.0 Eden released

* Fri Mar 16 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0-alt0.5
- 11.0-RC2 released

* Tue Feb 28 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0-alt0.4
- 11.0-RC1 released

* Fri Feb 10 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0-alt0.3
- 11.0-beta3 released

* Sun Jan 22 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0-alt0.2
- 11.0-beta2 released

* Sat Dec 31 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0-alt0.1
- 11.0-beta1 released

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 10.1-alt1.1
- Rebuild with Python-2.7

* Wed Aug 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.1-alt1
- 10.1 released

* Fri Dec 17 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.0-alt1
- 10.0 Dharma released

* Sat Dec 04 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.0-alt0.5
- rc2 released

* Sun Oct 31 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.0-alt0.4
- beta4 released

* Thu Oct 14 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.0-alt0.3
- beta3 released

* Wed Sep 08 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.0-alt0.2
- beta2 released

* Sun Aug 15 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.11-alt5
- preview build for forthcoming 'dharma' release

* Sat May 29 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.11-alt3
- tvheadend pvr plugin added

* Sun Apr 04 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.11-alt2
- use ffmpeg for dts from now

* Thu Dec 31 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.11-alt1
- 9.11 released
- PVR stuff added

* Tue Dec 15 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.0.4-alt5
- fixed breakage on nvidia proprietary drivers >= 190.xx
- fixed for and rebuilt with python 2.6 (real@)

* Mon Nov 16 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.0.4-alt4
- rebuilt with recent libcdio

* Sat Nov 07 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.0.4-alt3
- rebuilt with recent cdio

* Thu Oct  8 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.0.4-alt2
- few minor packaging improvements

* Wed Sep  9 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.0.4-alt1
- Initial build.

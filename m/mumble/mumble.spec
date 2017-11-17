%define _pseudouser_user     _mumble
%define _pseudouser_group    _mumble
%define _pseudouser_home     %_localstatedir/mumble-server

Name: mumble
Version: 1.2.8
Release: alt3

Summary: Voice chat software primarily intended for use while gaming
License: BSD
Group: Networking/Chat

Url: http://%name.sourceforge.net/

Source0: %name-%version.tar
Source1: altlinux.tar
Source2: celt-0.7.0-src.tar

Patch0: configure-libs.patch
Patch1: overlay_gl.patch
Patch2: mumble-overlay.patch
Patch3: mumble-fix-ftbfs.patch

%def_without sys_celt

%if_with sys_celt
%define celtopts celt no-bundled-celt
%else
%define celtopts celt bundled-celt
%endif

BuildRequires: boost-python-devel gcc-c++ libGL-devel libX11-devel libXi-devel libalsa-devel libavahi-devel libcap-devel libice-devel libogg-devel libprotobuf-devel libpulseaudio-devel libqt4-devel libsndfile-devel libspeechd-devel protobuf-compiler
BuildRequires: libspeex-devel libspeexdsp-devel
BuildRequires: libopus-devel

%if_with sys_celt
BuildRequires: libcelt-devel
Requires: libcelt >= 0:0.7.0-alt1
%endif

Requires: libqt4-sql-sqlite

%description
Low-latency, high-quality voice communication for gamers.
Includes game linking, so voice from other players comes
from the direction of their characters, and has echo
cancellation so the sound from your loudspeakers
won't be audible to other players.

%package -n murmur
Summary: Mumble voice chat server
Group: System/Servers
Provides: %name-server = %version-%release

%description -n murmur
Murmur (also called mumble-server) is part of VoIP suite Mumble
primarily intended for gamers. Murmur is server part of suite.

%package plugins
Summary: Plugins for VoIP program Mumble
Group: System/Libraries
Requires: %name = %version-%release

%description plugins
Mumble-plugins is part of VoIP suite Mumble primarily intended
for gamers. This plugin allows game linking so the voice of
players will come from the direction of their characters.

%package overlay
Summary: Start Mumble with overlay
Group: Networking/Chat
Requires: %name = %version-%release

%description overlay
Mumble-overlay is part of VoIP suite Mumble primarily intended
for gamers. Mumble-overlay shows players in current channel and linked channels
in game so you don't need to quit the game to see who is in your channel.

%package protocol
Summary: Package to support mumble protocol
Group: Networking/Chat
Requires: %name = %version-%release
#Requires: kde-filesystem

%description protocol
Low-latency, high-quality voice communication for gamers.
Includes game linking, so voice from other players comes
from the direction of their characters, and has echo
cancellation so the sound from your loudspeakers
won't be audible to other players.

%prep
%setup -a1 -a2
%patch0 -p2
%patch1 -p2
%patch2 -p2
%patch3 -p2

%build
%add_optflags -fpermissive
qmake-qt4 -recursive "CONFIG+=no-oss speex no-bundled-speex %celtopts opus no-bundled-opus no-g15 no-embed-qt-translation no-update" \
QMAKE_CFLAGS+='%optflags' \
QMAKE_CXXFLAGS+='%optflags' \
DEFINES+=PLUGIN_PATH=%_libdir/%name \
DEFINES+=DEFAULT_SOUNDSYSTEM=PulseAudio main.pro
%make_build

%install
# binaries
install -pD -m0755 release/%name %buildroot%_bindir/%name
#install -pD -m0755 release/%{name}11x %buildroot%_bindir/%{name}11x
install -pD -m0755 release/murmurd %buildroot%_sbindir/murmurd

install -d %buildroot%_libdir/%name/
cp -a release/libmumble.so* %buildroot%_libdir/
%if_without sys_celt
cp -a release/libcelt*.so* %buildroot%_libdir/%name/
%endif
install -p release/plugins/*.so %buildroot%_libdir/%name/

# murmur config
mkdir -p %buildroot%_sysconfdir/murmur/
install -pD scripts/murmur.ini %buildroot%_sysconfdir/murmur/murmur.ini

# murmur initscript
install -pDm0755 altlinux/murmur.init %buildroot%_initdir/murmur
install -pDm0644 altlinux/murmur.sysconfig %buildroot%_sysconfdir/sysconfig/murmur

# murmur logrotate
install -pDm0644 altlinux/murmur.logrotate %buildroot%_sysconfdir/logrotate.d/murmur

# overlay script. untested
mkdir -p %buildroot%_datadir/%name/
install -pD scripts/%name-overlay %buildroot%_bindir/%name-overlay

# man pages
mkdir -p %buildroot%_man1dir/
install -pD -m0644 man/murmurd.1 %buildroot%_man1dir/
install -pD -m0644 man/mumble* %buildroot%_man1dir/

#icons
install -pD icons/%name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

# desktop file
install -pD scripts/mumble.desktop %buildroot%_desktopdir/mumble.desktop

# install the mumble protocol
install -pD -m0644 scripts/%name.protocol %buildroot%_datadir/kde4/services/%name.protocol

# dbus murmur.conf
install -pD -m0644 scripts/murmur.conf %buildroot%_sysconfdir/dbus-1/system.d/murmur.conf

# dir for mumble-server.sqlite
mkdir -p %buildroot%_var/lib/mumble-server/

# log dir
mkdir -p %buildroot%_logdir/mumble-server/

# pid dir
mkdir -p %buildroot%_var/run/mumble-server/

%pre -n murmur
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'Mumble-server(murmur) user' \
	-d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%preun -n murmur
%preun_service murmur

%post -n murmur
%post_service murmur

%files
%doc README README.Linux LICENSE CHANGES
%doc scripts/*.pl
#%doc scripts/*php scripts/qt.conf
%_libdir/libmumble.so*
%if_without sys_celt
%_libdir/%name/libcelt*.so*
%endif
%_bindir/%name
#%_bindir/%{name}11x
#%%attr(664,root,root) %_datadir/%name/*
%_man1dir/%{name}*
%_iconsdir/hicolor/scalable/apps/%name.svg
%_desktopdir/%name.desktop

%files -n murmur
%doc README README.Linux CHANGES
%_sbindir/murmurd
%_initdir/murmur
%config(noreplace) %_sysconfdir/sysconfig/murmur
%dir %attr(0770,root,%_pseudouser_group) %_sysconfdir/murmur/
%config(noreplace) %attr(660,root,%_pseudouser_group) %_sysconfdir/murmur/murmur.ini
%_man1dir/murmurd.1*
%_sysconfdir/logrotate.d/murmur
%_sysconfdir/dbus-1/system.d/murmur.conf
%dir %attr(0770,root,%_pseudouser_group) %_pseudouser_home/
%dir %attr(0770,root,%_pseudouser_group) %_logdir/mumble-server/
%dir %attr(0775,root,%_pseudouser_group) %_var/run/mumble-server/

%files plugins
%_libdir/%name
%if_without sys_celt
%exclude %_libdir/%name/libcelt*.so*
%endif

%files overlay
%_bindir/%name-overlay

%files protocol
%_datadir/kde4/services/mumble.protocol

%changelog
* Fri Nov 17 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.8-alt3
- fix build

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.8-alt2.1.1
- NMU: added BR: libspeexdsp-devel

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2.8-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Mar 11 2015 Paul Wolneykien <manowar@altlinux.org> 1.2.8-alt2
- Configure speex, celt and opus libraries properly (patch).
- Build with bundled CELT codec (v0.7.0 and v0.11.0).

* Mon Mar 09 2015 Paul Wolneykien <manowar@altlinux.org> 1.2.8-alt1
- Freshed-up to the v1.2.8.
- Add libspeechd.patch.

* Fri Dec 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt2.1
- Fixed build with gcc 4.7

* Tue Nov 23 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.2.2-alt2
- Rebuild with libssl.so.10 and libcrypto.so.10.

* Fri Mar 05 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus (based on fedora spec).

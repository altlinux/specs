%def_without system_celt

%define _pseudouser_user     _mumble
%define _pseudouser_group    _mumble
%define _pseudouser_home     %_localstatedir/murmur
%define _pidfile_dir         /run/

Name: mumble
Version: 1.2.19
Release: alt1

Summary: Low latency encrypted VoIP client

Group: Networking/Chat
License: BSD
Url: http://mumble.info/

# VCS0: git://github.com/mumble-voip/mumble.git
Source0: %name-%version.tar
# VCS1: git://github.com/mumble-voip/celt-0.7.0-src.git
Source1: celt-0.7.0-src.tar
# VCS2: git://github.com/mumble-voip/celt-0.11.0-src.git
Source2: celt-0.11.0-src.tar

Patch: %name-%version-%release.patch

%if_with system_celt
%define celtopts celt no-bundled-celt
%else
%define celtopts celt bundled-celt
%endif

BuildRequires: boost-python-devel gcc-c++ libGL-devel libX11-devel libXi-devel libalsa-devel libavahi-devel libcap-devel libice-devel libogg-devel libprotobuf-devel libpulseaudio-devel libqt4-devel libsndfile-devel libspeechd-devel protobuf-compiler
BuildRequires: libspeex-devel libspeexdsp-devel
BuildRequires: libopus-devel

%if_with system_celt
BuildRequires: libcelt-devel
Requires: libcelt >= 0:0.7.0-alt1
%endif

%description
Mumble is a low-latency, high quality voice chat program primarily intended
for gaming. It features noise suppression, encrypted connections for both voice
and instant messaging, automatic gain control and low latency audio
with support for multiple audio standards. Mumble includes an in-game
overlay compatible with most open-source and commercial 3D applications.

%package -n murmur
Summary: Mumble voice chat server
Group: System/Servers
Provides: %name-server = %version-%release

Requires: libqt4-sql-sqlite

%description -n murmur
Murmur is the VoIP server component for Mumble. Murmur is installed
in a system-wide fashion, but can also be run by individual users.
Each murmur process supports multiple virtual servers, each with their
own user base and channel list.

%package plugins
Summary: Application helper plugins for Mumble
Group: System/Libraries
Requires: %name = %version-%release

%description plugins
This package is part of Mumble, a low-latency, high quality VoIP suite
primarily intended for gaming. Applications linked to these plugins can
augment the voices of chat participants; for example, a game can make
every chat participant sound as if their voice came from their character.

%package overlay
Summary: Start Mumble with overlay
Group: Networking/Chat
BuildArch: noarch
Requires: %name = %version-%release

%description overlay
This package is part of Mumble, a low-latency, high quality VoIP suite
primarily intended for gaming. Mumble's interactive overlay shows players
in current channel and linked channels in-game so the player needs not quit
the game to control Mumble.

%package protocol
Summary: Mumble protocol support for KIO
Group: Networking/Chat
BuildArch: noarch
Requires: %name = %version-%release
#Requires: kde-filesystem

%description protocol
This package is part of Mumble, a low-latency, high quality VoIP suite
primarily intended for gaming. It provides a KIO protocol description.

%prep
%setup -a1 -a2
%patch -p1

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
%if_without system_celt
cp -a release/libcelt*.so* %buildroot%_libdir/%name/
%endif
install -p release/plugins/*.so %buildroot%_libdir/%name/

# murmur config
mkdir -p %buildroot%_sysconfdir/murmur/
install -pD altlinux/murmur.ini %buildroot%_sysconfdir/murmur/murmur.ini

# murmur initscript
install -pDm0755 altlinux/murmur.service %buildroot%_unitdir/murmur.service
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
install -pD altlinux/mumble.desktop %buildroot%_desktopdir/mumble.desktop

# install the mumble protocol
install -pD -m0644 scripts/%name.protocol %buildroot%_datadir/kde4/services/%name.protocol

# dbus murmur.conf
install -pD -m0644 altlinux/dbus-net.sourceforge.mumble.murmur.conf %buildroot%_sysconfdir/dbus-1/system.d/murmur.conf

# dir for mumble-server.sqlite
mkdir -p %buildroot%_pseudouser_home/

# log dir
mkdir -p %buildroot%_logdir/murmur/

# pid dir
#mkdir -p %buildroot%_pidfile_dir/murmur/

%pre -n murmur
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'Mumble-server (Murmur)' \
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
%if_without system_celt
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
%doc altlinux/doc/murmur*
%_sbindir/murmurd
%_unitdir/murmur.service
%_initdir/murmur
%config(noreplace) %_sysconfdir/sysconfig/murmur
%dir %attr(0770,root,%_pseudouser_group) %_sysconfdir/murmur/
%config(noreplace) %attr(660,root,%_pseudouser_group) %_sysconfdir/murmur/murmur.ini
%_man1dir/murmurd.1*
%_sysconfdir/logrotate.d/murmur
%_sysconfdir/dbus-1/system.d/murmur.conf
%dir %attr(0770,root,%_pseudouser_group) %_pseudouser_home/
%dir %attr(0770,root,%_pseudouser_group) %_logdir/murmur/
#ghost %attr(0775,root,%_pseudouser_group) %_pidfile_dir/murmur/

%files plugins
%_libdir/%name
%if_without system_celt
%exclude %_libdir/%name/libcelt*.so*
%endif

%files overlay
%_bindir/%name-overlay

%files protocol
%_datadir/kde4/services/mumble.protocol

%changelog
* Wed Jan 10 2018 Arseny Maslennikov <arseny@altlinux.org> 1.2.19-alt1
- Arch-independent subpackages are now properly considered noarch.
- Moved a Murmur dependency away from Mumble package.
- "/var/run" -> "/run" to adhere to FHS 3.0.
- "mumble-server" -> "murmur".
- Added a disclaimer to /etc/sysconfig/murmur.
- Added an XDG desktop entry for Mumble client.
- Added a dbus compatibility service file.
- Added a systemd-compatible service unit.
- Added a default config for a Murmur system instance.
- 1.2.8 -> 1.2.19.

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

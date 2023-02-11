%define _unpackaged_files_terminate_build 1

%define _pseudouser_user     _mumble
%define _pseudouser_group    _mumble
%define _pseudouser_home     %_localstatedir/murmur
%define _pidfile_dir         /run/

Name: mumble
%define build_number 287
Version: 1.4.287
Release: alt1

Summary: Low latency encrypted VoIP client

Group: Networking/Chat
License: BSD
Url: http://mumble.info/

# VCS0: git://github.com/mumble-voip/mumble.git
Source0: %name-%version.tar
# The altlinux directory from head.
Source1: altlinux.tar
# VCS2: git://github.com/mumble-voip/celt-0.11.0.git
#Source2: celt-0.11.0-src.tar
# VCS3: git://github.com/mumble-voip/rnnoise.git
#Source3: rnnoise-src.tar
# VCS4: git://github.com/mumble-voip/mumble.git, copied from current master.
Source4: themes.tar.xz

#Patch: %name-%version-%release.patch
Patch2: upstream-0002-CHANGE-client-Drop-support-for-all-legacy-codecs.patch
#Patch1: link-mumble-with-lGL.patch
#Patch2: link-overlay-with-lGL.patch
Patch3: replace-submodule-to-find-python.patch
Patch4: gtav-exclusive-x86_64.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= 3.15

BuildRequires: boost-devel-headers libalsa-devel libavahi-devel libcap-devel libprotobuf-devel libpulseaudio-devel libqtav-devel libsndfile-devel libspeechd-devel libssl-devel protobuf-compiler
# BuildRequires: python3-modules-xml
BuildRequires: qt5-3d-devel qt5-charts-devel qt5-connectivity-devel qt5-datavis3d-devel qt5-enginio-devel qt5-gamepad-devel qt5-multimedia-devel qt5-networkauth-devel qt5-quickcontrols2-devel qt5-remoteobjects-devel qt5-script-devel qt5-scxml-devel qt5-sensors-devel qt5-serialbus-devel qt5-serialport-devel qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-virtualkeyboard-devel qt5-wayland-devel qt5-x11extras-devel qt5-xmlpatterns-devel
BuildRequires: libpoco-devel
# Poco dependencies. Should libpoco-devel depend on them?
BuildRequires: libpcre2-devel
BuildRequires: libexpat-devel
BuildRequires: libspeex-devel libspeexdsp-devel
BuildRequires: libopus-devel
BuildRequires: librnnoise-devel

Requires: qt5-sql-sqlite3

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

Requires: qt5-sql-sqlite3

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
Requires: %name = %version-%release

%description overlay
This package is part of Mumble, a low-latency, high quality VoIP suite
primarily intended for gaming. Mumble's interactive overlay shows players
in current channel and linked channels in-game so the player needs not quit
the game to control Mumble.

#package protocol
#Summary: Mumble protocol support for KIO
#Group: Networking/Chat
#BuildArch: noarch
#Requires: %name = %version-%release
#Requires: kde-filesystem

#description protocol
#This package is part of Mumble, a low-latency, high quality VoIP suite
#primarily intended for gaming. It provides a KIO protocol description.

%prep
%setup -a1 -a4
#setup -a1 -a2
#setup -a3 -a4
#patch -p1
#patch1 -p1
#patch2 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -Dpackaging:BOOL=ON \
    -DBUILD_NUMBER=%build_number \
    -Dbundled-opus:BOOL=OFF \
    -Dbundled-speex:BOOL=OFF \
    -Dclient:BOOL=ON \
    -Dice:BOOL=OFF \
    -Doss:BOOL=OFF \
    -Drnnoise:BOOL=ON \
    -Dbundled-rnnoise:BOOL=OFF \
    -Dserver:BOOL=ON \
    -Dsymbols:BOOL=ON \
    -Doverlay-xcompile=OFF \
    #
%cmake_build

%install
%cmake_install

# Compatibility with pre-1.4.
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot%_sysconfdir/logrotate.d
mkdir -p %buildroot%_sysconfdir/dbus-1/system.d
ln -sr %buildroot%_bindir/mumble-server %buildroot%_sbindir/murmurd
ln -sr %buildroot%_unitdir/mumble-server.service %buildroot%_unitdir/murmur.service
ln -sr %buildroot%_initdir/mumble-server %buildroot%_initdir/murmur
ln -sr %buildroot%_man1dir/mumble-server.1 %buildroot%_man1dir/murmurd.1

# murmur config
mkdir -p %buildroot%_sysconfdir/murmur/
install -pD altlinux/murmur.ini %buildroot%_sysconfdir/murmur/murmur.ini

# murmur initscript
install -pDm0644 altlinux/murmur.service %buildroot%_unitdir/mumble-server.service
install -pDm0755 altlinux/murmur.init %buildroot%_initdir/mumble-server
install -pDm0644 altlinux/murmur.sysconfig %buildroot%_sysconfdir/sysconfig/murmur

# murmur logrotate
install -pDm0644 altlinux/murmur.logrotate %buildroot%_sysconfdir/logrotate.d/murmur

# dbus murmur.conf
install -pD -m0644 altlinux/dbus-net.sourceforge.mumble.murmur.conf %buildroot%_sysconfdir/dbus-1/system.d/murmur.conf

# dir for mumble-server.sqlite
mkdir -p %buildroot%_pseudouser_home

# log dir
mkdir -p %buildroot%_logdir/murmur

%pre -n murmur
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'Mumble-server (Murmur)' \
	-d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%preun -n murmur
%preun_service murmur

%post -n murmur
%post_service murmur

%files
%define xdg_name info.mumble.Mumble
%doc README.md LICENSE CHANGES docs
%_bindir/%name
%_man1dir/%{name}*
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%xdg_name.desktop
%_datadir/metainfo/%xdg_name.appdata.xml

%files -n murmur
%doc README.md LICENSE CHANGES
%doc altlinux/doc/murmur*
%_bindir/mumble-server
%_sbindir/murmurd
%_unitdir/mumble-server.service
%_unitdir/murmur.service
%_initdir/mumble-server
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
%_libdir/%name/plugins

%files overlay
%add_findreq_skiplist %_bindir/%name-overlay
%_libdir/%name/libmumbleoverlay*.so*
%_bindir/%name-overlay

%changelog
* Thu Jan 19 2023 Arseny Maslennikov <arseny@altlinux.org> 1.4.287-alt1
- 1.3.2 -> 1.4.287.
- Backported 4d05018c2e4f ("Drop support for all legacy codecs") from master.
  This removes support of all codecs but Opus from the client. Opus support was
  introduced in Mumble 1.2.4, released in 2013, so this is unlikely to be a
  real problem. Upstream plans to remove it in 1.5.0.

* Wed Jul 29 2020 Arseny Maslennikov <arseny@altlinux.org> 1.3.2-alt1
- 1.3.1 -> 1.3.2.

* Mon Jun 08 2020 Arseny Maslennikov <arseny@altlinux.org> 1.3.1-alt1
- 1.3.0 -> 1.3.1.

* Wed Apr 15 2020 Arseny Maslennikov <arseny@altlinux.org> 1.3.0-alt1
- 1.2.19 -> 1.3.0.

* Mon Mar 25 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.19-alt5
- Built in c++11 mode.

* Sun Jan 20 2019 Arseny Maslennikov <arseny@altlinux.org> 1.2.19-alt4
- murmur.service: Fixed wrong path to executable in ExecStart=.
- mumble: Added a dependency on libqt4-sql-sqlite since the client
  needs a database driver as well as the server.

* Fri Dec 21 2018 Dmitry V. Levin <ldv@altlinux.org> 1.2.19-alt3
- murmur: blindfoldedly built without Ice RPC support.

* Wed Sep 05 2018 Oleg Solovyov <mcpain@altlinux.org> 1.2.19-alt2
- fix build
- build with new openssl 1.1

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

%define _unpackaged_files_terminate_build 1

Name: snapcast
Version: 0.35.0
Release: alt1

Summary: Snapcast is a multi-room time-synced client-server audio player
License: GPL-3.0
Group: Sound
Url: https://github.com/snapcast/snapcast
Vcs: https://github.com/snapcast/snapcast

Source0: %name-%version.tar
Source1: snapserver.service
Source2: snapclient.service
Source3: snapserver.default
Source4: snapclient.default

BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ cmake ctest
BuildRequires: boost-asio-devel
BuildRequires: boost-beast-devel
BuildRequires: boost-filesystem-devel
BuildRequires: libsoxr-devel
BuildRequires: libalsa-devel
BuildRequires: pipewire-libs-devel
BuildRequires: libavahi-devel
BuildRequires: libflac++-devel
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel
BuildRequires: libopus-devel
BuildRequires: libexpat-devel
BuildRequires: catch-devel

%description
Snapcast is a multi-room client-server audio player, where all clients are
time synchronized with the server to play perfectly synced audio. It is not
a standalone player, but an extension that turns your existing audio player
into a Sonos-like multi-room solution. The server's audio input is a named
pipe /tmp/snapfifo. All data that is fed into this file will be send to the
connected clients. One of the most generic ways to use Snapcast is in
conjunction with the music player daemon (MPD) or Mopidy, which can be
configured to use a named pipe as audio output.

%package -n snapserver
Summary: Snapcast server
Group: Sound

%description -n snapserver
Snapcast is a multi-room client-server audio player, where all clients are
time synchronized with the server to play perfectly synced audio. It's not a
standalone player, but an extension that turns your existing audio player into
a Sonos-like multi-room solution.  The server's audio input is a named
pipe `/tmp/snapfifo`. All data that is fed into this file will be send to
the connected clients. One of the most generic ways to use Snapcast is in
conjunction with the music player daemon, MPD, or Mopidy, which can be configured
to use a named pipe as audio output.
This package contains the server to which clients connect.

%package -n snapclient
Summary: Snapcast client
Group: Sound

%description -n snapclient
Snapcast is a multi-room client-server audio player, where all clients are
time synchronized with the server to play perfectly synced audio. It's not a
standalone player, but an extension that turns your existing audio player into
a Sonos-like multi-room solution.
This package contains the client which connects to the server and plays the audio.

%prep
%setup

%build
%cmake -DWERROR=ON \
		-DBUILD_TESTS=ON \
		-DBUILD_WITH_PIPEWIRE=ON \
		-DCMAKE_INSTALL_SYSCONFDIR=/etc
%cmake_build

%install
%cmake_install

%__mkdir_p %buildroot%_sharedstatedir/snapserver

install -Dm644 %SOURCE1 %buildroot%_unitdir/snapserver.service
install -Dm644 %SOURCE2 %buildroot%_unitdir/snapclient.service
install -Dm644 %SOURCE3 %buildroot%_sysconfdir/default/snapserver
install -Dm644 %SOURCE4 %buildroot%_sysconfdir/default/snapclient

%pre -n snapclient
%_bindir/getent passwd snapclient >/dev/null || %_sbindir/useradd --user-group --system --groups audio snapclient

%pre -n snapserver
getent passwd snapserver > /dev/null || %_sbindir/useradd --user-group --system --home-dir %_sharedstatedir/snapserver snapserver

%post -n snapclient
%systemd_post snapclient.service

%post -n snapserver
%systemd_post snapserver.service

%preun -n snapclient
%systemd_preun snapclient.service

%preun -n snapserver
%systemd_preun snapserver.service

%postun -n snapclient
%systemd_postun_with_restart snapclient.service
if [ $1 -eq 0 ]; then
   %_sbindir/userdel --force snapclient 2>/dev/null; true
fi

%postun -n snapserver
%systemd_postun_with_restart snapserver.service

%check
bin/snapcast_test

%files -n snapclient
%_bindir/snapclient
%_mandir/man1/snapclient.1.*
%config(noreplace) %_sysconfdir/default/snapclient
%_unitdir/snapclient.service
%doc *.md LICENSE

%files -n snapserver
%_bindir/snapserver
%_mandir/man1/snapserver.1.*
%_datadir/snapserver
%_pixmapsdir/snapcast.svg
%config(noreplace) %_sysconfdir/snapserver.conf
%config(noreplace) %_sysconfdir/default/snapserver
%attr(0750,snapserver,snapserver) %dir %_sharedstatedir/snapserver
%_unitdir/snapserver.service
%doc doc

%changelog
* Mon Sep 07 2026 Bogdan Boguslavskij <bogdanb@altlinux.org> 0.35.0-alt1
- Initial build for Sisyphus.
- Built without Snapweb.


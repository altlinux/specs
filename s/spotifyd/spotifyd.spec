Name: spotifyd
Version: 0.3.3
Release: alt1
Epoch: 1

Summary: Spotify client
License: GPLv3
Group: Sound
Url: https://github.com/Spotifyd/spotifyd

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc
BuildRequires: libalsa-devel libdbus-devel libpulseaudio-devel libssl-devel

%description
Spotifyd is an open source Spotify client running as a UNIX daemon.
Spotifyd streams music just like the official client, but is more
lightweight and supports more platforms. Spotifyd also supports the
Spotify Connect protocol, which makes it show up as a device that
can be controlled from the official clients.

%prep
%setup -a1

%build
export CARGO_HOME=${PWD}/cargo
cargo build --release --features alsa_backend,dbus_keyring,dbus_mpris,pulseaudio_backend

%install
install -pm0755 -D target/release/spotifyd %buildroot%_bindir/spotifyd
install -pm0644 -D contrib/spotifyd.service %buildroot%_unitdir/spotifyd.service
install -pm0644 -D contrib/spotifyd-user.service %buildroot%_libexecdir/systemd/user/spotifyd.service
install -pm0640 -D contrib/spotifyd.conf %buildroot%_sysconfdir/spotifyd.conf
mkdir -p %buildroot%_cachedir/%name

%pre
/usr/sbin/groupadd -r -f _spotify &>/dev/null ||:
/usr/sbin/useradd -r -g _spotify -d %_cachedir/%name -s /dev/null \
    -c "spotifyd service" -M -n _spotify &>/dev/null ||:

%post
%post_service spotifyd

%preun
%preun_service spotifyd

%files
%config(noreplace) %attr(0640,root,_spotify) %_sysconfdir/spotifyd.conf

%_unitdir/spotifyd.service
%_libexecdir/systemd/user/spotifyd.service

%_bindir/spotifyd
%dir %attr(0770,root,_spotify) %_cachedir/%name

%changelog
* Tue Feb 01 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.3.3-alt1
- 0.3.3 released

* Wed Mar 17 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.3.2-alt1
- 0.3.2 released

* Tue Feb 02 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.3.0-alt1
- 0.3.0 released

* Mon Aug 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22.4-alt3
- freshen crates cache
- built without dbus_mpris

* Mon Jul 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22.4-alt2
- built without dbus_keyring

* Wed Jul 15 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22.4-alt1
- 0.22.4 released

* Thu Jan 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22.3-alt1
- initial

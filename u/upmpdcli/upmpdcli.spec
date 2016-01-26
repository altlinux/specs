Name: upmpdcli
Version: 0.13.0
Release: alt1

Summary: UPnP front-end to the Music Player Daemon
License: GPL
Group: Sound
Url: http://www.lesbonscomptes.com/upmpdcli

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libmpdclient-devel libupnpp-devel

%description
%name implements an UPnP Media Renderer, using MPD to perform
the real work.

It has been tested with a number of UPnP control points running on
Android and Windows. Because of their good support of OpenHome
Playlists, which are a significant improvement over bare UPnP,
and their general quality, Bubble UPnP (Android app) and Linn Kinsky
(free on Windows) work best with it.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -pm0755 -D upmpdcli.init %buildroot%_initdir/upmpdcli
install -pm0644 -D upmpdcli.sysconfig %buildroot%_sysconfdir/sysconfig/upmpdcli
install -pm0644 -D upmpdcli.service %buildroot%_unitdir/upmpdcli.service
mkdir -p %buildroot%_cachedir/%name
# next time for sure
rm -rf %buildroot%_datadir/%name/web

%pre
/usr/sbin/groupadd -r -f _upmpd &>/dev/null ||:
/usr/sbin/useradd -r -g _upmpd -d %_cachedir/%name -s /dev/null \
    -c "upmpdcli service" -M -n _upmpd &>/dev/null ||:

%post
%post_service upmpdcli

%preun
%preun_service upmpdcli

%files
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/upmpdcli

%_initdir/upmpdcli
%_unitdir/upmpdcli.service

%_bindir/scctl
%_bindir/upmpdcli

%_datadir/%name
%_man1dir/%name.1*

%dir %attr(0770,root,_upmpd) %_cachedir/%name

%changelog
* Tue Jan 26 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.0-alt1
- initial

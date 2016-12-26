Name: upmpdcli
Version: 1.2.10
Release: alt1

Summary: UPnP front-end to the Music Player Daemon
License: GPL
Group: Sound
Url: http://www.lesbonscomptes.com/upmpdcli

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libmpdclient-devel libupnpp-devel >= 0.14.1
BuildRequires: libmicrohttpd-devel jsoncpp-devel

%package plugins
Summary: %name plugins
Group: Sound
Requires: %name = %version-%release

%description
%name implements an UPnP Media Renderer, using MPD to perform
the real work.

It has been tested with a number of UPnP control points running on
Android and Windows. Because of their good support of OpenHome
Playlists, which are a significant improvement over bare UPnP,
and their general quality, Bubble UPnP (Android app) and Linn Kinsky
(free on Windows) work best with it.

%description plugins
%name implements an UPnP Media Renderer, using MPD to perform
the real work.

It has been tested with a number of UPnP control points running on
Android and Windows. Because of their good support of OpenHome
Playlists, which are a significant improvement over bare UPnP,
and their general quality, Bubble UPnP (Android app) and Linn Kinsky
(free on Windows) work best with it.

This package contains various plugins, mostly for use with
popular streaming services like Google Music

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
%exclude %_datadir/%name/Analog-Input
%exclude %_datadir/%name/cdplugins
%exclude %_datadir/%name/rdpl2stream
%exclude %_datadir/%name/src_scripts
%_man1dir/%name.1*

%dir %attr(0770,root,_upmpd) %_cachedir/%name

%files plugins
%_datadir/%name/Analog-Input
%_datadir/%name/cdplugins
%_datadir/%name/rdpl2stream
%_datadir/%name/src_scripts

%changelog
* Mon Dec 26 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.10-alt1
- 1.2.10 released

* Mon Sep 05 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.1-alt1
- 1.1.1 released

* Tue Jan 26 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.0-alt1
- initial

Name: upmpdcli
Version: 1.4.2
Release: alt1

Summary: UPnP front-end to the Music Player Daemon
License: LGPLv2.1
Group: Sound
Url: http://www.lesbonscomptes.com/upmpdcli

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libmpdclient-devel libupnpp-devel >= 0.14.1
BuildRequires: libmicrohttpd-devel jsoncpp-devel rpm-build-python3

%package plugins
Summary: %name plugins
Group: Sound
Requires: %name = %version-%release
BuildArch: noarch
AutoReq: yes, nopython

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

# self-contained:
%add_python3_req_skip StreamDecoder
%add_python3_req_skip cmdtalkplugin
%add_python3_req_skip conftree routing session
%add_python3_req_skip tidalapi tidalapi.models
%add_python3_req_skip upmplgutils
%add_python3_req_skip uprclindex uprclinit uprclsearch uprclutils

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
%exclude %_datadir/%name/radio_scripts
%exclude %_datadir/%name/rdpl2stream
%exclude %_datadir/%name/src_scripts
%_man1dir/%name.1*

%dir %attr(0770,root,_upmpd) %_cachedir/%name

%files plugins
%_datadir/%name/Analog-Input
%_datadir/%name/cdplugins
%_datadir/%name/radio_scripts
%_datadir/%name/rdpl2stream
%_datadir/%name/src_scripts

%changelog
* Tue Dec 24 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.2-alt1
- 1.4.2 released

* Sat Mar 23 2019 Michael Shigorin <mike@altlinux.org> 1.3.3-alt2
- introduced python3 knob disabling python2 plugins (on by default)

* Thu Sep 20 2018 Alexey Shabalin <shaba@altlinux.org> 1.3.3-alt1
- 1.3.3 released

* Mon Dec 26 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.10-alt1
- 1.2.10 released

* Mon Sep 05 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.1-alt1
- 1.1.1 released

* Tue Jan 26 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.0-alt1
- initial

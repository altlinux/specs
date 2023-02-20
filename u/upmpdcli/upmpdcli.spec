Name: upmpdcli
Version: 1.7.2
Release: alt1

Summary: UPnP front-end to the Music Player Daemon
License: LGPLv2.1
Group: Sound
Url: http://www.lesbonscomptes.com/upmpdcli

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libmpdclient-devel libupnpp-devel >= 0.21.0
BuildRequires: libmicrohttpd-devel jsoncpp-devel rpm-build-python3

%package plugins
Summary: %name plugins
Group: Sound
Requires: %name = %version-%release
BuildArch: noarch

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

%set_python3_req_method strict

# self-contained:
%add_python3_req_skip StreamDecoder
%add_python3_req_skip cmdtalkplugin
%add_python3_req_skip conftree routing session
%add_python3_req_skip deezersession
%add_python3_req_skip tidalapi tidalapi.models
%add_python3_req_skip upmplgutils
%add_python3_req_skip upmplgmodels
%add_python3_req_skip minimconfig uprclindex uprclinit uprclsearch uprclutils
%add_python3_req_skip upradioconf
%add_python3_req_skip xbmcplug
# conditional(py2):
%add_python3_req_skip ConfigParser
%add_python3_req_skip Cookie
%add_python3_req_skip StringIO
%add_python3_req_skip UserDict
%add_python3_req_skip cPickle
%add_python3_req_skip httplib
%add_python3_req_skip thread
%add_python3_req_skip urlparse
# runtime alternatives:
%add_python3_req_skip aiohttp.wsgi
%add_python3_req_skip diesel.protocols.wsgi
%add_python3_req_skip django.utils.simplejson
%add_python3_req_skip fapws
%add_python3_req_skip fapws._evwsgi
%add_python3_req_skip google.appengine.ext.webapp
%add_python3_req_skip rocket
%add_python3_req_skip uvloop

%files
%config(noreplace) %attr(0640,root,_upmpd) %_sysconfdir/%name.conf
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
* Mon Feb 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.2-alt1
- 1.7.2 released

* Fri Dec 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.2-alt1
- 1.6.2 released

* Mon Nov 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.1-alt1
- 1.6.1 released

* Tue Sep 13 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.20-alt1
- 1.5.20 released

* Fri Jul 01 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.19-alt1
- 1.5.19 released

* Mon Jun 06 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.17-alt1
- 1.5.17 released

* Tue Apr 26 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.16-alt1
- 1.5.16 released

* Tue Nov 23 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.13-alt1
- 1.5.13 released

* Wed Sep 22 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.11-alt1
- 1.5.11 released

* Tue May 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.14-alt2
- fix build with recent changes in rpm-build-python*

* Mon Jan 25 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.14-alt1
- 1.4.14 released

* Sun Jul 26 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.12-alt1
- 1.4.12 released

* Wed Jan 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.5-alt1
- 1.4.5 released

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

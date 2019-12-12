Name: tvheadend
Version: 4.2.8
Release: alt2

Summary: Tvheadend TV streaming server
License: GPLv3
Group: System/Servers
Url: https://tvheadend.org/

Requires(post): pwgen

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++ libdbus-devel
BuildRequires: libssl-devel libsystemd-devel liburiparser-devel zlib-devel
BuildRequires: libavfilter-devel libavresample-devel libswresample-devel
BuildRequires: libswscale-devel libavformat-devel libavcodec-devel libavutil-devel
BuildRequires: python2.7(encodings)

%description
Tvheadend is a combined DVB receiver, Digital Video Recorder and
Live TV streaming server for Linux, configured and administered
through a modern web interface.

%prep
%setup

%build
export TVHEADEND_FILE_CACHE=${PWD}/.gear
PYTHON=%__python \
sh configure --bindir=%_sbindir --libdir=%_libdir \
	     --mandir=%_mandir --datadir=%_datadir \
	     --enable-libav --disable-ffmpeg_static
make

%install
%make_install prefix=%_prefix DESTDIR=%buildroot install
install -pm0755 -D tvheadend.init %buildroot%_initdir/tvheadend
install -pm0644 -D tvheadend.sysconfig %buildroot%_sysconfdir/sysconfig/tvheadend
install -pm0644 -D tvheadend.service %buildroot%_unitdir/tvheadend.service

mkdir -p %buildroot%_sysconfdir/tvheadend %buildroot%_localstatedir/tvheadend
touch %buildroot%_sysconfdir/tvheadend/superuser

%pre
%_sbindir/groupadd -r -f _hts &> /dev/null
%_sbindir/useradd -r -g _hts -G radio,video -d %_localstatedir/tvheadend \
	-s /dev/null -c 'Tvheadend pseudouser' -n _hts &> /dev/null ||:

%post
f=%_sysconfdir/tvheadend/superuser
[ -s $f ] || printf '{ "username": "tvheadend", "password": "%%s" }' $(pwgen 12 1) > $f
%post_service tvheadend

%preun
%preun_service tvheadend

%files
%doc README.md QUICKSTART

%_initdir/tvheadend
%_sysconfdir/sysconfig/tvheadend
%_unitdir/tvheadend.service

%dir %attr(0770,root,_hts) %_sysconfdir/tvheadend
%config(noreplace) %attr(0600,_hts,_hts) %_sysconfdir/tvheadend/superuser

%_sbindir/tvheadend
%_datadir/tvheadend
%_man1dir/tvheadend.1*

%dir %attr(0770,root,_hts) %_localstatedir/tvheadend

%changelog
* Thu Dec 12 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2.8-alt2
- fix build with python-base splitted

* Mon Jan 14 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2.8-alt1
- 4.2.8 released

* Tue Nov 27 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2.7-alt2
- fix systemd unit file

* Thu Nov 01 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2.7-alt1
- 4.2.7 released

* Wed Sep 12 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2.6-alt1
- 4.2.6 released

* Sun Sep 15 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.4.1-alt1
- 3.4p1 released

* Tue Apr 30 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.4-alt1
- 3.4 released

* Tue Sep 11 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt1
- 3.0 released

* Mon Jun 18 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.99-alt1
- 2.99 released

* Tue Nov 30 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.12-alt1
- 2.12 released

* Thu Nov 11 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.11-alt3
- updated to svn rev.5615

* Fri Sep 10 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.11-alt2
- updated to svn rev.5342

* Sun May 30 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.11-alt1
- 2.11 released

* Sat Dec 26 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7-alt1
- 2.7 released

* Fri Dec 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6-alt1
- built for ALTLinux

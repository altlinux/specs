# vim: set ft=spec: -*- rpm-spec -*-

Name: mediatomb
Version: 0.12.1
Release: alt6

Summary: UPnP AV Mediaserver for Linux
Group: System/Servers
License: GPLv2
Url: http://mediatomb.cc/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Source1: mediatomb.init
Source2: mediatomb.sysconfig
Source3: mediatomb.service

BuildRequires: gcc-c++ id3lib-devel libavformat-devel libcurl-devel libexif-devel libexpat-devel libffmpegthumbnailer-devel
BuildRequires: libjs-devel libmagic-devel libmpeg4ip-devel libMySQL-devel libsqlite3-devel libtag-devel

%description
MediaTomb is an open source (GPL) UPnP MediaServer with a nice web user
interface, it allows you to stream your digital media through your home
network and listen to/watch it on a variety of UPnP compatible devices.

MediaTomb implements the UPnP MediaServer V 1.0 specification that can
be found on http://www.upnp.org/.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--enable-sighup \
	--enable-mrreg-service \
	--enable-protocolinfo-extension \
	--enable-external-transcoding \
	--enable-curl \
	#
%make_build

%install
mkdir -p %buildroot{%_sysconfdir/sysconfig,%_initdir,%_localstatedir/%name}
%make_install DESTDIR=%buildroot install

install -p -m755 %SOURCE1 %buildroot%_initdir/mediatomb
install -p -m644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/mediatomb
install -pD -m0644 %SOURCE3 %buildroot%systemd_unitdir/mediatomb.service

%pre
%_sbindir/groupadd -r -f _mediatomb >/dev/null 2>&1 ||:
%_sbindir/useradd -r -n -g _mediatomb -d %_localstatedir/%name -s /dev/null -c 'MediaTomb UPnP(TM) A/V Media Server' _mediatomb >/dev/null 2>&1 ||:

%post
%post_service mediatomb

%preun
%preun_service mediatomb

%files
%doc README AUTHORS ChangeLog COPYING
%doc doc/scripting.txt doc/scripting_utf8.txt
%config %_initdir/mediatomb
%config(noreplace) %_sysconfdir/sysconfig/mediatomb
%systemd_unitdir/mediatomb.service
%_bindir/mediatomb
%_datadir/%name
%_man1dir/*
%attr(3770,root,_mediatomb) %dir %_localstatedir/%name

%changelog
* Thu May 31 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.1-alt6
- fixed FTBFS with gcc >= 4.6

* Mon May 28 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.1-alt5
- systemd service file added, actually (closes: #27370)

* Sat May 05 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.1-alt4
- systemd service file added (closes: #25439)

* Thu Sep 08 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.1-alt2
- adapted for libav >= 0.7

* Thu Nov 04 2010 Packager: Gennady Kushnir <baywind@altlinux.org> 0.12.1-alt1
- updated to version 0.12.1

* Thu Nov 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.11.0-alt5
- rebuild with libffmpegthumbnailer.so.4

* Sun Jan 24 2010 Alexey I. Froloff <raorn@altlinux.org> 0.11.0-alt4
- Updated to SVN revision 2056
- Enabled curl (YuoTube) and ffmpegthumbnailer support

* Tue Jul 07 2009 Alexey I. Froloff <raorn@altlinux.org> 0.11.0-alt3
- Fixed build with recent gcc

* Tue Dec 30 2008 Sir Raorn <raorn@altlinux.ru> 0.11.0-alt2
- Fixed typo in syslog support code

* Mon Jul 14 2008 Sir Raorn <raorn@altlinux.ru> 0.11.0-alt1
- Built for Sisyphus


%define _user _opentracker
%define _group _opentracker
%define _home /dev/null

%define cvsrev 30082010

Name: opentracker
Version: 1.6
Release: alt2

Summary: An open and free bittorrent tracker
License: Beerware
Group: System/Servers

# git cvsimport -v -o upstream -i -k -d :pserver:anoncvs@cvs.erdgeist.org:/home/cvsroot opentracker
Url: http://erdgeist.org/arts/software/opentracker

Source: %name-%version.tar

BuildRequires: libowfat-devel zlib-devel

%description
opentracker is a open and free bittorrent tracker project. It aims for minimal
resource usage and is intended to run at your wlan router. Currently it is
deployed as an open and free tracker instance.

Utilizing the highly scalable server framework from libowfat, opentracker can
easily serve multiple thousands of requests on a standard plastic WLAN-router,
limited only by your kernels capabilities ;)

One important design decision of opentracker was to not store any data
persistently. This reduces wear&tear on hard disks and eliminates problems
with corrupt databases.

opentracker allows several instances running in a cluster. Those clusters can
be synced with a simple protocol extension proposed here and implemented in
opentracker already

%prep
%setup

%build
export FEATURES="-DWANT_SYNC_LIVE -DWANT_SYNC_SCRAPE -DWANT_COMPRESSION_GZIP -DWANT_RESTRICT_STATS -DWANT_IP_FROM_QUERY_STRING"
%make_build

%install
install -dm1750 %buildroot%_localstatedir/%name

install -pDm0755 %name %buildroot%_bindir/%name

install -pDm0755 %name.init %buildroot%_initdir/%name
install -pDm0755 %name.sysconfig %buildroot%_sysconfdir/sysconfig/%name

install -D -m 644 %name.conf.sample %buildroot%_sysconfdir/%name/%name.conf
touch %buildroot%_sysconfdir/%name/whitelist.conf


%pre
/usr/sbin/groupadd -r -f %_group ||:
/usr/sbin/useradd -g %_group -c 'The opentracker Daemon' \
	-d %_home -s /dev/null -r %_user >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%_initdir/%name
%config(noreplace) %_sysconfdir/%name/opentracker.conf
%config(noreplace) %_sysconfdir/%name/whitelist.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %attr(1750,root,%_group) %_localstatedir/%name
%doc README* nginx.retracker.conf

%changelog
* Mon Aug 30 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.6-alt2
- Update to cvs snapshot from 30.08.2010.
- Add sample config for nginx (for retracker mode).
- Don't build with -DWANT_ACCESSLIST_WHITE.
- Add initscript.
- Fix configs packaging.

* Mon Nov 16 2009 Ilya Shpigor <elly@altlinux.org> 1.6-alt1
- initial build for ALT Linux Sisyphus

* Tue Sep 04 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.0-alt1.cvs.18082007
- Initial build for Sisyphus.

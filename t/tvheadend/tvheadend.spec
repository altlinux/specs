Name: tvheadend
Version: 2.99
Release: alt1

Summary: Tvheadend TV streaming server
License: GPLv3
Group: System/Servers
Url: http://www.lonelycoder.com/hts/

Requires: pwgen

Source: %name-%version-%release.tar
BuildRequires: libavahi-devel libssl-devel

%description
Tvheadend is a combined DVB receiver, Digital Video Recorder and
Live TV streaming server for Linux, configured and administered
through a modern web interface.

%prep
%setup

%build
sh configure --bindir=%_sbindir --mandir=%_man1dir --datadir=%_datadir/%name --release
make

%install
%make_install prefix=%_prefix DESTDIR=%buildroot install
install -pm0755 -D tvheadend.init %buildroot%_initdir/tvheadend
install -pm0644 -D tvheadend.sysconfig %buildroot%_sysconfdir/sysconfig/tvheadend

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
%doc README QUICKSTART
%doc docs/header.html docs/docresources docs/html

%_initdir/tvheadend
%_sysconfdir/sysconfig/tvheadend

%dir %attr(0770,root,_hts) %_sysconfdir/tvheadend
%config(noreplace) %attr(0600,_hts,_hts) %_sysconfdir/tvheadend/superuser

%_sbindir/tvheadend
%_datadir/tvheadend
%_man1dir/tvheadend.1*

%dir %attr(0770,root,_hts) %_localstatedir/tvheadend

%changelog
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

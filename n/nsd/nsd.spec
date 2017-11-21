Name: nsd
Version: 4.1.5
Release: alt3

Summary: Name Server Daemon
License: BSD
Group: System/Servers
Url: http://www.nlnetlabs.nl/projects/nsd/

Source0: %name-%version.tar
Source1: %name.conf
Source2: %name.service
Source3: example.com.zone
Source4: 0.0.10.zone

BuildRequires: flex bison libevent-devel libssl-devel

%description
NSD is an authoritative only, high performance, simple and open source name server

%prep
%setup

%build
%autoreconf
%configure \
  --with-user=_nsd \
  --enable-bind8-stats \
  --enable-zone-stats \
  --enable-ratelimit \
  --with-pidfile=%_runtimedir/%name.pid \
  --with-dbfile=%_localstatedir/%name/%name.db \
  --localstatedir=%_var
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/%systemd_unitdir
mkdir -p %buildroot/%_localstatedir/%name
mkdir -p %buildroot/%_initdir
mv %buildroot/%_sysconfdir/%name/%name.conf.sample .
cp %SOURCE1 %buildroot/%_sysconfdir/%name
cp %SOURCE2 %buildroot/%systemd_unitdir
cp %SOURCE3 %buildroot/%_sysconfdir/%name
cp %SOURCE4 %buildroot/%_sysconfdir/%name
cp contrib/%name.init %buildroot/%_initdir/%name

%pre
/usr/sbin/groupadd -r -f _nsd
/usr/sbin/useradd -r -g _nsd -d /var/empty -s /sbin/nologin -n -c "Name Server Daemon" _nsd >/dev/null 2>&1 ||:

%preun
%preun_service nsd

%post
%post_service nsd

%files
%_sbindir/*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_sysconfdir/%name/*.zone
%systemd_unitdir/%name.service
%attr(0755,root,root) %_initdir/%name
%attr(0755,_nsd,_nsd) %dir %_localstatedir/%name
%_man5dir/*
%_man8dir/*
%doc doc contrib %name.conf.sample

%changelog
* Tue Nov 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.5-alt3
- Fixed localstatedir.

* Tue Sep 29 2015 Eugene Prokopiev <enp@altlinux.ru> 4.1.5-alt2
- add old changelog rows to respect srpm inheritance check

* Tue Sep 29 2015 Eugene Prokopiev <enp@altlinux.ru> 4.1.5-alt1
- new version

* Fri Sep 04 2015 Eugene Prokopiev <enp@altlinux.ru> 4.1.3-alt1
- initial build from svn

* Tue Feb 28 2012 Victor Forsiuk <force@altlinux.org> 3.2.10-alt1
- 3.2.10

* Sat Nov 26 2011 Victor Forsiuk <force@altlinux.org> 3.2.9-alt1
- 3.2.9

* Sat Mar 26 2011 Victor Forsiuk <force@altlinux.org> 3.2.8-alt1
- 3.2.8

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 3.2.7-alt1
- 3.2.7

* Tue Dec 07 2010 Victor Forsiuk <force@altlinux.org> 3.2.6-alt2
- Rebuilt due to libcrypto.so.7 -> libcrypto.so.10 soname change.

* Wed Aug 04 2010 Victor Forsiuk <force@altlinux.org> 3.2.6-alt1
- 3.2.6

* Tue May 25 2010 Victor Forsiuk <force@altlinux.org> 3.2.5-alt1
- 3.2.5

* Tue Jan 26 2010 Victor Forsyuk <force@altlinux.org> 3.2.4-alt1
- 3.2.4

* Sun Nov 08 2009 Victor Forsyuk <force@altlinux.org> 3.2.3-alt1
- Initial build.

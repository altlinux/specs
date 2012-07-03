# Spec file for Policyd: an anti-spam plugin for Postfix

Name: policyd
Version: 1.82
Release: alt3.1

Summary: Postfix Policyd Daemon

License: %gpl2plus 
Group: System/Servers
URL: http://policyd.sourceforge.net/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: http://policyd.sourceforge.net/%name-%version.tar.bz2
Source1: %name.init
Source2: %name.cron
Source3: %name.conf
Source4: %name.chroot.all
Source5: %name.chroot.conf
Source6: %name.chroot.lib
Source7: README.ALT
Source8: README.ALT.UTF-8
Patch0:  %name-1.80-alt-uid_gid.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sat Aug 11 2007
BuildRequires: libMySQL-devel zlib-devel

Requires: postfix >= 2.1


%description
Policyd is a policy server for Postfix (written in C) that enables
advanced Greylisting with many other anti-spam facilities. See the
docs and policyd.conf for features that are ever being augmented. 
It needs MySQL v3 or greater and is currently only certified for
MySQL v4.

%define policyd_user  _policyd
%define policyd_group _policyd
%define chrootdir     %_localstatedir/%name

%prep
%setup -q
%patch0
install -m644 -- %SOURCE7 README.ALT
install -m644 -- %SOURCE8 README.ALT.UTF-8

# Need it there because of using COPYING in makefile
mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/LICENSE) LICENSE

%build
%make build

%install
mkdir -p -- $RPM_BUILD_ROOT%_sbindir
mkdir -p -- $RPM_BUILD_ROOT%_sysconfdir/cron.d
mkdir -p -- $RPM_BUILD_ROOT%_sysconfdir/%name
mkdir -p -- $RPM_BUILD_ROOT%_initdir

install -m755 -- %SOURCE1 $RPM_BUILD_ROOT%_initdir/%name
install -m644 -- %SOURCE2 $RPM_BUILD_ROOT/%_sysconfdir/cron.d/%name

install -m755 -- %name   $RPM_BUILD_ROOT%_sbindir/%name
install -m755 -- cleanup $RPM_BUILD_ROOT%_sbindir/%name-cleanup
install -m755 -- stats   $RPM_BUILD_ROOT%_sbindir/%name-stats
install -m600 -- %SOURCE3 $RPM_BUILD_ROOT%_sysconfdir/%name/%name.conf.sample
%__subst 's/@policyd_user@/%policyd_user/g' $RPM_BUILD_ROOT%_sysconfdir/%name/%name.conf.sample
%__subst 's/@policyd_group@/%policyd_group/g' $RPM_BUILD_ROOT%_sysconfdir/%name/%name.conf.sample

install -m 0750 -d -- %buildroot%chrootdir
install -m 0755 -d -- %buildroot%chrootdir/etc
install -m 0755 -d -- %buildroot%chrootdir/%_lib
install -p -m 0750 -D -- %SOURCE4 %buildroot%_sysconfdir/chroot.d/%name.all
install -p -m 0750 -D -- %SOURCE5 %buildroot%_sysconfdir/chroot.d/%name.conf
install -p -m 0750 -D -- %SOURCE6 %buildroot%_sysconfdir/chroot.d/%name.lib


%pre
# Add the "_policyd" user
%_sbindir/groupadd -r -f %policyd_group 2>/dev/null ||:
%_sbindir/useradd  -r -g %policyd_group -c 'policyd daemon' \
        -s /dev/null -d /dev/null %policyd_user 2>/dev/null ||:

%post
%_sysconfdir/chroot.d/%name.all
%post_service %name

%preun
%preun_service %name


%files
%doc ChangeLog DATABASE.mysql README TODO doc*
%doc README.ALT README.ALT.UTF-8
%doc --no-dereference LICENSE

%config(noreplace) %_sysconfdir/%name/%name.conf.sample
%config %_initdir/%name
%config %_sysconfdir/cron.d/%name
%config %_sysconfdir/chroot.d/%name.*

%_sbindir/%{name}*

%attr(0750,root,%policyd_group) %dir %chrootdir
				%dir %chrootdir/etc
				%dir %chrootdir/%_lib

%changelog
* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1.82-alt3.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Fri May 30 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.82-alt3
- Fix cron script (Closes: #15845)
- Add LSB header to the init script

* Wed Aug 22 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.82-alt2
- Fix chroot config files  

* Mon Aug 20 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.82-alt1
- New version 1.82
  * Fixed a memory leak when re-connecting to mysql
  * Fixed rare case in which mysql failure counter would get stuck

* Mon Aug 13 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.80-alt1
- Initial build for ALT Linux

* Sun May 20 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.80-alt0
- Initial build


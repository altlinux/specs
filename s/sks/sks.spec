Summary: Synchronizing Key Server
Name: sks
Version: 1.1.10
Release: alt2.qa1.1
License: GPL
Group: System/Servers
Source: http://minskyprimus.net/sks/releases/%name-%version.tar.gz
Source1: %{name}conf
Source2: %name.init
Source3: %name.log
Url: http://www.nongnu.org/%name/
Packager: Boris Savelev <boris@altlinux.org>

# Automatically added by buildreq on Tue Aug 26 2008
BuildRequires: camlp4 ocaml-cryptokit libdb4-devel
BuildRequires: perl-podlators

%description
SKS (Synchronizing Key Server) is a full-featured replacement
for the standard PKS OpenPGP Key Server. It matches all of PKS
features and interfaces, and at the same time provides a highly
efficient, gossip-based replication algorithm that ensures that
the replication is complete.

%prep
%setup -q

%build
%make dep
%make all

%install
PREFIX=%_usr \
MANDIR=%_mandir \
%makeinstall_std

mkdir -p %buildroot%_sysconfdir/%name
install %SOURCE1 %buildroot%_sysconfdir/%name
touch %buildroot%_sysconfdir/%name/membership
touch %buildroot%_sysconfdir/%name/mailsync

mkdir -p %buildroot%_initdir
install %SOURCE2 %buildroot%_initdir/%name

mkdir -p %buildroot%_sysconfdir/logrotate.d
install %SOURCE3 %buildroot%_sysconfdir/logrotate.d/%name

mkdir -p %buildroot%_var/lib/%name/{DB,PTree,dump,www}
mkdir -p %buildroot%_var/run/%name
mkdir -p %buildroot%_var/log/%name
mkdir -p %buildroot%_var/spool/%name/{messages,failed_messages}

%pre
/usr/sbin/groupadd -f -r _%{name} >/dev/null 2>&1 || :
/usr/sbin/useradd -r -g _%{name} -d /var/lib/%name -s /dev/null \
    -c "SKS user" -M -n _%{name} >/dev/null 2>&1 || :

%files
%doc BUGS CHANGELOG COPYING FILES README TODO VERSION
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%{name}conf
%config(noreplace) %_sysconfdir/%name/membership
%config(noreplace) %_sysconfdir/%name/mailsync
%config(noreplace) %_sysconfdir/logrotate.d/%name
%_initdir/%name
%_bindir/*
%_sbindir/*
%dir %_datadir/%name
%_datadir/%name/*
%attr(2770,root,_%{name}) %dir %_var/lib/%name
%attr(2770,root,_%{name}) %dir %_var/lib/%name/DB
%attr(2770,root,_%{name}) %dir %_var/lib/%name/PTree
%attr(2770,root,_%{name}) %dir %_var/lib/%name/dump
%attr(2770,root,_%{name}) %dir %_var/lib/%name/www
%attr(2770,root,_%{name}) %dir %_var/run/%name
%attr(2770,root,_%{name}) %dir %_var/log/%name
%attr(2770,root,_%{name}) %dir %_var/spool/%name
%attr(2770,root,_%{name}) %dir %_var/spool/%name/messages
%attr(2770,root,_%{name}) %dir %_var/spool/%name/failed_messages
%_man8dir/*

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt2.qa1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.10-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for sks
  * postclean-05-filetriggers for spec file

* Fri Sep 05 2008 Boris Savelev <boris@altlinux.org> 1.1.10-alt2
- rebuild with new ocaml-cryptokit

* Tue Aug 26 2008 Boris Savelev <boris@altlinux.org> 1.1.10-alt1
- initial build for Sisyphus


Summary: Synchronizing Key Server
Name: sks
Epoch: 1
Version: 1.1.6
Release: alt1
License: GPL
Group: System/Servers
Url: https://bitbucket.org/skskeyserver/sks-keyserver/wiki/Home

Source: %name-%version.tar
Source1: %{name}conf
Source2: %{name}-db.init
Source3: %{name}-recon.init
Source4: %name.log
Source5: sks-db.service
Source6: sks-recon.service
Source7: cryptokit-1.7-sks-uint32.patch

Patch1: %name-%version-fedora-makefile.patch
Patch2: %name-%version-alt-libdb.patch
Patch3: %name-%version-alt-build.patch

BuildRequires: ocaml-camlp4-devel ocaml-cryptokit-devel libdb6-devel zlib-devel
BuildRequires: perl-podlators
BuildRequires: chrpath

%description
SKS (Synchronizing Key Server) is a full-featured replacement
for the standard PKS OpenPGP Key Server. It matches all of PKS
features and interfaces, and at the same time provides a highly
efficient, gossip-based replication algorithm that ensures that
the replication is complete.

%prep
%setup
%patch1 -p1
%patch2 -p2
%patch3 -p2
cp %SOURCE7 .

%build
mv Makefile.local.unused Makefile.local
%make dep
%make all

%install
%makeinstall_std \
PREFIX="%{buildroot}%{_prefix}" \
MANDIR="%{buildroot}%{_mandir}"

chrpath -d %buildroot%_bindir/sks

mkdir -p %buildroot%_sysconfdir/%name
install %SOURCE1 %buildroot%_sysconfdir/%name
touch %buildroot%_sysconfdir/%name/membership
touch %buildroot%_sysconfdir/%name/mailsync

mkdir -p %buildroot%_initdir
install %SOURCE2 %buildroot%_initdir/%{name}-db
install %SOURCE3 %buildroot%_initdir/%{name}-recon

mkdir -p %buildroot%_sysconfdir/logrotate.d
install %SOURCE4 %buildroot%_sysconfdir/logrotate.d/%name

mkdir -p %buildroot%_var/lib/%name/{KDB,PTree,dump,www}
mkdir -p %buildroot%_var/run/%name
mkdir -p %buildroot%_var/log/%name
mkdir -p %buildroot%_var/spool/%name/{messages,failed_messages}

mkdir -p %buildroot%_unitdir
install -m 0644 %SOURCE5 %buildroot%_unitdir/%{name}-db.service
install -m 0644 %SOURCE6 %buildroot%_unitdir/%{name}-recon.service

%pre
/usr/sbin/groupadd -f -r _%{name} >/dev/null 2>&1 || :
/usr/sbin/useradd -r -g _%{name} -d /var/lib/%name -s /dev/null \
    -c "SKS user" -M -n _%{name} >/dev/null 2>&1 || :

%files
%doc BUGS CHANGELOG LICENSE FILES README.md TODO VERSION
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%{name}conf
%config(noreplace) %_sysconfdir/%name/membership
%config(noreplace) %_sysconfdir/%name/mailsync
%config(noreplace) %_sysconfdir/logrotate.d/%name
%_initdir/%{name}-db
%_initdir/%{name}-recon
%_unitdir/%{name}-db.service
%_unitdir/%{name}-recon.service
%_bindir/*
%attr(2770,root,_%{name}) %dir %_var/lib/%name
%attr(2770,root,_%{name}) %dir %_var/lib/%name/KDB
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
* Mon Oct 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.1.6-alt1
- Updated to upstream release version 1.1.6.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.10-alt2.qa2
- NMU: rebuilt for debuginfo.

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


Name: vzdump
Version: 1.0
Release: alt2.1

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Summary: OpenVZ backup scripts
Source: %name-%version.tar.gz
License: GPL
Group: Archiving/Backup

BuildArch: noarch
BuildPreReq: perl
Requires: vzctl rsync xdelta
BuildRequires: perl-podlators

%description
This package contains the vzdump script to backup and restore openvz images.

%prep
%setup
%__subst "s|/vz/root|/var/lib/vz/root|g" vzdump
%__subst "s|/vz/private|/var/lib/vz/private|g" vzdump
%__subst "s|/vz/dump|/var/lib/vz/dump|g" vzdump

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%attr(755,root,root) %_bindir/vzdump
%attr(644,root,root) %_mandir/man1/vzdump.1.*
%doc ChangeLog copyright

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Jan 13 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt2
- Add Requires: rsync xdelta (#13220)

* Tue Aug 14 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- New versoin

* Mon Jun 18 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4-alt1
- Update for Sisyphus

* Tue Mar 22 2007 Dietmar Maurer <dietmar@proxmox.com> 0.3-1
- added Vendor and Packager tags

* Tue Mar 20 2007 Kir Kolyshkin <kir@openvz.org> 0.3-1
- created spec file

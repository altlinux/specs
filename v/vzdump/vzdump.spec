Name: vzdump
Version: 1.2.6
Release: alt2

Summary: OpenVZ backup scripts
# http://deb.debian.org/debian/pool/main/v/vzdump/vzdump_1.2.6.orig.tar.gz
Source: %name-%version.tar
License: GPL-1.0
Group: Archiving/Backup
ExclusiveArch: x86_64

BuildRequires(Pre): perl
BuildRequires: perl-podlators
BuildRequires: perl(LockFile/Simple.pm)
Requires: vzctl rsync cstream
Conflicts: pve-manager

%description
This package contains the vzdump and vzrestore scripts to backup and restore OpenVZ images.

%prep
%setup

%install
%makeinstall_std

%files
%_sbindir/vzdump
%_sbindir/vzrestore
%_man1dir/vzdump.1.*
%_man1dir/vzrestore.1.*
%perl_vendor_privlib/OVZ/
%doc ChangeLog copyright hook-script.pl

%changelog
* Thu Dec 01 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.2.6-alt2
- fix from wiki.openvz.org
- set conflict with pve-manager (ALT #44504)

* Wed Nov 17 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.2.6-alt1
- new version 1.2.6
- adoptation for ALT OpenVZ, remove qemu support

* Mon Nov 05 2018 Alexey Shabalin <shaba@altlinux.org> 1.0-alt3
- build for x86_64 only

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Jan 13 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt2
- Add Requires: rsync xdelta (#13220)

* Tue Aug 14 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- New versoin

* Mon Jun 18 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4-alt1
- Update for Sisyphus


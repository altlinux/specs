Name: smbldap-tools
Version: 0.9.10
Release: alt1

Summary: User & Group administration tools for Samba-OpenLDAP
License: GPL
Group: System/Configuration/Networking

Url: http://gna.org/projects/smbldap-tools/
Source0: http://download.gna.org/smbldap-tools/packages/%name-%version.tar.gz
Source1: http://kostyalamer.narod.ru/smbldap/smbldap.html
Patch1: smbldap-tools-0.9.2-alt-separate_users_and_groups_in_smbldap_migrate_unix_accounts.patch

Requires: perl >= 5.6, samba, perl-ldap, perl-Crypt-SmbHash, perl-Digest-SHA1, perl-Unicode-MapUTF8, perl-Encode-JP, perl(FindBin.pm), perl(Getopt/Std.pm), perl(MIME/Base64.pm), perl(Net/LDAP.pm), perl(Net/LDAP/LDIF.pm), perl(Unicode/MapUTF8.pm), perl(lib.pm), perl-base
AutoReq: yes, noperl
BuildRequires: samba perl-ldap perl-Crypt-SmbHash perl-Digest-SHA1 perl-Unicode-MapUTF8 perl-Encode-JP perl-podlators

BuildArch: noarch

%description
In settings with OpenLDAP and Samba-LDAP servers, this collection is
useful to add, modify and delete users and groups, and to change
Unix and Samba passwords. In those context they replace the system
tools to manage users, groups and passwords.

%prep
%setup
#patch1 -p1

#Fix podlator section
cat << EOF >> smbldap-config.pl

exit(0);

########################################
=head1 NAME

smbldap-config - Smbldap-config

=head1 DESCRIPTION

The smbldap-config command configure 

=cut

#'
EOF

%autoreconf
%configure

%build
%make_build

%install
%make install DESTDIR=%buildroot
mv doc/migration_scripts/smbldap-migrate-unix-accounts %buildroot%_sbindir/smbldap-migrate-unix-accounts
mv doc/migration_scripts/smbldap-migrate-unix-groups %buildroot%_sbindir/smbldap-migrate-unix-groups

#install configs
mkdir -p %buildroot%_sysconfdir/smbldap-tools
install smbldap.conf %buildroot%_sysconfdir/smbldap-tools/smbldap.conf
install smbldap_bind.conf %buildroot%_sysconfdir/smbldap-tools/smbldap_bind.conf

#install man
mkdir -p %buildroot%_man8dir
cp *.8 %buildroot%_man8dir/

%files
%_sbindir/*
%attr(0644,root,root) %perl_vendor_privlib/*
%doc CONTRIBUTORS COPYING ChangeLog FILES INFRA README INSTALL TODO
%doc doc/*.*
%dir %_sysconfdir/smbldap-tools/
%config(noreplace) %_sysconfdir/smbldap-tools/smbldap.conf
%attr(0600,root,root) %config(noreplace) %_sysconfdir/smbldap-tools/smbldap_bind.conf
%_man8dir/*

%changelog
* Sat Apr 27 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.10-alt1
- 0.9.10

* Wed Feb 16 2011 Michael Shigorin <mike@altlinux.org> 0.9.6-alt3
- added russian docs (closes: #23395)

* Mon Jan 10 2011 Michael Shigorin <mike@altlinux.org> 0.9.6-alt2
- drop patch, breaks with perl-5.12 at the very least (closes: #24888)

* Mon Jan 10 2011 Michael Shigorin <mike@altlinux.org> 0.9.6-alt1
- 0.9.6

* Tue Jun 24 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.5-alt2
- Fix #16104

* Sat Jun 21 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.5-alt1
- New virsion

* Fri Dec 07 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.4-alt1
- New virsion
- Change URL
- Remove smbldap-howto.pdf
- Remove smbldap-tools-0.9.2-fix_UTF-8_usage-alt-smbldap-usermod.patch

* Thu Aug 03 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.2-alt0
- NMU: Fix #9839, #9912, #9840, 9913
- New virsion (#9839)
- Removed ALL patches (#9840)
- Add smbldap-tools-0.9.2-alt-separate_users_and_groups_in_smbldap_migrate_unix_accounts.patch (#9913)
- Add %_sbindir/smbldap-migrate-unix-accounts and %_sbindir/smbldap-migrate-unix-groups (#9912)
- Added patch to fix UTF-8 usage on smbldap-usermod.
- Add smbldap-howto.pdf
- Update BuildRequires: added perl-Unicode-MapUTF8, perl-Encode-JP
- Update Requires: added perl-Unicode-MapUTF8, perl-Encode-JP, perl(FindBin.pm), perl(Getopt/Std.pm),
  perl(MIME/Base64.pm), perl(Net/LDAP.pm), perl(Net/LDAP/LDIF.pm), perl(Unicode/MapUTF8.pm), perl(lib.pm), perl-base

* Mon May 29 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.9.1-alt4.2
- NMU: in-place idmap fix

* Wed Dec 07 2005 Nick S. Grechukh <gns@altlinux.org> 0.9.1-alt4.1
- new version works without slappasswd, so add Require: perl-Digest-SHA1.
- patched for optional in-place idmap (as described at http://www.freesource.info/wiki/ALTLinux/Dokumentacija/samba/idmapldap)

* Mon Aug 16 2004 Nick S. Grechukh <gns@altlinux.ru> 0.8.5-alt1
- first build for sisyphus. specfile from idealx.org adopted for ALT.

* Fri Nov 28 2003 Jerome Tournier <jerome.tournier@idealx.com> 0.8.2-1
- see Changelog file for updates in scripts

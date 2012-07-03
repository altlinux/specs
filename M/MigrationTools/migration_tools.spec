Name: MigrationTools
Version: 46
Release: alt2

# Define Migration Tools number
%define OpenLDAP_ver 2.1.30

Summary: Set of scripts for migration of a nis domain to a ldap annuary
Summary(ru_RU.KOI8-R): Набор скриптов, необходимый для миграции от nis к ldap

License: BSD redistributable
Group: System/Servers
Url: http://www.padl.com/tools.html
BuildArch: noarch
Provides: perl(migrate_common.ph)

# Migration Tools source
Source0: ftp://ftp.padl.com/pub/%name-%version.tar.bz2
Source1: migration-tools.txt
Source2: migrate_automount.pl

Patch0: %name-34-instdir.patch
Patch1: %name-36-mktemp.patch
Patch2: %name-27-simple.patch
Patch3: %name-26-suffix.patch
Patch4: %name-24-schema.patch
Patch5: %name-44-i18n.patch
# I think it's applied to HEAD
#Patch6: %name-44-alt-passwd-i18n.patch
Patch7: %name-46-ads.patch

Requires: openldap-servers >= %OpenLDAP_ver

%description
The MigrationTools are a set of Perl scripts for migrating users, groups,
aliases, hosts, netgroups, networks, protocols, RPCs, and services from
existing nameservices (flat files, NIS, and NetInfo) to LDAP.
Tools to load flat files (/etc) into LDAP as per RFC 2307.

%description -l ru_RU.KOI8-R
MigrationTools это набор скриптов, написанных на Perl, для миграции пользователей, групп, алиасов, имен хостов, сетевых групп, сетей, протоколов, RPC и сервисов из существующего пространства имен (файлы, NIS и NetInfo) в LDAP.
Скрипты закгрузки файлов (/etc) написаны согласно RFC 2307.

%prep
%setup -q
%patch0 -p1 
%patch1 -p1
%patch2 -p1 
%patch3 -p1 
%patch4 -p2 
%patch5 -p2 
#%patch6 -p1 
%patch7 -p1 

install %SOURCE2 .

%install
mkdir -p $RPM_BUILD_ROOT%_sbindir

# install the migration tools
mkdir -p $RPM_BUILD_ROOT%_datadir/openldap/migration
mkdir -p $RPM_BUILD_ROOT%_datadir/openldap/migration/ads
install -p -m755 migrate_* $RPM_BUILD_ROOT%_datadir/openldap/migration/
install -p -m755 ads/migrate_* $RPM_BUILD_ROOT%_datadir/openldap/migration/ads/
##install -p -m644 README %SOURCE1 $RPM_BUILD_ROOT%_datadir/openldap/migration/
install -p -m644 %SOURCE1 TOOLS.migration
##install -d $RPM_BUILD_ROOT%_sysconfdir/openldap

%files
%dir %_datadir/openldap/migration
%dir %_datadir/openldap/migration/ads
%config %_datadir/openldap/migration/*.ph
%config %_datadir/openldap/migration/ads/*.ph
%_datadir/openldap/migration/*.pl
%_datadir/openldap/migration/*.sh
%_datadir/openldap/migration/ads/*.pl
%_datadir/openldap/migration/ads/*.sh
%doc README TOOLS.migration

%changelog
* Fri Jan 14 2005 Serge A. Volkov <vserge at altlinux.ru> 46-alt2
- Fix Sisyphus unmet: /usr/bin/sh
- Spec cleanup 
- Add
  + %name-46-ads.patch

* Fri Dec 17 2004 Serge A. Volkov <vserge at altlinux.ru> 46-alt1
- Update to new version 46
- Remove Patch6

* Tue Dec 24 2002 Serge A. Volkov <vserge@altlinux.ru> 44-alt2
- Specfile cleanup -- correct install error.
- Fix Bug with name of script directory see bugs.altlinux.ru
- Add copy ads directory to packages.

* Tue Aug 6 2002 Serge A. Volkov <vserge@altlinux.ru> 44-alt1
- Update to new version
- Update %name-24-schema.patch becouse migrate_services.pl rewriten.
- Update %name-44-i18n.patch and %name-44-passwd-i18n.patch

* Sat Jun 1 2002 Serge A. Volkov <vserge@altlinux.ru> 40-alt1
- Update to new version
- Add Russian ru_RU.KOI8-R translate of decription.

* Mon Sep 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 39-alt2
- Specfile cleanup.

* Wed Sep 5 2001 Volkov Serge <vserge@hotbox.ru>
- I devied this package from OpenLDAP package version OpenLDAP-2.0.12-alt1

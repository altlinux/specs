%define _unpackaged_files_terminate_build 1
%define _runtimedir /run
%def_with check

%define _pseudouser_user     _opendnssec
%define _pseudouser_group    _opendnssec
%define _pseudouser_home     %_sharedstatedir/opendnssec

Name: opendnssec
Version: 2.1.12
Release: alt1

Summary: DNSSEC key and zone management software
License: BSD-2-Clause
Group: System/Servers

Url: http://www.opendnssec.org/
Source: %name-%version.tar
Source1: ods-enforcerd.service
Source2: ods-signerd.service
Source3: ods.sysconfig
Source4: conf.xml
Source5: tmpfiles-opendnssec.conf
Source6: ods-enforcerd.init
Source7: ods-signerd.init
Source8: alt_migrate_1.4_to_2.py
Source9: pylintrc
Patch0: %name-%version-alt.patch

BuildRequires: rpm-build-python3
BuildRequires: xml-utils xsltproc
BuildRequires: libxml2-devel libsqlite3-devel libldns-devel
BuildRequires: doxygen sqlite3
BuildRequires: java
BuildRequires: autoconf-archive

# softhsm 2.6.1-alt1 provides /usr/lib64/softhsm/libsofthsm2.so
Requires: softhsm >= 2.6.1-alt1

%if_with check
BuildRequires: CUnit-devel
BuildRequires: softhsm >= 2.6.1-alt1

# alt migration script
BuildRequires: python3(pylint)
BuildRequires: python3(black)
BuildRequires: python3(sqlite3)
BuildRequires: python3(lxml)
%endif

%description
OpenDNSSEC was created as an open-source turn-key solution for DNSSEC.
It secures zone data just before it is published in an authoritative
name server. It requires a PKCS#11 crypto module library, such as
SoftHSM.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure \
        --with-ldns=%_libdir \
        #

%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_sharedstatedir/opendnssec/tmp

touch %buildroot%_sharedstatedir/opendnssec/{kasp.db,kasp.db.our_lock}
touch %buildroot%_sharedstatedir/opendnssec/kasp.db.backup
install -Dm0644 %SOURCE1 %buildroot%_unitdir/ods-enforcerd.service
install -Dm0644 %SOURCE2 %buildroot%_unitdir/ods-signerd.service
install -Dm0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/ods
install -Dm0644 %SOURCE4 %buildroot%_sysconfdir/opendnssec/conf.xml
install -Dm0644 %SOURCE5 %buildroot%_tmpfilesdir/opendnssec.conf
install -Dm0755 %SOURCE6 %buildroot%_initdir/ods-enforcerd
install -Dm0755 %SOURCE7 %buildroot%_initdir/ods-signerd

# alt enforcer migration tools and DB schema
mkdir -p %buildroot%_datadir/opendnssec/enforcer
mkdir %buildroot%_datadir/opendnssec/enforcer/schema
cp ./enforcer/src/db/schema.{mysql,sqlite} %buildroot%_datadir/opendnssec/enforcer/schema/
cp -a ./enforcer/utils/ %buildroot%_datadir/opendnssec/enforcer/
cp %SOURCE8 %buildroot%_datadir/opendnssec/enforcer/

mkdir -p %buildroot%_localstatedir/opendnssec/backup

%check
%make check

# lint checks for alt migration script
python3 -m pylint --rcfile=%SOURCE9 %SOURCE8
python3 -m black -l 80 -v --check --diff %SOURCE8

%pre
groupadd -r -f %_pseudouser_group ||:
groupadd -r -f ods ||:
useradd -g %_pseudouser_group -G ods -c 'OpenDNSSEC daemon account' \
        -d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%post
%post_service ods-enforcerd 2>/dev/null
%post_service ods-signerd 2>/dev/null

# upgrade
if [ "$1" -gt 1 ]; then
    # migration, does nothing if already migrated
    %_datadir/opendnssec/enforcer/alt_migrate_1.4_to_2.py ||:

    # in case we update any xml conf file
    echo "ODS: updating configuration, this may take a while, please wait"
    ods-enforcer update all >/dev/null 2>&1 ||:
fi

%preun
%preun_service ods-signerd
%preun_service ods-enforcerd
%files
%dir %attr(0770,root,%_pseudouser_group) %_sysconfdir/opendnssec
%config(noreplace) %attr(0660,root,%_pseudouser_group) %_sysconfdir/opendnssec/*.xml
%config(noreplace) %attr(0644,root,root) %_sysconfdir/sysconfig/ods
%exclude %_sysconfdir/opendnssec/*.sample
%config %_tmpfilesdir/opendnssec.conf
%config %_unitdir/ods-enforcerd.service
%config %_unitdir/ods-signerd.service
%_initdir/ods-enforcerd
%_initdir/ods-signerd
%_bindir/ods-hsmspeed
%_bindir/ods-hsmutil
%_bindir/ods-kasp2html
%_bindir/ods-kaspcheck
%_sbindir/ods-control
%_sbindir/ods-enforcerd
%_sbindir/ods-signer
%_sbindir/ods-signerd
%_sbindir/ods-enforcer
%_sbindir/ods-enforcer-db-setup
%_sbindir/ods-migrate
%dir %attr(0770,root,%_pseudouser_group) %_sharedstatedir/opendnssec
%dir %attr(0770,root,%_pseudouser_group) %_sharedstatedir/opendnssec/signconf
%dir %attr(0770,root,%_pseudouser_group) %_sharedstatedir/opendnssec/signed
%dir %attr(0770,root,%_pseudouser_group) %_sharedstatedir/opendnssec/unsigned
%dir %attr(0770,root,%_pseudouser_group) %_sharedstatedir/opendnssec/enforcer
%dir %attr(0770,root,%_pseudouser_group) %_sharedstatedir/opendnssec/tmp
%dir %attr(0770,root,%_pseudouser_group) %_sharedstatedir/opendnssec/backup
%dir %attr(0770,root,%_pseudouser_group) %_runtimedir/opendnssec
%ghost %config(noreplace) %_sharedstatedir/opendnssec/kasp.db
%ghost %config(noreplace) %_sharedstatedir/opendnssec/kasp.db.backup
%ghost %_sharedstatedir/opendnssec/kasp.db.our_lock
%_datadir/opendnssec/
%_man1dir/*
%_man5dir/*
%_man7dir/*
%_man8dir/*

%changelog
* Wed Nov 16 2022 Stanislav Levin <slev@altlinux.org> 2.1.12-alt1
- 2.1.10 -> 2.1.12.

* Thu Feb 10 2022 Stanislav Levin <slev@altlinux.org> 2.1.10-alt3
- Fixed FTBFS (Pylint 2.12.2).

* Wed Sep 22 2021 Stanislav Levin <slev@altlinux.org> 2.1.10-alt2
- Fixed migration of default installations.

* Wed Sep 15 2021 Stanislav Levin <slev@altlinux.org> 2.1.10-alt1
- 2.1.9 -> 2.1.10.

* Tue Aug 17 2021 Stanislav Levin <slev@altlinux.org> 2.1.9-alt1
- 1.4.14 -> 2.1.9.

* Sun Nov 24 2019 Stanislav Levin <slev@altlinux.org> 1.4.14-alt5
- Fixed build.

* Mon Sep 09 2019 Stanislav Levin <slev@altlinux.org> 1.4.14-alt4
- Fixed integration with FreeIPA.

* Thu Oct 18 2018 Stanislav Levin <slev@altlinux.org> 1.4.14-alt3
- Fixed filesystem intersections.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.14-alt2.qa1
- NMU: applied repocop patch

* Wed Sep 05 2018 Stanislav Levin <slev@altlinux.org> 1.4.14-alt2
- Enable tests.
- Fix requirements to sqlite3 in post script.

* Tue Sep 04 2018 Stanislav Levin <slev@altlinux.org> 1.4.14-alt1
- 1.4.12 -> 1.4.14.

* Tue Dec 13 2016 Mikhail Efremov <sem@altlinux.org> 1.4.12-alt2
- Fix dirs owner.
- Fix pidfile location.

* Wed Nov 02 2016 Mikhail Efremov <sem@altlinux.org> 1.4.12-alt1
- Initial build.


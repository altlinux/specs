Name: opendnssec
Version: 1.4.12
Release: alt1

Summary: DNSSEC key and zone management software
License: %bsd
Group: System/Servers

URL: http://www.opendnssec.org/
Source: %name-%version.tar
Source1: ods-enforcerd.service
Source2: ods-signerd.service
Source3: ods.sysconfig
Source4: conf.xml
Source5: tmpfiles-opendnssec.conf
Source6: ods-enforcerd.init
Source7: ods-signerd.init
Patch: %name-%version-%release.patch


BuildRequires(pre): rpm-build-licenses

BuildRequires: xml-utils xsltproc
BuildRequires: libxml2-devel libsqlite3-devel libldns-devel
BuildRequires: doxygen sqlite3

Requires: softhsm

%define _unpackaged_files_terminate_build 1

%define _pseudouser_user     _opendnssec
%define _pseudouser_group    _opendnssec
%define _pseudouser_home     %_sysconfdir/opendnssec

%description
OpenDNSSEC was created as an open-source turn-key solution for DNSSEC.
It secures zone data just before it is published in an authoritative
name server. It requires a PKCS#11 crypto module library, such as
SoftHSM.

%prep
%setup
%patch -p1

%build
#autoreconf
%configure \
	--with-ldns=%_libdir
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_localstatedir/opendnssec/{tmp,signed,signconf}
mkdir -p %buildroot%_runtimedir/opendnssec
install -Dm0644 %SOURCE1 %buildroot%_unitdir/ods-enforcerd.service
install -Dm0644 %SOURCE2 %buildroot%_unitdir/ods-signerd.service
install -Dm0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/ods
install -Dm0644 %SOURCE4 %buildroot%_sysconfdir/opendnssec/conf.xml
install -Dm0644 %SOURCE5 %buildroot%_tmpfilesdir/opendnssec.conf
install -Dm0755 %SOURCE6 %buildroot%_initdir/ods-enforcerd
install -Dm0755 %SOURCE7 %buildroot%_initdir/ods-signerd

%pre
groupadd -r -f %_pseudouser_group ||:
groupadd -r -f ods ||:
useradd -g %_pseudouser_group -G ods -c 'OpenDNSSEC daemon account' \
        -d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%post
# Initialise a slot on the softhsm on first install
if [ "$1" -eq 1 ]; then
	su -s /bin/sh -c 'softhsm2-util --init-token --slot 0 \
		--label "OpenDNSSEC" --pin 1234 --so-pin 1234' %_pseudouser_user
	if [ ! -s %_localstatedir/opendnssec/kasp.db ]; then
		echo y | ods-ksmutil setup
	fi
fi

# in case we update any xml conf file
ods-ksmutil update all >/dev/null 1>&2 ||:
%post_service ods-enforcerd
%post_service ods-signerd

%preun
%preun_service ods-signerd
%preun_service ods-enforcerd

%files
%config(noreplace) %_sysconfdir/opendnssec/
%config(noreplace) %_sysconfdir/sysconfig/ods
%config %_tmpfilesdir/opendnssec.conf
%config %_unitdir/*.service
%_initdir/ods-*
%_bindir/ods-*
%_sbindir/ods-*
%_man1dir/*
%_man5dir/*
%_man7dir/*
%_man8dir/*
%_localstatedir/opendnssec/
%_datadir/opendnssec/
%dir %_runtimedir/opendnssec/

%exclude %_sysconfdir/opendnssec/*.sample

%changelog
* Wed Nov 02 2016 Mikhail Efremov <sem@altlinux.org> 1.4.12-alt1
- Initial build.


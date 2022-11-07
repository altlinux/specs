%global optflags_lto %nil
%define _unpackaged_files_terminate_build 1
%define libwbc_alternatives_version 0.15.0
%def_with kcm
%def_with check
%def_with samba
%def_without gdm_pam_extensions
%def_disable systemtap

Name: sssd
Version: 2.8.1
Release: alt1
Group: System/Servers
Summary: System Security Services Daemon
License: GPLv3+
Url: https://pagure.io/SSSD/sssd
Source: %name-%version.tar
Source2: %name.init
Source3: system-auth-sss.pam
Source4: system-auth-use_first_pass-sss.pam
Source5: system-auth-sss-only.pam
Source6: system-auth-use_first_pass-sss-only.pam
Source7: sssd-example.conf
Source8: sssd-default.conf

Patch: %name-%version-alt.patch

# Determine the location of the LDB modules directory
%define ldb_modulesdir %(pkg-config --variable=modulesdir ldb)
%define ldb_modversion %(pkg-config --modversion ldb)

%define nfsidmapdir %_libdir/libnfsidmap

%define _localstatedir /var
%define _libexecdir /usr/libexec
%define _pamdir %_sysconfdir/pam.d

%define sssdstatedir %_localstatedir/lib/sss
%define dbpath %sssdstatedir/db
%define keytabdir %sssdstatedir/keytabs
%define pipepath %sssdstatedir/pipes
%define mcpath %sssdstatedir/mc
%define pubconfpath %sssdstatedir/pubconf
%define gpocachepath %sssdstatedir/gpo_cache
%define deskprofilepath %sssdstatedir/deskprofile
%define dotcachepath %sssdstatedir/.cache

%define sssd_user _sssd

Requires: %name-client = %version-%release
Requires: libsss_idmap = %version-%release
Requires: libldb = %ldb_modversion

Requires: libkrb5 >= 1.14.4-alt2

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): libldb-devel

### Build Dependencies ###
BuildRequires: libpopt-devel
BuildRequires: libtalloc-devel
BuildRequires: libtevent-devel
BuildRequires: libtdb-devel >= 1.1.3
BuildRequires: libldb-devel >= 1.3.3
BuildRequires: libdhash-devel >= 0.4.2
BuildRequires: libcollection-devel >= 0.5.1
BuildRequires: libini_config-devel >= 1.3.0
BuildRequires: libdbus-devel
BuildRequires: libldap-devel
BuildRequires: libpam-devel
BuildRequires: libnss-devel
BuildRequires: libnspr-devel
#BuildRequires: libssl-devel
BuildRequires: libpcre2-devel
BuildRequires: libxslt
BuildRequires: libxml2-devel
BuildRequires: docbook-dtds docbook-style-xsl xsltproc xml-utils
BuildRequires: libkrb5-devel
BuildRequires: libcares-devel
BuildRequires: python3-devel
BuildRequires: libcheck-devel
BuildRequires: doxygen
BuildRequires: libselinux-devel
BuildRequires: libsemanage-devel
BuildRequires: bind-utils
BuildRequires: libkeyutils-devel
BuildRequires: libnl-devel
BuildRequires: glib2-devel
BuildRequires: diffstat
BuildRequires: findutils
BuildRequires: samba-devel
BuildRequires: samba-winbind
BuildRequires: libsmbclient-devel
BuildRequires: libsystemd-devel
BuildRequires: cifs-utils-devel
BuildRequires: libsasl2-devel
BuildRequires: libnfsidmap-devel >= 1:2.2.1-alt1
BuildRequires: libunistring-devel
BuildRequires: libssl-devel libgnutls-devel libp11-kit-devel
BuildRequires: nscd
%if_with kcm
BuildRequires: libuuid-devel
%endif
BuildRequires: libhttp-parser-devel libcurl-devel
%if_with gdm_pam_extensions
BuildRequires: gdm-libs-devel
%endif
BuildRequires: libjansson-devel
BuildRequires: libjose-devel

%if_with check
BuildRequires: /proc
BuildRequires: openssl
BuildRequires: openssh
BuildRequires: nss-utils
BuildRequires: libcmocka-devel >= 1.0.0
BuildRequires: uid_wrapper
BuildRequires: nss_wrapper
BuildRequires: pam_wrapper
BuildRequires: softhsm
BuildRequires: adcli
%endif
BuildRequires: po4a

# Due sssd-drop-privileges control for unprivileged mode support
Requires: local-policy >= 0.4.8

%description
Provides a set of daemons to manage access to remote directories and
authentication mechanisms. It provides an NSS and PAM interface toward
the system and a pluggable backend system to connect to multiple different
account sources. It is also the basis to provide client auditing and policy
services for projects like FreeIPA.

The sssd subpackage is a meta-package that contains the deamon as well as all
the existing back ends.

%package client
Summary: SSSD Client libraries for NSS and PAM
Group: Networking/Other
License: LGPLv3+
Provides: libnss_sss
Provides: pam_sss
Requires: pam-config >= 1.9.0

%description client
Provides the libraries needed by the PAM and NSS stacks to connect to the SSSD
service.

%package -n libsss_sudo
Summary: A library to allow communication between SUDO and SSSD
Group: System/Libraries
License: LGPLv3+

%description -n libsss_sudo
A utility library to allow communication between SUDO and SSSD

%package -n libsss_autofs
Summary: A library to allow communication between Autofs and SSSD
Group: System/Libraries
License: LGPLv3+

%description -n libsss_autofs
A utility library to allow communication between Autofs and SSSD

%package tools
Summary: Userspace tools for use with the SSSD
Group: System/Configuration/Networking
License: GPLv3+
Requires: %name = %version-%release
Requires: python3-module-sss = %EVR
Requires: python3-module-sssd = %EVR
Requires: python3-module-sssdconfig = %EVR

%description tools
Provides several administrative tools:
    * sss_debuglevel to change the debug level on the fly
    * sss_seed which pre-creates a user entry for use in kickstarts
    * sss_obfuscate for generating an obfuscated LDAP password
    * sssctl -- an sssd status and control utility

%package ldap
Summary: The LDAP back end of the SSSD
Group: System/Servers
License: GPLv3+
Requires: %name-krb5-common = %version-%release

%description ldap
Provides the LDAP back end that the SSSD can utilize to fetch identity data
from and authenticate against an LDAP server.

%package krb5-common
Summary: SSSD helpers needed for Kerberos and GSSAPI authentication
Group: System/Servers
License: GPLv3+
Requires: %name = %version-%release
Requires: libsasl2-plugin-gssapi

%description krb5-common
Provides helper processes that the LDAP and Kerberos back ends can use for
Kerberos user or host authentication.

%package krb5
Summary: The Kerberos authentication back end for the SSSD
Group: System/Servers
License: GPLv3+
Requires: %name-krb5-common = %version-%release

%description krb5
Provides the Kerberos back end that the SSSD can utilize authenticate
against a Kerberos server.

%package pac
Summary: Common files needed for supporting PAC processing
Group: System/Servers
License: GPLv3+
Requires: %name = %version-%release

%description pac
Provides common files needed by SSSD providers such as IPA and Active Directory
for handling Kerberos PACs.

%package ipa
Summary: The IPA back end of the SSSD
Group: System/Servers
License: GPLv3+
Requires: %name-krb5-common = %version-%release
Requires: %name-pac = %version-%release
Requires: libipa_hbac = %version-%release

%description ipa
Provides the IPA back end that the SSSD can utilize to fetch identity data
from and authenticate against an IPA server.

%package ad
Summary: The AD back end of the SSSD
Group: System/Servers
License: GPLv3+
Requires: %name-krb5-common = %version-%release
Requires: %name-pac = %version-%release
Requires: %name-winbind-idmap = %version-%release
Requires: adcli

%description ad
Provides the Active Directory back end that the SSSD can utilize to fetch
identity data from and authenticate against an Active Directory server.

%package proxy
Summary: The proxy back end of the SSSD
Group: System/Servers
License: GPLv3+
Requires: %name = %version-%release

%description proxy
Provides the proxy back end which can be used to wrap an existing NSS and/or
PAM modules to leverage SSSD caching.

%package kcm
Summary: The SSSD Kerberos credentials manager
Group: System/Servers
License: GPLv3+
Requires: %name = %version-%release

%description kcm
An implementation of a Kerberos KCM server is a process that stores, tracks and
manages Kerberos credential caches. It originates in the Heimdal Kerberos
project, although the MIT Kerberos library also provides client side support for
the KCM credential cache.

%package idp
Summary: Kerberos plugins and OIDC helper for external identity providers.
Group: System/Servers
License: GPLv3+
Requires: %name = %version-%release

%description idp
This package provides Kerberos plugins that are required to enable
authentication against external identity providers. Additionally a helper
program to handle the OAuth 2.0 Device Authorization Grant is provided.

%package -n libsss_idmap
Summary: FreeIPA Idmap library
Group: System/Libraries
License: LGPLv3+

%description -n libsss_idmap
Utility library to convert SIDs to Unix uids and gids

%package -n libsss_idmap-devel
Summary: FreeIPA Idmap library
Group: Development/C
License: LGPLv3+
Requires: libsss_idmap = %version-%release

%description -n libsss_idmap-devel
Utility library to SIDs to Unix uids and gids

%package -n libsss_certmap
Summary: SSSD Certficate Mapping Library
Group: System/Libraries
License: LGPLv3+
Conflicts: sssd < %version-%release

%description -n libsss_certmap
Library to map certificates to users based on rules

%package -n libsss_certmap-devel
Summary: SSSD Certficate Mapping Library
Group: Development/C
License: LGPLv3+
Requires: libsss_certmap = %version-%release

%description -n libsss_certmap-devel
Library to map certificates to users based on rules

%package -n libipa_hbac
Summary: FreeIPA HBAC Evaluator library
Group: System/Libraries
License: LGPLv3+

%description -n libipa_hbac
Utility library to validate FreeIPA HBAC rules for authorization requests

%package -n libipa_hbac-devel
Summary: FreeIPA HBAC Evaluator library
Group: Development/C
License: LGPLv3+
Requires: libipa_hbac = %version-%release

%description -n libipa_hbac-devel
Utility library to validate FreeIPA HBAC rules for authorization requests

%package -n libsss_nss_idmap
Summary: Library for SID based lookups and certificate based lookups
Group: System/Libraries
License: LGPLv3+

%description -n libsss_nss_idmap
Utility library for SID based lookups and certificate based lookups

%package -n libsss_nss_idmap-devel
Summary: Library for SID based lookups and certificate based lookups
Group: Development/C
License: LGPLv3+
Requires: libsss_nss_idmap = %version-%release

%description -n libsss_nss_idmap-devel
Utility library for SID based lookups and certificate based lookups

%package dbus
Summary: The D-Bus responder of the SSSD
Group: System/Servers
License: GPLv3+
Requires: %name = %version-%release

%description dbus
Provides the D-Bus responder of the SSSD, called the InfoPipe, that allows
the information from the SSSD to be transmitted over the system bus.

%package -n libsss_simpleifp
Summary: The SSSD D-Bus responder helper library
Group: System/Libraries
License: GPLv3+
Requires: %name-dbus = %version-%release

%description -n libsss_simpleifp
Provides library that simplifies D-Bus API for the SSSD InfoPipe responder.

%package -n libsss_simpleifp-devel
Summary: The SSSD D-Bus responder helper library
Group: Development/C
License: GPLv3+
Requires: libsss_simpleifp = %version-%release

%description -n libsss_simpleifp-devel
Provides library that simplifies D-Bus API for the SSSD InfoPipe responder.

%package winbind-idmap
Summary: SSSD's idmap_sss Backend for Winbind
Group: System/Servers
License: GPLv3+ and LGPLv3+

%description winbind-idmap
The idmap_sss module provides a way for Winbind to call SSSD to map UIDs/GIDs
and SIDs.

%package nfs-idmap
Summary: SSSD plug-in for NFSv4 rpc.idmapd
Group: System/Servers
License: GPLv3+

%description nfs-idmap
The libnfsidmap sssd module provides a way for rpc.idmapd to call SSSD to map
UIDs/GIDs to names and vice versa. It can be also used for mapping principal
(user) name to IDs(UID or GID) or to obtain groups which user are member of.

%package -n python3-module-sssdconfig
Summary: SSSD and IPA configuration file manipulation classes and functions
Group: Development/Python3
License: GPLv3+
BuildArch: noarch

%description -n python3-module-sssdconfig
Provides python3 files for manipulation SSSD and IPA configuration files.

%package -n python3-module-ipa_hbac
Summary: Python3 bindings for the FreeIPA HBAC Evaluator library
Group: Development/Python3
License: LGPLv3+
Requires: libipa_hbac = %EVR

%description -n python3-module-ipa_hbac
The python3-module-libipa_hbac contains the bindings so that libipa_hbac can be
used by Python3 applications.

%package -n python3-module-sss_nss_idmap
Summary: Python3 bindings for libsss_nss_idmap
Group: Development/Python3
License: LGPLv3+
Requires: libsss_nss_idmap = %EVR

%description -n python3-module-sss_nss_idmap
The python3-module-libsss_nss_idmap contains the bindings so that
libsss_nss_idmap can be used by Python applications.

%package -n python3-module-sss
Summary: Python3 bindings for sss
Group: Development/Python3
License: LGPLv3+
Requires: %name = %EVR

%description -n python3-module-sss
Provides python3 bindings:
    * function for retrieving list of groups user belongs to
    * class for obfuscation of passwords

%package -n python3-module-sss-murmur
Summary: Python3 bindings for murmur hash function
Group: Development/Python3
License: LGPLv3+

%description -n python3-module-sss-murmur
Provides python3 module for calculating the murmur hash version 3

%package -n python3-module-sssd
Summary: Python3 programs with sssd analyze tools
Group: System/Configuration/Other
License: GPLv3+

%add_python3_req_skip modules

%description -n python3-module-sssd
Provides python3 programs with sssd analyze tools

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
    --with-db-path=%dbpath \
    --with-pipe-path=%pipepath \
    --with-pubconf-path=%pubconfpath \
    --with-mcache-path=%mcpath \
    --with-gpo-cache-path=%gpocachepath \
    --with-init-dir=%_initdir \
    --with-initscript=systemd \
    --with-systemdunitdir=%_unitdir \
    --with-krb5-rcache-dir=%_localstatedir/cache/krb5rcache \
    --enable-nsslibdir=/%_lib \
    --enable-pammoddir=/%_lib/security \
    --enable-nfsidmaplibdir=%nfsidmapdir \
    --with-syslog=journald \
    --with-test-dir=/dev/shm \
    --enable-ldb-version-check \
    --enable-krb5-locator-plugin \
    --enable-pac-responder \
    --enable-sss-default-nss-plugin \
    --with-sssd-user=%sssd_user \
    --disable-rpath \
    --disable-static \
    %{subst_with kcm} \
    %{subst_with samba} \
    %{?!_enable_systemtap:--disable-systemtap} \
    --without-python2-bindings \
    #

%make_build all
%make docs

%install
for f in \
    src/tools/sss_obfuscate \
    src/tools/analyzer/sss_analyze;
do
    sed -i -e 's:/usr/bin/python:/usr/bin/python3:' \
           -e 's:/usr/bin/env\s*python\s*:/usr/bin/python3:' \
        "$f"
done

%make install DESTDIR=%buildroot

%find_lang sssd

# Prepare empty config file
install -D -m600 %SOURCE8 %buildroot%_sysconfdir/%name/%name.conf

# Copy default logrotate file
install -D -m644 src/examples/logrotate %buildroot%_sysconfdir/logrotate.d/%name

touch %buildroot%mcpath/passwd
touch %buildroot%mcpath/group
touch %buildroot%mcpath/initgroups

install -D -m755 %SOURCE2 %buildroot%_initdir/%name
install -D -m644 %SOURCE3 %buildroot%_pamdir/system-auth-sss
install -D -m644 %SOURCE4 %buildroot%_pamdir/system-auth-use_first_pass-sss
install -D -m644 %SOURCE5 %buildroot%_pamdir/system-auth-sss-only
install -D -m644 %SOURCE6 %buildroot%_pamdir/system-auth-use_first_pass-sss-only

# Remove .la files created by libtool
find %buildroot -name "*.la" -exec rm -f {} \;

# Suppress developer-only documentation
rm -Rf %buildroot%_docdir/%name

mkdir -p %buildroot%pubconfpath/krb5.include.d
mkdir -p %buildroot%dotcachepath
mkdir -p %buildroot%_sysconfdir/krb5.conf.d

# Kerberos KCM credential cache would be ruled by control
# cp %buildroot%_datadir/sssd/krb5-snippets/kcm_default_ccache %buildroot%_sysconfdir/krb5.conf.d/kcm_default_ccache

# Enable krb5 idp plugins by default (when sssd-idp package is installed)
cp %buildroot%_datadir/sssd/krb5-snippets/sssd_enable_idp %buildroot%_sysconfdir/krb5.conf.d/sssd_enable_idp

# krb5 configuration snippet
cp %buildroot%_datadir/sssd/krb5-snippets/enable_sssd_conf_dir %buildroot%_sysconfdir/krb5.conf.d/enable_sssd_conf_dir

# Add alternatives for idmap-plugin
mkdir -p %buildroot/%_altdir
printf '%_libdir/cifs-utils/idmap-plugin\t%_libdir/cifs-utils/cifs_idmap_sss.so\t20\n' > %buildroot%_altdir/cifs-idmap-plugin-sss

%if_disabled systemtap
# Clean manpages l10n
rm -f %buildroot/%_mandir/*/man5/sssd-systemtap.5*
%endif

%check
export CK_TIMEOUT_MULTIPLIER=10
%make check VERBOSE=yes
unset CK_TIMEOUT_MULTIPLIER

%pre
%_sbindir/groupadd -r -f %sssd_user 2> /dev/null ||:
%_sbindir/useradd -r -n -g %sssd_user -G _keytab -d %sssdstatedir -s /dev/null -c "User for sssd" %sssd_user 2> /dev/null ||:

%post
chown root:root %_sysconfdir/sssd/sssd.conf

# Don't restart sssd services until reboot or manual restart
#post_service %name
#
#preun
#preun_service %name

%triggerpostun -- %name < 2.4.2-alt1
[ "$(control sssd-drop-privileges)" != "unknown" ] ||
    control sssd-drop-privileges unprivileged

#triggerpostun -- %name < 1.14.2-alt5
#_bindir/gpasswd -a %sssd_user _keytab

%files -f sssd.lang
%doc COPYING
%doc $RPM_SOURCE_DIR/sssd-example.conf
%_sbindir/%name
%_initdir/%name
%_unitdir/%name.service
%_unitdir/sssd-nss.service
%_unitdir/sssd-nss.socket
%_unitdir/sssd-pam-priv.socket
%_unitdir/sssd-pam.service
%_unitdir/sssd-pam.socket
%_unitdir/sssd-ssh.service
%_unitdir/sssd-ssh.socket

%dir %_libexecdir/%name
%_libexecdir/%name/sssd_be
%_libexecdir/%name/sssd_check_socket_activated_responders
%_libexecdir/%name/sssd_nss
%_libexecdir/%name/sssd_pam
%_libexecdir/%name/sssd_autofs
%_libexecdir/%name/sssd_ssh
%_libexecdir/%name/sssd_sudo
%_libexecdir/%name/p11_child
%_datadir/polkit-1/rules.d/*

%dir %_libdir/%name
%_libdir/%name/libsss_simple.so

#Internal shared libraries
%_libdir/%name/libsss_child.so
%_libdir/%name/libsss_crypt.so
%_libdir/%name/libsss_cert.so
%_libdir/%name/libsss_debug.so
%_libdir/%name/libsss_files.so
%_libdir/%name/libsss_krb5_common.so
%_libdir/%name/libsss_ldap_common.so
%_libdir/%name/libsss_util.so
%_libdir/%name/libsss_semanage.so
%_libdir/%name/libsss_sbus.so
%_libdir/%name/libsss_sbus_sync.so
%_libdir/%name/libsss_iface.so
%_libdir/%name/libsss_iface_sync.so
%_libdir/%name/libifp_iface.so
%_libdir/%name/libifp_iface_sync.so

# 3rd party application libraries
%dir %_libdir/%name/modules

%ldb_modulesdir/memberof.so
%_bindir/sss_ssh_authorizedkeys
%_bindir/sss_ssh_knownhostsproxy
%_sbindir/sss_cache
%_libexecdir/%name/sss_signal

%dir %sssdstatedir
%dir %_localstatedir/cache/krb5rcache
%attr(700,%sssd_user,%sssd_user) %dir %dbpath
%attr(755,%sssd_user,%sssd_user) %dir %mcpath
%attr(700,%sssd_user,%sssd_user) %dir %deskprofilepath
%ghost %attr(0644,%sssd_user,%sssd_user) %verify(not md5 size mtime) %mcpath/passwd
%ghost %attr(0644,%sssd_user,%sssd_user) %verify(not md5 size mtime) %mcpath/group
%ghost %attr(0644,%sssd_user,%sssd_user) %verify(not md5 size mtime) %mcpath/initgroups
%attr(755,%sssd_user,%sssd_user) %dir %pipepath
%attr(750,%sssd_user,root) %dir %pipepath/private
%attr(755,%sssd_user,%sssd_user) %dir %gpocachepath
%attr(755,%sssd_user,%sssd_user) %dir %pubconfpath
%attr(755,%sssd_user,%sssd_user) %dir %dotcachepath
%attr(770,root,%sssd_user) %dir %_logdir/%name
%attr(750,root,%sssd_user) %dir %_sysconfdir/sssd
%attr(750,root,%sssd_user) %dir %_sysconfdir/sssd/conf.d
%attr(0600,root,root) %config(noreplace) %_sysconfdir/sssd/sssd.conf
%dir %_sysconfdir/systemd/system/sssd.service.d
%config(noreplace) %_sysconfdir/logrotate.d/sssd
%dir %_datadir/%name
%_sysconfdir/pam.d/sssd-shadowutils
%dir %_libdir/%name/conf
%_libdir/%name/conf/sssd.conf

%_datadir/%name/cfg_rules.ini
%_datadir/%name/sssd.api.conf
%dir %_datadir/%name/sssd.api.d
%_datadir/%name/sssd.api.d/sssd-simple.conf
%_datadir/%name/sssd.api.d/sssd-files.conf
%_man1dir/sss_ssh_*
%_mandir/*/man1/sss_ssh_*
%_man5dir/sssd.conf.5*
%_mandir/*/man5/sssd.conf.5*
%_man5dir/sssd-files.5*
%_mandir/*/man5/sssd-files.5*
%_man5dir/sssd-simple.5*
%_mandir/*/man5/sssd-simple.5*
%_man5dir/sssd-sudo.5*
%_mandir/*/man5/sssd-sudo.5*
%_man5dir/sssd-session-recording.5*
%_mandir/*/man5/sssd-session-recording.5*
%_man5dir/sss_rpcidmapd.5*
%_mandir/*/man5/sss_rpcidmapd.5*
%_man8dir/sssd.8*
%_mandir/*/man8/sssd.8*
%_man8dir/sss_cache.8*
%_mandir/*/man8/sss_cache.8*

%if_enabled systemtap
%dir %_datadir/%name/systemtap
%_datadir/%name/systemtap/*.stp
%dir %_datadir/systemtap
%dir %_datadir/systemtap/tapset
%_datadir/systemtap/tapset/sssd*.stp
%_man5dir/sssd-systemtap.5*
%endif

%files ldap
%_libdir/%name/libsss_ldap.so
%_man5dir/sssd-ldap*
%_mandir/*/man5/sssd-ldap*
%_datadir/%name/sssd.api.d/sssd-ldap.conf

%files krb5-common
%attr(755,%sssd_user,%sssd_user) %dir %pubconfpath/krb5.include.d
%attr(4710,root,%sssd_user) %_libexecdir/%name/ldap_child
%attr(4710,root,%sssd_user) %_libexecdir/%name/krb5_child

%files krb5
%_libdir/%name/libsss_krb5.so
%_man5dir/sssd-krb5*
%_mandir/*/man5/sssd-krb5*
%_datadir/%name/sssd.api.d/sssd-krb5.conf
%config(noreplace) %_sysconfdir/krb5.conf.d/enable_sssd_conf_dir
%dir %_datadir/sssd/krb5-snippets
%_datadir/sssd/krb5-snippets/enable_sssd_conf_dir

%files pac
%_libexecdir/%name/sssd_pac
%_unitdir/sssd-pac.service
%_unitdir/sssd-pac.socket

%files ipa
%attr(700,%sssd_user,%sssd_user) %dir %keytabdir
%_libdir/%name/libsss_ipa.so
%attr(4710,root,%sssd_user) %_libexecdir/%name/selinux_child
%_man5dir/sssd-ipa*
%_mandir/*/man5/sssd-ipa*
%_datadir/%name/sssd.api.d/sssd-ipa.conf

%files ad
%_libdir/%name/libsss_ad.so
%_libexecdir/%name/gpo_child
%_man5dir/sssd-ad*
%_mandir/*/man5/sssd-ad*
%_datadir/%name/sssd.api.d/sssd-ad.conf

%files proxy
%attr(4710,root,%sssd_user) %_libexecdir/%name/proxy_child
%_libdir/%name/libsss_proxy.so
%_datadir/%name/sssd.api.d/sssd-proxy.conf

%files client
%config(noreplace) %_pamdir/*-sss*
/%_lib/libnss_sss.so.2
/%_lib/security/pam_sss.so
/%_lib/security/pam_sss_gss.so
%_libdir/krb5/plugins/libkrb5/sssd_krb5_locator_plugin.so
%_libdir/krb5/plugins/authdata/sssd_pac_plugin.so
%_libdir/cifs-utils/cifs_idmap_sss.so
%_altdir/cifs-idmap-plugin-sss
%_libdir/%name/modules/sssd_krb5_localauth_plugin.so
%_man8dir/pam_sss*
%_mandir/*/man8/pam_sss*
%_man8dir/sssd_krb5_locator_plugin*
%_mandir/*/man8/sssd_krb5_locator_plugin*
%_man8dir/sssd_krb5_localauth_plugin*
%_mandir/*/man8/sssd_krb5_localauth_plugin*

%files -n libsss_sudo
%_libdir/libsss_sudo.so*
%_unitdir/sssd-sudo.service
%_unitdir/sssd-sudo.socket

%files -n libsss_autofs
%_libdir/%name/modules/libsss_autofs.so
%_unitdir/sssd-autofs.service
%_unitdir/sssd-autofs.socket

%files tools
%_sbindir/sss_*
%_sbindir/sssctl
%_libexecdir/%name/sss_analyze
%_man8dir/sss_*
%_mandir/*/man8/sss_*
%_man8dir/sssctl*
%_mandir/*/man8/sssctl*
%exclude %_sbindir/sss_cache
%exclude %_man8dir/sss_cache*
%exclude %_mandir/*/man8/sss_cache*

%files -n libsss_idmap
%_libdir/libsss_idmap.so.*

%files -n libsss_idmap-devel
%doc idmap_doc/html
%_includedir/sss_idmap.h
%_libdir/libsss_idmap.so
%_pkgconfigdir/sss_idmap.pc

%files -n libsss_certmap
%_libdir/libsss_certmap.so.*
%_man5dir/sss-certmap*
%_mandir/*/man5/sss-certmap*

%files -n libsss_certmap-devel
%doc certmap_doc/html
%_includedir/sss_certmap.h
%_libdir/libsss_certmap.so
%_pkgconfigdir/sss_certmap.pc

%files -n libipa_hbac
%_libdir/libipa_hbac.so.*

%files -n libipa_hbac-devel
%doc hbac_doc/html
%_includedir/ipa_hbac.h
%_libdir/libipa_hbac.so
%_pkgconfigdir/ipa_hbac.pc

%files -n libsss_nss_idmap
%_libdir/libsss_nss_idmap.so.*

%files -n libsss_nss_idmap-devel
%doc nss_idmap_doc/html
%_includedir/sss_nss_idmap.h
%_libdir/libsss_nss_idmap.so
%_pkgconfigdir/sss_nss_idmap.pc

%files dbus
%doc COPYING
%_libexecdir/%name/sssd_ifp
%_man5dir/sssd-ifp*
%_mandir/*/man5/sssd-ifp*
# InfoPipe DBus plumbing
%_sysconfdir/dbus-1/system.d/org.freedesktop.sssd.infopipe.conf
%_datadir/dbus-1/system-services/org.freedesktop.sssd.infopipe.service
%_unitdir/sssd-ifp.service

%if_with kcm
%files kcm
%_libexecdir/%name/sssd_kcm
%dir %_datadir/sssd-kcm
%_datadir/sssd-kcm/kcm_default_ccache
%_unitdir/sssd-kcm.socket
%_unitdir/sssd-kcm.service
%_man8dir/sssd-kcm*
%_mandir/*/man8/sssd-kcm*
%endif

%files idp
%_libexecdir/%name/oidc_child
%_libdir/%name/modules/sssd_krb5_idp_plugin.so
%_datadir/sssd/krb5-snippets/sssd_enable_idp
%config(noreplace) %_sysconfdir/krb5.conf.d/sssd_enable_idp

%files -n libsss_simpleifp
%_libdir/libsss_simpleifp.so.*

%files -n libsss_simpleifp-devel
%_includedir/sss_sifp.h
%_includedir/sss_sifp_dbus.h
%_libdir/libsss_simpleifp.so
%_pkgconfigdir/sss_simpleifp.pc

%files winbind-idmap
%_libdir/samba/idmap/sss.so
%_man8dir/idmap_sss*
%_mandir/*/man8/idmap_sss*

%files nfs-idmap
%nfsidmapdir/sss.so

%files -n python3-module-sss
%python3_sitelibdir/pysss.so

%files -n python3-module-sss-murmur
%python3_sitelibdir/pysss_murmur.so

%files -n python3-module-ipa_hbac
%python3_sitelibdir/pyhbac.so

%files -n python3-module-sss_nss_idmap
%python3_sitelibdir/pysss_nss_idmap.so

%files -n python3-module-sssdconfig
%dir %python3_sitelibdir_noarch/SSSDConfig
%python3_sitelibdir_noarch/SSSDConfig/*.py*
%python3_sitelibdir_noarch/SSSDConfig*.egg-info
%dir %python3_sitelibdir_noarch/SSSDConfig/__pycache__
%python3_sitelibdir_noarch/SSSDConfig/__pycache__/*.py*

%files -n python3-module-sssd
%dir %python3_sitelibdir_noarch/sssd
%python3_sitelibdir_noarch/sssd/*.py*
%dir %python3_sitelibdir_noarch/sssd/__pycache__
%python3_sitelibdir_noarch/sssd/__pycache__/*.py*
%dir %python3_sitelibdir_noarch/sssd/modules
%python3_sitelibdir_noarch/sssd/modules/*.py*
%dir %python3_sitelibdir_noarch/sssd/modules/__pycache__
%python3_sitelibdir_noarch/sssd/modules/__pycache__/*.py*

%changelog
* Mon Nov 07 2022 Evgeny Sinelnikov <sin@altlinux.org> 2.8.1-alt1
- Update to latest 2.8 major release.
- Important fixes:
  + A regression when running sss_cache when no SSSD domain is enabled would
    produce a syslog critical message was fixed.
  + Several fixes in D-Bus infopipe functions:
    ListByName(), Groups.ListByName() and Groups.ListByDomainAndName().

* Sat Oct 29 2022 Evgeny Sinelnikov <sin@altlinux.org> 2.8.0-alt2
- Redesign become_user patch to should assign supplementary groups for server
  part of code only (due race condition in krb5_child, for example).

* Sat Oct 15 2022 Evgeny Sinelnikov <sin@altlinux.org> 2.8.0-alt1
- AD GPO: Fix support processing referrals for hostname
- New features
  + Introduced the dbus function
    org.freedesktop.sssd.infopipe.Users.ListByAttr(attr, value, limit)
    listing upto limit users matching the filter attr=value.
  + sssctl is now able to create, list and delete indexes on the local caches.
    Indexes are useful for the new D-Bus ListByAttr() function.
  + sssctl is now able to read and set each component's debug level
    independently.
- Important fixes:
  + domains option in [sssd] section can now be completely omitted if domains
    are enabled via domains/enabled option.
- New options:
  + core_dumpable, ldap_enumeration_refresh_offset,
    subdomain_refresh_interval_offset, dyndns_refresh_interval_offset
    refresh_expired_interval_offset, ldap_purge_cache_offset.
- Configuration changes:
  + Option 'ad_machine_account_password_renewal_opts' now accepts an optional
    third part as the maximum deviation in the provided period (first part) and
    initial delay (second part). If the period and initial delay are provided
    but not the offset, the offset is assumed to be 0. If no part is provided,
    the default is 86400:750:300.
  + override_homedir now recognizes the %h template which is replaced by the
    original home directory retrieved from the identity provider, but in lower
    case.

* Wed Sep 07 2022 Evgeny Sinelnikov <sin@altlinux.org> 2.7.4-alt1
- Update to latest 2.7 major release.
- Lock-free client support will be only built if libc provides
  pthread_key_create() and pthread_once().
  For glibc this means version 2.34+
- Add requirement of adcli to sssd-ad.

* Fri Jul 15 2022 Evgeny Sinelnikov <sin@altlinux.org> 2.7.3-alt1
- Update to latest 2.7 major release:
  + CLIENT: use thread local storage for socket to a.void the need for a lock.
  + SSS_CLIENT: got rid of code duplication.
  + SSS_CLIENT: mem-cache: fixed missing error code.
  + PAM P11: fixed minor mem-leak.

* Sat Jun 18 2022 Evgeny Sinelnikov <sin@altlinux.org> 2.7.2-alt2
- Update russian translations (by Elena Mishina <lepata@basealt.ru>)

* Tue Jun 14 2022 Evgeny Sinelnikov <sin@altlinux.org> 2.7.2-alt1
- Update to 2.7 major release:
  + Added a new krb5 plugin idp and a new binary oidc_child which performs
    OAuth2 authentication against FreeIPA.
  + Better default for IPA/AD re_expression. Tunning for group names
    containing '@' is no longer needed.
  + Added support for anonymous PKINIT to get FAST credentials.
  + SSSD now correctly falls back to UPN search if the user was not found even
    with cache_first = true.
  + SSSD can now handle multi-valued RDNs if a unique name must be determined
    with the help of the RDN.
  + New option implicit_pac_responder to control if the PAC responder is started
    for the IPA and AD providers, default is true.
  + New option krb5_check_pac to control the PAC validation behavior.
  + Multiple crl_file arguments can be used in the certificate_verification
    option.

* Thu Jan 27 2022 Evgeny Sinelnikov <sin@altlinux.org> 2.6.3-alt1
- AD Domain in the AD Forest Missing after sssd latest update
- sdap_idmap.c/sssd_idmap.c incorrectly calculates rangesize from upper/lower
- Regression on rawhide with ssh auth using password
- sssd-ad broken in 2.6.2, 389 used as kerberos port
- sssd error triggers backtrace: write_krb5info_file_from_fo_server

* Wed Jan 12 2022 Evgeny Sinelnikov <sin@altlinux.org> 2.6.2-alt1
- Update to latest release:
  + Lookup with fully-qualified name does not work with cache_first is True.
  + sssd_be segfault due to empty forest root name.
  + Groups are missing while performing id lookup as SSSD switching to offline
    mode due to the wrong domain name in the ldap-pings(netlogon).
  + LDAP sp_expire policy does not match other libraries.
  + Passwordless (GSSAPI) SSH not working due to missing
    includedir  /var/lib/sss/pubconf/krb5.include.d directive in /etc/krb5.conf.
  + pam responder does not call initgroups to refresh the user entry.
  + FindByValidCertificate() treats unconfigured CA as Invalid certificate provide.
  + sssd does not use kerberos port that is set.

* Mon Dec 13 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.6.1-alt3
- Update with latest libldb-2.3.2-alt2 fixes.
- Backport newest fixes from upstream:
  + utils: ignore systemd and sd-pam process in get_active_uid_linux()
  + cldap: use dns_resolver_server_timeout timeout for cldap ping
  + ad: only send cldap-ping to our local domain
  + ad: make ad_srv_plugin_ctx_switch_site() public
  + ad: use already discovered forest name

* Mon Nov 15 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.6.1-alt2
- Revert reverted patch with change owner/permissions of user deskprofile path
  due it still needed.

* Wed Nov 10 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.6.1-alt1
- Update to 2.6.1 stable release.
- Revert "Don't change owner/permissions of user deskprofile path" patch
  due CAP_DAC_OVERRIDE was added to systemd configs in 2.4.2 release.

* Sun Nov 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.6.0-alt1
- Update to 2.6.0 (with upstream fixes from master - 7bfdd3db8e4c).
- Security issue in the sssctl command - shell command injection via the
  logs-fetch and cache-expire subcommands (fixes: CVE-2021-3621).
- pam_sss: Allow offline authentication against non-ipa-desktopprofiles aware DC
- Add filter for Active Directory trusted domains which are not trusted (one-way
  trust) or are from a different forest (direct trust). Both should be ignored
  because they are not trusted or can currently not be handled properly.

* Fri Oct 29 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.5.2-alt2
- FTBFS: disable LTO

* Thu Jul 29 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.5.2-alt1
- Update to 2.5.2:
  + auto_private_groups option can be set centrally through ID range setting
    in IPA (see ipa idrange commands family).
  + Default value of ldap_sudo_random_offset changed to 0 (disabled).
  + originalADgidNumber attribute in the SSSD cache is now indexed.
  + Add new config option fallback_to_nss.

* Fri May 14 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.5.0-alt1
- Update to 2.5.0:
  + Deprecated support of secrets, local-provider, libwbclient, pcre1.
  + Added support for automatic renewal of renewable TGTs stored in KCM cache.
  + Backround sudo periodic tasks (smart and full refresh) periods are now
    extended by a random offset.
  + Completing a sudo full refresh now postpones the smart refresh by
    ldap_sudo_smart_refresh_interval value.
  + Besides trusted domains known by the forest root, trusted domains known by
    the local domain are used as well.
  + New configuration option offline_timeout_random_offset to control random
    factor in backend probing interval when SSSD is in offline mode.

* Fri May 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.4.2-alt2
- Apply internal, domain and service fixes from upstream.
- Add compatibility support of unprivileged mode with "user = _sssd"
  due from sssd-2.4.2 default user is set to root.

* Tue Feb 23 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.4.2-alt1
- Update to 2.4.2
- Add CapabilityBoundingSet option as a security hardening measure
  for systemd service configs

* Tue Feb 16 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.4.1-alt3
- Update authentication features:
  + pam_sss: Don't fail on deskprofiles phase for AD users
  + pam_sss_gss: support authentication indicators

* Tue Feb 09 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.4.1-alt2
- Fixate that upstream fixed the memory leak in the
  simple access provider (fixes: OVE-20210209-0001)

* Fri Feb 05 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.4.1-alt1
- Update to 2.4.1
- Add PAM module pam_sss_gss for authentication using GSSAPI

* Tue Feb 02 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.4.0-alt3
- Add krb5_use_subdomain_realm=True to support upnSuffixes for trusted domains
- Allow to set case_sensitive=Preserving in subdomain section
- Add auto_private_groups to subdomain_inherit
- Add /var/lib/sss/.cache directory for gencache.tdb using samba gpo libraries

* Thu Nov 12 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.4.0-alt2
- Reapply patch with ignore GPO if SecEdit/GptTmpl.inf is missing

* Thu Oct 15 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.4.0-alt1
- Update to 2.4.0

* Sat Aug 01 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.3.1-alt1
- Update to 2.3.1
- Remove derecated libwbclient-sssd

* Thu Jul 23 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.3.0-alt3
- Rebuild with libldb-2.0.12

* Tue Jun 30 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.3.0-alt2
- Rebuild with libldb-2.0.11

* Wed Jun 10 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.3.0-alt1
- Update to 2.3.0

* Sun May 17 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.2.3-alt3
- Rewrite PAM rules for sss system-auth method with new pam-config-1.9.0 scheme
  using pam_localuser.so to separate configuration for local and remote users.
- Added dependency sssd-client to pam-config-1.9.0 supported configurable
  session substack system-policy.
- Added dependency sssd-ad to winbind-idmap for compatibility installation.

* Wed Apr 29 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.2.3-alt2
- Updated sss system-auth method with pam_auth_common substack
- Added requires to pam-config-1.8.0 supported pam_auth_common substack

* Tue Apr 28 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.2.3-alt1.1
- Rebuild with libldb-2.0.10

* Thu Mar 19 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.2.3-alt1
- Update to 2.2.3

* Tue Mar 10 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.2.2-alt4
- Rebuild with libldb-2.0.9

* Fri Nov 01 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.2.2-alt3
- Rebuild with latest version on libldb-2.0.8 with release of Samba 4.11

* Sat Oct 19 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.2.2-alt2
- Rebuild with latest version libldb-1.5.6

* Sun Sep 22 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.2.2-alt1
- Update to 2.2.2

* Fri Aug 30 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.2.1-alt1
- Update to 2.2.1

* Mon Aug 12 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.2.0-alt3
- Rebuild with latest version libldb-1.5.5

* Tue Jul 02 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.2.0-alt2
- Fix sssd-ad System error during access deny to sysvol when it not replicated
  or not configured with 'samba-tool ntacl sysvolreset' command
- Clean spec compatibility base on ubt macroses

* Fri Jun 28 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.2.0-alt1
- Update to 2.2.0

* Fri Jun 28 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.1.0-alt2
- Update libwbclient-sssd interface to version 0.15 (Closes: 36750)

* Tue Mar 26 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.1.0-alt1
- Update to 2.1.0 for samba-4.10.0

* Sun Mar 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.0.0-alt5.gitf0603645f
- Rebuild with latest version libldb
- Revert strict requirement to version of libldb

* Thu Feb 21 2019 Stanislav Levin <slev@altlinux.org> 2.0.0-alt4.gitf0603645f
- Fixed FleetCommander integration.
- Stopped build Python2 bindings.

* Fri Dec 07 2018 Evgeny Sinelnikov <sin@altlinux.org> 2.0.0-alt3.gitf0603645f
- Remove build requires for selinux-policy-targeted

* Thu Oct 25 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt2.gitf0603645f
- Applied an upstream snapshot due to a huge amount of issues in 2.0.0.
- Fixed start under a non-privileged user (Closes: #35545).

* Fri Oct 19 2018 Alexey Shabalin <shaba@altlinux.org> 2.0.0-alt1
- 2.0.0

* Tue Aug 14 2018 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.16.3-alt1
- New upstream version 1.16.3
  + Dropped patch `nss: skip incomplete groups instead of bailing out',
    included by upstream
  + Refreshed become_user patch (unit test passes now)

* Thu Jul 19 2018 Stanislav Levin <slev@altlinux.org> 1.16.2-alt2
- build with Python3 bindings

* Wed Jul 04 2018 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.16.2-alt1
- New upstream release 1.16.2

* Fri Jun 08 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.16.1-alt7
- Rebuild with latest version on libldb-1.3.3
- Disable strict requirement to version of libldb

* Fri May 25 2018 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.16.1-alt6
- Applied patches fixing AD and generic issues from Fedora 1.16.2 pre-release
  (https://src.fedoraproject.org/rpms/sssd/tree/5f75f7e4f25f4844)
  + 0001-IPA-Handle-empty-nisDomainName.patch
  + 0002-intg-enhance-netgroups-test.patch
  + 0003-CONFDB-Start-a-ldb-transaction-from-sss_ldb_modify_p.patch
  + 0004-TOOLS-Take-into-consideration-app-domains.patch
  + 0005-TESTS-Move-get_call_output-to-util.py.patch
  + 0006-TESTS-Make-get_call_output-more-flexible-about-the-s.patch
  + 0007-TESTS-Add-a-basic-test-of-sssctl-domain-list.patch
  + 0008-KCM-Use-json_loadb-when-dealing-with-sss_iobuf-data.patch
  + 0009-KCM-Remove-mem_ctx-from-kcm_new_req.patch
  + 0010-KCM-Introduce-kcm_input_get_payload_len.patch
  + 0011-KCM-Do-not-use-2048-as-fixed-size-for-the-payload.patch
  + 0012-KCM-Adjust-REPLY_MAX-to-the-one-used-in-krb5.patch
  + 0014-KCM-Fix-typo-in-ccdb_sec_delete_list_done.patch
  + 0015-KCM-Only-print-the-number-of-found-items-after-we-ha.patch
  + 0016-SYSDB-When-marking-an-entry-as-expired-also-set-the-.patch
  + 0019-SERVER-Tone-down-shutdown-messages-for-socket-activa.patch
  + 0025-AD-Missing-header-in-ad_access.h.patch
  + 0026-GPO-Add-ad_options-to-ad_gpo_process_som_state.patch
  + 0027-GPO-Use-AD-site-override-if-set.patch
  + 0030-sssctl-Showing-help-even-when-sssd-not-configured.patch
  + 0031-sssctl-move-check-for-version-error-to-correct-place.patch
  + 0032-MAN-Add-sss-certmap-man-page-regarding-priority-proc.patch
  + 0033-SDAP-Improve-a-DEBUG-message-about-GC-detection.patch
  + 0034-MAN-Improve-docs-about-GC-detection.patch
  + 0035-nss-idmap-do-not-set-a-limit.patch
  + 0036-nss-idmap-use-right-group-list-pointer-after-sss_get.patch
  + 0037-NSS-Add-InvalidateGroupById-handler.patch
  + 0038-DP-Add-dp_sbus_invalidate_group_memcache.patch
  + 0039-ERRORS-Add-ERR_GID_DUPLICATED.patch
  + 0040-LDAP-Augment-the-sdap_opts-structure-with-a-data-pro.patch
  + 0041-SDAP-Add-sdap_handle_id_collision_for_incomplete_gro.patch
  + 0042-SDAP-Properly-handle-group-id-collision-when-renamin.patch
  + 0043-SYSDB_OPS-Error-out-on-id-collision-when-adding-an-i.patch
  + 0044-TESTS-Add-an-integration-test-for-renaming-incomplet.patch
  + 0045-SYSDB-sysdb_add_incomplete_group-now-returns-EEXIST-.patch
  + 0046-MAN-Document-which-principal-does-the-AD-provider-us.patch
  + 0047-GPO-Fix-bug-with-empty-GPO-rules.patch
  + 0057-AD-Warn-if-the-LDAP-schema-is-overriden-with-the-AD-.patch
  + 0058-SYSDB-Only-check-non-POSIX-groups-for-GID-conflicts.patch
  + 0060-CACHE_REQ-Do-not-fail-the-domain-locator-plugin-if-I.patch
  + 0061-NSS-nss_clear_netgroup_hash_table-do-not-free-data.patch
  + 0062-SYSDB-Properly-handle-name-gid-override-when-using-d.patch

* Fri Apr 20 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.16.1-alt5
- Set ownership of sssd.ldb even if local provider is not used

* Fri Apr 06 2018 Evgeny Sinelikov <sin@altlinux.org> 1.16.1-alt4
- Build for e2k without selinux-policy-targeted

* Tue Mar 27 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16.1-alt3
- libnfsidmap soname bump

* Sat Mar 24 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.16.1-alt2
- Revert libwbclient-sssd interface to version 0.14 for samba-4.7

* Mon Mar 12 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.16.1-alt1
- Update to latest stable release
- Revert libwbclient-sssd interface to version 0.13 for samba-4.6

* Fri Mar 02 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.15.3-alt7
- Rebuild with fixes from p8

* Tue Feb 27 2018 Alexey Shabalin <shaba@altlinux.ru> 1.15.3-alt6
- Rebuild with http-parser-2.8.0
- backport fix for building the PAC plugin with krb5 1.16

* Fri Dec 22 2017 Evgeny Sinelnikov <sin@altlinux.org> 1.15.3-alt5
- Fix logrotate insecure parent directory permissions (closes: 34335)
- Fix trouble with incomplete group object found during initgroups

* Thu Nov 23 2017 Evgeny Sinelnikov <sin@altlinux.org> 1.15.3-alt5
- Backport sssd to legacy stable branches
- Fix trouble with ubt macros id on branch c8

* Tue Nov 21 2017 Evgeny Sinelnikov <sin@altlinux.org> 1.15.3-alt5
- Backport sssd to stable branches

* Tue Nov 21 2017 Evgeny Sinelnikov <sin@altlinux.org> 1.15.3-alt5
- Don't restart sssd services until reboot or manual restart (ALT #34054)

* Fri Nov 03 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15.3-alt4
- relocate nfs-idmap plugin back under %%_libdir

* Thu Sep 21 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.3-alt3
- Avoid build another trouble with ubt macros id on branch c8

* Wed Sep 20 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.3-alt2
- Avoid build trouble with ubt macros id on branch c8

* Thu Aug 17 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.3-alt1
- Update to latest release with:
 + SSSD Kerberos credentials manager (sssd-kcm)
 + SSSD Certficate Mapping Library (libsss_certmap)

* Sat Jul 15 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.2-alt7
- Rebuild new version with latest fixes for p7 and c7

* Sat Jun 17 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.2-alt6
- Fix PAM config with pam_localuser.so

* Fri Jun 16 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.2-alt5
- Update PAM config with pam_localuser.so

* Fri Jun 09 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.2-alt4
- Add PAM auth config with pam_localuser.so

* Fri Apr 28 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.2-alt3
- Fix PAM config with pam_localuser.so for separate configuration for local and global users

* Fri Apr 07 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.2-alt2
- Rebuild with http-parser-2.7.1

* Thu Mar 23 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.2-alt1
- Updated to last spring release

* Wed Mar 08 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.14.2-alt6
- Rebuild with libldb-1.1.29

* Tue Feb 28 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.14.2-alt5
- Add _sssd user to _keytab group
- Set right group privileges: use initgroups() instead of setgroups()

* Thu Jan 12 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.14.2-alt4
- Set selinux provider none only if selinux disabled

* Sat Dec 31 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1.14.2-alt3
- Set default selinux provider to none

* Mon Dec 05 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1.14.2-alt2
- Set sssd.conf owner to root:root
  due it hardcoded in sss_ini_config_access_check()

* Mon Nov 07 2016 Alexey Shabalin <shaba@altlinux.ru> 1.14.2-alt1
- 1.14.2

* Tue Sep 13 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1.14.1-alt2
- Rebuild with libldb-1.1.27

* Tue Aug 30 2016 Alexey Shabalin <shaba@altlinux.ru> 1.14.1-alt1
- 1.14.1

* Fri Jul 08 2016 Alexey Shabalin <shaba@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Mon Apr 25 2016 Alexey Shabalin <shaba@altlinux.ru> 1.13.4-alt1
- 1.13.4

* Fri Mar 04 2016 Andrey Cherepanov <cas@altlinux.org> 1.13.3-alt1.2
- Rebuild with libldb-1.1.26

* Tue Jan 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.13.3-alt1.1
- Rebuild with libldb-1.1.25

* Mon Dec 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.13.3-alt1
- 1.13.3

* Thu Dec 17 2015 Andrey Cherepanov <cas@altlinux.org> 1.13.2-alt1.1
- Rebuild with libldb-1.1.24

* Wed Dec 09 2015 Alexey Shabalin <shaba@altlinux.ru> 1.13.2-alt1
- 1.13.2

* Mon Nov 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.13.1-alt0.2
- Rebuild with libldb-1.1.23

* Thu Sep 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.13.1-alt0.1
- upstram snapshot

* Mon Jul 20 2015 Alexey Shabalin <shaba@altlinux.ru> 1.13.0-alt1
- 1.13.0
- add alternatives for libwbclient
- add alternatives for cifs-idmap plugin
- use _sssd user for run services

* Mon Apr 20 2015 Alexey Shabalin <shaba@altlinux.ru> 1.12.4-alt2.git.bdb7e
- branch upstream/sssd-1-12 bdb7e7f514629696e73902b2af3a93839be3e8a4

* Mon Mar 23 2015 Alexey Shabalin <shaba@altlinux.ru> 1.12.4-alt1
- 1.12.4

* Mon Jan 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1.12.3-alt1
- 1.12.3

* Tue Dec 16 2014 Alexey Shabalin <shaba@altlinux.ru> 1.12.2-alt2
- rebuild with libldb-1.1.18

* Thu Nov 13 2014 Alexey Shabalin <shaba@altlinux.ru> 1.12.2-alt1
- 1.12.2

* Wed Sep 10 2014 Alexey Shabalin <shaba@altlinux.ru> 1.12.1-alt1
- 1.12.1
- add libwbclient package

* Mon Jul 28 2014 Alexey Shabalin <shaba@altlinux.ru> 1.12.0-alt1
- 1.12.0

* Wed Jun 04 2014 Alexey Shabalin <shaba@altlinux.ru> 1.11.6-alt1
- 1.11.6

* Thu May 15 2014 Alexey Shabalin <shaba@altlinux.ru> 1.11.5.1-alt2
- rebuild with new libldb

* Mon Apr 28 2014 Alexey Shabalin <shaba@altlinux.ru> 1.11.5.1-alt1
- 1.11.5.1

* Wed Mar 12 2014 Alexey Shabalin <shaba@altlinux.ru> 1.11.4-alt2
- add pam config files
- add libsasl2-plugin-gssapi to Requires for krb5-common

* Tue Feb 18 2014 Alexey Shabalin <shaba@altlinux.ru> 1.11.4-alt1
- 1.11.4

* Tue Feb 04 2014 Alexey Shabalin <shaba@altlinux.ru> 1.11.3-alt1
- initial build

%define libwbc_alternatives_version 0.13.0
%def_with kcm
%def_without python3_bindings

Name: sssd
Version: 1.15.3
Release: alt5%ubt
Group: System/Servers
Summary: System Security Services Daemon
License: GPLv3+
Url: http://fedorahosted.org/sssd/
Source: %name-%version.tar
Source2: %name.init
Source3: system-auth-sss.pam
Source4: system-auth-use_first_pass-sss.pam

Patch: %name-%version-alt.patch

# Determine the location of the LDB modules directory
%define ldb_modulesdir %(pkg-config --variable=modulesdir ldb)
%define ldb_version 1.1.29

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
%global secdbpath %sssdstatedir/secrets

%define sssd_user _sssd

Requires: %name-client = %version-%release
Requires: libsss_idmap = %version-%release
Requires: libldb = %ldb_version

# Avoid trouble with rpm-macros-ubt-0.2-alt1.M80C.2.noarch.rpm
# where %__ubt_branch_id N.M80C in /usr/lib/rpm/macros.d/ubt
#if %ubt_id == "M70C"
#Requires: libkrb5 > 1.13.7-alt1
#else
Requires: libkrb5 >= 1.14.4-alt2
#endif

BuildRequires(pre):rpm-build-ubt

### Build Dependencies ###
BuildRequires: /proc
BuildRequires: libpopt-devel
BuildRequires: libtalloc-devel
BuildRequires: libtevent-devel
BuildRequires: libtdb-devel >= 1.1.3
BuildRequires: libldb-devel = %ldb_version
BuildRequires: libdhash-devel >= 0.4.2
BuildRequires: libcollection-devel >= 0.5.1
BuildRequires: libini_config-devel >= 1.3.0
BuildRequires: libdbus-devel
BuildRequires: libldap-devel
BuildRequires: libpam-devel
BuildRequires: libnss-devel
BuildRequires: libnspr-devel
#BuildRequires: libssl-devel
BuildRequires: libpcre-devel >= 7
BuildRequires: libxslt
BuildRequires: libxml2-devel
BuildRequires: docbook-dtds docbook-style-xsl xsltproc xml-utils
BuildRequires: libkrb5-devel
BuildRequires: libcares-devel
BuildRequires: python-devel
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
BuildRequires: libsmbclient-devel
# Avoid trouble with rpm-macros-ubt-0.2-alt1.M80C.2.noarch.rpm
# where %__ubt_branch_id N.M80C in /usr/lib/rpm/macros.d/ubt
#if %ubt_id <= "M70P"
#BuildRequires: systemd-devel libsystemd-daemon-devel libsystemd-journal-devel libsystemd-login-devel
#else
BuildRequires: libsystemd-devel
#endif
BuildRequires: selinux-policy-targeted
BuildRequires: cifs-utils-devel
BuildRequires: libsasl2-devel
BuildRequires: libnfsidmap-devel >= 1:2.2.1-alt1
BuildRequires: libaugeas-devel
BuildRequires: libcmocka-devel >= 1.0.0
BuildRequires: nscd
BuildRequires: libjansson-devel
BuildRequires: libhttp-parser-devel
%if_with kcm
BuildRequires: libuuid-devel libcurl-devel
%endif

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
Requires: python-module-sssdconfig = %version-%release
Requires: python-module-sss = %version-%release

%description tools
Provides userspace tools for manipulating users, groups, and nested groups in
SSSD when using id_provider = local in /etc/sssd/sssd.conf.

Also provides several other administrative tools:
    * sss_debuglevel to change the debug level on the fly
    * sss_seed which pre-creates a user entry for use in kickstarts
    * sss_obfuscate for generating an obfuscated LDAP password

%package -n python-module-sssdconfig
Summary: SSSD and IPA configuration file manipulation classes and functions
Group: Development/Python
License: GPLv3+
BuildArch: noarch

%description -n python-module-sssdconfig
Provides python files for manipulation SSSD and IPA configuration files.

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

%package -n python-module-ipa_hbac
Summary: Python bindings for the FreeIPA HBAC Evaluator library
Group: Development/Python
License: LGPLv3+
Requires: libipa_hbac = %version-%release

%description -n python-module-ipa_hbac
The python-module-libipa_hbac contains the bindings so that libipa_hbac can be
used by Python applications.

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

%package -n python-module-sss_nss_idmap
Summary: Python bindings for libsss_nss_idmap
Group: Development/Python
License: LGPLv3+
Requires: libsss_nss_idmap = %version-%release

%description -n python-module-sss_nss_idmap
The python-module-libsss_nss_idmap contains the bindings so that libsss_nss_idmap can
be used by Python applications.

%package -n python-module-sss
Summary: Python bindings for sss
Group: Development/Python
License: LGPLv3+
Requires: %name = %version-%release

%description -n python-module-sss
The python-module-sss contains the bindings so that sss can
be used by Python applications.

%package -n python-module-sss-murmur
Summary: Python bindings for murmur hash function
Group: Development/Python
License: LGPLv3+

%description -n python-module-sss-murmur
Provides python module for calculating the murmur hash version 3

%package -n libwbclient-%name
Summary: The SSSD libwbclient implementation
Group: System/Libraries
License: GPLv3+ and LGPLv3+
Conflicts: libwbclient < 4.2.3-alt1

%description -n libwbclient-%name
The SSSD libwbclient implementation.

%package -n libwbclient-%name-devel
Summary: Development libraries for the SSSD libwbclient implementation
Group: Development/C
License: GPLv3+ and LGPLv3+
Requires: libwbclient-%name = %version-%release

%description -n libwbclient-%name-devel
Development libraries for the SSSD libwbclient implementation.

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
    --enable-ldb-version-check \
    --with-syslog=journald \
    --with-test-dir=/dev/shm \
    --enable-krb5-locator-plugin \
    --enable-pac-responder \
    --enable-sss-default-nss-plugin \
    --with-sssd-user=%sssd_user \
    --disable-rpath \
    --disable-static \
    %{subst_with kcm} \
%if_without python3_bindings
    --without-python3-bindings \
%endif
    #

# %%make_build all docs
%make all docs

%install
%make install DESTDIR=%buildroot

if [ ! -f %buildroot%_libdir/%name/modules/libwbclient.so.%libwbc_alternatives_version]
    then
	echo "Expected libwbclient version not found, please check if version has changed."
	exit -1
fi

%find_lang sssd

# Prepare empty config file
install -D -m640 src/examples/sssd-example.conf %buildroot%_sysconfdir/%name/%name.conf

# Copy default logrotate file
install -D -m644 src/examples/logrotate %buildroot%_sysconfdir/logrotate.d/%name

touch %buildroot%mcpath/passwd
touch %buildroot%mcpath/group
touch %buildroot%mcpath/initgroups

install -D -m755 %SOURCE2 %buildroot%_initdir/%name
install -D -m644 %SOURCE3 %buildroot%_pamdir/system-auth-sss
install -D -m644 %SOURCE4 %buildroot%_pamdir/system-auth-use_first_pass-sss

# Remove .la files created by libtool
find %buildroot -name "*.la" -exec rm -f {} \;

# Suppress developer-only documentation
rm -Rf %buildroot%_docdir/%name

mkdir -p %buildroot%pubconfpath/krb5.include.d

# Add alternatives for libwbclient
mkdir -p %buildroot%_altdir
printf '%_libdir/libwbclient.so.%libwbc_alternatives_version\t%_libdir/%name/modules/libwbclient.so.%libwbc_alternatives_version\t20\n' > %buildroot%_altdir/libwbclient-sss
printf '%_libdir/libwbclient.so.0\t%_libdir/%name/modules/libwbclient.so.0\t20\n' >> %buildroot%_altdir/libwbclient-sss

printf '%_libdir/libwbclient.so\t%_libdir/%name/modules/libwbclient.so\t20\n' >> %buildroot%_altdir/libwbclient-sss-devel

ln -s ../..%_libdir/%name/modules/libwbclient.so.%libwbc_alternatives_version %buildroot%_libdir/
ln -s ../..%_libdir/%name/modules/libwbclient.so.0 %buildroot%_libdir/
ln -s ../..%_libdir/%name/modules/libwbclient.so %buildroot%_libdir/

# Add alternatives for idmap-plugin
mkdir -p %buildroot/%_altdir
printf '%_libdir/cifs-utils/idmap-plugin\t%_libdir/cifs-utils/cifs_idmap_sss.so\t20\n' > %buildroot%_altdir/cifs-idmap-plugin-sss


%check
export CK_TIMEOUT_MULTIPLIER=10
%make check VERBOSE=yes ||:
unset CK_TIMEOUT_MULTIPLIER

%pre
%_sbindir/groupadd -r -f %sssd_user 2> /dev/null ||:
%_sbindir/useradd -r -n -g %sssd_user -G _keytab -d %sssdstatedir -s /dev/null -c "User for sssd" %sssd_user 2> /dev/null ||:

%post
# Sinse 0.13.0 we are run sssd as non-root user. Migrate files owner.
#chown %sssd_user:%sssd_user %dbpath/cache* %dbpath/ccache* %dbpath/config.ldb
#chown %sssd_user:%sssd_user %mcpath/*
#chown %sssd_user:%sssd_user %pubconfpath/kdcinfo* %pubconfpath/kpasswdinfo*
#chown %sssd_user:%sssd_user  %_logdir/%name/sssd_*
chown root:root %_sysconfdir/sssd/sssd.conf

# Don't restart sssd services until reboot or manual restart
#post_service %name
#post_service sssd-secrets
#
#preun
#preun_service %name
#preun_service sssd-secrets

%triggerpostun -- %name < 1.14.2-alt5
%_bindir/gpasswd -a %sssd_user _keytab

%files -f sssd.lang
%doc COPYING
%doc src/examples/sssd-example.conf
%_sbindir/%name
%_initdir/%name
%_unitdir/%name.service
%_unitdir/sssd-secrets.socket
%_unitdir/sssd-secrets.service
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
%_libexecdir/%name/sssd_secrets
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
%attr(700,root,root) %dir %secdbpath
%ghost %attr(0644,%sssd_user,%sssd_user) %verify(not md5 size mtime) %mcpath/passwd
%ghost %attr(0644,%sssd_user,%sssd_user) %verify(not md5 size mtime) %mcpath/group
%ghost %attr(0644,%sssd_user,%sssd_user) %verify(not md5 size mtime) %mcpath/initgroups
%attr(755,%sssd_user,%sssd_user) %dir %pipepath
%attr(750,%sssd_user,root) %dir %pipepath/private
%attr(755,%sssd_user,%sssd_user) %dir %gpocachepath
%attr(755,%sssd_user,%sssd_user) %dir %pubconfpath
%attr(770,root,%sssd_user) %dir %_logdir/%name
%attr(750,root,%sssd_user) %dir %_sysconfdir/sssd
%attr(750,root,%sssd_user) %dir %_sysconfdir/sssd/conf.d
%attr(0600,root,root) %config(noreplace) %_sysconfdir/sssd/sssd.conf
%dir %_sysconfdir/systemd/system/sssd.service.d
%config(noreplace) %_sysconfdir/systemd/system/sssd.service.d/journal.conf
%config(noreplace) %_sysconfdir/logrotate.d/sssd
%dir %_datadir/%name
%_sysconfdir/pam.d/sssd-shadowutils
%dir %_libdir/%name/conf
%_libdir/%name/conf/sssd.conf

%_datadir/%name/cfg_rules.ini
%_datadir/%name/sssd.api.conf
%dir %_datadir/%name/sssd.api.d
%_datadir/%name/sssd.api.d/sssd-local.conf
%_datadir/%name/sssd.api.d/sssd-simple.conf
%_man1dir/sss_ssh_*
%_man5dir/sssd.conf.5*
%_man5dir/sssd-files.5*
%_man5dir/sssd-simple.5*
%_man5dir/sssd-sudo.5*
%_man5dir/sssd-secrets.5*
%_man5dir/sss_rpcidmapd.5*
%_man8dir/sssd.8*
%_man8dir/sss_cache.8*

%files -n python-module-sss
%python_sitelibdir/pysss.so

%if_with python3_bindings
%files -n python3-module-sss
%python3_sitelibdir/pysss.so
%endif

%files -n python-module-sss-murmur
%python_sitelibdir/pysss_murmur.so

%files ldap
%_libdir/%name/libsss_ldap.so
%_man5dir/sssd-ldap*
%_datadir/%name/sssd.api.d/sssd-ldap.conf

%files krb5-common
%attr(755,%sssd_user,%sssd_user) %dir %pubconfpath/krb5.include.d
%attr(4710,root,%sssd_user) %_libexecdir/%name/ldap_child
%attr(4710,root,%sssd_user) %_libexecdir/%name/krb5_child

%files krb5
%_libdir/%name/libsss_krb5.so
%_man5dir/sssd-krb5*
%_datadir/%name/sssd.api.d/sssd-krb5.conf

%files pac
%_libexecdir/%name/sssd_pac
%_unitdir/sssd-pac.service
%_unitdir/sssd-pac.socket

%files ipa
%attr(700,%sssd_user,%sssd_user) %dir %keytabdir
%_libdir/%name/libsss_ipa.so
%attr(4710,root,%sssd_user) %_libexecdir/%name/selinux_child
%_man5dir/sssd-ipa*
%_datadir/%name/sssd.api.d/sssd-ipa.conf

%files ad
%_libdir/%name/libsss_ad.so
%_libexecdir/%name/gpo_child
%_man5dir/sssd-ad*
%_datadir/%name/sssd.api.d/sssd-ad.conf

%files proxy
%attr(4710,root,%sssd_user) %_libexecdir/%name/proxy_child
%_libdir/%name/libsss_proxy.so
%_datadir/%name/sssd.api.d/sssd-proxy.conf

%files client
%config(noreplace) %_pamdir/*-sss
/%_lib/libnss_sss.so.2
/%_lib/security/pam_sss.so
%_libdir/krb5/plugins/libkrb5/sssd_krb5_locator_plugin.so
%_libdir/krb5/plugins/authdata/sssd_pac_plugin.so
%_libdir/cifs-utils/cifs_idmap_sss.so
%_altdir/cifs-idmap-plugin-sss
%_libdir/%name/modules/sssd_krb5_localauth_plugin.so
%_man8dir/pam_sss*
%_man8dir/sssd_krb5_locator_plugin*

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
%_man8dir/sss_*
%_man8dir/sssctl*
%exclude %_sbindir/sss_cache
%exclude %_man8dir/sss_cache*

%files -n python-module-sssdconfig
%dir %python_sitelibdir_noarch/SSSDConfig
%python_sitelibdir_noarch/SSSDConfig*.egg-info
%python_sitelibdir_noarch/SSSDConfig/*.py

%if_with python3_bindings
%files -n python3-sssdconfig
%dir %python3_sitelibdir_noarch/SSSDConfig
%python3_sitelibdir_noarch/SSSDConfig/*.py*
%dir %python3_sitelibdir_noarch/SSSDConfig/__pycache__
%python3_sitelibdir_noarch/SSSDConfig/__pycache__/*.py*
%endif

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

%files -n python-module-ipa_hbac
%python_sitelibdir/pyhbac.so

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
%endif

%files -n libsss_simpleifp
%_libdir/libsss_simpleifp.so.*

%files -n libsss_simpleifp-devel
%_includedir/sss_sifp.h
%_includedir/sss_sifp_dbus.h
%_libdir/libsss_simpleifp.so
%_pkgconfigdir/sss_simpleifp.pc

%files -n python-module-sss_nss_idmap
%python_sitelibdir/pysss_nss_idmap.so

%files -n libwbclient-%name
%_libdir/%name/modules/libwbclient.so.*
%ghost %_libdir/libwbclient.so.0
%ghost %_libdir/libwbclient.so.%libwbc_alternatives_version
%_altdir/libwbclient-sss

%files -n libwbclient-%name-devel
%_includedir/wbclient_sssd.h
%_libdir/%name/modules/libwbclient.so
%ghost %_libdir/libwbclient.so
%_pkgconfigdir/wbclient_sssd.pc
%_altdir/libwbclient-sss-devel

%files winbind-idmap
%_libdir/samba/idmap/sss.so
%_man8dir/idmap_sss*

%files nfs-idmap
%_libdir/libnfsidmap/sss.so

%changelog
* Tue Nov 21 2017 Evgeny Sinelnikov <sin@altlinux.org> 1.15.3-alt5%ubt
- Don't restart sssd services until reboot or manual restart (ALT #34054)

* Fri Nov 03 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15.3-alt4%ubt
- relocate nfs-idmap plugin back under %%_libdir

* Thu Sep 21 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.3-alt3%ubt
- Avoid build another trouble with ubt macros id on branch c8

* Wed Sep 20 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.3-alt2%ubt
- Avoid build trouble with ubt macros id on branch c8

* Thu Aug 17 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.3-alt1%ubt
- Update to latest release with:
 + SSSD Kerberos credentials manager (sssd-kcm)
 + SSSD Certficate Mapping Library (libsss_certmap)

* Sat Jul 15 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.2-alt7%ubt
- Rebuild new version with latest fixes for p7 and c7

* Sat Jun 17 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.2-alt6%ubt
- Fix PAM config with pam_localuser.so

* Fri Jun 16 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.2-alt5%ubt
- Update PAM config with pam_localuser.so

* Fri Jun 09 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.2-alt4%ubt
- Add PAM auth config with pam_localuser.so

* Fri Apr 28 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.2-alt3%ubt
- Fix PAM config with pam_localuser.so for separate configuration for local and global users

* Fri Apr 07 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.2-alt2%ubt
- Rebuild with http-parser-2.7.1

* Thu Mar 23 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.2-alt1%ubt
- Updated to last spring release

* Wed Mar 08 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.14.2-alt6%ubt
- Rebuild with libldb-1.1.29

* Tue Feb 28 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.14.2-alt5%ubt
- Add _sssd user to _keytab group
- Set right group privileges: use initgroups() instead of setgroups()

* Thu Jan 12 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.14.2-alt4%ubt
- Set selinux provider none only if selinux disabled

* Sat Dec 31 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1.14.2-alt3%ubt
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

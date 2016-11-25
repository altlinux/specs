%define plugin_dir %_libdir/dirsrv/plugins
%define POLICYCOREUTILSVER 2.1.12
%define _localstatedir %_var
%define _libexecdir /usr/libexec
%define etc_systemd_dir %_sysconfdir/systemd/system

%define _unpackaged_files_terminate_build 1

Name: freeipa
Version: 4.3.2
Release: alt3
Summary: The Identity, Policy and Audit system

Group: System/Base
License: GPLv3+
Url: http://www.freeipa.org/
Source: %name-%version.tar
Source1: nss.conf
Patch: %name-%version-%release.patch

BuildRequires: 389-ds-devel >= 1.3.1.3
BuildRequires: libsvrcore-devel
BuildRequires: policycoreutils >= %POLICYCOREUTILSVER
BuildRequires: systemd-devel
BuildRequires: samba-devel >= 4.0.5
BuildRequires: python-module-samba
BuildRequires: libwbclient-devel
BuildRequires: libtalloc-devel
BuildRequires: libtevent-devel
BuildRequires: libnspr-devel
BuildRequires: libnss-devel
BuildRequires: libssl-devel
BuildRequires: libldap-devel
BuildRequires: libkrb5-devel >= 1.11
BuildRequires: libuuid-devel
BuildRequires: libcurl-devel >= 7.21.7-2
BuildRequires: libxmlrpc-devel >= 1.27.4
BuildRequires: libpopt-devel
BuildRequires: gettext
BuildRequires: python-devel
BuildRequires: python-module-ldap
BuildRequires: python-module-setuptools
BuildRequires: python-module-krbV
BuildRequires: python-module-nss
BuildRequires: python-module-netaddr
BuildRequires: python-module-kerberos
BuildRequires: python-module-cryptography >= 0.9
BuildRequires: python-module-OpenSSL
BuildRequires: pylint
BuildRequires: python-module-polib
BuildRequires: python-module-ipa_hbac
BuildRequires: python-module-memcached
BuildRequires: sssd >= 1.9.2
BuildRequires: python-module-lxml
BuildRequires: python-module-pyasn1 >= 0.0.9a
BuildRequires: python-module-dns
BuildRequires: python-module-lesscpy
BuildRequires: python-module-cffi
BuildRequires: python-module-six
BuildRequires: python-module-gssapi
BuildRequires: libsss_idmap-devel
BuildRequires: libsss_nss_idmap-devel
BuildRequires: java-1.8.0-openjdk
BuildRequires: libverto-devel
BuildRequires: systemd
BuildRequires: libunistring-devel
BuildRequires: libsasl2-devel
BuildRequires: rpm-macros-webserver-common
BuildRequires: libini_config-devel

BuildRequires: rhino

%description
IPA is an integrated solution to provide centrally managed Identity
(machine, user, virtual machines, groups, authentication credentials),
Policy (configuration settings, access control information) and Audit
(events, logs, analysis thereof).

%package server
Summary: The IPA authentication server
Group: System/Base
Requires: %name-server-common = %version-%release
Requires: python-module-ipaserver = %version-%release
Requires: python-module-%name = %version-%release
Requires: %name-client = %version-%release
Requires: %name-admintools = %version-%release
Requires: krb5-kinit
Requires: ntpd
Requires: certmonger
Requires: pki-server
Requires: pki-ca
Requires: java-1.8.0-openjdk
Requires: apache2-mod_nss
Requires: apache2-mod_auth_gssapi
Requires: apache2-mod_wsgi
Requires: krb5-kdc
Requires: 389-ds-base
Requires: sssd-krb5
Requires: sssd-ipa
Requires: memcached
Requires: python-module-kdcproxy
Requires: oddjob

%description server
IPA is an integrated solution to provide centrally managed Identity
(machine, user, virtual machines, groups, authentication credentials),
Policy (configuration settings, access control information) and Audit
(events, logs, analysis thereof).
If you are installing an IPA server you need to install this package
(in other words, most people should NOT install this package).

%package -n python-module-ipaserver
Summary: Python libraries used by IPA server
Group: Development/Python
BuildArch: noarch
Requires: %name-server-common = %version-%release
Requires: %name-common = %version-%release
Requires: python-module-ipaclient = %version-%release

%description -n python-module-ipaserver
IPA is an integrated solution to provide centrally managed Identity
(users, hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution
provides features for further integration with Linux based clients
(SUDO, automount) and integration with Active Directory based
infrastructures (Trusts).
If you are installing an IPA server, you need to install this package.

%package server-common
Summary: Common files used by IPA server
Group: System/Base
BuildArch: noarch
Requires: %name-client-common = %version-%release
Requires: apache2-base webserver-common
Requires: custodia

%description server-common
IPA is an integrated solution to provide centrally managed Identity
(users, hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution
provides features for further integration with Linux based clients
(SUDO, automount) and integration with Active Directory based
infrastructures (Trusts).
If you are installing an IPA server, you need to install this package.

%package server-dns
Summary: IPA integrated DNS server with support for automatic DNSSEC signing
Group: System/Base
BuildArch: noarch
Requires: %name-server = %version-%release
#Requires: bind-dyndb-ldap
Requires: bind
Requires: bind-utils
#Requires: bind-pkcs11
#Requires: bind-pkcs11-utils
Requires: opendnssec

%description server-dns
IPA integrated DNS server with support for automatic DNSSEC signing.
Integrated DNS server is BIND 9. OpenDNSSEC provides key management.

%package server-trust-ad
Summary: Virtual package to install packages required for Active Directory trusts
Group: System/Base
Requires: %name-server = %version-%release

%description server-trust-ad
Cross-realm trusts with Active Directory in IPA require working Samba 4
installation. This package is provided for convenience to install all
required dependencies at once.

%package client
Summary: IPA authentication for use on clients
Group: System/Base
Requires: %name-client-common = %version-%release
Requires: python-module-%name = %version-%release
Requires: python-module-ipaclient = %version-%release
Requires: oddjob-mkhomedir

%description client
IPA is an integrated solution to provide centrally managed Identity
(machine, user, virtual machines, groups, authentication credentials),
Policy (configuration settings, access control information) and Audit
(events, logs, analysis thereof).
If your network uses IPA for authentication, this package should be
installed on every client machine.

%package -n python-module-ipaclient
Summary: Python module for IPA client
Group: Development/Python
BuildArch: noarch

%description -n python-module-ipaclient
IPA is an integrated solution to provide centrally managed Identity
(users, hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution
provides features for further integration with Linux based clients
(SUDO, automount) and integration with Active Directory based
infrastructures (Trusts).
If your network uses IPA for authentication, this package should be
installed on every client machine.

%package client-common
Summary: Common files used by IPA client
Group: System/Base
BuildArch: noarch
Requires: %name-common = %version-%release

%description client-common
IPA is an integrated solution to provide centrally managed Identity
(users, hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution
provides features for further integration with Linux based clients
(SUDO, automount) and integration with Active Directory based
infrastructures (Trusts).
If your network uses IPA for authentication, this package should be
installed on every client machine.

%package admintools
Summary: IPA administrative tools
Group: System/Base
BuildArch: noarch
Requires: python-module-%name = %version-%release
Requires: %name-client-common = %version-%release

%description admintools
IPA is an integrated solution to provide centrally managed Identity
(machine, user, virtual machines, groups, authentication credentials),
Policy (configuration settings, access control information) and Audit
(events, logs, analysis thereof).
This package provides command-line tools for IPA administrators.

%package -n python-module-freeipa
Summary: Python libraries used by IPA
Group: Development/Python
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: gnupg
Requires: keyutils
Requires: curl
# Drop %%python_sitelibdir_noarch from requires.
# Otherwise it will be removed by the dependency optimizator
# on i586, but not on x86_64 and noarch check will fail.
%filter_from_requires /^\/usr\/lib\/python[[:digit:].]\+\/site-packages$/d

%description -n python-module-freeipa
IPA is an integrated solution to provide centrally managed Identity (machine,
user, virtual machines, groups, authentication credentials), Policy
(configuration settings, access control information) and Audit (events,
logs, analysis thereof). If you are using IPA you need to install this
package.

%package common
Summary: Common files used by IPA
Group: System/Base
BuildArch: noarch


%description common
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are using IPA, you need to install this package.

%package tests
Summary: IPA tests and test tools
Group: System/Base
Requires: %name-client-common = %version-%release
Requires: python-module-%name = %version-%release
BuildArch: noarch

%description tests
IPA is an integrated solution to provide centrally managed Identity (machine,
user, virtual machines, groups, authentication credentials), Policy
(configuration settings, access control information) and Audit (events,
logs, analysis thereof).
This package contains tests that verify IPA functionality.

%prep
%setup -n freeipa-%version
%patch -p1

%build
export CFLAGS="$CFLAGS %optflags -I/usr/include/krb5"
export CPPFLAGS="$CPPFLAGS %optflags -I/usr/include/krb5"
export SUPPORTED_PLATFORM=altlinux
# Force re-generate of platform support
rm -f ipapython/services.py
%make SKIP_API_VERSION_CHECK="yes" PYTHON="python" version-update
# cd ipa-client; ../autogen.sh --prefix=%_usr --sysconfdir=%_sysconfdir --localstatedir=%_localstatedir --libdir=%_libdir --mandir=%_mandir; cd ..
pushd client
	%autoreconf
	%configure
popd
#cd daemons; ../autogen.sh --prefix=%_usr --sysconfdir=%_sysconfdir --localstatedir=%_localstatedir --libdir=%_libdir --mandir=%_mandir --with-openldap; cd ..
pushd daemons
	%autoreconf
	%configure --with-openldap
popd
#cd install; ../autogen.sh --prefix=%_usr --sysconfdir=%_sysconfdir --localstatedir=%_localstatedir --libdir=%_libdir --mandir=%_mandir; cd ..
pushd install
	%autoreconf
	%configure
popd

%make_build IPA_VERSION_IS_GIT_SNAPSHOT=no SKIP_API_VERSION_CHECK="yes" PYTHON="python" all

%install
export SUPPORTED_PLATFORM=altlinux
# Force re-generate of platform support
rm -f ipapython/services.py
%makeinstall_std SKIP_API_VERSION_CHECK="yes" PYTHON="python"
install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/httpd2/conf/extra-available/ipa-nss.conf
%find_lang ipa

# [ "/usr/lib/python2.7/site-packages" != "%python_sitelibdir" ] && mv %buildroot/usr/lib/python2.7/site-packages/* %buildroot/%python_sitelibdir/

rm -f %buildroot/%plugin_dir/*.la
rm -f %buildroot%_libdir/krb5/plugins/kdb/ipadb.la
rm -f %buildroot%_libdir/samba/pdb/ipasam.la

# Some user-modifiable HTML files are provided. Move these to /etc
# and link back.
mkdir -p %buildroot/%_sysconfdir/ipa/html
mkdir %buildroot%_datadir/ipa/html/
ln -s ../../../..%_sysconfdir/ipa/html/ffconfig.js \
    %buildroot%_datadir/ipa/html/ffconfig.js
ln -s ../../../..%_sysconfdir/ipa/html/ffconfig_page.js \
    %buildroot%_datadir/ipa/html/ffconfig_page.js
ln -s ../../../..%_sysconfdir/ipa/html/ssbrowser.html \
    %buildroot%_datadir/ipa/html/ssbrowser.html
ln -s ../../../..%_sysconfdir/ipa/html/unauthorized.html \
    %buildroot%_datadir/ipa/html/unauthorized.html
ln -s ../../../..%_sysconfdir/ipa/html/browserconfig.html \
    %buildroot%_datadir/ipa/html/browserconfig.html

# So we can own our Apache configuration
mkdir -p %buildroot%_sysconfdir/httpd2/conf/{sites-available,extra-available}
touch %buildroot%_sysconfdir/httpd2/conf/sites-available/ipa.conf
touch %buildroot%_sysconfdir/httpd2/conf/ipa-kdc-proxy.conf
touch %buildroot%_sysconfdir/httpd2/conf/ipa-pki-proxy.conf
touch %buildroot%_sysconfdir/httpd2/conf/ipa-rewrite.conf
mkdir -p %buildroot%_datadir/ipa/html/
touch %buildroot%_datadir/ipa/html/ca.crt
touch %buildroot%_datadir/ipa/html/configure.jar
touch %buildroot%_datadir/ipa/html/kerberosauth.xpi
touch %buildroot%_datadir/ipa/html/krb.con
touch %buildroot%_datadir/ipa/html/krb.js
touch %buildroot%_datadir/ipa/html/krb5.ini
touch %buildroot%_datadir/ipa/html/krbrealm.con
touch %buildroot%_datadir/ipa/html/preferences.html
mkdir -p %buildroot%_initdir
mkdir %buildroot%_sysconfdir/sysconfig/
install -m 644 init/ipa_memcached.conf %buildroot%_sysconfdir/sysconfig/ipa_memcached
install -m 644 init/ipa-dnskeysyncd.conf %buildroot%_sysconfdir/sysconfig/ipa-dnskeysyncd
install -m 644 init/ipa-ods-exporter.conf %buildroot%_sysconfdir/sysconfig/ipa-ods-exporter
install -m 644 daemons/dnssec/ipa-ods-exporter.socket %buildroot%_unitdir/ipa-ods-exporter.socket
install -m 644 daemons/dnssec/ipa-ods-exporter.service %buildroot%_unitdir/ipa-ods-exporter.service
install -m 644 daemons/dnssec/ipa-dnskeysyncd.service %buildroot%_unitdir/ipa-dnskeysyncd.service

# dnssec daemons
mkdir -p %buildroot/usr/libexec/ipa/
install daemons/dnssec/ipa-dnskeysyncd %buildroot%_libexecdir/ipa/ipa-dnskeysyncd
install daemons/dnssec/ipa-dnskeysync-replica %buildroot%_libexecdir/ipa/ipa-dnskeysync-replica
install daemons/dnssec/ipa-ods-exporter %buildroot%_libexecdir/ipa/ipa-ods-exporter

# Web UI plugin dir
mkdir -p %buildroot%_datadir/ipa/ui/js/plugins

# DNSSEC config
mkdir -p %buildroot%_sysconfdir/ipa/dnssec

# KDC proxy config (Apache config sets KDCPROXY_CONFIG to load this file)
mkdir -p %buildroot%_sysconfdir/ipa/kdcproxy/
mkdir -p %buildroot%_sharedstatedir/kdcproxy/
install -m 644 install/share/kdcproxy.conf %buildroot%_sysconfdir/ipa/kdcproxy/kdcproxy.conf
touch %buildroot%_sysconfdir/ipa/kdcproxy/ipa-kdc-proxy.conf

# NOTE: systemd specific section
mkdir -p %buildroot/lib/tmpfiles.d
install -m 0644 init/systemd/ipa.conf.tmpfiles %buildroot/lib/tmpfiles.d/%name.conf
# END

mkdir -p %buildroot%_runtimedir
install -d -m 0700 %buildroot%_runtimedir/ipa_memcached/
install -d -m 0700 %buildroot%_runtimedir/ipa/
install -d -m 0700 %buildroot%_runtimedir/httpd2/ipa
install -d -m 0700 %buildroot%_runtimedir/httpd2/ipa/clientcaches
install -d -m 0700 %buildroot%_runtimedir/run/httpd2/ipa/krbcache

#mkdir -p %{buildroot}%{_libdir}/krb5/plugins/libkrb5
#touch %{buildroot}%{_libdir}/krb5/plugins/libkrb5/winbind_krb5_locator.so

# NOTE: systemd specific section
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%etc_systemd_dir
install -m 644 init/systemd/ipa.service %buildroot%_unitdir/ipa.service
install -m 644 init/systemd/ipa_memcached.service %buildroot%_unitdir/ipa_memcached.service
install -m 644 init/systemd/httpd.service %buildroot%etc_systemd_dir/httpd2.service
install -m 644 init/systemd/ipa-custodia.service %buildroot%_unitdir/ipa-custodia.service
# END
mkdir -p %buildroot%_localstatedir/lib/ipa/backup


touch %buildroot%_sysconfdir/ipa/default.conf
touch %buildroot%_sysconfdir/ipa/ca.crt
mkdir -p %buildroot%_sysconfdir/ipa/nssdb
touch %buildroot%_sysconfdir/ipa/nssdb/cert8.db
touch %buildroot%_sysconfdir/ipa/nssdb/key3.db
touch %buildroot%_sysconfdir/ipa/nssdb/secmod.db
touch %buildroot%_sysconfdir/ipa/nssdb/pwdfile.txt
mkdir -p %buildroot%_localstatedir/lib/ipa-client/sysrestore

mkdir -p %buildroot%_sysconfdir/bash_completion.d
install -pm 644 contrib/completion/ipa.bash_completion %buildroot%_sysconfdir/bash_completion.d/ipa
mkdir -p %buildroot%_sysconfdir/cron.d

mkdir -p %buildroot%_sysconfdir/ipa/custodia

mkdir -p %buildroot%_localstatedir/lib/ipa/pki-ca
touch %buildroot%_localstatedir/lib/ipa/pki-ca/publish

mkdir -p %buildroot%_sysconfdir/pki/ca-trust/source/
touch %buildroot%_sysconfdir/pki/ca-trust/source/ipa.p11-kit

%files server
%doc COPYING README Contributors.txt
%_sbindir/*

%exclude %_sbindir/ipa-adtrust-install
%exclude %_sbindir/ipa-client-*
%exclude %_sbindir/ipa-*keytab
%exclude %_sbindir/ipa-join
%exclude %_sbindir/ipa-certupdate
%exclude %_sbindir/ipa-dns-install

%_libexecdir/certmonger/dogtag-ipa-ca-renew-agent-submit
%_libexecdir/certmonger/ipa-server-guard
%_libexecdir/ipa-otpd
%dir %_libexecdir/ipa/
%_libexecdir/ipa/ipa-dnskeysyncd
%_libexecdir/ipa/ipa-dnskeysync-replica
%_libexecdir/ipa/ipa-ods-exporter
%_libexecdir/ipa/ipa-httpd-kdcproxy
%dir %_libexecdir/ipa/oddjob/

%_libexecdir/ipa/oddjob/org.freeipa.server.conncheck
%_sysconfdir/dbus-1/system.d/org.freeipa.server.conf
%_sysconfdir/oddjobd.conf.d/ipa-server.conf
%_libexecdir/ipa/certmonger/
# NOTE: systemd specific section
%attr(644,root,root) %_unitdir/ipa.service
%attr(644,root,root) %_unitdir/ipa-otpd.socket
%attr(644,root,root) %_unitdir/ipa-otpd@.service
%attr(644,root,root) %_unitdir/ipa-dnskeysyncd.service
%attr(644,root,root) %_unitdir/ipa-ods-exporter.socket
%attr(644,root,root) %_unitdir/ipa-ods-exporter.service
# END

%plugin_dir/*.so

%_libdir/krb5/plugins/kdb/ipadb.so
%_man1dir/ipa-replica-conncheck.1.*
%_man1dir/ipa-replica-install.1.*
%_man1dir/ipa-replica-manage.1.*
%_man1dir/ipa-csreplica-manage.1.*
%_man1dir/ipa-replica-prepare.1.*
%_man1dir/ipa-server-certinstall.1.*
%_man1dir/ipa-server-install.1.*
%_man1dir/ipa-server-upgrade.1.*
%_man1dir/ipa-ca-install.1.*
%_man1dir/ipa-kra-install.1.*
%_man1dir/ipa-compat-manage.1.*
%_man1dir/ipa-nis-manage.1.*
%_man1dir/ipa-managed-entries.1.*
%_man1dir/ipa-ldap-updater.1.*
%_man8dir/ipactl.8.*
%_man8dir/ipa-upgradeconfig.8.*
%_man1dir/ipa-backup.1.*
%_man1dir/ipa-restore.1.*
%_man1dir/ipa-advise.1.*
%_man1dir/ipa-otptoken-import.1.*
%_man1dir/ipa-cacert-manage.1.*
%_man1dir/ipa-winsync-migrate.1.*

%files -n python-module-ipaserver
%python_sitelibdir_noarch/freeipa-*.egg-info
%python_sitelibdir_noarch/ipaserver

%files server-common
%ghost %verify(not user group) %dir %_sharedstatedir/kdcproxy
%dir %attr(0755,root,root) %_sysconfdir/ipa/kdcproxy
%config(noreplace) %_sysconfdir/sysconfig/ipa_memcached
%config(noreplace) %_sysconfdir/sysconfig/ipa-dnskeysyncd
%config(noreplace) %_sysconfdir/sysconfig/ipa-ods-exporter
%config(noreplace) %_sysconfdir/ipa/kdcproxy/kdcproxy.conf
%dir %attr(0770,root,%webserver_group) %_runtimedir/ipa_memcached
%dir %attr(0700,root,root) %_runtimedir/ipa
%attr(0700,apache2,apache2) %_runtimedir/httpd2/ipa/
# NOTE: systemd specific section
%_tmpfilesdir/%name.conf
%attr(644,root,root) %_unitdir/ipa_memcached.service
%attr(644,root,root) %_unitdir/ipa-custodia.service
%attr(644,root,root) %etc_systemd_dir/httpd2.service
# END
%_datadir/ipa/*
%exclude %_datadir/ipa/smb.conf.empty
%ghost %attr(0644,root,%webserver_group) %config(noreplace) %_datadir/ipa/html/ca.crt
%ghost %attr(0644,root,%webserver_group) %_datadir/ipa/html/configure.jar
%ghost %attr(0644,root,%webserver_group) %_datadir/ipa/html/kerberosauth.xpi
%ghost %attr(0644,root,%webserver_group) %_datadir/ipa/html/krb.con
%ghost %attr(0644,root,%webserver_group) %_datadir/ipa/html/krb.js
%ghost %attr(0644,root,%webserver_group) %_datadir/ipa/html/krb5.ini
%ghost %attr(0644,root,%webserver_group) %_datadir/ipa/html/krbrealm.con
%ghost %attr(0644,root,%webserver_group) %_datadir/ipa/html/preferences.html
%dir %_sysconfdir/ipa
%dir %_sysconfdir/ipa/html
%config(noreplace) %attr(0644,root,%webserver_group) %_sysconfdir/ipa/html/*

%config(noreplace) %_sysconfdir/httpd2/conf/extra-available/ipa-nss.conf
%ghost %attr(0644,root,%webserver_group) %config(noreplace) %_sysconfdir/httpd2/conf/ipa-rewrite.conf
%ghost %attr(0644,root,%webserver_group) %config(noreplace) %_sysconfdir/httpd2/conf/sites-available/ipa.conf
%ghost %attr(0644,root,%webserver_group) %config(noreplace) %_sysconfdir/httpd2/conf/ipa-pki-proxy.conf
%ghost %attr(0644,root,%webserver_group) %config(noreplace) %_sysconfdir/httpd2/conf/ipa-kdc-proxy.conf
%ghost %attr(0644,root,apache2) %config(noreplace) %_sysconfdir/ipa/kdcproxy/ipa-kdc-proxy.conf
%dir %attr(0755,root,root) %_sysconfdir/ipa/dnssec
%dir %_localstatedir/lib/ipa

%attr(700,root,root) %dir %_localstatedir/lib/ipa/backup
%attr(700,root,root) %dir %_localstatedir/lib/ipa/sysrestore
%attr(700,root,root) %dir %_localstatedir/lib/ipa/sysupgrade
%attr(755,root,root) %dir %_localstatedir/lib/ipa/pki-ca
%ghost %_localstatedir/lib/ipa/pki-ca/publish
#%ghost %_localstatedir/named/dyndb-ldap/ipa
%dir %attr(0700,root,root) %_sysconfdir/ipa/custodia

%files server-dns
%_sbindir/ipa-dns-install
%_man1dir/ipa-dns-install.1.*

%files server-trust-ad
%_sbindir/ipa-adtrust-install
%_datadir/ipa/smb.conf.empty
%_libdir/samba/pdb/ipasam.so
%_man1dir/ipa-adtrust-install.1.*
%_sysconfdir/dbus-1/system.d/oddjob-ipa-trust.conf
%_sysconfdir/oddjobd.conf.d/oddjobd-ipa-trust.conf
%_libexecdir/ipa/oddjob/com.redhat.idm.trust-fetch-domains

%files client
%_sbindir/ipa-client-*
%_sbindir/ipa-*keytab
%_sbindir/ipa-join
%_sbindir/ipa-certupdate
#_datadir/ipa/ipaclient
%_man1dir/ipa-getkeytab.1.*
%_man1dir/ipa-rmkeytab.1.*
%_man1dir/ipa-client-install.1.*
%_man1dir/ipa-client-automount.1.*
%_man1dir/ipa-join.1.*
%_man1dir/ipa-certupdate.1.*

%files -n python-module-ipaclient
%dir %python_sitelibdir_noarch/ipaclient
%python_sitelibdir_noarch/ipaclient/*.py*
%python_sitelibdir_noarch/ipaclient-*.egg-info

%files client-common
%ghost %attr(0644,root,%webserver_group) %config(noreplace) %_sysconfdir/ipa/default.conf
%ghost %attr(0644,root,%webserver_group) %config(noreplace) %_sysconfdir/ipa/ca.crt
%dir %_sysconfdir/ipa/nssdb
%ghost %config(noreplace) %_sysconfdir/ipa/nssdb/cert8.db
%ghost %config(noreplace) %_sysconfdir/ipa/nssdb/key3.db
%ghost %config(noreplace) %_sysconfdir/ipa/nssdb/secmod.db
%ghost %config(noreplace) %_sysconfdir/ipa/nssdb/pwdfile.txt
%ghost %config(noreplace) %_sysconfdir/pki/ca-trust/source/ipa.p11-kit
%dir %_localstatedir/lib/ipa-client
%dir %_localstatedir/lib/ipa-client/sysrestore
%_man5dir/default.conf.5.*

%files admintools
%_bindir/ipa
%config %_sysconfdir/bash_completion.d
%_man1dir/ipa.1.*

%files -n python-module-freeipa
%python_sitelibdir_noarch/ipapython
%python_sitelibdir_noarch/ipalib
%python_sitelibdir_noarch/ipaplatform
%python_sitelibdir_noarch/ipaplatform-*.egg-info
%python_sitelibdir_noarch/ipapython-*.egg-info
%python_sitelibdir_noarch/ipalib-*.egg-info

%files common -f ipa.lang
%doc README Contributors.txt
%dir %_sysconfdir/ipa/
%dir %_datadir/ipa

%files tests
%python_sitelibdir_noarch/ipatests
%_bindir/ipa-run-tests
%_bindir/ipa-test-config
%_bindir/ipa-test-task
%python_sitelibdir_noarch/ipatests-*.egg-info
%_man1dir/ipa-run-tests.1.*
%_man1dir/ipa-test-config.1.*
%_man1dir/ipa-test-task.1.*

%changelog
* Fri Nov 25 2016 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt3
- Require java-1.8.0-openjdk.
- Require pki.
- Drop hack for old certmonger.

* Thu Nov 10 2016 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt2
- Merge spec with Fedora.

* Tue Nov 08 2016 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt1
- Patch from upstream:
    + ipa-kdb: Allow to build with samba 4.5
- Update spec.
- ipa-client-install: Hack for old certmonger.
- Fix opendnssec user/group.
- Disable dyndb-ldap stuff for now.
- Fix httpd2 confs paths.
- Fix user for ipa_memcached.
- Fix NSSCertificateDatabase path.
- ipa.conf: Fix paths.
- Add nss.conf.
- constants: Fix apache user name.
- Fix apache user name for oddjobd.
- Fix path to custodia socket.
- Hack bind configuration for now.
- Fix ipa.conf.
- Fix httpd.service.
- Add initial ALT Linux platform support.
- Updated to 4.3.2.

* Wed May 04 2016 Mikhail Efremov <sem@altlinux.org> 4.3.1-alt1
- Updated to 4.3.1.

* Fri Nov 20 2015 Mikhail Efremov <sem@altlinux.org> 4.2.3-alt1
- Updated to 4.2.3.

* Mon Apr 28 2014 Timur Aitov <timonbl4@altlinux.org> 3.3.5-alt1
- new version

* Wed Mar 26 2014 Timur Aitov <timonbl4@altlinux.org> 3.3.4-alt1
- first build for alt

* Fri Oct 25 2013 Martin Kosek <mkosek@redhat.com> - 3.3.2-1
- Remove mod_ssl conflict, it can now live with mod_nss installed

* Wed Sep 4 2013 Ana Krivokapic <akrivoka@redhat.com> - 3.3.0-3
- Conform to tmpfiles.d packaging guidelines

* Wed Aug 28 2013 Petr Viktorin <pviktori@redhat.com> - 3.3.0-2
- Add man pages to the tests subpackage

* Mon Aug 12 2013 Petr Viktorin <pviktori@redhat.com> - 3.3.0-1
- Downgrade required version of python-paramiko for the tests subpackage

* Thu Aug 8 2013 Martin Kosek <mkosek@redhat.com> - 3.2.99-13
- Require slapi-nis 0.47.7 and sssd 1.11.0-0.1.beta2 required for core
  features of 3.3.0 release

* Fri Jul 26 2013 Martin Kosek <mkosek@redhat.com> - 3.2.99-12
- Require pki-ca 10.0.4 which fixes external CA installation (#986901)

* Wed Jul 24 2013 Petr Viktorin <pviktori@redhat.com> - 3.2.99-11
- Add tar and xz dependencies to freeipa-tests

* Wed Jul 24 2013 Tomas Babej <tbabej@redhat.com> - 3.2.99-10
- Move requirement for keyutils from freeipa-server to freeipa-python

* Wed Jul 24 2013 Martin Kosek <mkosek@redhat.com> - 3.2.99-9
- Bump minimum version of sssd to 1.10.92 to pick up latest SSSD 1.11 Beta
  development

* Thu Jul 18 2013 Ana Krivokapic <akrivoka@redhat.com> - 3.2.99-8
- Bump minimum version of sssd to 1.10.90 for the 'ipa_server_mode' option.

* Wed Jul 17 2013 Martin Kosek <mkosek@redhat.com> - 3.2.99-7
- Require selinux-policy 3.12.1-65 containing missing policy after removal of
  freeipa-server-selinux subpackage

* Tue Jul 16 2013 Tomas Babej <tbabej@redhat.com> - 3.2.99-6
- Do not create /var/lib/ipa/pki-ca/publish, retain reference as ghost

* Thu Jul 11 2013 Martin Kosek <mkosek@redhat.com> - 3.2.99-5
- Run ipa-upgradeconfig and server restart in posttrans to avoid inconsistency
  issues when there are still old parts of software (like entitlements plugin)

* Wed Jul 10 2013 Ana Krivokapic <akrivoka@redhat.com> - 3.2.99-4
- Bump minimum version of 389-ds-base to 1.3.1.3 for user password change fix.

* Wed Jun 26 2013 Jan Cholasta <jcholast@redhat.com> - 3.2.99-3
- Bump minimum version of 389-ds-base to 1.3.1.1 for SASL mapping priority
  support.

* Mon Jun 17 2013 Petr Viktorin <pviktori@redhat.com> - 3.2.99-2
- Add the freeipa-tests subpackage

* Thu Jun 13 2013 Martin Kosek <mkosek@redhat.com> - 3.2.99-1
- Drop freeipa-server-selinux subpackage
- Drop redundant directory /var/cache/ipa/sessions

* Fri May 10 2013 Martin Kosek <mkosek@redhat.com> - 3.1.99-13
- Add requires for openldap-2.4.35-4 to pickup fixed SASL_NOCANON behavior for
  socket based connections (#960222)

* Tue May  7 2013 Petr Viktorin <pviktori@redhat.com> - 3.1.99-12
- Require libsss_nss_idmap-python in Fedora 19+

* Mon May  6 2013 Petr Vobornik <pvoborni@redhat.com> - 3.1.99-11
- Web UI plugins

* Fri May  3 2013 Rob Crittenden <rcritten@redhat.com> - 3.1.99-10
- Require pki-ca 10.0.2 for 501 response code on find for d9 -> d10 upgrades

* Tue Apr 30 2013 Rob Crittenden <rcritten@redhat.com> - 3.1.99-9
- Add Conflicts on nss-pam-ldapd < 0.8.4. The mapping from uniqueMember to
  member is now done automatically and having it in the config file raises
  an error.

* Tue Apr 30 2013 Jan Cholasta <jcholast@redhat.com> - 3.1.99-8
- Add triggerin scriptlet to update sshd_config on openssh-server update

* Thu Apr 25 2013 Rob Crittenden <rcritten@redhat.com> - 3.1.99-7
- Update nss and nss-tools dependency to fix certutil problem (#872761)

* Mon Apr 15 2013 Martin Kosek <mkosek@redhat.com> - 3.1.99-6
- Require samba 4.0.5, includes new passdb API
- Require krb5 1.11.2-1, fixes missing PAC issue
- Change permissions on backup dir to 700

* Fri Apr  5 2013 Rob Crittenden <rcritten@redhat.com> - 3.1.99-5
- Add backup and restore
- Own /var/lib/ipa/backup

* Thu Apr  4 2013 Alexander Bokovoy <abokovoy@redhat.com> - 3.1.99-4
- Make sure build against Krb5 1.11 in Fedora 18 environment creates proper dependencies

* Tue Apr  2 2013 Martin Kosek <mkosek@redhat.com> - 3.1.99-3
- Require 389-base-base >= 1.3.0.5 to pull the following fixes:
- upgrade deadlock caused by DNA plugin reconfiguration
- CVE-2013-1897: unintended information exposure when
  nsslapd-allow-anonymous-access is set to rootdse

* Wed Mar 27 2013 Martin Kosek <mkosek@redhat.com> - 3.1.99-2
- Remove conflict with krb5-server > 1.11 as ipa-kdb is compatible
- ipa-ldap-updater show produce errors only
- update policycoreutils version to 2.1.12-5 to match Requires in Fedora
- require at least systemd 38 which provides the journal (we no longer
  need to require syslog.target)

* Thu Mar 21 2013 Martin Kosek <mkosek@redhat.com> - 3.1.99-1
- Require selinux-policy 3.11.1-86 to fix Fedora 17 to 18 upgrade issue

* Tue Jan 29 2013 Petr Viktorin <pviktori@redhat.com> - 3.0.99-14
- Use ipa-ldap-updater --quiet instead of redirecting to /dev/null

* Tue Jan 29 2013 Rob Crittenden <rcritten@redhat.com> - 3.0.99-13
- Set certmonger minimum version to 0.65 for NSS locking during
  renewal
- Set selinux-policy to 3.11.1-73 so certmonger can run in post
  scriptlet

* Thu Jan 24 2013 Rob Crittenden <rcritten@redhat.com> - 3.0.99-12
- Add certmonger condrestart to server post scriptlet
- Make certmonger a (pre) Requires on the server subpackage

* Tue Jan 22 2013 Petr Vobornik <pvoborni@redhat.com> - 3.0.99-11
- dependency fix
- Add BuildRequires: java-1.7.0-openjdk.
- Removed BuildRequires: rhino

* Fri Jan 18 2013 Petr Vobornik <pvoborni@redhat.com> - 3.0.99-10
- Add Web UI layer JS files in ui/js/{dojo,freeipa,libs} directories
- Add BuildRequires: rhino

* Fri Dec 7 2012 Endi S. Dewata <edewata@redhat.com> - 3.0.99-9
- Bump minimum version of pki-ca to 10.0.0-0.54.b3

* Fri Dec 7 2012 Martin Kosek <mkosek@redhat.com> - 3.0.99-8
- Bump minimum version of 389-ds-base to 1.3.0 to get transaction support

* Thu Dec  6 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.99-7
- Set min for selinux-policy to 3.11.1-60 to fix errors including sssd
  domain mapping in krb5.conf (#873429)

* Wed Nov 21 2012 Alexander Bokovoy <abokovoy@redhat.com> - 3.0.99-6
- Replace python-crypto by m2crypto dependency

* Fri Nov 16 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.99-5
- Bump minimum version of slapi-nis to 0.44

* Wed Nov 14 2012 Martin Kosek <mkosek@redhat.com> - 3.0.99-4
- Remove compatibility definitions for unsupported Fedora versions (Fedora 16 and lower)
  - Do not require specific package version when the package was available in Fedora 17
  - Remove old SysV initscript compatibility code - we run on systemd now
- Add Requires for the new Dogtag 10 and dogtag-pki-server-theme
- Remove Requires on tomcat6 for Fedora 18 and later, Dogtag 10 pulls tomcat7 itself
- Add Requires for tar (used by ipa-replica-prepare)

* Fri Nov 09 2012 Martin Kosek <mkosek@redhat.com> - 3.0.99-3
- Set min for bind-dyndb-ldap to 2.3-2 to pick up disabling global
  forwarder per-zone

* Fri Oct 26 2012 Sumit Bose <sbose@redhat.com> - 3.0.99-2
- Restart httpd in post install of server-trust-ad

* Wed Oct 24 2012 Martin Kosek <mkosek@redhat.com> - 3.0.99-1
- Add strict Requires for 389-ds-base and policycoreutils to avoid user
  removing them during package lifetime

* Wed Oct 17 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-51
- Print ipa-upgradeconfig errors during RPM update

* Wed Oct 10 2012 Alexander Bokovoy <abokovoy@redhat.com> - 2.99.0-50
- Make sure server-trust-ad subpackage alternates winbind_krb5_locator.so
  plugin to /dev/null since they cannot be used when trusts are configured

* Wed Oct 10 2012 Petr Viktorin <pviktori@redhat.com> - 2.99.0-49
- Add zip dependency, needed for creating unsigned Firefox extensions

* Mon Oct  8 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-48
- Add directory /var/lib/ipa/pki-ca/publish for CRL published by pki-ca

* Mon Oct  1 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-47
- Require samba packages instead of samba4 packages obsoleted in Fedora 18 and later
- Add libwbclient-devel BuildRequires to pick up libwbclient.h on Fedora 18 and later

* Tue Sep 18 2012 Petr Viktorin <pviktori@redhat.com> - 2.99.0-46
- Set certmonger minimum version to 0.60 for Dogtag 10 support.

* Mon Sep 17 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-45
- Set min for 389-ds-base to 1.2.11.14-1 on F17+ to pull in updated
  RUV code and nsslapd-readonly schema.

* Fri Sep 14 2012 Sumit Bose <sbose@redhat.com> - 2.99.0-44
- Updated samba4-devel dependency due to API change

* Mon Aug 20 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-43
- Set min for 389-ds-base to 1.2.11.9-1 on F17+ to pull in warning about
  low nsslapd-cachememsize.

* Mon Aug 20 2012 Tomas Babej <tbabej@redhat.com> - 2.99.0-42
- Add samba4-winbind to build dependencies for AD server-side code

* Fri Aug 17 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-41
- Set min for bind-dyndb-ldap to 1.1.0-0.16.rc1 to pick up complete zone transfer
  support

* Thu Aug 2 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-40
- Set min for bind-dyndb-ldap to 1.1.0-0.15.rc1 to pick up SOA serial autoincrement
  feature

* Tue Jul 24 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-39
- Set minimum certmonger to 0.58 for dogtag cert renewal

* Wed Jul 18 2012 Alexander Bokovoy <abokovoy@redhat.com> - 2.99.0-38
- Require samba4-devel >= 4.0.0-128 due to passdb API change in beta4

* Fri Jun 29 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-37
- Add Requires on openssl
- Set minimum tomcat6 to 6.0.35-4 in F-18
- Set minimum mod_auth_kerb to 5.4-16 in F-18

* Thu Jun 21 2012 Sumit Bose <sbose@redhat.com> - 2.99.0-36
- Add extdom extop plugin

* Thu Jun 21 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-35
- Add client requires on libsss-autofs, autofs, libnfsidmap and nfs-utils
  for configuring automount and NFS.

* Thu Jun 21 2012 Petr Vobornik <pvoborni@redhat.com> - 2.99.0-34
- Add Web UI reset password pages

* Wed Jun 20 2012 Ondrej Hamada <ohamada@redhat.com> - 2.99.0-33
- Set min for 389-ds-base to 1.2.11.5-1 on F17 to fix installation issue
- Set min for 389-ds-base to 1.2.10.10-1 on F16 (and lower) to fix CN case persistence

* Fri Jun 8 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-32
- Add directory /var/lib/ipa/sysupgrade for package upgrade metadata
- Set min for bind-dyndb-ldap to 1.1.0-0.12.rc1 to pick up persistent search
  related bug fixes

* Mon Jun  4 2012 Alexander Bokovoy <abokovoy@redhat.com> - 2.99.0-31
- Add python-crypto to build dependencies for AD server-side code

* Tue May 29 2012 Alexander Bokovoy <abokovoy@redhat.com> - 2.99.0-30
- Add freeipa-server-trust-ad virtual package to capture all required dependencies
  for Active Directory trust management

* Fri May 11 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-29
- Replace used DNS client library (acutil) with python-dns

* Tue Apr 10 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-28
- Set min for selinux-policy to 3.10.0-110 on F-17 to pick up certmonger
  policy for restarting services.
- Set min for certmonger to 0.53 so we have the -C option to set restart
  commands.

* Thu Apr  5 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-27
- Bump minimum version of slapi-nis to 0.40

* Tue Mar 27 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-26
- Add python-krbV Requires on client package

* Mon Mar 26 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-25
- Set min for 389-ds-base to 1.2.10.4-2 to fix upgrade issue

* Fri Mar 23 2012 Petr Viktorin <pviktori@redhat.com> - 2.99.0-24
- Add python-lxml and python-pyasn1 to BuildRequires

* Mon Mar 19 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-23
- Set min for bind-dyndb-ldap and bind to pick up new features and bug fixes

* Thu Mar 1 2012 Jan Cholasta <jcholast@redhat.com> - 2.99.0-22
- Set min nvr of sssd to 1.8.0 for SSH support
- Add BuildRequires on sssd >= 1.8.0

* Wed Feb 29 2012 Petr Vobornik <pvoborni@redhat.com> - 2.99.0-21
- Add Web UI form based login page
- Removed ipa_migration.css

* Wed Feb 29 2012 Petr Vobornik <pvoborni@redhat.com> - 2.99.0-20
- Add Web UI logout page

* Mon Feb 27 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-19
- Add Requires to ipa-client on oddjob-mkhomedir

* Fri Feb 24 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-18
- Set min for bind-dyndb-ldap to 1.1.0-0.8.a2 to pick up new features

* Thu Feb 23 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-17
- Add Conflicts on mod_ssl

* Thu Feb 16 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-16
- Set min for 389-ds-base to 1.2.10.1-1 to fix install segfault,
  schema replication.

* Tue Jan 31 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-15
- Set min for krb5-server to 1.9.2-6 to pick up needed s4u2proxy patches

* Wed Jan 11 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-14
- Set min for mod_auth_kerb to 5.4-8 to pick up s4u2proxy support

* Fri Dec 9 2011 Alexander Bokovoy <abokovoy@redhat.com> - 2.99.0-13
- Fix dependency for samba4-devel package

* Thu Nov 17 2011 Simo Sorce <simo@redhat.com> - 2.99.0-12
- Add CLDAP plugin
- Set min nvr of 389-ds-base to 1.2.10-0.5.a5 for SLAPI_PLUGIN_CONFIG_ENTRY
  support

* Mon Nov 14 2011 Endi S. Dewata <edewata@redhat.com> - 2.99.0-11
- Make sure changes to extension.js are not removed.

* Wed Oct 26 2011 Endi S. Dewata <edewata@redhat.com> - 2.99.0-10
- Moved UI images into install/ui/images

* Mon Oct 24 2011 Endi S. Dewata <edewata@redhat.com> - 2.99.0-9
- Removed hbac-deny-remove.html

* Fri Oct 21 2011 Alexander Bokovoy <abokovoy@redhat.com> - 2.99.0-8
- Default to systemd for Fedora 16 and onwards

* Fri Oct 14 2011 Rob Crittenden <rcritten@redhat.com> - 2.99.0-7
- Set min nvr of 389-ds-base to 1.2.10-0.4.a4 for limits fixes (740942, 742324)

* Fri Oct  7 2011 Adam Young <ayoung@redhat.com> - 2.99.0-6
- Add explicit dependency on pki-setup.

* Tue Sep 13 2011 Alexander Bokovoy <abokovoy@redhat.com> - 2.99.0-5
- Make sure platform adaptation is packaged in -python sub-package

* Fri Sep 9 2011 Martin Kosek <mkosek@redhat.com> - 2.99.0-4
- Add soft dependency for bind and bind-dyndb-ldap required versions

* Wed Aug 31 2011 Rob Crittenden <rcritten@redhat.com> - 2.99.0-3
- Set min nvr of 389-ds-base to 1.2.9.7-1 for BZ 728605

* Mon Aug 29 2011 Rob Crittenden <rcritten@redhat.com> - 2.99.0-2
- Set min nvr of pki-ca to 9.0.12 for fix in BZ 700505

* Thu Aug 25 2011 Simo Sorce <ssorce#redhat.com> - 2.99.0-1
- Remove ipa_kpasswd.

* Tue Aug 23 2011 Jan Cholasta <jcholast@redhat.com> - 2.1.0-1
- Add subscription-manager dependency for RHEL.

* Thu Aug 11 2011 Martin Kosek <mkosek@redhat.com> - 2.0.90-12
- Set min nvr of 389-ds-base to 1.2.9.6 for fix in BZ 725743,
  723937, and 725542
- Set min nvr of pki-ca to 9.0.11 for fix in BZ 728332

* Thu Aug 11 2011 Martin Kosek <mkosek@redhat.com> - 2.0.90-11
- Set min nvr of xmlrpc-c and libcurl to make sure GSSAPI delegation
  support is in

* Tue Aug 2 2011 Endi S. Dewata <edewata@redhat.com> - 2.0.90-10
- Add *.ico files

* Fri Jul 29 2011 Alexander Bokovoy <abokovoy@redhat.com> - 2.0.90-9
- Add libipa_hbac-python dependency for hbactest plugin

* Thu Jul 28 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.90-8
- Set min nvr of pki-ca to 9.0.10 on F-15+ to pick up updated
  caIPAserviceCert.cfg profile

* Wed Jul 20 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.90-7
- Make cyrus-sasl-gssapi requires arch-specific

* Thu Jul 14 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.90-6
- Add ipa-csreplica-manage tool.

* Wed Jul  6 2011 Adam Young <ayoung@redhat.com> - 2.0.90-5
- Add HTML file describing issues with HBAC deny rules

* Fri Jun 17 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.90-4
- Ship ipa-ca-install utility

* Thu May 12 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.90-3
- Set min nvr of selinux-policy to 3.9.16-18 on F-15+
- Set min nvr of pki-ca to 9.0.7 on F-15+

* Thu May  5 2011 Martin Kosek <mkosek@redhat.com> - 2.0.90-2
- Add BuildRequires on pylint, python-rhsm to enable a build with enforced
  pylint check

* Tue May  3 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.90-1
- Bump version to 2.0.90

* Tue Apr  5 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-47
- Set min version of 389-ds-base to 1.2.8.0-1 for fix in BZ 693466.

* Thu Mar 17 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-46
- Automatically apply updates when the package is upgraded.

* Thu Feb 17 2011 Jakub Hrozek <jhrozek@redhat.com> - 1.99-45
- Set minimum version of python-nss to 0.11 to make sure IPv6 support is in

* Wed Feb  9 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-44
- Set minimum version of sssd to 1.5.1

* Wed Feb  2 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-43
- Set min version of 389-ds-base to 1.2.8
- Set min version of mod_nss 1.0.8-10
- Set min version of selinux-policy to 3.9.7-27

* Thu Jan 27 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-42
- Apply changes discovered in Fedora package review process (#672986)

* Tue Jan 25 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-41
- Re-arrange doc and defattr to clean up rpmlint warnings
- Remove conditionals on older releases
- Move some man pages into admintools subpackage
- Remove some explicit Requires in client that aren't needed
- Consistent use of buildroot vs RPM_BUILD_ROOT

* Wed Jan 19 2011 Adam Young <ayoung@redhat.com> - 1.99-40
- Moved directory install/static to install/ui

* Thu Jan 13 2011 Simo Sorce <ssorce@redhat.com> - 1.99-39
- Remove dependency on nss_ldap/nss-pam-ldapd
- The official client is sssd and that's what we use by default.

* Thu Jan 13 2011 Simo Sorce <ssorce@redhat.com> - 1.99-38
- Remove radius subpackages

* Thu Jan 13 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-37
- Set minimum pki-ca and pki-silent versions to 9.0.0

* Wed Jan 12 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-36
- Drop BuildRequires on mozldap-devel

* Mon Dec 13 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-35
- Add Requires on krb5-pkinit-openssl

* Fri Dec 10 2010 Jr Aquino <jr.aquino@citrix.com> - 1.99-34
- Add ipa-host-net-manage script

* Tue Dec  7 2010 Simo Sorce <ssorce@redhat.com> - 1.99-33
- Add ipa init script

* Fri Nov 19 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-32
- Set minimum level of 389-ds-base to 1.2.7 for enhanced memberof plugin

* Wed Nov  3 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-31
- remove ipa-fix-CVE-2008-3274

* Wed Oct  6 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-30
- Remove duplicate %%files entries on share/ipa/static
- Add python default encoding shared library

* Mon Sep 20 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-29
- Drop requires on python-configobj (not used any more)
- Drop ipa-ldap-updater message, upgrades are done differently now

* Wed Sep  8 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-28
- Drop conflicts on mod_nss
- Require nss-pam-ldapd on F-14 or higher instead of nss_ldap (#606847)
- Drop a slew of conditionals on older Fedora releases (< 12)
- Add a few conditionals against RHEL 6
- Add Requires of nss-tools on ipa-client

* Fri Aug 13 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-27
- Set minimum version of certmonger to 0.26 (to pck up #621670)
- Set minimum version of pki-silent to 1.3.4 (adds -key_algorithm)
- Set minimum version of pki-ca to 1.3.6
- Set minimum version of sssd to 1.2.1

* Tue Aug 10 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-26
- Add BuildRequires for authconfig

* Mon Jul 19 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-25
- Bump up minimum version of python-nss to pick up nss_is_initialize() API

* Thu Jun 24 2010 Adam Young <ayoung@redhat.com> - 1.99-24
- Removed python-asset based webui

* Thu Jun 24 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-23
- Change Requires from fedora-ds-base to 389-ds-base
- Set minimum level of 389-ds-base to 1.2.6 for the replication
  version plugin.

* Tue Jun  1 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-22
- Drop Requires of python-krbV on ipa-client

* Mon May 17 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-21
- Load ipa_dogtag.pp in post install

* Mon Apr 26 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-20
- Set minimum level of sssd to 1.1.1 to pull in required hbac fixes.

* Thu Mar  4 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-19
- No need to create /var/log/ipa_error.log since we aren't using
  TurboGears any more.

* Mon Mar 1 2010 Jason Gerard DeRose <jderose@redhat.com> - 1.99-18
- Fixed share/ipa/wsgi.py so .pyc, .pyo files are included

* Wed Feb 24 2010 Jason Gerard DeRose <jderose@redhat.com> - 1.99-17
- Added Require mod_wsgi, added share/ipa/wsgi.py

* Thu Feb 11 2010 Jason Gerard DeRose <jderose@redhat.com> - 1.99-16
- Require python-wehjit >= 0.2.2

* Wed Feb  3 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-15
- Add sssd and certmonger as a Requires on ipa-client

* Wed Jan 27 2010 Jason Gerard DeRose <jderose@redhat.com> - 1.99-14
- Require python-wehjit >= 0.2.0

* Fri Dec  4 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-13
- Add ipa-rmkeytab tool

* Tue Dec  1 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-12
- Set minimum of python-pyasn1 to 0.0.9a so we have support for the ASN.1
  Any type

* Wed Nov 25 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-11
- Remove v1-style /etc/ipa/ipa.conf, replacing with /etc/ipa/default.conf

* Fri Nov 13 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-10
- Add bash completion script and own /etc/bash_completion.d in case it
  doesn't already exist

* Tue Nov  3 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-9
- Remove ipa_webgui, its functions rolled into ipa_httpd

* Mon Oct 12 2009 Jason Gerard DeRose <jderose@redhat.com> - 1.99-8
- Removed python-cherrypy from BuildRequires and Requires
- Added Requires python-assets, python-wehjit

* Mon Aug 24 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-7
- Added httpd SELinux policy so CRLs can be read

* Thu May 21 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-6
- Move ipalib to ipa-python subpackage
- Bump minimum version of slapi-nis to 0.15

* Wed May  6 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-5
- Set 0.14 as minimum version for slapi-nis

* Wed Apr 22 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-4
- Add Requires: python-nss to ipa-python sub-package

* Thu Mar  5 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-3
- Remove the IPA DNA plugin, use the DS one

* Wed Mar  4 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-2
- Build radius separately
- Fix a few minor issues

* Tue Feb  3 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-1
- Replace TurboGears requirement with python-cherrypy

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 1.2.1-3
- rebuild with new openssl

* Fri Dec 19 2008 Dan Walsh <dwalsh@redhat.com> - 1.2.1-2
- Fix SELinux code

* Mon Dec 15 2008 Simo Sorce <ssorce@redhat.com> - 1.2.1-1
- Fix breakage caused by python-kerberos update to 1.1

* Fri Dec 5 2008 Simo Sorce <ssorce@redhat.com> - 1.2.1-0
- New upstream release 1.2.1

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.2.0-4
- Rebuild for Python 2.6

* Fri Nov 14 2008 Simo Sorce <ssorce@redhat.com> - 1.2.0-3
- Respin after the tarball has been re-released upstream
  New hash is 506c9c92dcaf9f227cba5030e999f177

* Thu Nov 13 2008 Simo Sorce <ssorce@redhat.com> - 1.2.0-2
- Conditionally restart also dirsrv and httpd when upgrading

* Wed Oct 29 2008 Rob Crittenden <rcritten@redhat.com> - 1.2.0-1
- Update to upstream version 1.2.0
- Set fedora-ds-base minimum version to 1.1.3 for winsync header
- Set the minimum version for SELinux policy
- Remove references to Fedora 7

* Wed Jul 23 2008 Simo Sorce <ssorce@redhat.com> - 1.1.0-3
- Fix for CVE-2008-3274
- Fix segfault in ipa-kpasswd in case getifaddrs returns a NULL interface
- Add fix for bug #453185
- Rebuild against openldap libraries, mozldap ones do not work properly
- TurboGears is currently broken in rawhide. Added patch to not build
  the UI locales and removed them from the ipa-server files section.

* Wed Jun 18 2008 Rob Crittenden <rcritten@redhat.com> - 1.1.0-2
- Add call to /usr/sbin/upgradeconfig to post install

* Wed Jun 11 2008 Rob Crittenden <rcritten@redhat.com> - 1.1.0-1
- Update to upstream version 1.1.0
- Patch for indexing memberof attribute
- Patch for indexing uidnumber and gidnumber
- Patch to change DNA default values for replicas
- Patch to fix uninitialized variable in ipa-getkeytab

* Fri May 16 2008 Rob Crittenden <rcritten@redhat.com> - 1.0.0-5
- Set fedora-ds-base minimum version to 1.1.0.1-4 and mod_nss minimum
  version to 1.0.7-4 so we pick up the NSS fixes.
- Add selinux-policy-base(post) to Requires (446496)

* Tue Apr 29 2008 Rob Crittenden <rcritten@redhat.com> - 1.0.0-4
- Add missing entry for /var/cache/ipa/kpasswd (444624)
- Added patch to fix permissions problems with the Apache NSS database.
- Added patch to fix problem with DNS querying where the query could be
  returned as the answer.
- Fix spec error where patch1 was in the wrong section

* Fri Apr 25 2008 Rob Crittenden <rcritten@redhat.com> - 1.0.0-3
- Added patch to fix problem reported by ldapmodify

* Fri Apr 25 2008 Rob Crittenden <rcritten@redhat.com> - 1.0.0-2
- Fix Requires for krb5-server that was missing for Fedora versions > 9
- Remove quotes around test for fedora version to package egg-info

* Fri Apr 18 2008 Rob Crittenden <rcritten@redhat.com> - 1.0.0-1
- Update to upstream version 1.0.0

* Tue Mar 18 2008 Rob Crittenden <rcritten@redhat.com> 0.99-12
- Pull upstream changelog 722
- Add Conflicts mod_ssl (435360)

* Fri Feb 29 2008 Rob Crittenden <rcritten@redhat.com> 0.99-11
- Pull upstream changelog 698
- Fix ownership of /var/log/ipa_error.log during install (435119)
- Add pwpolicy command and man page

* Thu Feb 21 2008 Rob Crittenden <rcritten@redhat.com> 0.99-10
- Pull upstream changelog 678
- Add new subpackage, ipa-server-selinux
- Add Requires: authconfig to ipa-python (bz #433747)
- Package i18n files

* Mon Feb 18 2008 Rob Crittenden <rcritten@redhat.com> 0.99-9
- Pull upstream changelog 641
- Require minimum version of krb5-server on F-7 and F-8
- Package some new files

* Thu Jan 31 2008 Rob Crittenden <rcritten@redhat.com> 0.99-8
- Marked with wrong license. IPA is GPLv2.

* Tue Jan 29 2008 Rob Crittenden <rcritten@redhat.com> 0.99-7
- Ensure that /etc/ipa exists before moving user-modifiable html files there
- Put html files into /etc/ipa/html instead of /etc/ipa

* Tue Jan 29 2008 Rob Crittenden <rcritten@redhat.com> 0.99-6
- Pull upstream changelog 608 which renamed several files

* Thu Jan 24 2008 Rob Crittenden <rcritten@redhat.com> 0.99-5
- package the sessions dir /var/cache/ipa/sessions
- Pull upstream changelog 597

* Thu Jan 24 2008 Rob Crittenden <rcritten@redhat.com> 0.99-4
- Updated upstream pull (596) to fix bug in ipa_webgui that was causing the
  UI to not start.

* Thu Jan 24 2008 Rob Crittenden <rcritten@redhat.com> 0.99-3
- Included LICENSE and README in all packages for documentation
- Move user-modifiable content to /etc/ipa and linked back to
  /usr/share/ipa/html
- Changed some references to /usr to the {_usr} macro and /etc
  to {_sysconfdir}
- Added popt-devel to BuildRequires for Fedora 8 and higher and
  popt for Fedora 7
- Package the egg-info for Fedora 9 and higher for ipa-python

* Tue Jan 22 2008 Rob Crittenden <rcritten@redhat.com> 0.99-2
- Added auto* BuildRequires

* Mon Jan 21 2008 Rob Crittenden <rcritten@redhat.com> 0.99-1
- Unified spec file

* Thu Jan 17 2008 Rob Crittenden <rcritten@redhat.com> - 0.6.0-2
- Fixed License in specfile
- Include files from /usr/lib/python*/site-packages/ipaserver

* Fri Dec 21 2007 Karl MacMillan <kmacmill@redhat.com> - 0.6.0-1
- Version bump for release

* Wed Nov 21 2007 Karl MacMillan <kmacmill@mentalrootkit.com> - 0.5.0-1
- Preverse mode on ipa-keytab-util
- Version bump for relase and rpm name change

* Thu Nov 15 2007 Rob Crittenden <rcritten@redhat.com> - 0.4.1-2
- Broke invididual Requires and BuildRequires onto separate lines and
  reordered them
- Added python-tgexpandingformwidget as a dependency
- Require at least fedora-ds-base 1.1

* Thu Nov  1 2007 Karl MacMillan <kmacmill@redhat.com> - 0.4.1-1
- Version bump for release

* Wed Oct 31 2007 Karl MacMillan <kmacmill@redhat.com> - 0.4.0-6
- Add dep for freeipa-admintools and acl

* Wed Oct 24 2007 Rob Crittenden <rcritten@redhat.com> - 0.4.0-5
- Add dependency for python-krbV

* Fri Oct 19 2007 Rob Crittenden <rcritten@redhat.com> - 0.4.0-4
- Require mod_nss-1.0.7-2 for mod_proxy fixes

* Thu Oct 18 2007 Karl MacMillan <kmacmill@redhat.com> - 0.4.0-3
- Convert to autotools-based build

* Tue Sep 25 2007 Karl MacMillan <kmacmill@redhat.com> - 0.4.0-2

* Fri Sep 7 2007 Karl MacMillan <kmacmill@redhat.com> - 0.3.0-1
- Added support for libipa-dna-plugin

* Fri Aug 10 2007 Karl MacMillan <kmacmill@redhat.com> - 0.2.0-1
- Added support for ipa_kpasswd and ipa_pwd_extop

* Sun Aug  5 2007 Rob Crittenden <rcritten@redhat.com> - 0.1.0-3
- Abstracted client class to work directly or over RPC

* Wed Aug  1 2007 Rob Crittenden <rcritten@redhat.com> - 0.1.0-2
- Add mod_auth_kerb and cyrus-sasl-gssapi to Requires
- Remove references to admin server in ipa-server-setupssl
- Generate a client certificate for the XML-RPC server to connect to LDAP with
- Create a keytab for Apache
- Create an ldif with a test user
- Provide a certmap.conf for doing SSL client authentication

* Fri Jul 27 2007 Karl MacMillan <kmacmill@redhat.com> - 0.1.0-1
- Initial rpm version

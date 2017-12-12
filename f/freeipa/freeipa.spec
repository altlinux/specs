%define _unpackaged_files_terminate_build 1

%define _libexecdir /usr/libexec
%define plugin_dir %_libdir/dirsrv/plugins
%define _localstatedir %_var

# Build with ipatests
%define with_ipatests 1
%define with_ipatests_option --with-ipatests

%define with_python3 0

# lint is not executed during rpmbuild
# %%define with_lint 1
%if 0%{?with_lint}
    %define linter_options --enable-pylint --with-jslint
%else
    %define linter_options --disable-pylint --without-jslint
%endif

%define krb5_version 1.15.2
%define python_netaddr_version 0.7.5
# 0.7.16: https://github.com/drkjam/netaddr/issues/71
# Require 4.7.0 which brings Python 3 bindings
%define samba_version 4.6.8
%define selinux_policy_version 3.11.1
%define slapi_nis_version 0.56.1

%define plugin_dir %_libdir/dirsrv/plugins
%define etc_systemd_dir %_sysconfdir/systemd/system

Name: freeipa
Version: 4.6.1
Release: alt2%ubt
Summary: The Identity, Policy and Audit system

Group: System/Base
License: GPLv3+
Url: http://www.freeipa.org/
Source0: %name-%version.tar
Source1: freeipa-server.filetrigger 
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires(pre): rpm-macros-apache2
BuildRequires: rpm-macros-webserver-common
BuildRequires: rpm-build-python
BuildRequires: rpm-build-python3
BuildRequires: libkrb5-devel >= %krb5_version
BuildRequires: java-1.8.0-openjdk-headless
BuildRequires: libldap-devel
BuildRequires: libsasl2-devel
BuildRequires: libsystemd-devel

BuildRequires: libxmlrpc-devel
BuildRequires: libpopt-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: python-dev
BuildRequires: python-module-setuptools >= 36.5.0
BuildRequires: python-module-pyparsing
BuildRequires: python-module-execnet
BuildRequires: python-module-mock
BuildRequires: python-module-appdirs
BuildRequires: python3-module-pyparsing
BuildRequires: python3-module-execnet
BuildRequires: python3-module-mock
BuildRequires: python3-module-appdirs
%if 0%{?with_python3}
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools >= 36.5.0
%endif # with_python3
BuildRequires: systemd
BuildRequires: apache2-base
BuildRequires: libnspr-devel
BuildRequires: libnss-devel
BuildRequires: libssl-devel
BuildRequires: libini_config-devel
BuildRequires: libsasl2-devel
BuildRequires: 389-ds-base-devel >= 1.3.3.9
BuildRequires: libsvrcore-devel
BuildRequires: samba-devel >= 4.0.0
BuildRequires: libtalloc-devel
BuildRequires: libtevent-devel
BuildRequires: libuuid-devel
BuildRequires: libsss_idmap-devel
BuildRequires: libsss_certmap-devel
BuildRequires: libsss_nss_idmap-devel >= 1.15.3
BuildRequires: rhino
BuildRequires: libverto-devel
BuildRequires: libunistring-devel
BuildRequires: python-module-lesscpy

#
# Build dependencies for makeapi/makeaci
# makeapi/makeaci is using Python 2 only for now
#
BuildRequires: python-module-pyldap
BuildRequires: python-module-netaddr
BuildRequires: python-module-pyasn1 >= 0.3.2
BuildRequires: python-module-pyasn1-modules >= 0.1.5
BuildRequires: python-module-dns
BuildRequires: python-module-six
BuildRequires: python-module-sss_nss_idmap
BuildRequires: python-module-cffi

#
# Build dependencies for wheel packaging and PyPI upload
#
#%%if 0%%{?with_wheels}
#BuildRequires:  dbus-glib-devel
#BuildRequires:  libffi-devel
#BuildRequires:  python2-tox
#BuildRequires:  python2-twine
#BuildRequires:  python2-wheel
#%%if 0%%{?with_python3}
#BuildRequires:  python3-tox
#BuildRequires:  python3-twine
#BuildRequires:  python3-wheel
#%%endif
#%%endif # with_wheels

#
# Build dependencies for lint
#
%if 0%{?with_lint}
BuildRequires: python-module-cryptography >= 1.6
BuildRequires: python-module-gssapi >= 1.2.2
BuildRequires: pylint >= 1.7
BuildRequires: python-module-polib
BuildRequires: python-module-ipa_hbac
BuildRequires: python-module-lxml
BuildRequires: python-module-qrcode >= 5.0.0
BuildRequires: python-module-dns >= 1.15
#BuildRequires:  jsl
BuildRequires: python-module-yubico
# pki Python package
BuildRequires: pki-base
BuildRequires: python-module-pytest-multihost
BuildRequires: python-module-pytest_sourceorder
# 0.4.2: Py3 fix https://bugzilla.redhat.com/show_bug.cgi?id=1476150
BuildRequires: python-module-jwcrypto >= 0.4.2
# 0.3: sd_notify (https://pagure.io/freeipa/issue/5825)
BuildRequires: python-module-custodia >= 0.5.0
BuildRequires: python-module-dbus
BuildRequires: python-module-dateutil
BuildRequires: python-module-enum34
BuildRequires: python-module-netifaces
BuildRequires: python-module-sss
BuildRequires: python-module-sss-murmur
BuildRequires: python-module-sssdconfig
BuildRequires: python-module-nose
BuildRequires: python-module-paste
BuildRequires: python-module-systemd
BuildRequires: python-module-jinja2
BuildRequires: python-module-augeas

%if 0%{?with_python3}
#BuildRequires:  python3-module-samba added smbc
BuildRequires: python3-module-smbc
# 1.6: x509.Name.rdns (https://github.com/pyca/cryptography/issues/3199)
BuildRequires: python3-module-cryptography >= 1.6
BuildRequires: python3-module-gssapi >= 1.2.2
BuildRequires: pylint-py3 >= 1.7
# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1096506
BuildRequires: python3-module-polib
BuildRequires: python3-module-ipa_hbac
BuildRequires: python3-module-memcached
BuildRequires: python3-module-lxml
BuildRequires: python3-module-qrcode >= 5.0.0
BuildRequires: python3-module-dns >= 1.15
BuildRequires: python3-module-yubico
# pki Python package
BuildRequires: pki-base-python3
BuildRequires: python3-module-pytest-multihost
BuildRequires: python3-module-pytest_sourceorder
# 0.4.2: Py3 fix https://bugzilla.redhat.com/show_bug.cgi?id=1476150
BuildRequires: python3-module-jwcrypto >= 0.4.2
# 0.3: sd_notify (https://pagure.io/freeipa/issue/5825)
BuildRequires: python3-module-custodia >= 0.5.0
BuildRequires: python3-module-dbus
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-enum34
BuildRequires: python3-module-netifaces
BuildRequires: python3-module-sss
BuildRequires: python3-module-sss-murmur
BuildRequires: python3-module-sssdconfig
BuildRequires: python3-module-libsss_nss_idmap
BuildRequires: python3-module-nose
BuildRequires: python3-module-paste
BuildRequires: python3-module-systemd
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-augeas
BuildRequires: python3-module-netaddr
BuildRequires: python3-module-pyasn1
BuildRequires: python3-module-pyasn1-modules
BuildRequires: python3-module-pyldap
%endif # with_python3
%endif # with_lint

#
# Build dependencies for unit tests
#
BuildRequires: libcmocka-devel
BuildRequires: nss_wrapper
# Required by ipa_kdb_tests

%description
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).

%package server
Summary: The IPA authentication server
Group: System/Base
Requires: %name-server-common = %version-%release
Requires: %name-client = %version-%release
Requires: %name-common = %version-%release
%if 0%{?with_python3}
Requires: python3-module-ipaserver = %version-%release
%else
Requires: python-module-ipaserver = %version-%release
%endif
Requires: 389-ds-base >= 1.3.5.14
Requires: openldap-clients > 2.4.35
Requires: libnss >= 3.14.3
Requires: nss-utils >= 3.14.3
Requires: krb5-kdc >= %krb5_version
Requires: krb5-kinit >= %krb5_version
Requires: libsasl2-plugin-gssapi
Requires: openntpd
Requires: apache2-base >= 2.4.6
%if 0%with_python3
Requires: python3-mod_wsgi
%else
Requires: apache2-mod_wsgi
%endif
Requires: apache2-mod_auth_gssapi >= 1.6.0
# 1.0.14-3: https://bugzilla.redhat.com/show_bug.cgi?id=1431206
Requires: apache2-mod_nss >= 1.0.14-alt3
# 0.9.9: https://github.com/adelton/mod_lookup_identity/pull/3
Requires: mod_lookup_identity >= 1.0.0
Requires: python-module-pyldap >= 2.4.15
Requires: python-module-gssapi >= 1.2.2
Requires: acl
Requires: systemd >= 38
Requires(pre): shadow-utils
Requires: selinux-policy >= %selinux_policy_version
Requires(post): selinux-policy-base >= %selinux_policy_version
Requires: slapi-nis >= %slapi_nis_version
Requires: pki-ca >= 10.4.8
Requires: pki-kra >= 10.4.8
Requires: python-module-systemd
Requires: policycoreutils >= 2.1.5
Requires: tar
# certmonger-0.79.4-2 fixes newlines in PEM files
#Requires(pre): certmonger >= 0.79.4
Requires(pre): certmonger
Requires: 389-ds-base >= 1.3.5.14
Requires: fonts-font-awesome
Requires: fonts-ttf-open-sans
Requires: openssl
Requires: softhsm >= 2.0.0
Requires: libp11-kit
Requires: %etc_systemd_dir
Requires: gzip
Requires: oddjob
# 0.7.0-2: https://pagure.io/gssproxy/pull-request/172
Requires: gssproxy >= 0.7.0
# 1.15.2: FindByNameAndCertificate (https://pagure.io/SSSD/sssd/issue/3050)
Requires: sssd-dbus >= 1.15.2

# upgrade path from monolithic -server to -server + -server-dns
Obsoletes: %name-server <= 4.2.0

# Versions of nss-pam-ldapd < 0.8.4 require a mapping from uniqueMember to
# member.
Conflicts: nss-ldapd < 0.8.4

%description server
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are installing an IPA server, you need to install this package.

%package -n python-module-ipaserver
Summary: Python libraries used by IPA server
Group: System/Libraries
BuildArch: noarch
Requires: %name-server-common = %version-%release
Requires: %name-common = %version-%release
Requires: python-module-ipaclient = %version-%release
Requires: python-module-custodia >= 0.5.0
Requires: python-module-pyldap >= 2.4.15
Requires: python-module-lxml
Requires: python-module-gssapi >= 1.2.2
Requires: python-module-sssdconfig
Requires: python-module-pyasn1 >= 0.3.2
Requires: python-module-dbus
Requires: python-module-dns >= 1.15
Requires: python-module-kdcproxy >= 0.3
#Requires: rpm-libs
Requires: pki-base
Requires: python-module-augeas

%description -n python-module-ipaserver
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are installing an IPA server, you need to install this package.

%if 0%{?with_python3}

%package -n python3-module-ipaserver
Summary: Python libraries used by IPA server
Group: System/Libraries
BuildArch: noarch
Requires: %name-server-common = %version-%release
Requires: %name-common = %version-%release
Requires: python3-module-ipaclient = %version-%release
Requires: python3-module-custodia >= 0.5.0
Requires(pre): python3-module-pyldap >= 2.4.35
Requires: python3-module-lxml
Requires: python3-module-gssapi >= 1.2.2
#Requires: python3-module-sssdconfig
Requires: python3-module-pyasn1 >= 0.3.2
Requires: python3-module-dbus
Requires: python3-module-dns >= 1.15
#Requires: python3-module-kdcproxy >= 0.3
Requires: python3-module-augeas
#Requires: rpm-libs
#Requires: pki-base-python3

%description -n python3-module-ipaserver
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are installing an IPA server, you need to install this package.

%endif  # with_python3

%package server-common
Summary: Common files used by IPA server
Group: System/Base
BuildArch: noarch
Requires: %name-client-common = %version-%release
Requires: apache2-base >= 2.4.6
Requires: systemd >= 38
Requires: custodia >= 0.5.0
Requires: fonts-font-awesome
Requires: fonts-ttf-open-sans


%description server-common
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are installing an IPA server, you need to install this package.

%package server-dns
Summary: IPA integrated DNS server with support for automatic DNSSEC signing
Group: System/Base
BuildArch: noarch
Requires: %name-server = %version-%release
Requires: bind-dyndb-ldap >= 11.0
Requires: bind >= 9.11.0
Requires: bind-utils >= 9.11.0
Requires: opendnssec >= 1.4.6
# Keep python2 dependencies until DNSSEC daemons are ported to Python 3
Requires: python
Requires: python-module-freeipa
Requires: python-module-ipaserver


# upgrade path from monolithic -server to -server + -server-dns
Obsoletes: %name-server <= 4.2.0

%description server-dns
IPA integrated DNS server with support for automatic DNSSEC signing.
Integrated DNS server is BIND 9. OpenDNSSEC provides key management.

%package server-trust-ad
Summary: Virtual package to install packages required for Active Directory trusts
Group: System/Base
Requires: %name-server = %version-%release
Requires: %name-common = %version-%release

Requires: samba >= %samba_version
Requires: samba-winbind
Requires: libsss_idmap

%if 0%{?with_python3}
Requires: python3-module-samba
Requires: python3-module-sss_nss_idmap
Requires: python3-module-sss
%else
Requires: python-module-samba
Requires: python-module-sss_nss_idmap
Requires: python-module-sss
%endif  # with_python3


%description server-trust-ad
Cross-realm trusts with Active Directory in IPA require working Samba 4
installation. This package is provided for convenience to install all required
dependencies at once.

%package client
Summary: IPA authentication for use on clients
Group: System/Base
Requires: %name-client-common = %version-%release
Requires: %name-common = %version-%release
%if 0%{?with_python3}
Requires: python3-module-ipaclient = %version-%release
%else
Requires: python-module-ipaclient = %version-%release
%endif
Requires: python-module-pyldap
Requires: libsasl2-plugin-gssapi
Requires: openntpd
Requires: ntpdate
Requires: curl
# NIS domain name config: /usr/lib/systemd/system/*-domainname.service
#Requires: initscripts
Requires: libcurl >= 7.21.7
Requires: xmlrpc-c >= 1.27.4
Requires: sssd >= 1.14.0
Requires: sssd-krb5
Requires: sssd-ipa
Requires: libsss_sudo
Requires: python-module-sssdconfig
# certmonger-0.79.4-2 fixes newlines in PEM files
#Requires: certmonger >= 0.79.4
Requires: certmonger
Requires: nss-utils
Requires: bind-utils
Requires: oddjob-mkhomedir
Requires: python-module-gssapi >= 1.2.2
Requires: libsss_autofs
Requires: autofs
Requires: libnfsidmap
Requires: nfs-utils
Requires(post): policycoreutils


Obsoletes: %name-admintools < 4.4.1
Provides: %name-admintools = %EVR

%description client
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If your network uses IPA for authentication, this package should be
installed on every client machine.
This package provides command-line tools for IPA administrators.

%package -n python-module-ipaclient
Summary: Python libraries used by IPA client
Group: System/Libraries
BuildArch: noarch
Requires: %name-client-common = %version-%release
Requires: %name-common = %version-%release
Requires: python-module-freeipa = %version-%release
Requires: python-module-dns >= 1.15
Requires: python-module-jinja2

%description -n python-module-ipaclient
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If your network uses IPA for authentication, this package should be
installed on every client machine.

%if 0%{?with_python3}

%package -n python3-module-ipaclient
Summary: Python libraries used by IPA client
Group: System/Libraries
BuildArch: noarch
Requires: %name-client-common = %version-%release
Requires: %name-common = %version-%release
Requires: python3-module-freeipa = %version-%release
Requires: python3-module-dns >= 1.15
Requires: python3-module-jinja2

%description -n python3-module-ipaclient
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If your network uses IPA for authentication, this package should be
installed on every client machine.

%endif  # with_python3

%package client-common
Summary: Common files used by IPA client
Group: System/Base
BuildArch: noarch


%description client-common
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If your network uses IPA for authentication, this package should be
installed on every client machine.


%package -n python-module-freeipa
Summary: Python libraries used by IPA
Group: System/Libraries
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: python-module-gssapi >= 1.2.2
Requires: gnupg
Requires: libkeyutils
Requires: python-module-OpenSSL
Requires: python >= 2.7.9
Requires: python-module-cryptography >= 1.6
Requires: python-module-netaddr >= %python_netaddr_version
Requires: python-module-ipa_hbac
Requires: python-module-qrcode >= 5.0.0
Requires: python-module-pyasn1 >= 0.3.2
Requires: python-module-pyasn1-modules >= 0.1.5
Requires: python-module-dateutil
Requires: python-module-yubico >= 1.2.3
Requires: python-module-sss-murmur
Requires: python-module-dbus
Requires: python-module-setuptools
Requires: python-module-six
# 0.4.2: Py3 fix https://bugzilla.redhat.com/show_bug.cgi?id=1476150
Requires: python-module-jwcrypto >= 0.4.2
Requires: python-module-cffi
Requires: python-module-pyldap >= 2.4.15
Requires: python-module-requests
Requires: python-module-dns >= 1.15
Requires: python-module-enum34
Requires: python-module-netifaces >= 0.10.4
Requires: python-module-pyusb


%description -n python-module-freeipa
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are using IPA, you need to install this package.

%if 0%{?with_python3}

%package -n python3-module-freeipa
Summary: Python3 libraries used by IPA
Group: System/Libraries
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: python3-module-gssapi >= 1.2.2
Requires: gnupg
Requires: keyutils
Requires: python3-python-module-OpenSSL
Requires: python3-module-cryptography >= 1.6
Requires: python3-module-netaddr >= %python_netaddr_version
#Requires: python3-module-ipa_hbac
Requires: python3-module-qrcode >= 5.0.0
Requires: python3-module-pyasn1 >= 0.3.2
Requires: python3-module-pyasn1-modules >= 0.1.5
Requires: python3-module-dateutil
# fixes searching for yubikeys in python3
#Requires: python3-module-yubico >= 1.3.2-7
Requires: python3-module-sss-murmur
Requires: python3-module-dbus
Requires: python3-module-setuptools
Requires: python3-module-six
# 0.4.2: Py3 fix https://bugzilla.redhat.com/show_bug.cgi?id=1476150
Requires: python3-module-jwcrypto >= 0.4.2
Requires: python3-module-cffi
# we need pre-requires since earlier versions may break upgrade
Requires: python3-module-pyldap >= 2.4.35
Requires: python3-module-requests
Requires: python3-module-dns >= 1.15
Requires: python3-module-netifaces >= 0.10.4
#Requires: python3-module-pyusb

%description -n python3-module-freeipa
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are using IPA with Python 3, you need to install this package.

%endif # with_python3

%package common
Summary: Common files used by IPA
Group: System/Libraries
BuildArch: noarch


%description common
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are using IPA, you need to install this package.

%if 0%{?with_ipatests}

%package -n python-module-ipatests
Summary: IPA tests and test tools
Group: System/Base
BuildArch: noarch
Obsoletes: %name-tests <= 4.4.4
Provides: %name-tests = %EVR
Requires: python-module-ipaclient = %version-%release
Requires: python-module-ipaserver = %version-%release
Requires: tar
Requires: xz
Requires: python-module-nose
Requires: pytest >= 2.6
Requires: python-module-paste
Requires: python-module-coverage
# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1096506
Requires: python-module-polib
#Requires: python-pytest-multihost >= 0.5
Requires: python-module-pytest-multihost
Requires: python-module-pytest_sourceorder
#Requires: ldns-utils
Requires: python-module-sssdconfig
Requires: python-module-cryptography >= 1.6
Requires: iptables


%description -n python-module-ipatests
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
This package contains tests that verify IPA functionality.

%if 0%{?with_python3}

%package -n python3-module-ipatests
Summary: IPA tests and test tools
Group: System/Base
BuildArch: noarch
Requires: python3-module-ipaclient = %version-%release
Requires: python3-module-ipaserver = %version-%release
Requires: tar
Requires: xz
Requires: python3-module-nose
Requires: python3-module-pytest >= 2.6
Requires: python3-module-coverage
Requires: python3-module-polib
Requires: python3-module-pytest-multihost >= 0.5
#Requires: python3-module-pytest_sourceorder
#Requires: ldns-utils
Requires: python3-module-sssdconfig
Requires: python3-module-cryptography >= 1.6
Requires: iptables

%description -n python3-module-ipatests
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
This package contains tests that verify IPA functionality under Python 3.

%endif # with_python3

%endif # with_ipatests

%prep
%setup -n %name-%version
%patch -p1
%if 0%{?with_python3}
# Workaround: We want to build Python things twice. To be sure we do not mess
# up something, do two separate builds in separate directories.
cp -r %_builddir/freeipa-%version %_builddir/freeipa-%version-python3
%endif # with_python3

%build
# UI compilation segfaulted on some arches when the stack was lower (#1040576)
export JAVA_STACK_SIZE="8m"
# PATH is workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1005235
export PYTHON=%__python
# Workaround: make sure all shebangs are pointing to Python 2
# This should be solved properly using setuptools
# and this hack should be removed.
find \
	! -name '*.pyc' -a \
	! -name '*.pyo' -a \
	-type f -exec grep -qsm1 '^#!.*\bpython' {} \; \
	-exec sed -i -e '1 s|^#!.*\bpython[^ ]*|#!%__python|' {} \;

%if 0%{?with_python3}
# TODO: temporary solution until all scripts are ported to python3,
# TODO: workaround: some scripts are copied over, so the are always py2.
# We have to explicitly set python3 here for ported files here
PY3_SUBST_PATHS='
client/ipa-certupdate
client/ipa-client-automount
client/ipa-client-install
daemons/ipa-otpd/test.py
install/certmonger/ipa-server-guard
install/certmonger/dogtag-ipa-ca-renew-agent-submit
install/oddjob/com.redhat.idm.trust-fetch-domains
install/restart_scripts/renew_ra_cert_pre
install/restart_scripts/renew_ca_cert
install/restart_scripts/renew_ra_cert
install/restart_scripts/restart_httpd
install/restart_scripts/renew_kdc_cert
install/restart_scripts/stop_pkicad
install/restart_scripts/restart_dirsrv
install/tools/ipa-advise
install/tools/ipa-adtrust-install
install/tools/ipa-backup
install/tools/ipa-ca-install
install/tools/ipa-cacert-manage
install/tools/ipa-compat-manage
install/tools/ipa-csreplica-manage
install/tools/ipa-custodia
install/tools/ipa-dns-install
install/tools/ipa-httpd-kdcproxy
install/tools/ipa-kra-install
install/tools/ipa-ldap-updater
install/tools/ipa-managed-entries
install/tools/ipa-nis-manage
install/tools/ipa-otptoken-import
install/tools/ipa-pkinit-manage
install/tools/ipa-pki-retrieve-key
install/tools/ipa-replica-conncheck
install/tools/ipa-replica-install
install/tools/ipa-replica-manage
install/tools/ipa-replica-prepare
install/tools/ipa-restore
install/tools/ipa-server-certinstall
install/tools/ipa-server-install
install/tools/ipa-server-upgrade
install/tools/ipa-winsync-migrate
install/tools/ipactl
ipa
'
for P in $PY3_SUBST_PATHS; do
    sed -i -e '1 s|^#!\s\?.*\bpython[0-9]*|#!%__python3|' $P
done;

%endif # with_python3
%autoreconf
%configure --with-vendor-suffix=-%release \
           --enable-server \
           --with-ipatests \
	   --with-ipaplatform=altlinux \
	   IPA_VERSION_IS_GIT_SNAPSHOT=no \
           %linter_options

%make_build

%if 0%{?with_python3}
pushd %_builddir/freeipa-%version-python3
export PYTHON=%__python3
# Workaround: make sure all shebangs are pointing to Python 3
# This should be solved properly using setuptools
# and this hack should be removed.
find \
	! -name '*.pyc' -a \
	! -name '*.pyo' -a \
	-type f -exec grep -qsm1 '^#!.*\bpython' {} \; \
	-exec sed -i -e '1 s|^#!.*\bpython[^ ]*|#!%__python3|' {} \;
%autoreconf 
%configure --with-vendor-suffix=-%release \
           --enable-server \
           --with-ipatests \
	   --with-ipaplatform=altlinux \
	   IPA_VERSION_IS_GIT_SNAPSHOT=no \
           %linter_options
popd
%endif # with_python3


%install
# Please put as much logic as possible into make install. It allows:
# - easier porting to other distributions
# - rapid devel & install cycle using make install
#   (instead of full RPM build and installation each time)
#
# All files and directories created by spec install should be marked as ghost.
# (These are typically configuration files created by IPA installer.)
# All other artifacts should be created by make install.
#
# Exception to this rule are test programs which where want to install
# Python2/3 versions at the same time so we need to rename them. Yuck.

%if 0%{?with_python3}
# Python 3 installation needs to be done first. Subsequent Python 2 install
# will overwrite /usr/bin/ipa and other scripts with variants using
# python2 shebang.
pushd %_builddir/freeipa-%version-python3
(cd ipaclient && %makeinstall_std)
(cd ipalib && %makeinstall_std)
(cd ipaplatform && %makeinstall_std)
(cd ipapython && %makeinstall_std)
(cd ipaserver && %makeinstall_std)
(cd ipatests && %makeinstall_std)
popd

%if 0%{?with_ipatests}
mv %buildroot%_bindir/ipa-run-tests %buildroot%_bindir/ipa-run-tests-%_python3_version
mv %buildroot%_bindir/ipa-test-config %buildroot%_bindir/ipa-test-config-%_python3_version
mv %buildroot%_bindir/ipa-test-task %buildroot%_bindir/ipa-test-task-%_python3_version
ln -s %_bindir/ipa-run-tests-%_python3_version %buildroot%_bindir/ipa-run-tests-3
ln -s %_bindir/ipa-test-config-%_python3_version %buildroot%_bindir/ipa-test-config-3
ln -s %_bindir/ipa-test-task-%_python3_version %buildroot%_bindir/ipa-test-task-3
%endif # with_ipatests

%endif # with_python3

# Python 2 installation
%makeinstall_std

%if 0%{?with_ipatests}
mv %buildroot%_bindir/ipa-run-tests %buildroot%_bindir/ipa-run-tests-%__python_version
mv %buildroot%_bindir/ipa-test-config %buildroot%_bindir/ipa-test-config-%__python_version
mv %buildroot%_bindir/ipa-test-task %buildroot%_bindir/ipa-test-task-%__python_version
ln -s %_bindir/ipa-run-tests-%__python_version %buildroot%_bindir/ipa-run-tests-2
ln -s %_bindir/ipa-test-config-%__python_version %buildroot%_bindir/ipa-test-config-2
ln -s %_bindir/ipa-test-task-%__python_version %buildroot%_bindir/ipa-test-task-2
# test framework defaults to Python 2
ln -s %_bindir/ipa-run-tests-%__python_version %buildroot%_bindir/ipa-run-tests
ln -s %_bindir/ipa-test-config-%__python_version %buildroot%_bindir/ipa-test-config
ln -s %_bindir/ipa-test-task-%__python_version %buildroot%_bindir/ipa-test-task
%endif # with_ipatests

# remove files which are useful only for make uninstall
find %buildroot -wholename '*/site-packages/*/install_files.txt' -exec rm {} \;


%find_lang ipa

# Remove .la files from libtool - we don't want to package
# these files
rm %buildroot/%plugin_dir/libipa_pwd_extop.la
rm %buildroot/%plugin_dir/libipa_enrollment_extop.la
rm %buildroot/%plugin_dir/libipa_winsync.la
rm %buildroot/%plugin_dir/libipa_repl_version.la
rm %buildroot/%plugin_dir/libipa_uuid.la
rm %buildroot/%plugin_dir/libipa_modrdn.la
rm %buildroot/%plugin_dir/libipa_lockout.la
rm %buildroot/%plugin_dir/libipa_cldap.la
rm %buildroot/%plugin_dir/libipa_dns.la
rm %buildroot/%plugin_dir/libipa_sidgen.la
rm %buildroot/%plugin_dir/libipa_sidgen_task.la
rm %buildroot/%plugin_dir/libipa_extdom_extop.la
rm %buildroot/%plugin_dir/libipa_range_check.la
rm %buildroot/%plugin_dir/libipa_otp_counter.la
rm %buildroot/%plugin_dir/libipa_otp_lasttoken.la
rm %buildroot/%plugin_dir/libtopology.la
rm %buildroot/%_libdir/krb5/plugins/kdb/ipadb.la
rm %buildroot/%_libdir/samba/pdb/ipasam.la

# So we can own our Apache configuration
mkdir -p %buildroot%apache2_confdir/{sites-available,extra-available,extra-enabled}
/bin/touch %buildroot%apache2_sites_available/ipa.conf
/bin/touch %buildroot%apache2_extra_enabled/ipa-kdc-proxy.conf
/bin/touch %buildroot%apache2_extra_enabled/ipa-pki-proxy.conf
/bin/touch %buildroot%apache2_confdir/ipa-rewrite.conf
/bin/touch %buildroot%_datadir/ipa/html/ca.crt
/bin/touch %buildroot%_datadir/ipa/html/krb.con
/bin/touch %buildroot%_datadir/ipa/html/krb5.ini
/bin/touch %buildroot%_datadir/ipa/html/krbrealm.con

#mkdir -p %%buildroot%%_libdir/krb5/plugins/libkrb5
#touch %%buildroot%%_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so


/bin/touch %buildroot%_sysconfdir/ipa/default.conf
/bin/touch %buildroot%_sysconfdir/ipa/ca.crt

mkdir -p %buildroot%etc_systemd_dir/httpd2.service.d
touch %buildroot%etc_systemd_dir/httpd2.service.d/ipa.conf

mkdir -p %buildroot%_sysconfdir/cron.d

mkdir -p %buildroot%_sharedstatedir/kdcproxy
mkdir -p %buildroot%_sharedstatedir/ipa/backup
mkdir -p %buildroot%_sharedstatedir/ipa/gssproxy
mkdir -p %buildroot%_sharedstatedir/ipa/sysrestore
mkdir -p %buildroot%_sharedstatedir/ipa/sysupgrade
mkdir -p %buildroot%_sharedstatedir/ipa/pki-ca
mkdir -p %buildroot%_sharedstatedir/bind/zone/dyndb-ldap
mkdir -p %buildroot%_sharedstatedir/bind/data
mkdir -p %buildroot%_sharedstatedir/bind/dynamic
touch %buildroot%_sharedstatedir/bind/zone/dyndb-ldap/ipa
touch %buildroot%_sharedstatedir/ipa/pki-ca/publish
touch %buildroot%_sysconfdir/ipa/kdcproxy/ipa-kdc-proxy.conf

# NSS
touch %buildroot%_sysconfdir/ipa/nssdb/cert8.db
touch %buildroot%_sysconfdir/ipa/nssdb/key3.db
touch %buildroot%_sysconfdir/ipa/nssdb/secmod.db
touch %buildroot%_sysconfdir/ipa/nssdb/pwdfile.txt

mkdir -p %buildroot%_sysconfdir/pki/ca-trust/source
touch %buildroot%_sysconfdir/pki/ca-trust/source/ipa.p11-kit

mkdir -p %buildroot%_sharedstatedir/ipa-client
mkdir -p %buildroot%_sharedstatedir/ipa-client/pki
mkdir -p %buildroot%_sharedstatedir/ipa-client/sysrestore

mkdir -p %buildroot%_runtimedir
install -d -m 0700 %buildroot%_runtimedir/ipa/

# install filetrigger
mkdir -p %buildroot%_rpmlibdir
install -D -p -m 0755 %SOURCE1 %buildroot%_rpmlibdir/freeipa-server.filetrigger

%check
%make %{?_smp_mflags} check VERBOSE=yes LIBDIR=%_libdir

%post server
# NOTE: systemd specific section
    /bin/systemctl --system daemon-reload 2>&1 ||:
# END
if [ $1 -gt 1 ] ; then
    /bin/systemctl condrestart certmonger.service 2>&1 ||:
fi
/bin/systemctl reload-or-try-restart dbus ||:
/bin/systemctl reload-or-try-restart oddjobd ||:

%tmpfiles_create ipa.conf

%preun server
if [ $1 = 0 ]; then
# NOTE: systemd specific section
    /bin/systemctl --quiet stop ipa.service ||:
    /bin/systemctl --quiet disable ipa.service ||:
    /bin/systemctl reload-or-try-restart dbus ||:
    /bin/systemctl reload-or-try-restart oddjobd ||:
# END
fi

%triggerpostun server-common -- freeipa-server-common <= 4.6.1
if /usr/bin/python -c "import sys; from ipaserver.install import installutils; sys.exit(0 if installutils.is_ipa_configured() else 1);" > /dev/null 2>&1; then
        a2dismod ipa-nss >/dev/null 2>&1 ||:

        if systemctl is-enabled httpd2.service >/dev/null 2>&1; then
                systemctl try-restart httpd2.service >/dev/null 2>&1 ||:
        fi
fi

%pre server
# Stop ipa_kpasswd if it exists before upgrading so we don't have a
# zombie process when we're done.
if [ -e /usr/sbin/ipa_kpasswd ]; then
# NOTE: systemd specific section
    /bin/systemctl stop ipa_kpasswd.service >/dev/null 2>&1 ||:
# END
fi

# create users and groups
# create kdcproxy group and user
getent group kdcproxy >/dev/null || groupadd -f -r kdcproxy ||:
getent passwd kdcproxy >/dev/null || useradd -r -g kdcproxy -s /sbin/nologin -d / -c "IPA KDC Proxy User" kdcproxy ||:
# create ipaapi group and user
getent group ipaapi >/dev/null || groupadd -f -r ipaapi ||:
getent passwd ipaapi >/dev/null || useradd -r -g ipaapi -s /sbin/nologin -d / -c "IPA Framework User" ipaapi ||:
# add apache to ipaaapi group
id -Gn apache2 | grep '\bipaapi\b' >/dev/null || usermod apache2 -a -G ipaapi ||:


#%%posttrans server-trust-ad
#python2 -c "import sys; from ipaserver.install import installutils; sys.exit(0 if installutils.is_ipa_configured() else 1);" > /dev/null 2>&1
#if [  $? -eq 0 ]; then
## NOTE: systemd specific section
#    /bin/systemctl try-restart httpd.service >/dev/null 2>&1 || :
## END
#fi


%post client
if [ $1 -gt 1 ] ; then
    # Has the client been configured?
    restore=0
    test -f '/var/lib/ipa-client/sysrestore/sysrestore.index' && restore=$(wc -l '/var/lib/ipa-client/sysrestore/sysrestore.index' | awk '{print $1}') ||:

    if [ -f '/etc/sssd/sssd.conf' -a $restore -ge 2 ]; then
        if ! grep -E -q '/var/lib/sss/pubconf/krb5.include.d/' /etc/krb5.conf  2>/dev/null ; then
            echo "includedir /var/lib/sss/pubconf/krb5.include.d/" > /etc/krb5.conf.ipanew
            cat /etc/krb5.conf >> /etc/krb5.conf.ipanew
            mv -Z /etc/krb5.conf.ipanew /etc/krb5.conf
        fi
    fi

    if [ $restore -ge 2 ]; then
        if grep -E -q '\s*pkinit_anchors = FILE:/etc/ipa/ca.crt$' /etc/krb5.conf 2>/dev/null; then
            sed -E 's|(\s*)pkinit_anchors = FILE:/etc/ipa/ca.crt$|\1pkinit_anchors = FILE:/var/lib/ipa-client/pki/kdc-ca-bundle.pem\n\1pkinit_pool = FILE:/var/lib/ipa-client/pki/ca-bundle.pem|' /etc/krb5.conf >/etc/krb5.conf.ipanew
            mv -Z /etc/krb5.conf.ipanew /etc/krb5.conf
            cp /etc/ipa/ca.crt /var/lib/ipa-client/pki/kdc-ca-bundle.pem
            cp /etc/ipa/ca.crt /var/lib/ipa-client/pki/ca-bundle.pem
        fi
    fi

    if [ $restore -ge 2 ]; then
        python2 -c 'from ipaclient.install.client import update_ipa_nssdb; update_ipa_nssdb()' >/var/log/ipaupgrade.log 2>&1
    fi
fi

%triggerin client -- openssh-server
# Has the client been configured?
restore=0
test -f '/var/lib/ipa-client/sysrestore/sysrestore.index' && restore=$(wc -l '/var/lib/ipa-client/sysrestore/sysrestore.index' | awk '{print $1}') ||:

if [ -f '/etc/openssh/sshd_config' -a $restore -ge 2 ]; then
    if grep -E -q '^(AuthorizedKeysCommand /usr/bin/sss_ssh_authorizedkeys|PubKeyAgent /usr/bin/sss_ssh_authorizedkeys %%u)$' /etc/openssh/sshd_config 2>/dev/null; then
        sed -r '
            /^(AuthorizedKeysCommand(User|RunAs)|PubKeyAgentRunAs)[ \t]/ d
        ' /etc/openssh/sshd_config >/etc/openssh/sshd_config.ipanew

        if /usr/sbin/sshd -t -f /dev/null -o 'AuthorizedKeysCommand=/usr/bin/sss_ssh_authorizedkeys' -o 'AuthorizedKeysCommandUser=nobody' 2>/dev/null; then
            sed -ri '
                s/^PubKeyAgent (.+) %%u$/AuthorizedKeysCommand \1/
                s/^AuthorizedKeysCommand .*$/\0\nAuthorizedKeysCommandUser nobody/
            ' /etc/openssh/sshd_config.ipanew
        elif /usr/sbin/sshd -t -f /dev/null -o 'AuthorizedKeysCommand=/usr/bin/sss_ssh_authorizedkeys' -o 'AuthorizedKeysCommandRunAs=nobody' 2>/dev/null; then
            sed -ri '
                s/^PubKeyAgent (.+) %%u$/AuthorizedKeysCommand \1/
                s/^AuthorizedKeysCommand .*$/\0\nAuthorizedKeysCommandRunAs nobody/
            ' /etc/openssh/sshd_config.ipanew
        elif /usr/sbin/sshd -t -f /dev/null -o 'PubKeyAgent=/usr/bin/sss_ssh_authorizedkeys %%u' -o 'PubKeyAgentRunAs=nobody' 2>/dev/null; then
            sed -ri '
                s/^AuthorizedKeysCommand (.+)$/PubKeyAgent \1 %%u/
                s/^PubKeyAgent .*$/\0\nPubKeyAgentRunAs nobody/
            ' /etc/openssh/sshd_config.ipanew
        fi

        mv -Z /etc/openssh/sshd_config.ipanew /etc/openssh/sshd_config
        chmod 600 /etc/openssh/sshd_config

        /bin/systemctl condrestart sshd.service 2>&1 ||:
    fi
fi


%files server
%doc COPYING README.md Contributors.txt
%_sbindir/ipa-backup
%_sbindir/ipa-restore
%_sbindir/ipa-ca-install
%_sbindir/ipa-kra-install
%_sbindir/ipa-server-install
%_sbindir/ipa-replica-conncheck
%_sbindir/ipa-replica-install
%_sbindir/ipa-replica-prepare
%_sbindir/ipa-replica-manage
%_sbindir/ipa-csreplica-manage
%_sbindir/ipa-server-certinstall
%_sbindir/ipa-server-upgrade
%_sbindir/ipa-ldap-updater
%_sbindir/ipa-otptoken-import
%_sbindir/ipa-compat-manage
%_sbindir/ipa-nis-manage
%_sbindir/ipa-managed-entries
%_sbindir/ipactl
%_sbindir/ipa-advise
%_sbindir/ipa-cacert-manage
%_sbindir/ipa-winsync-migrate
%_sbindir/ipa-pkinit-manage
%_libexecdir/certmonger/dogtag-ipa-ca-renew-agent-submit
%_libexecdir/certmonger/ipa-server-guard
%dir %_libexecdir/ipa
%_libexecdir/ipa/ipa-custodia
%_libexecdir/ipa/ipa-dnskeysyncd
%_libexecdir/ipa/ipa-dnskeysync-replica
%_libexecdir/ipa/ipa-ods-exporter
%_libexecdir/ipa/ipa-httpd-kdcproxy
%_libexecdir/ipa/ipa-pki-retrieve-key
%_libexecdir/ipa/ipa-otpd
%dir %_libexecdir/ipa/oddjob
%attr(0755,root,root) %_libexecdir/ipa/oddjob/org.freeipa.server.conncheck
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.freeipa.server.conf
%config(noreplace) %_sysconfdir/oddjobd.conf.d/ipa-server.conf
%dir %_libexecdir/ipa/certmonger
%attr(755,root,root) %_libexecdir/ipa/certmonger/*
# NOTE: systemd specific section
%attr(644,root,root) %_unitdir/ipa.service
%attr(644,root,root) %_unitdir/ipa-otpd.socket
%attr(644,root,root) %_unitdir/ipa-otpd@.service
%attr(644,root,root) %_unitdir/ipa-dnskeysyncd.service
%attr(644,root,root) %_unitdir/ipa-ods-exporter.socket
%attr(644,root,root) %_unitdir/ipa-ods-exporter.service
# END
%attr(755,root,root) %plugin_dir/libipa_pwd_extop.so
%attr(755,root,root) %plugin_dir/libipa_enrollment_extop.so
%attr(755,root,root) %plugin_dir/libipa_winsync.so
%attr(755,root,root) %plugin_dir/libipa_repl_version.so
%attr(755,root,root) %plugin_dir/libipa_uuid.so
%attr(755,root,root) %plugin_dir/libipa_modrdn.so
%attr(755,root,root) %plugin_dir/libipa_lockout.so
%attr(755,root,root) %plugin_dir/libipa_cldap.so
%attr(755,root,root) %plugin_dir/libipa_dns.so
%attr(755,root,root) %plugin_dir/libipa_range_check.so
%attr(755,root,root) %plugin_dir/libipa_otp_counter.so
%attr(755,root,root) %plugin_dir/libipa_otp_lasttoken.so
%attr(755,root,root) %plugin_dir/libtopology.so
%attr(755,root,root) %plugin_dir/libipa_sidgen.so
%attr(755,root,root) %plugin_dir/libipa_sidgen_task.so
%attr(755,root,root) %plugin_dir/libipa_extdom_extop.so
%attr(755,root,root) %_libdir/krb5/plugins/kdb/ipadb.so
%_mandir/man1/ipa-replica-conncheck.1*
%_mandir/man1/ipa-replica-install.1*
%_mandir/man1/ipa-replica-manage.1*
%_mandir/man1/ipa-csreplica-manage.1*
%_mandir/man1/ipa-replica-prepare.1*
%_mandir/man1/ipa-server-certinstall.1*
%_mandir/man1/ipa-server-install.1*
%_mandir/man1/ipa-server-upgrade.1*
%_mandir/man1/ipa-ca-install.1*
%_mandir/man1/ipa-kra-install.1*
%_mandir/man1/ipa-compat-manage.1*
%_mandir/man1/ipa-nis-manage.1*
%_mandir/man1/ipa-managed-entries.1*
%_mandir/man1/ipa-ldap-updater.1*
%_mandir/man8/ipactl.8*
%_mandir/man1/ipa-backup.1*
%_mandir/man1/ipa-restore.1*
%_mandir/man1/ipa-advise.1*
%_mandir/man1/ipa-otptoken-import.1*
%_mandir/man1/ipa-cacert-manage.1*
%_mandir/man1/ipa-winsync-migrate.1*
%_mandir/man1/ipa-pkinit-manage.1*

%_rpmlibdir/freeipa-server.filetrigger

%files -n python-module-ipaserver
%doc COPYING README.md Contributors.txt
%python_sitelibdir_noarch/ipaserver
%python_sitelibdir_noarch/ipaserver-*.egg-info

%if 0%{?with_python3}

%files -n python3-module-ipaserver
%doc COPYING README.md Contributors.txt
%python3_sitelibdir_noarch/ipaserver
%python3_sitelibdir_noarch/ipaserver-*.egg-info

%endif # with_python3

%files server-common
%doc COPYING README.md Contributors.txt
%dir %attr(0700,root,root) %_runtimedir/ipa
%ghost %verify(not user group) %dir %_sharedstatedir/kdcproxy
%dir %attr(0755,root,root) %_sysconfdir/ipa/kdcproxy
%config(noreplace) %_sysconfdir/sysconfig/ipa-dnskeysyncd
%config(noreplace) %_sysconfdir/sysconfig/ipa-ods-exporter
%config(noreplace) %_sysconfdir/ipa/kdcproxy/kdcproxy.conf
# NOTE: systemd specific section
%_tmpfilesdir/ipa.conf
%attr(644,root,root) %_unitdir/ipa-custodia.service
%ghost %attr(644,root,root) %etc_systemd_dir/httpd2.service.d/ipa.conf
# END
%dir %_datadir/ipa
%_datadir/ipa/wsgi.py*
%_datadir/ipa/kdcproxy.wsgi
%_datadir/ipa/*.ldif
%_datadir/ipa/*.uldif
%_datadir/ipa/*.template
%dir %_datadir/ipa/advise
%dir %_datadir/ipa/advise/legacy
%_datadir/ipa/advise/legacy/*.template
%dir %_datadir/ipa/profiles
%_datadir/ipa/profiles/README
%_datadir/ipa/profiles/*.cfg
%dir %_datadir/ipa/html
%_datadir/ipa/html/ssbrowser.html
%_datadir/ipa/html/unauthorized.html
%dir %_datadir/ipa/migration
%_datadir/ipa/migration/error.html
%_datadir/ipa/migration/index.html
%_datadir/ipa/migration/invalid.html
%_datadir/ipa/migration/migration.py*
%dir %_datadir/ipa/ui
%_datadir/ipa/ui/index.html
%_datadir/ipa/ui/reset_password.html
%_datadir/ipa/ui/sync_otp.html
%_datadir/ipa/ui/*.ico
%_datadir/ipa/ui/*.css
%_datadir/ipa/ui/*.js
%dir %_datadir/ipa/ui/css
%_datadir/ipa/ui/css/*.css
%dir %_datadir/ipa/ui/js
%dir %_datadir/ipa/ui/js/dojo
%_datadir/ipa/ui/js/dojo/dojo.js
%dir %_datadir/ipa/ui/js/libs
%_datadir/ipa/ui/js/libs/*.js
%dir %_datadir/ipa/ui/js/freeipa
%_datadir/ipa/ui/js/freeipa/app.js
%_datadir/ipa/ui/js/freeipa/core.js
%dir %_datadir/ipa/ui/js/plugins
%dir %_datadir/ipa/ui/images
%_datadir/ipa/ui/images/*.jpg
%_datadir/ipa/ui/images/*.png
%dir %_datadir/ipa/wsgi
%_datadir/ipa/wsgi/plugins.py*
%dir %_sysconfdir/ipa
%dir %_sysconfdir/ipa/html
%config(noreplace) %_sysconfdir/ipa/html/ssbrowser.html
%config(noreplace) %_sysconfdir/ipa/html/unauthorized.html
%ghost %attr(0644,root,apache2) %config(noreplace) %apache2_confdir/ipa-rewrite.conf
%ghost %attr(0644,root,apache2) %config(noreplace) %apache2_sites_available/ipa.conf
%ghost %attr(0644,root,apache2) %config(noreplace) %apache2_extra_enabled/ipa-kdc-proxy.conf
%ghost %attr(0644,root,apache2) %config(noreplace) %apache2_extra_enabled/ipa-pki-proxy.conf
%ghost %attr(0644,root,apache2) %config(noreplace) %_sysconfdir/ipa/kdcproxy/ipa-kdc-proxy.conf
%dir %attr(0755,root,root) %_sysconfdir/ipa/dnssec
%_datadir/ipa/ipa.conf
%_datadir/ipa/ipa-rewrite.conf
%_datadir/ipa/ipa-pki-proxy.conf
%ghost %attr(0644,root,apache2) %config(noreplace) %_datadir/ipa/html/ca.crt
%ghost %attr(0644,root,apache2) %_datadir/ipa/html/krb.con
%ghost %attr(0644,root,apache2) %_datadir/ipa/html/krb5.ini
%ghost %attr(0644,root,apache2) %_datadir/ipa/html/krbrealm.con
%dir %_datadir/ipa/updates/
%_datadir/ipa/updates/*
%dir %_sharedstatedir/ipa
%attr(700,root,root) %dir %_sharedstatedir/ipa/backup
%attr(700,root,root) %dir %_sharedstatedir/ipa/gssproxy
%attr(711,root,root) %dir %_sharedstatedir/ipa/sysrestore
%attr(700,root,root) %dir %_sharedstatedir/ipa/sysupgrade
%attr(755,root,root) %dir %_sharedstatedir/ipa/pki-ca
%attr(770,root,named) %dir %_sharedstatedir/bind/data
%attr(770,root,named) %dir %_sharedstatedir/bind/dynamic
%ghost %_sharedstatedir/ipa/pki-ca/publish
%ghost %_sharedstatedir/bind/zone/dyndb-ldap/ipa

%dir %attr(0700,root,root) %_sysconfdir/ipa/custodia
%dir %_datadir/ipa/schema.d
%attr(0644,root,root) %_datadir/ipa/schema.d/README
%attr(0644,root,root) %_datadir/ipa/gssapi.login
%_datadir/ipa/ipakrb5.aug

%files server-dns
%doc COPYING README.md Contributors.txt
%_sbindir/ipa-dns-install
%_mandir/man1/ipa-dns-install.1*

%files server-trust-ad
%doc COPYING README.md Contributors.txt
%_sbindir/ipa-adtrust-install
%_datadir/ipa/smb.conf.empty
%attr(755,root,root) %_libdir/samba/pdb/ipasam.so
%_mandir/man1/ipa-adtrust-install.1*
%_sysconfdir/dbus-1/system.d/oddjob-ipa-trust.conf
%_sysconfdir/oddjobd.conf.d/oddjobd-ipa-trust.conf
%%attr(755,root,root) %_libexecdir/ipa/oddjob/com.redhat.idm.trust-fetch-domains


%files client
%doc COPYING README.md Contributors.txt
%_sbindir/ipa-client-install
%_sbindir/ipa-client-automount
%_sbindir/ipa-certupdate
%_sbindir/ipa-getkeytab
%_sbindir/ipa-rmkeytab
%_sbindir/ipa-join
%_bindir/ipa
%config %_sysconfdir/bash_completion.d
%_mandir/man1/ipa.1*
%_mandir/man1/ipa-getkeytab.1*
%_mandir/man1/ipa-rmkeytab.1*
%_mandir/man1/ipa-client-install.1*
%_mandir/man1/ipa-client-automount.1*
%_mandir/man1/ipa-certupdate.1*
%_mandir/man1/ipa-join.1*

%files -n python-module-ipaclient
%doc COPYING README.md Contributors.txt
%dir %python_sitelibdir_noarch/ipaclient
%python_sitelibdir_noarch/ipaclient/*.py*
%dir %python_sitelibdir_noarch/ipaclient/install
%python_sitelibdir_noarch/ipaclient/install/*.py*
%dir %python_sitelibdir_noarch/ipaclient/plugins
%python_sitelibdir_noarch/ipaclient/plugins/*.py*
%dir %python_sitelibdir_noarch/ipaclient/remote_plugins
%python_sitelibdir_noarch/ipaclient/remote_plugins/*.py*
%dir %python_sitelibdir_noarch/ipaclient/remote_plugins/2_*
%python_sitelibdir_noarch/ipaclient/remote_plugins/2_*/*.py*
%dir %python_sitelibdir_noarch/ipaclient/csrgen
%dir %python_sitelibdir_noarch/ipaclient/csrgen/profiles
%python_sitelibdir_noarch/ipaclient/csrgen/profiles/*.json
%dir %python_sitelibdir_noarch/ipaclient/csrgen/rules
%python_sitelibdir_noarch/ipaclient/csrgen/rules/*.json
%dir %python_sitelibdir_noarch/ipaclient/csrgen/templates
%python_sitelibdir_noarch/ipaclient/csrgen/templates/*.tmpl
%python_sitelibdir_noarch/ipaclient-*.egg-info

%if 0%{?with_python3}

%files -n python3-module-ipaclient
%doc COPYING README.md Contributors.txt
%dir %python3_sitelibdir_noarch/ipaclient
%python3_sitelibdir_noarch/ipaclient/*.py
%python3_sitelibdir_noarch/ipaclient/__pycache__/*.py*
%dir %python3_sitelibdir_noarch/ipaclient/install
%python3_sitelibdir_noarch/ipaclient/install/*.py
%python3_sitelibdir_noarch/ipaclient/install/__pycache__/*.py*
%dir %python3_sitelibdir_noarch/ipaclient/plugins
%python3_sitelibdir_noarch/ipaclient/plugins/*.py
%python3_sitelibdir_noarch/ipaclient/plugins/__pycache__/*.py*
%dir %python3_sitelibdir_noarch/ipaclient/remote_plugins
%python3_sitelibdir_noarch/ipaclient/remote_plugins/*.py
%python3_sitelibdir_noarch/ipaclient/remote_plugins/__pycache__/*.py*
%dir %python3_sitelibdir_noarch/ipaclient/remote_plugins/2_*
%python3_sitelibdir_noarch/ipaclient/remote_plugins/2_*/*.py
%python3_sitelibdir_noarch/ipaclient/remote_plugins/2_*/__pycache__/*.py*
%dir %python3_sitelibdir_noarch/ipaclient/csrgen
%dir %python3_sitelibdir_noarch/ipaclient/csrgen/profiles
%python3_sitelibdir_noarch/ipaclient/csrgen/profiles/*.json
%dir %python3_sitelibdir_noarch/ipaclient/csrgen/rules
%python3_sitelibdir_noarch/ipaclient/csrgen/rules/*.json
%dir %python3_sitelibdir_noarch/ipaclient/csrgen/templates
%python3_sitelibdir_noarch/ipaclient/csrgen/templates/*.tmpl
%python3_sitelibdir_noarch/ipaclient-*.egg-info

%endif # with_python3

%files client-common
%doc COPYING README.md Contributors.txt
%dir %attr(0755,root,root) %_sysconfdir/ipa/
%ghost %attr(0644,root,apache2) %config(noreplace) %_sysconfdir/ipa/default.conf
%ghost %attr(0644,root,apache2) %config(noreplace) %_sysconfdir/ipa/ca.crt
%dir %attr(0755,root,root) %_sysconfdir/ipa/nssdb
%ghost %config(noreplace) %_sysconfdir/ipa/nssdb/cert8.db
%ghost %config(noreplace) %_sysconfdir/ipa/nssdb/key3.db
%ghost %config(noreplace) %_sysconfdir/ipa/nssdb/secmod.db
%ghost %config(noreplace) %_sysconfdir/ipa/nssdb/pwdfile.txt
%ghost %config(noreplace) %_sysconfdir/pki/ca-trust/source/ipa.p11-kit
%dir %_sharedstatedir/ipa-client
%dir %_sharedstatedir/ipa-client/pki
%dir %_sharedstatedir/ipa-client/sysrestore
%_mandir/man5/default.conf.5*


%files -n python-module-freeipa
%doc COPYING README.md Contributors.txt
%dir %python_sitelibdir_noarch/ipapython
%python_sitelibdir_noarch/ipapython/*.py*
%dir %python_sitelibdir_noarch/ipapython/install
%python_sitelibdir_noarch/ipapython/install/*.py*
%dir %python_sitelibdir_noarch/ipalib
%python_sitelibdir_noarch/ipalib/*.py*
%dir %python_sitelibdir_noarch/ipalib/install
%python_sitelibdir_noarch/ipalib/install/*.py*
%dir %python_sitelibdir_noarch/ipaplatform
%python_sitelibdir_noarch/ipaplatform/*
%python_sitelibdir_noarch/ipapython-*.egg-info
%python_sitelibdir_noarch/ipalib-*.egg-info
%python_sitelibdir_noarch/ipaplatform-*.egg-info

%files common -f ipa.lang
%doc COPYING README.md Contributors.txt

%if 0%{?with_python3}

%files -n python3-module-freeipa
%doc COPYING README.md Contributors.txt

%python3_sitelibdir_noarch/ipapython/
%python3_sitelibdir_noarch/ipalib/
%python3_sitelibdir_noarch/ipaplatform/
%python3_sitelibdir_noarch/ipapython-*.egg-info
%python3_sitelibdir_noarch/ipalib-*.egg-info
%python3_sitelibdir_noarch/ipaplatform-*.egg-info

%endif # with_python3

%if 0%{?with_ipatests}

%files -n python-module-ipatests
%doc COPYING README.md Contributors.txt
%python_sitelibdir_noarch/ipatests
%python_sitelibdir_noarch/ipatests-*.egg-info
%_bindir/ipa-run-tests
%_bindir/ipa-test-config
%_bindir/ipa-test-task
%_bindir/ipa-run-tests-2
%_bindir/ipa-test-config-2
%_bindir/ipa-test-task-2
%_bindir/ipa-run-tests-%__python_version
%_bindir/ipa-test-config-%__python_version
%_bindir/ipa-test-task-%__python_version
%_mandir/man1/ipa-run-tests.1*
%_mandir/man1/ipa-test-config.1*
%_mandir/man1/ipa-test-task.1*

%if 0%{?with_python3}

%files -n python3-module-ipatests
%doc COPYING README.md Contributors.txt
%python3_sitelibdir_noarch/ipatests
%python3_sitelibdir_noarch/ipatests-*.egg-info
%_bindir/ipa-run-tests-3
%_bindir/ipa-test-config-3
%_bindir/ipa-test-task-3
%_bindir/ipa-run-tests-%_python3_version
%_bindir/ipa-test-config-%_python3_version
%_bindir/ipa-test-task-%_python3_version

%endif # with_python3

%endif # with_ipatests

%changelog
* Tue Dec 12 2017 Stanislav Levin <slev@altlinux.org> 4.6.1-alt2%ubt
- Add openntpd support (based on patches from Mikhail Efremov) (closes: #34307)
- Save and restore state of apache modules during installation/uninstallation

* Sat Oct 07 2017 Stanislav Levin <slev@altlinux.org> 4.6.1-alt1%ubt
- 4.4.4 -> 4.6.1

* Thu Oct 06 2017 Stanislav Levin <slev@altlinux.org> 4.4.4-alt4%ubt
- Fix ipa client schema cache: Handle malformed server info data gracefully
- Fix ipa client requirements
- Import patches from 4.3.3-alt9

* Thu Oct 05 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt9
- selinux: Allow digits in SELinux user names (closes: #33838).
- Require zip.

* Thu Oct 4 2017 Stanislav Levin <slev@altlinux.org> 4.4.4-alt3%ubt
- Fix ipa server upgrade

* Thu Oct 2 2017 Stanislav Levin <slev@altlinux.org> 4.4.4-alt2%ubt
- Import patches from 4.3.3-alt8

* Wed Sep 27 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt8
- Fix replica creation (closes: #33513):
    + Don't try to use bundled urllib3 in the python-module-request.
    + Use ipa CA certificate for https checks.

* Thu Sep 25 2017 Stanislav Levin <slev@altlinux.org> 4.4.4-alt1%ubt
- Update to upstream's 4.4.4 version

* Thu Aug 24 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt7
- httpd2: Update existing ipa.conf for fontawesome path.

* Wed Aug 23 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt6
- Requires: fonts-ttf-fontawesome-web -> fonts-font-awesome.
- Change paths to fontawesome.

* Mon Aug 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.3-alt5
- Enabled tests.

* Thu Aug 10 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt4
- Add %%apache_conf_dir macro.
- Move ipa_configured script to server-common subpackage.
- Init argument for slapi_pblock_get() (closes: #33538).
- Fix httpd2 configuration (closes: #33513, #33466).

* Tue May 16 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt3
- server: Require pki-kra.
- Run ipa-server-upgrade at package update.
- Add ipa_configured script.
- Fix ipa-server-upgrade (closes: #33463).
- Set JAVA_STACK_SIZE to 8m.

* Wed Apr 26 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt2
- Fix build with 389-ds-1.3.6.4.

* Fri Apr 21 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt1
- client: Require bind-utils.
- client: Require krb5-kinit.
- Updated to 4.3.3.

* Tue Feb 28 2017 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt9
- Fix chown krb5.keytab.

* Tue Feb 28 2017 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt8
- Use ALT-specific SELinux users.
- Grant read access to krb5.keytab file for _keytab group.
- ipaclient: Reduce ntpdate timeout.
- client: Require ntpdate.

* Wed Feb 15 2017 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt7
- Explicitly require python-module-samba.
- Fixed %%_runtimedir/ipa_memcached permissions.
- server-trust-ad: Require samba and samba-winbind (closes: #33084).
- openntpd support.
- Change dogtag default insecure port to 8090.
- client: Require libsss_sudo.

* Mon Jan 23 2017 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt6
- client: Require nss-utils (closes: #33031).
- Patches from upstream:
  + Fixed CVE-2016-7030.
  + Fixed CVE-2016-9575.

* Mon Jan 16 2017 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt5
- bindinstance: Drop 'generating rndc key' step.
- bindinstance: Use resolvconf if needed.
- tasks: Implement {set/restore}_control_state() functions.
- Disable bind chroot and fix paths in configs.
- altlinux/tasks.py: Implement check_selinux_status().
- ipa-client-automount: Configure nsswitch.conf for sssd.
- Configure nsswitch.conf for use sssd.
- Require ntpd in the client subpackage.

* Wed Dec 28 2016 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt4
- Move some requires to client subpackage (closes: #32952).
- Require slapi-nis.
- Require fonts for web ui.
- web ui: Fix fonts.
- Use bash as default login shell.
- Update server-dns description.
- Disable DNSSEC support for now.
- Require openssl.
- Fix opendnssec paths.
- Update named.conf and paths.
- Increase httpd.service start timeout.
- Enable/disable apache2 modules/configs.
- Enable dyndb-ldap.

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

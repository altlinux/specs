%define _unpackaged_files_terminate_build 1
%define pki_version 11.8.0
%def_with check

# pki is a drop-in replacement for Dogtag's client library. The girar
# duplicate-provides check tracks python3(...) module names but not plain
# capability names, so hide the auto-generated python3(pki) provides that
# python3-module-dogtag-pki already has. FreeIPA manages the dependency
# through the plain python3-module-pki-base capability, which both packages
# may provide.
%filter_from_provides /python3(pki\(\..*\)\?)/d
%filter_from_requires /python3(pki\(\..*\)\?)/d

Name: ipacta
Version: 0.1.1
Release: alt1

Summary: Python Certificate Authority compatible with Dogtag PKI
License: GPL-3.0-or-later
Group: System/Servers
Url: https://forge.fedoraproject.org/freeipa/ipacta
Vcs: https://forge.fedoraproject.org/freeipa/ipacta.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

Provides: pki-ca = %pki_version
Provides: pki-kra = %pki_version
Provides: pki-acme = %pki_version
Conflicts: dogtag-pki-base
Conflicts: dogtag-pki-server
Conflicts: dogtag-pki-ca
Conflicts: dogtag-pki-kra
Conflicts: dogtag-pki-acme
# ipacta ships its own /usr/sbin/tomcat version shim for FreeIPA; tomcat10
# owns the same path, and the two PKI stacks are mutually exclusive.
Conflicts: tomcat10
Requires: python3-module-ipacta = %EVR
Requires: nss-utils openssl openldap-clients systemd

BuildRequires(pre): rpm-build-python3 rpm-macros-systemd
BuildRequires: autoconf automake pkg-config libsystemd-devel python3-devel
BuildRequires: python3-module-cryptography >= 49
BuildRequires: python3-module-cachetools python3-module-dns python3-module-flask
BuildRequires: python3-module-ldap python3-module-pyasn1 python3-module-pyasn1-modules
BuildRequires: python3-module-requests python3-module-systemd python3-module-werkzeug
%if_with check
BuildRequires: python3-module-pytest nss-utils openssl openldap-clients systemd
%endif

%description
ipacta is a Python Certificate Authority providing a Dogtag-compatible
REST API, command-line tools, certificate profiles and a PKI client library.
It implements CA, KRA, ACME and OCSP services without Java or Tomcat.

%package -n python3-module-ipacta
Summary: Python modules for the ipacta Certificate Authority
Group: Development/Python3
Requires: python3-module-ipacta-pki = %EVR
Requires: python3-module-cryptography >= 49
Requires: python3-module-cachetools python3-module-dns python3-module-pyasn1-modules

%description -n python3-module-ipacta
CA engine, LDAP storage, REST API, installer and other Python modules
implementing the ipacta Certificate Authority.

%package -n python3-module-ipacta-pki
Summary: Dogtag-compatible Python PKI client library from ipacta
Group: Development/Python3
License: LGPL-3.0-or-later AND GPL-2.0-or-later
Provides: python3-module-pki-base = %pki_version
Conflicts: python3-module-dogtag-pki

%description -n python3-module-ipacta-pki
Python PKI client library implementing the Dogtag interfaces used by FreeIPA.
This package cannot be installed alongside the original Dogtag PKI library.

%prep
%setup
%patch -p1
sed -i \
    -e 's/^m4_define(\[IPACTA_VERSION\], .*/m4_define([IPACTA_VERSION], [%version])/' \
    -e 's/^m4_define(\[IPACTA_RELEASE\], .*/m4_define([IPACTA_RELEASE], [%release])/' \
    configure.ac
sed -i 's/^__version__ = .*/__version__ = "%version"/' src/ipacta/__init__.py
mkdir -p m4
%autoreconf

%build
%configure \
    PYTHON=%__python3 \
    --with-systemdsystemunitdir=%_unitdir \
    --with-systemdsysusersdir=%_sysusersdir \
    --with-systemdtmpfilesdir=%_tmpfilesdir
%make_build

%install
%makeinstall_std pythondir=%python3_sitelibdir_noarch
# FreeIPA invokes administrative commands at the stock Dogtag paths.
install -d %buildroot%_sbindir
for command in pkispawn pkidestroy pki-server tomcat; do
    mv %buildroot%_bindir/"$command" %buildroot%_sbindir/
done

%check
%if_with check
for command in pkispawn pkidestroy pki-server tomcat; do
    test -x %buildroot%_sbindir/"$command"
    test ! -e %buildroot%_bindir/"$command"
done
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
export PATH=%buildroot%_sbindir:%buildroot%_bindir:$PATH
export PYTHONDONTWRITEBYTECODE=1
%__python3 -m pytest -q -p no:cacheprovider --basetemp="$PWD/.pytest-tmp" tests
%endif

%files
%doc README.md doc
%_bindir/ipacta-verify-certs
%_bindir/PKCS12Export
%_bindir/pki
%_sbindir/pkidestroy
%_sbindir/pki-server
%_sbindir/pkispawn
%_sbindir/tomcat
%_datadir/ipacta/
%_datadir/pki/VERSION
%_datadir/pki/acme/
%_datadir/pki/ca/
%_unitdir/pki-tomcatd.target
%_unitdir/pki-tomcatd@.service
%_unitdir/pki-tomcatd@.socket
%config(noreplace) %_sysconfdir/systemd/journald@ipacta.conf
%_sysusersdir/ipacta.conf
%_tmpfilesdir/ipacta.conf

%files -n python3-module-ipacta
%python3_sitelibdir_noarch/ipacta/

%files -n python3-module-ipacta-pki
%python3_sitelibdir_noarch/pki/

%changelog
* Sun Nov 08 2026 Andrey Limachko <liannnix@altlinux.org> 0.1.1-alt1
- ALT Sisyphus packaging: port 8090/8443/8009, admin commands in /usr/sbin,
  pkiuser state directories through sysusers/tmpfiles.
- KRA readiness version, both response casings and OAEP-first unwrap.
- ACME directory JSON, optional contacts and kid challenge authentication.
- Disabled raw profile import; issuer-id/AuthorityID selection.
- Preserve revocation times for OCSP/CRL; update sub-CA key hosts.
- Initial build for Sisyphus.

%define ShortName LDAPAuthentication2
%define mwversion 1.40
%setup_mediawiki_ext %mwversion %ShortName
%define commit 2864ae9
%define defphp php8.1

Name: mediawiki-extensions-%ShortName
Version: 2.2.0.%mwversion
Release: alt1.%commit

Summary: Mediawiki extension to do LDAP authentication

License: GPLv2
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:LDAPAuthentication2

# Source-url: https://extdist.wmflabs.org/dist/extensions/%ShortName-%MWREL-%commit.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-mediawiki >= 0.6

Requires: %defphp-ldap

Requires: mediawiki >= %mwversion

%description
This plugin should be scalable for use in small to large organizations,
and provides the following functionality:

    Single and multi domain authentication (including local database)
        Simple bind authentication
        Proxy bind authentication
        Smartcard/CAC/PKI Soft Certificate authentication
        Kerberos authentication
        SSL/TLS or non-SSL/TLS binding allowed
        Nested/Unnested Group based restriction support
        Filter based restriction support
    Retrieval of user information from LDAP
        Email address
        Real name
        Nickname
        Language
    Synchronization of LDAP groups to MediaWiki security groups
    (LDAP->MediaWiki only)
        Nested group support available in 1.2b+
    Storing preferences in LDAP
        Update passwords
        Mail me a password
        Update all preferences that are currently retrievable
    Creation and modification of users in LDAP

%prep
%setup

%build

%install
%mediawiki_ext_install 50 %ShortName
rm -rv %buildroot%mediawiki_ext_dir/tests/

%files -f %ShortName.files

%changelog
* Sat Aug 12 2023 Vitaly Lipatov <lav@altlinux.ru> 2.2.0.1.40-alt1.2864ae9
- initial build for ALT Sisyphus


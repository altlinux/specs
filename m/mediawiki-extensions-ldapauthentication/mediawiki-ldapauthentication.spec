%define oldname mediawiki-ldapauthentication
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# disable find_requires as it generate incorrect require on
# pear(Renameuser/SpecialRenameuser_body.php)
%define __find_requires %{nil}

%define mediawiki_extensions %{_datadir}/mediawiki/extensions
%define oname LdapAuthentication
%define mwikiver 1.27
%define gitsnap 12d743d

Name:		mediawiki-extensions-ldapauthentication
Summary:	Mediawiki extension to do ldap authentication
Version:	2.1.0
Release:	alt1_6
URL:		http://www.mediawiki.org/wiki/Extension:LDAP_Authentication
Source0:	https://extdist.wmflabs.org/dist/extensions/LdapAuthentication-REL1_27-%{gitsnap}.tar.gz

License:	GPLv2+
Requires:	mediawiki-common >= %{mwikiver}
Requires:	php5-ldap
Group:		System/Servers
BuildArch:	noarch
Source44: import.info
Provides: mediawiki-ldap = %version
Obsoletes: mediawiki-ldap < 1.3

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
%setup -q -n LdapAuthentication

%install
install -d %{buildroot}%{mediawiki_extensions}/%{oname}
install *.php README %{buildroot}%{mediawiki_extensions}/%{oname}
install -d %{buildroot}%{mediawiki_extensions}/%{oname}/schema
install schema/* %{buildroot}%{mediawiki_extensions}/%{oname}/schema

%files
%{mediawiki_extensions}/%{oname}


%changelog
* Tue Mar 27 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_6
- new version


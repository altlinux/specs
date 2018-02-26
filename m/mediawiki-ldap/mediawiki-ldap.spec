%define _mediawiki_extdir %_datadir/mediawiki/extensions
%define _mediawiki_webapps_extdir  %{_var}/www/webapps/mediawiki/extensions
%define _mediawiki_ldap_php LdapAuthentication.php

Name: mediawiki-ldap
Version: 1.2a
Release: alt3
Summary: Mediawiki ldap extension
License: GPL

Group: Networking/WWW

Packager:  Lebedev Sergey <barabashka@altlinux.org>

#http://svn.wikimedia.org/viewvc/mediawiki/trunk/extensions/LdapAuthentication/LdapAuthentication.php
Source: %name-%version.tar.gz

BuildArch: noarch

Requires: mediawiki

%description
This extension allow to use user information from ldap.


%prep
%setup -q 

%build

%install
mkdir -p %buildroot%{_mediawiki_extdir}
install -Dp -m644 %{_mediawiki_ldap_php} %buildroot/%{_mediawiki_extdir}

%post
ln -s %{_mediawiki_extdir} %{_mediawiki_webapps_extdir} 2>/dev/null

%files
%{_mediawiki_extdir}/%{_mediawiki_ldap_php}

%changelog
* Thu Jul 30 2009 Lebedev Sergey <barabashka@altlinux.org> 1.2a-alt3
- first build for Sisyphus

* Tue Jan 13 2009 Lebedev Sergey <barabashka@altlinux.org> 1.2a-alt2.M41
- add symlink for extensions

* Wed Dec 31 2008 Lebedev Sergey <barabashka@altlinux.org> 1.2a-alt1.M41
- initial build


%define appdir %_var/lib/tomcat/webapps

Name: guacamole
Version: 1.5.5
Release: alt1
Summary: Clientless remote desktop gateway
License: Apache-2.0
Group: Networking/Remote access
Url: https://guac-dev.org/

#Source1: https://www.apache.org/dist/%name/%version/source/%name-client-%version.tar.gz
Source2: https://www.apache.org/dist/%name/%version/binary/%name-%version.war
Source3: guacamole.properties
Source4: user-mapping.xml
Source10: https://www.apache.org/dist/%name/%version/binary/%name-auth-sso-%version.tar.gz
Source11: https://www.apache.org/dist/%name/%version/binary/%name-auth-duo-%version.tar.gz
Source12: https://www.apache.org/dist/%name/%version/binary/%name-auth-header-%version.tar.gz
Source13: https://www.apache.org/dist/%name/%version/binary/%name-auth-jdbc-%version.tar.gz
Source14: https://www.apache.org/dist/%name/%version/binary/%name-auth-ldap-%version.tar.gz
Source16: https://www.apache.org/dist/%name/%version/binary/%name-auth-quickconnect-%version.tar.gz
Source18: https://www.apache.org/dist/%name/%version/binary/%name-auth-totp-%version.tar.gz
Source19: https://www.apache.org/dist/%name/%version/binary/%name-auth-json-%version.tar.gz

BuildRequires: /proc rpm-build-java java-devel
#BuildRequires: maven-local
#BuildRequires: maven
BuildRequires: mysql-connector-java
BuildRequires: postgresql-jdbc
BuildRequires: tomcat
BuildArch: noarch
AutoReqProv: noosgi, noosgi-fc

%description
Guacamole is an HTML5 web application that provides access
to desktop environments using remote desktop protocols such as VNC or RDP.
A centralized server acts as a tunnel and proxy,
allowing access to multiple desktops through a web browser.
No plugins are needed: the client requires nothing more than a web browser
supporting HTML5 and AJAX.
This is the client-part.

%package client
Summary: Guacamole web application
Group: Networking/Remote access
Provides: tomcat-%name-webapps = %EVR
Requires: tomcat
Requires: java-headless
AutoReqProv: noosgi, noosgi-fc

%description client
The Guacamole web application, providing authentication and an HTML5
remote desktop client.

%package auth-sso
Summary: Guacamole support for secondary SSO providers
Group: Networking/Remote access
Requires: %name-client = %EVR
AutoReqProv: noosgi, noosgi-fc
Provides: %name-auth-cas = %EVR
Provides: %name-auth-openid = %EVR
Provides: %name-auth-saml = %EVR
Obsoletes: %name-auth-cas < 1.4.0
Obsoletes: %name-auth-openid < 1.4.0
Obsoletes: %name-auth-saml < 1.4.0

%description auth-sso
Guacamole's support for single sign-on has historically been all-or-nothing,
with either all users using SSO to authenticate or none at all.
This is no longer the case: Guacamole may now be configured to allow
normal username/password authentication in addition to SSO,
and multiple SSO providers may be used at the same time.

Included:
 * CAS Authentication
 * OpenID Connect Authentication
 * SAML Authentication

%package auth-duo
Summary: Guacamole Duo TFA Authentication Backend
Group: Networking/Remote access
Requires: %name-client = %EVR
AutoReqProv: noosgi, noosgi-fc

%description auth-duo
Guacamole supports Duo as a second authentication factor,
layered on top of any other authentication extension,
including those available from the main project website.
The Duo authentication extension allows users
to be additionally verified against the Duo service
before the authentication process is allowed to succeed.

%package auth-header
Summary: Guacamole HTTP Header Authentication Extension
Group: Networking/Remote access
Requires: %name-client = %EVR
AutoReqProv: noosgi, noosgi-fc

%description auth-header
Guacamole supports delegating authentication to an arbitrary external service,
relying on the presence of an HTTP header which contains the username of the authenticated user.
This authentication method must be layered on top of some other authentication extension,
such as those available from the main project website, in order to provide access to actual connections.

%package auth-jdbc-mysql
Summary: Guacamole JDBC MySQL Authentication Extension
Group: Networking/Remote access
Requires: %name-client = %EVR
Requires: mysql-connector-java
AutoReqProv: noosgi, noosgi-fc

%description auth-jdbc-mysql
Guacamole supports authentication via MySQL database.

%package auth-jdbc-postgresql
Summary: Guacamole JDBC PostgreSQL Authentication Extension
Group: Networking/Remote access
Requires: %name-client = %EVR
Requires: postgresql-jdbc
AutoReqProv: noosgi, noosgi-fc

%description auth-jdbc-postgresql
Guacamole supports authentication via PostgreSQL database.

%package auth-jdbc-sqlserver
Summary: Guacamole JDBC SQLServer Authentication Extension
Group: Networking/Remote access
Requires: %name-client = %EVR
AutoReqProv: noosgi, noosgi-fc

%description auth-jdbc-sqlserver
Guacamole supports authentication via PostgreSQL database.

%package auth-ldap
Summary: Guacamole LDAP Authentication Extension
Group: Networking/Remote access
Requires: %name-client = %EVR
AutoReqProv: noosgi, noosgi-fc

%description auth-ldap
Guacamole supports LDAP authentication via an extension.
This extension allows users and connections to be stored directly
within an LDAP directory.
If you have a centralized authentication system that uses LDAP,
Guacamole's LDAP support can be a good way to allow your users
to use their existing usernames and passwords to log into Guacamole.

%package auth-quickconnect
Summary: Guacamole Adhoc Connections Extension
Group: Networking/Remote access
Requires: %name-client = %EVR
AutoReqProv: noosgi, noosgi-fc

%description auth-quickconnect
The quickconnect extension provides a connection bar on the Guacamole Client home page
that allows users to type in the URI of a server to which they want to connect
and the client will parse the URI and immediately establish the connection.
The purpose of the extension is to allow situations where administrators
want to allow users the flexibility of establishing their own connections
without having to grant them access to edit connections or even to have to create
the connections at all, aside from typing the URI.

%package auth-totp
Summary: Guacamole TOTP TFA Authentication Extension
Group: Networking/Remote access
Requires: %name-client = %EVR
AutoReqProv: noosgi, noosgi-fc

%description auth-totp
Guacamole supports TOTP as a second authentication factor, layered on top of
any other authentication extension, providing base requirements
for key storage and enrollment are met.
The TOTP authentication extension allows users to be additionally verified
against a user-specific and secret key generated during enrollment
of their authentication device.

%package auth-json
Summary: Guacamole Encrypted JSON authentication Extension
Group: Networking/Remote access
Requires: %name-client = %EVR
AutoReqProv: noosgi, noosgi-fc

%description auth-json
Guacamole supports delegating authentication to an arbitrary external service,
relying on receipt of JSON data which has been signed using HMAC/SHA-256
and encrypted with 128-bit AES in CBC mode. This JSON contains all information
describing the user being authenticated, as well as any connections
they have access to, and is accepted only if the configured secret key was used
to sign and encrypt the data.

%prep
#%setup -T -D -b 1  -n %name-client-%version
%setup -T -D -b 10 -n %name-auth-sso-%version
%setup -T -D -b 11 -n %name-auth-duo-%version
%setup -T -D -b 12 -n %name-auth-header-%version
%setup -T -D -b 13 -n %name-auth-jdbc-%version
%setup -T -D -b 14 -n %name-auth-ldap-%version
%setup -T -D -b 16 -n %name-auth-quickconnect-%version
%setup -T -D -b 18 -n %name-auth-totp-%version
%setup -T -D -b 19 -n %name-auth-json-%version

%build
%install
mkdir -p %buildroot%_docdir/%name
mkdir -p %buildroot{%_sysconfdir,%_datadir}/%name/{extensions,lib}
mkdir -p %buildroot%_datadir/tomcat
cp %SOURCE3 %buildroot%_sysconfdir/%name
cp %SOURCE4 %buildroot%_sysconfdir/%name
ln -s %_sysconfdir/%name %buildroot%_datadir/tomcat/.guacamole
mkdir -p %buildroot%appdir/%name
#cp %SOURCE2 %buildroot/%appdir/guacamole.war
pushd %buildroot%appdir/%name
%jar -xf %SOURCE2
popd

for prov in duo header ldap quickconnect totp json; do
	mkdir -p %buildroot%_docdir/%name/auth-${prov}
	pushd %_builddir/%name-auth-${prov}-%version
	mv %name-auth-${prov}-%version.jar %buildroot%_datadir/%name/extensions
	ln -r -s %buildroot%_datadir/%name/extensions/%name-auth-${prov}-%version.jar %buildroot%_sysconfdir/%name/extensions
	cp -r * %buildroot%_docdir/%name/auth-${prov}/
	popd
done

pushd %_builddir/%name-auth-sso-%version
for sso in cas openid saml; do
	mv ${sso}/%name-auth-sso-${sso}-%version.jar %buildroot%_datadir/%name/extensions
	ln -r -s %buildroot%_datadir/%name/extensions/%name-auth-sso-${sso}-%version.jar %buildroot%_sysconfdir/%name/extensions
done

pushd %_builddir/%name-auth-jdbc-%version
for db in mysql postgresql sqlserver; do
	mkdir -p %buildroot%_docdir/%name/auth-jdbc-${db}
	mv ${db}/%name-auth-jdbc-${db}-%version.jar %buildroot%_datadir/%name/extensions
	ln -r -s %buildroot%_datadir/%name/extensions/%name-auth-jdbc-${db}-%version.jar %buildroot%_sysconfdir/%name/extensions
	cp -r ${db}/* %buildroot%_docdir/%name/auth-jdbc-${db}/
done
popd

# LIB
# install/symlink mysql-jdbc
ln -r -s %buildroot%_datadir/java/mysql-connector-java.jar %buildroot%_sysconfdir/%name/lib/mysql-connector-java.jar
# install/symlink postgresql-jdbc
ln -r -s %buildroot%_datadir/java/postgresql-jdbc.jar %buildroot%_sysconfdir/%name/lib/postgresql-jdbc.jar

%files client
%dir %_docdir/%name
%dir %_sysconfdir/%name
%config(noreplace) %attr(0640,root,tomcat) %_sysconfdir/%name/user-mapping.xml
%config(noreplace) %attr(0640,root,tomcat) %_sysconfdir/%name/%name.properties
%dir %_sysconfdir/%name/extensions
%dir %_sysconfdir/%name/lib
%dir %_datadir/%name/extensions
%_datadir/tomcat/.guacamole
#%appdir/%name.war
%defattr(0644,tomcat,tomcat,0755)
%appdir/%name

%files auth-sso
%_sysconfdir/%name/extensions/%name-auth-sso-cas-%version.jar
%_sysconfdir/%name/extensions/%name-auth-sso-saml-%version.jar
%_sysconfdir/%name/extensions/%name-auth-sso-openid-%version.jar
%_datadir/%name/extensions/%name-auth-sso-cas-%version.jar
%_datadir/%name/extensions/%name-auth-sso-saml-%version.jar
%_datadir/%name/extensions/%name-auth-sso-openid-%version.jar

%files auth-duo
%_sysconfdir/%name/extensions/%name-auth-duo-%version.jar
%_datadir/%name/extensions/%name-auth-duo-%version.jar
%doc %_docdir/%name/auth-duo

%files auth-header
%_sysconfdir/%name/extensions/%name-auth-header-%version.jar
%_datadir/%name/extensions/%name-auth-header-%version.jar
%doc %_docdir/%name/auth-header

%files auth-jdbc-mysql
%_sysconfdir/%name/extensions/%name-auth-jdbc-mysql-%version.jar
%_sysconfdir/%name/lib/mysql-connector-java.jar
%_datadir/%name/extensions/%name-auth-jdbc-mysql-%version.jar
%doc %_docdir/%name/auth-jdbc-mysql

%files auth-jdbc-postgresql
%_sysconfdir/%name/extensions/%name-auth-jdbc-postgresql-%version.jar
%_sysconfdir/%name/lib/postgresql*.jar
%_datadir/%name/extensions/%name-auth-jdbc-postgresql-%version.jar
%doc %_docdir/%name/auth-jdbc-postgresql

%files auth-jdbc-sqlserver
%_sysconfdir/%name/extensions/%name-auth-jdbc-sqlserver-%version.jar
%_datadir/%name/extensions/%name-auth-jdbc-sqlserver-%version.jar
%doc %_docdir/%name/auth-jdbc-sqlserver

%files auth-ldap
%_sysconfdir/%name/extensions/%name-auth-ldap-%version.jar
%_datadir/%name/extensions/%name-auth-ldap-%version.jar
%doc %_docdir/%name/auth-ldap

%files auth-quickconnect
%_sysconfdir/%name/extensions/%name-auth-quickconnect-%version.jar
%_datadir/%name/extensions/%name-auth-quickconnect-%version.jar
%doc %_docdir/%name/auth-quickconnect

%files auth-totp
%_sysconfdir/%name/extensions/%name-auth-totp-%version.jar
%_datadir/%name/extensions/%name-auth-totp-%version.jar
%doc %_docdir/%name/auth-totp

%files auth-json
%_sysconfdir/%name/extensions/%name-auth-json-%version.jar
%_datadir/%name/extensions/%name-auth-json-%version.jar
%doc %_docdir/%name/auth-json

%changelog
* Sun May 19 2024 Alexey Shabalin <shaba@altlinux.org> 1.5.5-alt1
- 1.5.5

* Mon Dec 25 2023 Alexander Burmatov <thatman@altlinux.org> 1.5.4-alt1
- 1.5.4 (Fixes: CVE-2023-43826).

* Fri Aug 18 2023 Alexey Shabalin <shaba@altlinux.org> 1.5.3-alt1
- 1.5.3

* Thu Oct 13 2022 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- 1.4.0
- Moved extensions from /etc to /usr/share

* Tue Jan 19 2021 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt1
- 1.3.0

* Thu Nov 19 2020 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt1
- Initial build

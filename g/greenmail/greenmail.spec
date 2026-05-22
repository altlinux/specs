%define _unpackaged_files_terminate_build 1
%define _greenmail_standalone_dir %_javadir/%name
%define greenmail_webapp_dir %_datadir/%name

Name: greenmail
Version: 2.1.8
Release: alt2

Summary: Email test server for integration tests
License: Apache-2.0
Group: Development/Java
Url: https://greenmail-mail-test.github.io/greenmail
Vcs: https://github.com/greenmail-mail-test/greenmail.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: greenmail
Source2: greenmail-webapp
Source3: greenmail-standalone.classpath

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-17-compat
BuildRequires: maven-local
BuildRequires: maven-war-plugin
BuildRequires: jackson-bom
BuildRequires: maven-failsafe-plugin
BuildRequires: jakarta-mail
BuildRequires: angus-mail
BuildRequires: angus-activation
BuildRequires: jakarta-servlet
BuildRequires: jakarta-ws-rs
BuildRequires: slf4j log4j-slf4j
BuildRequires: jul-to-slf4j
BuildRequires: log4j
BuildRequires: junit
BuildRequires: junit5
BuildRequires: jersey-bom
BuildRequires: jersey-common
BuildRequires: jersey-client
BuildRequires: jersey-server
BuildRequires: jersey-hk2
BuildRequires: jersey-container-jdk-http
BuildRequires: jersey-container-servlet
BuildRequires: jersey-container-jetty-http
BuildRequires: jersey-media-json-jackson

%description
GreenMail provides in-memory mail servers (SMTP, SMTPS, POP3, POP3S, IMAP,
IMAPS) for integration tests and local development.

%package standalone
Summary: GreenMail standalone launcher
Group: Development/Java
Requires: java-17-openjdk-headless
Requires: angus-activation
Requires: angus-mail
Requires: jakarta-mail
Requires: jersey-container-jdk-http
Requires: jersey-hk2
Requires: jersey-media-json-jackson
Requires: jul-to-slf4j
Requires: log4j
Requires: log4j-slf4j
Requires: slf4j

%description standalone
Standalone GreenMail launcher with HTTP API support.

%package webapp
Summary: GreenMail embedded web application
Group: Development/Java
Requires: java-17-openjdk-headless
Requires: tomcat10

%description webapp
Embedded GreenMail web application archive.

%package junit4
Summary: GreenMail JUnit 4 support
Group: Development/Java

%description junit4
GreenMail integration helpers for JUnit 4 tests.

%package junit5
Summary: GreenMail JUnit 5 support
Group: Development/Java

%description junit5
GreenMail integration helpers for JUnit 5 tests.

%prep
%setup

# Spring modules are not available in target repository.
%pom_disable_module greenmail-spring pom.xml

# inject-maven-plugin is not packaged in ALT.
%pom_remove_plugin de.m3y.maven:inject-maven-plugin greenmail-core/pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-shade-plugin greenmail-standalone/pom.xml
%pom_remove_plugin -r -f org.codehaus.mojo:keytool-maven-plugin
%pom_remove_plugin -r -f :maven-enforcer-plugin

sed -i 's|<groupId>jakarta.servlet</groupId>|<groupId>javax.servlet</groupId>|' greenmail-webapp/pom.xml
sed -i 's|<artifactId>jakarta.servlet-api</artifactId>|<artifactId>javax.servlet-api</artifactId>|' greenmail-webapp/pom.xml
sed -i 's|<artifactId>jakarta.mail</artifactId>|<artifactId>angus-mail</artifactId>|g' pom.xml greenmail-core/pom.xml

# Parent POM is only a build aggregator.
%mvn_package :greenmail-parent __noinstall

# WAR artifact is installed manually because xmvn-install repository rejects WAR packaging.
%mvn_package :greenmail-webapp __noinstall

%build
# Skip tests because of no network access.
%mvn_build -s -j -f

%install
%mvn_install

install -Dpm0644 greenmail-webapp/target/greenmail-webapp-%version.war \
  %buildroot%greenmail_webapp_dir/greenmail-webapp.war
install -Dpm0644 %SOURCE3 \
  %buildroot%_greenmail_standalone_dir/greenmail-standalone.classpath

install -d %buildroot%_bindir
sed -e 's|@GREENMAIL_STANDALONE_DIR@|%_greenmail_standalone_dir|g' \
  %SOURCE1 > %buildroot%_bindir/%name
chmod 0755 %buildroot%_bindir/%name

sed -e 's|@GREENMAIL_WEBAPP_DIR@|%greenmail_webapp_dir|g' \
  %SOURCE2 > %buildroot%_bindir/greenmail-webapp
chmod 0755 %buildroot%_bindir/greenmail-webapp

%files -f .mfiles-greenmail
%doc --no-dereference README.md
%doc --no-dereference license.txt

%files standalone -f .mfiles-greenmail-standalone
%_bindir/greenmail
%_greenmail_standalone_dir/greenmail-standalone.classpath

%files webapp
%_bindir/greenmail-webapp
%greenmail_webapp_dir/greenmail-webapp.war

%files junit4 -f .mfiles-greenmail-junit4
%files junit5 -f .mfiles-greenmail-junit5
%changelog
* Thu May 21 2026 Ivan Khanas <xeno@altlinux.org> 2.1.8-alt2
- Unbandle dependencies from greenmail-standalone.

* Wed Mar 18 2026 Ivan Khanas <xeno@altlinux.org> 2.1.8-alt1
- Initial build for ALT.

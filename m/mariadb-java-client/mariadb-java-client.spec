Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global build_javadoc 0

Name:		mariadb-java-client
Version:	3.5.0
Release:	alt1
Summary:	Connects applications developed in Java to MariaDB and MySQL databases
# added BSD license because of https://bugzilla.redhat.com/show_bug.cgi?id=1291558#c13
License:	LGPL-2.1-or-later
URL:			https://mariadb.com/kb/en/mariadb/about-mariadb-connector-j/
Source0:	https://github.com/mariadb-corporation/mariadb-connector-j/archive/refs/tags/%{version}.tar.gz#/mariadb-connector-j-%{version}.tar.gz
# optional dependency not in Fedora
Patch0:		remove_waffle-jna.patch

BuildArch:	noarch
BuildRequires:	maven-local
BuildRequires:	mvn(net.java.dev.jna:jna)
BuildRequires:	mvn(net.java.dev.jna:jna-platform)
BuildRequires:	mvn(org.osgi:osgi.cmpn)
BuildRequires:	mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)

Source44: import.info

%description
MariaDB Connector/J is a Type 4 JDBC driver, also known as the Direct to
Database Pure Java Driver. It was developed specifically as a lightweight
JDBC connector for use with MySQL and MariaDB database servers.

%package javadoc
Group: Development/Java
Summary:	Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -qn mariadb-connector-j-%{version}

# remove missing optional dependency waffle-jna
%pom_remove_dep com.github.waffle:waffle-jna
%pom_remove_dep ch.qos.logback:logback-classic
%pom_remove_dep software.amazon.awssdk:bom
%pom_remove_dep software.amazon.awssdk:rds
%pom_remove_dep org.junit:junit-bom
%pom_remove_dep org.junit.jupiter:junit-jupiter-engine
%pom_remove_dep org.slf4j:slf4j-api
# used in buildtime for generating OSGI metadata
%pom_remove_plugin biz.aQute.bnd:bnd-maven-plugin

%pom_add_dep net.java.dev.jna:jna
%pom_add_dep net.java.dev.jna:jna-platform
# add slf4j dep again, this time not dependent on any specific version
%pom_add_dep org.slf4j:slf4j-api

# use latest OSGi implementation
%pom_change_dep -r :org.osgi.core org.osgi:osgi.core
%pom_change_dep -r :org.osgi.compendium org.osgi:osgi.cmpn

rm -r src/main/java/org/mariadb/jdbc/plugin/credential/aws
# removing dependencies and 'provides', which mariadb-java-client cannot process from module-info.java
sed -i '/aws/d' src/main/java9/module-info.java
sed -i '/waffle/d' src/main/java9/module-info.java
# removing missing dependencies form META-INF, so that the mariadb-java-client module would be valid
sed -i '/aws/d' src/main/resources/META-INF/services/org.mariadb.jdbc.plugin.CredentialPlugin
sed -i '/aws/d' src/test/resources/META-INF/services/org.mariadb.jdbc.plugin.CredentialPlugin


# also remove the file using the removed plugin
rm -f src/main/java/org/mariadb/jdbc/plugin/authentication/addon/gssapi/WindowsNativeSspiAuthentication.java
# patch the sources so that the missing file is not making trouble
%patch0 -p1

%mvn_file org.mariadb.jdbc:%{name} %{name}
%mvn_alias org.mariadb.jdbc:%{name} mariadb:mariadb-connector-java

%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin -r :maven-gpg-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%build
# tests are skipped, while they require running application server
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Mon Dec 08 2025 Anton Meleshnikov <alton@altlinux.org> 3.5.0-alt1
- new version

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 3.0.7-alt1_1jpp11
- new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 3.0.3-alt1_3jpp11
- new version

* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 3.0.1-alt1_1jpp11
- new version

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 3.0.0-alt1_1jpp11
- new version

* Tue Jun 15 2021 Igor Vlasenko <viy@altlinux.org> 2.7.2-alt1_1jpp11
- new version

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 2.7.1-alt1_2jpp11
- new version


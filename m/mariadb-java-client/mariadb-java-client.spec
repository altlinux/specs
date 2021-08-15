Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		mariadb-java-client
Version:	3.0.0
Release:	alt1_1jpp11
Summary:	Connects applications developed in Java to MariaDB and MySQL databases
# added BSD license because of https://bugzilla.redhat.com/show_bug.cgi?id=1291558#c13
License:	BSD and LGPLv2+
URL:		https://mariadb.com/kb/en/mariadb/about-mariadb-connector-j/
Source0:	https://github.com/MariaDB/mariadb-connector-j/archive/%{version}.tar.gz
# optional dependency not in Fedora
Patch0:		remove_waffle-jna.patch

BuildArch:	noarch
BuildRequires:	maven-local
BuildRequires:	mvn(net.java.dev.jna:jna)
BuildRequires:	mvn(net.java.dev.jna:jna-platform)
BuildRequires:	mvn(com.google.code.maven-replacer-plugin:replacer)
# fedora 25
BuildRequires:	mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:	mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
Source44: import.info
# Since version 2.4.0
# removing coverage test because of dependencies
#BuildRequires:	mvn(org.jacoco:jacoco-maven-plugin)
# since version 1.5.2 missing optional dependency (windows)
#BuildRequires:	mvn(com.github.dblock.waffle:waffle-jna)

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
%pom_remove_dep com.amazonaws:aws-java-sdk-rds
%pom_remove_dep com.amazonaws:aws-java-sdk-bom
%pom_remove_dep org.junit:junit-bom

%pom_add_dep net.java.dev.jna:jna
%pom_add_dep net.java.dev.jna:jna-platform
%pom_add_dep org.slf4j:slf4j-api

# use latest OSGi implementation
%pom_change_dep -r :org.osgi.core org.osgi:osgi.core
%pom_change_dep -r :org.osgi.compendium org.osgi:osgi.cmpn 
 
rm -r src/main/java/org/mariadb/jdbc/plugin/credential/aws

sed -i 's/public void close() {/public void close() throws Exception {/' src/main/java/org/mariadb/jdbc/pool/Pool.java

# also remove the file using the removed plugin
rm -f src/main/java/org/mariadb/jdbc/plugin/authentication/addon/gssapi/WindowsNativeSspiAuthentication.java
# patch the sources so that the missing file is not making trouble
%patch0 -p1

%mvn_file org.mariadb.jdbc:%{name} %{name}
%mvn_alias org.mariadb.jdbc:%{name} mariadb:mariadb-connector-java

%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin com.coveo:fmt-maven-plugin
%pom_remove_plugin -r :maven-gpg-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%build
# tests are skipped, while they require running application server
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 3.0.0-alt1_1jpp11
- new version

* Tue Jun 15 2021 Igor Vlasenko <viy@altlinux.org> 2.7.2-alt1_1jpp11
- new version

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 2.7.1-alt1_2jpp11
- new version


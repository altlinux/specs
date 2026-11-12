%define _unpackaged_files_terminate_build 1

Name: h2
Version: 2.5.252
Release: alt1

Summary: Java SQL database engine
License: (MPL-2.0 or EPL-1.0) and Apache-2.0
Group: Development/Java
URL: https://h2database.com
VCS: https://github.com/h2database/h2database.git

Source: %name-%version.tar
Patch: h2-system.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(jakarta.servlet:jakarta.servlet-api)
BuildRequires: mvn(org.apache.lucene:lucene-core)
BuildRequires: mvn(org.apache.lucene:lucene-analysis-common)
BuildRequires: mvn(org.apache.lucene:lucene-queryparser)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-nop)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(org.osgi:osgi.cmpn)
BuildRequires: mvn(org.locationtech.jts:jts-core)
BuildRequires: mvn(org.postgresql:postgresql)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.openjdk.nashorn:nashorn-core)

%description
H2 is a SQL database engine with a JDBC API, embedded and server modes,
in-memory and persistent databases, and a browser based console.

%package javadoc
Summary: API documentation for H2 Database
Group: Development/Documentation

%description javadoc
API documentation for the H2 JDBC database engine.

%prep
%setup
%patch -p1
# ALT compendium exports the JDBC 1.0 DataSourceFactory API.
%pom_change_dep org.osgi:org.osgi.service.jdbc \
    org.osgi:osgi.cmpn:7.0.0 h2
# Build the Java 21 multi-release implementation from source.
find . -name '*.class' -delete
# The historical Lucene 6 port is superseded by upstream's Lucene 9 API.

%build
cd h2
# Java 21 is needed only for the MR implementation; base classes target 11.
%_jvmdir/java-21/bin/javac --release 21 \
    -d src/java21/precompiled src/java21/src/org/h2/util/Utils21.java
# Keep the JVM and SQL timezone names consistent in the upstream tests.
TZ=UTC %mvn_build

%install
cd h2
%mvn_install

%files -f h2/.mfiles
%doc LICENSE.txt

%files javadoc -f h2/.mfiles-javadoc

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 2.5.252-alt1
- New version.

* Tue Jun 18 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.196-alt1_6jpp8
- fixed build with new jts

* Wed May 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.196-alt1_3jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.196-alt1_2jpp8
- new version

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.192-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.176-alt1_6jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.176-alt1_4jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.168-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.168-alt1_3jpp7
- new release

* Sun Sep 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.168-alt1_2jpp7
- new version

* Sat Sep 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.147-alt2_5jpp7
- fixed build

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.147-alt1_5jpp7
- new version


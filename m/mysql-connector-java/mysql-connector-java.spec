Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
#BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

Summary:       Official JDBC driver for MySQL
Name:          mysql-connector-java
Version:       8.0.30
Release:       alt1_2jpp11
Epoch:         1
License:       GPLv2 with exceptions
URL:           http://dev.mysql.com/downloads/connector/j/
Source0:       %{name}-%{version}-nojars.tar.xz

# Mysql has a mirror redirector for its downloads
# You can get this tarball by following a link from:
# http://dev.mysql.com/get/Downloads/Connector-J/%%{name}-%%{version}.tar.gz
#
# OR
# https://github.com/mysql/mysql-connector-j/archive/%%{version}.tar.gz
# Following prebuilt jars and sources have been removed from the tarball:
#
# %%{name}-%%{version}-bin.jar
# lib/c3p0-0.9.1-pre6.jar
# lib/c3p0-0.9.1-pre6.src.zip
# lib/jboss-common-jdbc-wrapper.jar
# lib/jboss-common-jdbc-wrapper-src.jar
# lib/protobuf-java-3.6.1.jar
# lib/slf4j-api-1.6.1.jar
#
# See http://bugs.mysql.com/bug.php?id=28512 for details.

# To make it easier a script generate-tarball.sh has been created:
# ./generate-tarball.sh version
# will create a new tarball compressed with xz and without those jar files.
Source1:       generate-tarball.sh

Patch1:        remove-coverage-test.patch
Patch2:        java-11-migration.patch
Patch3:        remove-authentication-plugin.patch
Patch4:        remove-StatementsTest.patch

BuildArch:     noarch

BuildRequires: ant >= 1.6.0
BuildRequires: ant-junit
BuildRequires: apache-commons-logging
BuildRequires: git
BuildRequires: javassist
BuildRequires: javapackages-local
BuildRequires: junit5
BuildRequires: protobuf-java
BuildRequires: slf4j
BuildRequires: java-17-openjdk-devel

Requires:      slf4j
Requires: java
Source44: import.info

%description
MySQL Connector/J is a native Java driver that converts JDBC (Java Database
Connectivity) calls into the network protocol used by the MySQL database.
It lets developers working with the Java programming language easily build
programs and applets that interact with MySQL and connect all corporate
data, even in a heterogeneous environment. MySQL Connector/J is a Type
IV JDBC driver and has a complete JDBC feature set that supports the
capabilities of MySQL.

%prep
%setup -q -n mysql-connector-j-%{version}

# fix line endings
for file in README README.md; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

sed -i 's/>@.*</>%{version}</' src/build/misc/pom.xml

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build

# We need both JDK1.5 (for JDBC3.0; appointed by $JAVA_HOME) and JDK1.6 (for JDBC4.0; appointed in the build.xml)
export CLASSPATH=$(build-classpath jdbc-stdext junit slf4j commons-logging.jar)

# We currently need to disable jboss integration because of missing jboss-common-jdbc-wrapper.jar (built from sources).
# See BZ#480154 and BZ#471915 for details.
rm -rf src/main/user-impl/java/com/mysql/cj/jdbc/integration/jboss
rm src/test/java/testsuite/regression/ConnectionRegressionTest.java
rm src/test/java/testsuite/regression/DataSourceRegressionTest.java
rm src/test/java/testsuite/simple/StatementsTest.java

ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  -Dcom.mysql.cj.build.jdk=/usr/lib/jvm/java-17-openjdk \
    -Dcom.mysql.cj.extra.libs=%{_javadir} \
    test dist

%install
# Install the Maven build information
%mvn_file mysql:mysql-connector-java %{name}
%mvn_artifact src/build/misc/pom.xml build/%{name}-%{version}-SNAPSHOT/%{name}-%{version}-SNAPSHOT.jar
%mvn_install

%files -f .mfiles
%doc CHANGES README README.md
%doc --no-dereference LICENSE

%changelog
* Mon Apr 17 2023 Igor Vlasenko <viy@altlinux.org> 1:8.0.30-alt1_2jpp11
- update

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1:8.0.28-alt1_3jpp11
- new version

* Tue Jun 15 2021 Igor Vlasenko <viy@altlinux.org> 1:8.0.25-alt1_2jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:8.0.23-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1:8.0.21-alt1_2jpp8
- new version

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1:8.0.15-alt1_1jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1:5.1.38-alt1_6jpp8
- java fc28+ update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.1.38-alt1_5jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.1.38-alt1_4jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1:5.1.38-alt1_3jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1:5.1.36-alt1_1jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:5.1.26-alt1_2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:5.1.24-alt1_1jpp7
- new release

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 1:5.1.22-alt1_1jpp7
- new version

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 1:5.1.21-alt1_3jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1:5.1.15-alt2_1jpp6
- built with java 6

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 1:5.1.15-alt1_1jpp6
- new version

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 1:5.0.8-alt2_4jpp5
- selected java5 compiler explicitly

* Sun Aug 30 2009 Igor Vlasenko <viy@altlinux.ru> 1:5.0.8-alt1_4jpp5
- build w/o jboss support

* Wed Jan 16 2008 Igor Vlasenko <viy@altlinux.ru> 1:5.0.8-alt1_1jpp1.7
- converted from JPackage by jppimport script


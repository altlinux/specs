Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global     builddir        build-mysql-jdbc
%global     distdir         dist-mysql-jdbc

Summary:       Official JDBC driver for MySQL
Name:          mysql-connector-java
Version:       5.1.38
Release:       alt1_3jpp8
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
# src/lib/c3p0-0.9.1-pre6.jar
# src/lib/c3p0-0.9.1-pre6.src.zip
# src/lib/jboss-common-jdbc-wrapper.jar
# src/lib/jboss-common-jdbc-wrapper-src.jar
# src/lib/slf4j-api-1.6.1.jar
#
# See http://bugs.mysql.com/bug.php?id=28512 for details.

# To make it easier a script generate-tarball.sh has been created:
# ./generate-tarball.sh version
# will create a new tarball compressed with xz and without those jar files.
Source1:       generate-tarball.sh
# Patch to build with JDBC 4.1/Java 7
Patch0:        %{name}-5.1.38-jdbc4.1.patch
# Add system libraries
Patch1:        %{name}-5.1.38-build.patch
Patch2:        %{name}-hibernate.patch

BuildArch:     noarch

BuildRequires: ant >= 1.6.0
BuildRequires: ant-contrib >= 1.0
BuildRequires: apache-commons-logging
BuildRequires: c3p0
BuildRequires: git
BuildRequires: hibernate-core
BuildRequires: java-devel >= 1.6.0
BuildRequires: javapackages-local
BuildRequires: jta >= 1.0
BuildRequires: junit
BuildRequires: slf4j

Requires:      jta >= 1.0
Requires:      slf4j
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

sed -i 's/>@.*</>%{version}</' src/doc/sources/pom.xml

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build

# We need both JDK1.5 (for JDBC3.0; appointed by $JAVA_HOME) and JDK1.6 (for JDBC4.0; appointed in the build.xml)
export CLASSPATH=$(build-classpath jdbc-stdext jta junit slf4j commons-logging.jar)

# We currently need to disable jboss integration because of missing jboss-common-jdbc-wrapper.jar (built from sources).
# See BZ#480154 and BZ#471915 for details.
rm -rf src/com/mysql/jdbc/integration/jboss
rm src/testsuite/regression/ConnectionRegressionTest.java
rm src/testsuite/regression/DataSourceRegressionTest.java
rm src/testsuite/regression/jdbc4/ConnectionRegressionTest.java
rm src/testsuite/simple/ReadOnlyCallableStatementTest.java
rm src/testsuite/simple/jdbc4/StatementsTest.java

ant -DbuildDir=%{builddir} -DdistDir=%{distdir} \
    -Dcom.mysql.jdbc.jdk8=%{java_home} \
    -Dcom.mysql.jdbc.jdk6=%{java_home}/jre/lib/rt.jar \
    -Dcom.mysql.jdbc.extra.libs=/usr/share/java \
    dist

%install
# Install the Maven build information
%mvn_file mysql:mysql-connector-java %{name}
%mvn_artifact src/doc/sources/pom.xml build-mysql-jdbc/%{name}-%{version}-SNAPSHOT/%{name}-%{version}-SNAPSHOT-bin.jar
%mvn_install

%files -f .mfiles
%doc CHANGES README README.md
%doc COPYING

%changelog
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


# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global     builddir        build-mysql-jdbc
%global     distdir         dist-mysql-jdbc
%global     gcj_support     0
%global     java6_rtpath    %{java_home}/jre/lib/rt.jar
%global     java6_javacpath /usr/bin/javac
%global     java6_javapath  /usr/bin/javac

Summary:    Official JDBC driver for MySQL
Name:       mysql-connector-java
Version:    5.1.24
Release:    alt1_1jpp7
Epoch:      1 

# MySQL FLOSS Exception
License:    GPLv2 with exceptions
Group:      System/Libraries
URL:        http://dev.mysql.com/downloads/connector/j/

# Mysql has a mirror redirector for its downloads
# You can get this tarball by following a link from:
# http://dev.mysql.com/get/Downloads/Connector-J/%{name}-%{version}.zip/from/pick#mirrors
#
# Following prebuilt jars and sources have been removed from the tarball:
#
# %{name}-%{version}-bin.jar
# src/lib/ant-contrib.jar
# src/lib/c3p0-0.9.1-pre6.jar
# src/lib/c3p0-0.9.1-pre6.src.zip
# src/lib/jboss-common-jdbc-wrapper.jar
# src/lib/jboss-common-jdbc-wrapper-src.jar
# src/lib/slf4j-api-1.6.1.jar
#
# See http://bugs.mysql.com/bug.php?id=28512 for details.
Source0:            %{name}-%{version}.tar.gz

# Patch to build with JDBC 4.1/Java 7
Patch0:             %{name}-jdbc-4.1.patch


%if ! %{gcj_support}
BuildArch:          noarch
%endif

%if %{gcj_support}
BuildRequires:      java-gcj-compat-devel >= 1.0.31
Requires(post):     java-gcj-compat >= 1.0.31
Requires(postun):   java-gcj-compat >= 1.0.31
%endif

BuildRequires:      ant >= 1.6.0
BuildRequires:      ant-contrib >= 1.0
BuildRequires:      jpackage-utils >= 1.6
BuildRequires:      jta >= 1.0
BuildRequires:      junit
BuildRequires:      slf4j
%if %{gcj_support}
BuildRequires:      java-1.5.0-gcj-devel
%endif
BuildRequires:      jakarta-commons-logging

Requires:           jta >= 1.0
Requires:           slf4j
Requires:               jpackage-utils
Requires(post):         jpackage-utils
Requires(postun):       jpackage-utils
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
%setup -q -n %{name}-%{version}

# Remove duplicate README.txt files
rm README README.txt

# fix line endings
sed -i 's/\r//' docs/README.txt

%patch0 -p1 -F3

%build

# We need both JDK1.5 (for JDBC3.0; appointed by $JAVA_HOME) and JDK1.6 (for JDBC4.0; appointed in the build.xml)
export CLASSPATH=$(build-classpath jdbc-stdext jta junit slf4j commons-logging.jar)
%if %{gcj_support}
%endif

# We currently need to disable jboss integration because of missing jboss-common-jdbc-wrapper.jar (built from sources).
# See BZ#480154 and BZ#471915 for details.
rm -rf src/com/mysql/jdbc/integration/jboss
rm src/testsuite/regression/ConnectionRegressionTest.java
rm src/testsuite/regression/DataSourceRegressionTest.java
rm src/testsuite/simple/ReadOnlyCallableStatementTest.java
rm src/testsuite/simple/jdbc4/StatementsTest.java

ant -DbuildDir=%{builddir} -DdistDir=%{distdir} -Dcom.mysql.jdbc.java6.rtjar=%{java6_rtpath} -Dcom.mysql.jdbc.java6.javac=%{java6_javacpath} -Dcom.mysql.jdbc.java6.java=%{java6_javapath}

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{builddir}/%{name}-%{version}-SNAPSHOT/%{name}-%{version}-SNAPSHOT-bin.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# natively compile
%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

# Install the Maven build information
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 src/doc/sources/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
sed -i 's/>@.*</>%{version}</' $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_to_maven_depmap mysql %{name} %{version} JPP %{name}


%files
%doc CHANGES COPYING docs
%attr(0644,root,root) %{_javadir}/*.jar
%config(noreplace) %{_mavendepmapfragdir}/*
%{_mavenpomdir}/*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}
%endif

%changelog
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


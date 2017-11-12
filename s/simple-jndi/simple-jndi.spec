Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          simple-jndi
Version:       0.11.4.1
Release:       alt2_12jpp8
Summary:       A JNDI implementation
License:       BSD
Url:           https://github.com/hen/osjava
Source0:       http://osjava.googlecode.com/svn/dist/releases/official/simple-jndi/simple-jndi-0.11.4.1-src.tar.gz
# wget -O simple-jndi-0.11.4.1.pom http://osjava.googlecode.com/svn/releases/simple-jndi-0.11.4.1/pom.xml
Source1:       simple-jndi-%{version}.pom
Patch0:        simple-jndi-0.11.4.1-jdk7.patch

BuildRequires: java-devel
BuildRequires: javapackages-local
BuildRequires: ant
BuildRequires: apache-commons-dbcp
BuildRequires: apache-commons-pool
BuildRequires: junit

BuildArch:     noarch
Source44: import.info

%description
Simple-JNDI is intended to solve two problems. The first is
that of finding a container independent way of opening a
database connection, the second is to find a good way of
specifying application configurations.
1. Unit tests or prototype code often need to emulate the
  environment within which the code is expected to run.
  A very common one is to get an object of type
  javax.sql.DataSource from JNDI so a java.sql.Connection
  to your database of choice may be opened.
2. Applications need configuration; a JNDI implementation
  makes a handy location for configuration values. Either
  as a globally available system, or via IoC through the
  use of some kind of JNDI configuration facade (see gj-config).
A solution: simple implementation of JNDI. It is entirely
library based, so no server instances are started, and it
sits upon Java .properties files, XML files or Windows-style
.ini files, so it is easy to use and simple to understand.
The files may be either on the file system or in the classpath.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n simple-jndi-%{version}
find . -name "*.class" -delete
find . -name "*.jar" -delete
%patch0 -p0

# this test at random fails
rm -r src/test/org/osjava/sj/memory/SharedMemoryTest.java

%build

%ant \
  -Dlibdir=lib \
  -Dcommons-pool.jar=file://$(build-classpath commons-pool) \
  -Dcommons-dbcp.jar=file://$(build-classpath commons-dbcp) \
  jar javadoc

%install
%mvn_artifact %{SOURCE1} target/%{name}-%{version}.jar
%mvn_file %{name}:%{name} %{name}
%mvn_install -J dist/docs/api

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.11.4.1-alt2_12jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.11.4.1-alt2_11jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.11.4.1-alt2_10jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.11.4.1-alt2_9jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.11.4.1-alt2_6jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.11.4.1-alt2_2jpp7
- fc update

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.4.1-alt2_2jpp6
- built with java 6 due to abstract getParentLogger

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.4.1-alt1_2jpp6
- new jpp relase

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0.11.4.1-alt1_1jpp6
- new version


Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

Name:          simple-jndi
Version:       0.11.4.1
Release:       alt2_6jpp7
Summary:       A JNDI implementation
License:       BSD
Url:           http://code.google.com/p/osjava/
Source0:       http://osjava.googlecode.com/svn/dist/releases/official/simple-jndi/simple-jndi-0.11.4.1-src.tar.gz
# wget -O simple-jndi-0.11.4.1.pom http://osjava.googlecode.com/svn/releases/simple-jndi-0.11.4.1/pom.xml
Source1:       simple-jndi-%{version}.pom
Patch0:        simple-jndi-0.11.4.1-jdk7.patch

BuildRequires: jpackage-utils

BuildRequires: ant ant-junit
BuildRequires: apache-commons-dbcp
BuildRequires: apache-commons-pool
BuildRequires: junit

Requires:      apache-commons-dbcp
Requires:      apache-commons-pool

Requires:      jpackage-utils
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

mkdir -p %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}/

%files -f .mfiles
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
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


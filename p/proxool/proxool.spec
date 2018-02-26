BuildRequires: /proc
BuildRequires: jpackage-compat
%define git_commit 659fc71

Summary: Java connection pool library
Name:    proxool
Version: 0.9.1
Release: alt2_6jpp7
Epoch: 0
License: ASL 2.0
URL: http://proxool.sourceforge.net/
Group: Development/Java
# Grabbing a newer version from git due to license change
# https://github.com/proxool/proxool/tarball/master
# (commit 659fc71e617151327779802a5171f0da8205918d)
Source0: proxool-proxool-%{git_commit}.tar.gz
Source1: proxool.pom
Patch0: proxool-no-embedded-cglib.patch

BuildRequires: jpackage-utils
BuildRequires: ant >= 0:1.7.1
BuildRequires: ant-junit
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: cglib
BuildRequires: dom4j
BuildRequires: avalon-framework
BuildRequires: hsqldb >= 0:1.80
BuildRequires: junit
BuildRequires: log4j
BuildRequires: tomcat6-servlet-2.5-api
BuildRequires: checkstyle

Requires: avalon-logkit
Requires: dom4j
Requires: jta
Requires: jpackage-utils
BuildArch: noarch
Source44: import.info

%description
Transparently adds connection pooling to your existing JDBC driver.
Complies with the J2SE API, giving you the confidence to develop to
standards. You can monitor the performance of your database
connections and listen to connection events.
It's easy to configure using the JDBC API, XML, or Java property
files - you decide.

%package javadoc
Summary: Javadoc for %{name}
Group:   Development/Java
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{git_commit}
#find . -name "*.jar" -exec rm {} \;
find . -type f -a -executable -exec chmod -x {} \;
rm -rf lib jarjar

%patch0 -p1 -b .sav0

%build
echo ant.build.javac.source=1.5 >> %name-ant.properties
echo ant.build.javac.target=1.5 >> %name-ant.properties
CLASSPATH=$( build-classpath cglib avalon-framework servlet ) ant build-jar javadoc

%install
# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -m 0644 build/%{name}-%{version}.jar \
$RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 0644 %{S:1} $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc *.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENCE.txt
%doc %{_javadocdir}/%{name}

%changelog
* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1-alt2_6jpp7
- target 5 build

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1-alt1_6jpp7
- fc version

* Wed May 13 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.8.3-alt4_10jpp5
- repocop bugfixes

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.8.3-alt3_10jpp5
- fixed build with java 5

* Mon Mar 24 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.8.3-alt2_10jpp1.7
- fixed alternatives intersection

* Sat Nov 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.8.3-alt1_10jpp1.7
- converted from JPackage by jppimport script


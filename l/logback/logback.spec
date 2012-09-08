BuildRequires: geronimo-jms
Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		logback
Version:	1.0.6
Release:	alt1_3jpp7
Summary:	A Java logging library

Group:		Development/Java
License:	LGPLv2 or EPL
URL:		http://logback.qos.ch/
Source0:	http://logback.qos.ch/dist/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-00-build.xml
Source2:	%{name}-%{version}-core-osgi.bnd
Source3:	%{name}-%{version}-classic-osgi.bnd
Source4:	%{name}-%{version}-access-osgi.bnd
# Use Janino 2.6 API
Patch0:		%{name}-%{version}-janino-2_6.patch

# Java dependencies
BuildRequires:	jpackage-utils

# Required libraries
BuildRequires:	jms
BuildRequires:	janino
# require jansi 1.8
BuildRequires:	jansi
# Using the version of jetty in the pom.xml file
BuildRequires:	jetty >= 7.5.1
BuildRequires:	slf4j
BuildRequires:	tomcat-servlet-3.0-api
BuildRequires:	tomcat-lib
BuildRequires:	javamail
BuildRequires:	apache-commons-cli
BuildRequires:	antlr-tool
BuildRequires:	log4j

# Build tools -- build with ant for now because of circular dependencies
BuildRequires:	ant
BuildRequires:	aqute-bnd
BuildRequires:	groovy

BuildArch:	noarch

# Java runtime dependencies
Requires:	jpackage-utils

# Java library dependencies
Requires:	jansi
Requires:	jms
Requires:	janino
Requires:	slf4j
Source44: import.info

%description
Logback is intended as a successor to the popular log4j project. At present
time, logback is divided into three modules, logback-core, logback-classic
and logback-access.

The logback-core module lays the groundwork for the other two modules. The
logback-classic module can be assimilated to a significantly improved
version of log4j. Moreover, logback-classic natively implements the SLF4J
API so that you can readily switch back and forth between logback and other
logging frameworks such as log4j or java.util.logging (JUL).

The logback-access module integrates with Servlet containers, such as
Tomcat and Jetty, to provide HTTP-access log functionality. Note that you
could easily build your own module on top of logback-core.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for the Logback library

%package access
Summary:	Logback-access module for Servlet integration
Group:		Development/Java
Requires:	%{name} = %{version}
Requires:	jetty >= 7.5.1
Requires:	tomcat-lib
Requires:	tomcat-servlet-3.0-api

%description access
The logback-access module integrates with Servlet containers, such as Tomcat
and Jetty, to provide HTTP-access log functionality. Note that you could
easily build your own module on top of logback-core. 

%package examples
Summary:	Sample code for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}

%description examples
Sample code for the Logback library

%prep
%setup -q
%{__cp} %{SOURCE1} ./build.xml
%patch0 -p0

find . -name "*.jar" -delete

# Clean up the documentation
sed -i 's/\r//' LICENSE.txt README.txt docs/*.* docs/*/*.* docs/*/*/*.*
sed -i 's#"apidocs#"%{_javadocdir}/%{name}#g' docs/*.html
rm -rf docs/apidocs docs/project-reports docs/testapidocs docs/project-reports.html
rm -f docs/manual/.htaccess docs/css/site.css # Zero-length file

cp -p %{SOURCE2} osgi-core.bnd
cp -p %{SOURCE3} osgi-classic.bnd
cp -p %{SOURCE4} osgi-access.bnd

sed -i 's#<artifactId>groovy-all</artifactId#<artifactId>groovy</artifactId#' $(find . -name "pom.xml")

%build
ant dist javadoc

%install
install -d -m 755 p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -r dist/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom
%add_maven_depmap JPP.%{name}-%{name}-parent.pom

for sub in logback-access logback-classic logback-core; do
	install -m 644 dist/$sub-%{version}.jar \
		$RPM_BUILD_ROOT%{_javadir}/%{name}/$sub.jar
	install -m 644 $sub/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-$sub.pom
    %add_maven_depmap JPP.%{name}-$sub.pom %{name}/$sub.jar
done


install -m 644 dist/logback-examples-%{version}.jar \
	$RPM_BUILD_ROOT%{_javadir}/%{name}/logback-examples.jar
install -m 644 logback-examples/pom.xml \
	$RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-logback-examples.pom
%add_maven_depmap JPP.%{name}-logback-examples.pom %{name}/logback-examples.jar -f examples

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/examples
cp -r logback-examples/pom.xml logback-examples/src $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/examples

%files
%doc LICENSE.txt README.txt docs/*
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/logback-classic.jar
%{_javadir}/%{name}/logback-core.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP.logback-logback-classic.pom
%{_mavenpomdir}/JPP.logback-logback-core.pom
%{_mavenpomdir}/JPP.logback-logback-parent.pom
%exclude %{_javadir}/%{name}/%{name}-examples.jar
%exclude %{_mavenpomdir}/JPP.%{name}-%{name}-examples.pom

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%files access
%{_javadir}/%{name}/logback-access.jar
%{_mavenpomdir}/JPP.logback-logback-access.pom

%files examples
%doc LICENSE.txt
%{_datadir}/%{name}-%{version}
%{_javadir}/%{name}/%{name}-examples.jar
%{_mavendepmapfragdir}/%{name}-examples
%{_mavenpomdir}/JPP.%{name}-%{name}-examples.pom

%changelog
* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_3jpp7
- new version

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.27-alt1_1jpp6
- new version

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.14-alt2_2jpp6
- build with compat slf4j15

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.14-alt1_2jpp6
- new version


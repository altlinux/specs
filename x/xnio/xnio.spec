BuildRequires: javassist
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name xnio
%define version 3.0.3
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             xnio
Version:          3.0.3
Release:          alt2_3jpp7
Summary:          JBoss XNIO
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/xnio

# git clone git://github.com/jboss-remoting/xnio.git
# cd xnio/ && git archive --format=tar --prefix=xnio-3.0.3.GA/ 3.0.3.GA | xz > xnio-3.0.3.GA.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz
Patch00:          %{name}-%{namedversion}-jmock.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven

BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin
BuildRequires:    maven-eclipse-plugin
BuildRequires:    maven-ejb-plugin
BuildRequires:    jboss-parent
BuildRequires:    jboss-logging
BuildRequires:    jboss-logmanager
BuildRequires:    maven-injection-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    junit4

Requires:         jboss-logmanager
Requires:         jboss-logging
Requires:         jpackage-utils
Source44: import.info

%description
A simplified low-level I/O layer which can be used anywhere you are
using NIO today. It frees you from the hassle of dealing with Selectors and
the lack of NIO support for multicast sockets and non-socket I/O, while still
maintaining all the capabilities present in NIO.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1

%build
# No jmock
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p api/target/%{name}-api-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-api.jar
cp -p nio-impl/target/%{name}-nio-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-nio.jar

# APIDOCS
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POMS
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 api/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-api.pom
install -pm 644 nio-impl/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-nio.pom
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}-api.pom %{name}-api.jar
%add_maven_depmap JPP-%{name}-nio.pom %{name}-nio.jar
%add_maven_depmap JPP-%{name}.pom

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc COPYING.txt

%files javadoc
%{_javadocdir}/%{name}
%doc COPYING.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_3jpp7
- new version


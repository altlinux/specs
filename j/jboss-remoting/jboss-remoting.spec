BuildRequires: javassist
Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-remoting
%define version 3.2.4
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jboss-remoting
Version:          3.2.4
Release:          alt2_2jpp7
Summary:          JBoss Remoting 3
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/jbossremoting

# git clone git://github.com/jboss-remoting/jboss-remoting.git
# cd jboss-remoting && git checkout 3.2.4.GA && git checkout-index -f -a --prefix=jboss-remoting-3.2.4.GA/
# rm jboss-remoting-3.2.4.GA/src/test/resources/test-content.bin
# tar -cJf jboss-remoting-3.2.4.GA-CLEAN.tar.xz jboss-remoting-3.2.4.GA
Source0:          %{name}-%{namedversion}-CLEAN.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-injection-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    maven-enforcer-plugin
BuildRequires:    jboss-parent
BuildRequires:    xnio
BuildRequires:    jboss-logmanager
BuildRequires:    jboss-logging-tools
BuildRequires:    junit4
BuildRequires:    apiviz

Requires:         jboss-logmanager
Requires:         jboss-logging-tools
Requires:         xnio
Requires:         jpackage-utils
Source44: import.info

%description
The purpose of JBoss Remoting is to provide a general purpose framework
for symmetric and asymmetric communication over a network. It supports
various modes of interaction, including invocations, one way messaging,
and asynchronous callbacks.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%build
# Skipped test because of removing binary content from test dir which is required to run them
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# APIDOCS
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc COPYING.txt

%files javadoc
%{_javadocdir}/%{name}
%doc COPYING.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt1_2jpp7
- new version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt2_4jpp6
- hack: built w/o jdk6 support for jboss/jbossas 4 support

* Sat Jan 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_4jpp6
- converted from JPackage by jppimport script

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2.2-alt1_3.SP8.1jpp5
- new version

* Fri Mar 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2.2-alt0.1jpp
- bootstrap for jbossas


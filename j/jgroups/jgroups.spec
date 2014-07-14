Epoch: 1
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jgroups
%define version 3.0.6
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:     jgroups
Version:  3.0.6
Release:  alt2_2jpp7
Summary:  Toolkit for reliable multicast communication
License:  LGPLv2+
URL:      http://www.jgroups.org
Group:    Development/Java

# git clone git://github.com/belaban/JGroups.git jgroups
# cd jgroups && git checkout JGroups_3_0_6_Final && git checkout-index -f -a --prefix=jgroups-3.0.6.Final/
# find jgroups-3.0.6.Final/ -name '*.class' -delete
# find jgroups-3.0.6.Final/ -name '*.jar' -delete
# tar cafJ jgroups-3.0.6.Final-CLEAN.tar.xz jgroups-3.0.6.Final
Source0:  %{name}-%{namedversion}-CLEAN.tar.xz
Patch0:   %{name}-%{namedversion}-pom.patch

Requires: jpackage-utils

BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: bsh
BuildRequires: log4j
BuildRequires: maven
BuildRequires: maven-antrun-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-surefire-provider-junit
BuildRequires: testng

BuildArch:     noarch
Source44: import.info

%description
JGroups is a toolkit for reliable multicast communication. (Note that
this doesn't necessarily mean IP Multicast, JGroups can also use
transports such as TCP). It can be used to create groups of processes
whose members can send messages to each other.

%package  javadoc
Summary:  API documentation for %{name}
Group:    Development/Java
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion} 
%patch0 -p1

%build
mvn-rpmbuild install javadoc:aggregate

%install

# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# JAVADOC
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
%doc INSTALL.html LICENSE README

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.0.6-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.0.6-alt1_2jpp7
- new version

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 1:2.6.10-alt1_4jpp6
- new version

* Sat Sep 27 2008 Igor Vlasenko <viy@altlinux.ru> 1:2.4.1-alt2_1.SP4.1jpp5
- fixed build

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:2.4.1-alt1_1.SP4.1jpp5
- converted from JPackage by jppimport script

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2.9.2-alt1_3jpp1.7
- converted from JPackage by jppimport script


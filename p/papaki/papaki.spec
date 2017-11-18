BuildRequires: javapackages-local
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.0
%global namedreltag .Beta3
%global namedversion %{version}%{?namedreltag}

Name:           papaki
Version:        1.0.0
Release:        alt2_0.9.Beta3jpp8
Summary:        An annotation scanner and repository

License:        LGPLv2+
URL:            http://anonsvn.jboss.org/repos/jbossas/projects/annotations/trunk/


# svn export http://anonsvn.jboss.org/repos/jbossas/projects/annotations/tags/PAPAKI_1_0_0_BETA3 papaki-1.0.0.Beta3
# find papaki-1.0.0.Beta3 -name "*.jar" -type f -delete
# find papaki-1.0.0.Beta3 -name ".svn" -type d | xargs rm -rf
# tar -czf papaki-1.0.0.Beta3.tar.gz papaki-1.0.0.Beta3
# List of removed files: https://gist.github.com/2496466
Source0:        %{name}-%{namedversion}.tar.gz

# POM file for artifact: papaki-core
Source1:        https://repository.jboss.org/nexus/content/groups/public/org/jboss/papaki/papaki-core/1.0.0.Beta3/papaki-core-1.0.0.Beta3.pom

# POM file for artifact: papaki-indexer
Source2:        https://repository.jboss.org/nexus/content/groups/public/org/jboss/papaki/papaki-indexer/1.0.0.Beta3/papaki-indexer-1.0.0.Beta3.pom

# Commented out retrieving jars from Internet and limiting the jars to build
Patch0:         %{name}-ivy.patch

# Commented out trying to download Ivy from the Internet
Patch1:         %{name}-build.patch

# Add jdepend to classpath for javadoc
Patch2:         %{name}-javadoc.patch
 
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  java-devel >= 1.6.0

BuildRequires:  apache-ivy
BuildRequires:  junit
BuildRequires:  ant
BuildRequires:  apiviz
BuildRequires:  jdepend
BuildRequires:  javassist

Requires:       jpackage-utils
Requires:       javassist
Source44: import.info

%description
Papaki is a library for scanning annotations in Java 5+ code
and generate a repository of these annotations.

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
%patch1 -p1
%patch2 -p1

# Remove class-path from MANIFEST.MF
sed -i '/class-path/I d' core/src/main/resources/core-manifest.mf
sed -i '/class-path/I d' indexer/src/main/resources/indexer-manifest.mf

%build
ant docs release

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JARs
install -pm 644 target/%{name}-core.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core.jar
install -pm 644 target/%{name}-indexer.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-indexer.jar

# POMs
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-core.pom
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-indexer.pom

%add_maven_depmap JPP.%{name}-%{name}-core.pom %{name}/%{name}-core.jar
%add_maven_depmap JPP.%{name}-%{name}-indexer.pom %{name}/%{name}-indexer.jar

# JAVADOC
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}/%{name}-core
cp -rp build/%{name}-%{namedversion}/doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/%{name}-core
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}/%{name}-indexer
cp -rp target/docs/indexer/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/%{name}-indexer

%files
%{_mavenpomdir}/*
%{_javadir}/*
%{_datadir}/maven-metadata/*
%doc README.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.9.Beta3jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.9.Beta3jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.8.Beta3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.7.Beta3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.4.Beta3jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.3.Beta3jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.2.Beta3jpp7
- new version


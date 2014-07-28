Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-vfs
%define version 3.1.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-vfs
Version:          3.1.0
Release:          alt2_6jpp7
Summary:          JBoss Virtual File System
Group:            Development/Java
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-vfs/

# Microsoft JDBC driver needs to be removed
#
# git clone git://github.com/jbossas/jboss-vfs.git
# cd jboss-vfs && git checkout 3.1.0.Final && git checkout-index -f -a --prefix=jboss-vfs-3.1.0.Final/
# rm jboss-vfs-3.1.0.Final/src/test/resources/vfs/test/zipeinit.jar
# tar -cJf jboss-vfs-3.1.0.Final-CLEAN.tar.xz jboss-vfs-3.1.0.Final
Source0:          %{name}-%{namedversion}-CLEAN.tar.xz
Patch0:           %{name}-%{namedversion}-pom.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
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
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    jboss-logging
BuildRequires:    junit4
BuildRequires:    jboss-parent

Requires:         jboss-logging
Requires:         jpackage-utils
Source44: import.info

%description
This package contains the JBoss Virtual File System.

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

rm -rf .classpath archives/ .project

%build
# Skipped because jboss-test is not packaged already
mvn-rpmbuild install -Dmaven.test.skip=true javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt1_4jpp7
- new version

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_2jpp5
- new version


Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-naming
%define version 5.0.6
%global namedreltag .CR1
%global namedversion %{version}%{?namedreltag}

Name:             jboss-naming
Version:          5.0.6
Release:          alt2_0.6.CR1jpp7
Summary:          JBoss Naming
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org

# svn export http://anonsvn.jboss.org/repos/jbossas/projects/naming/tags/5.0.6.CR1/ jboss-naming-5.0.6.CR1
# tar cafJ jboss-naming-5.0.6.CR1.tar.xz jboss-naming-5.0.6.CR1
Source0:          %{name}-%{namedversion}.tar.xz

Patch0:           %{name}-%{namedversion}-pom.patch

BuildArch:        noarch

BuildRequires:    jboss-common-core
BuildRequires:    jboss-logging
BuildRequires:    jboss-parent
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-antrun-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    rmic-maven-plugin

Requires:         jboss-common-core
Requires:         jboss-logging
Requires:         jpackage-utils
Source44: import.info

%description
The JBoss JNDI name server implementation

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
# No jboss-test and jboss-kernel packages
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 jnpclient/target/jnp-client-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-client.jar
install -pm 644 jnpserver/target/jnpserver-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-server.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-build.pom
install -pm 644 jnpclient/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-client.pom
install -pm 644 jnpserver/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-server.pom

# DEPMAP
%add_maven_depmap JPP-%{name}-build.pom
%add_maven_depmap JPP-%{name}-client.pom %{name}-client.jar
%add_maven_depmap JPP-%{name}-server.pom %{name}-server.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc JBossORG-EULA.txt

%files javadoc
%{_javadocdir}/%{name}
%doc JBossORG-EULA.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0.6-alt2_0.6.CR1jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0.6-alt2_0.4.CR1jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.6-alt1_0.4.CR1jpp7
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.3-alt1_3jpp6
- new version


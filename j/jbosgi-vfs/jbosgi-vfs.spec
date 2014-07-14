BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbosgi-vfs
%define version 1.1.2
%global namedreltag .CR1
%global namedversion %{version}%{?namedreltag}

Name:             jbosgi-vfs
Version:          1.1.2
Release:          alt2_0.4.CR1jpp7
Summary:          JBoss OSGi Virtual File System
Group:            Development/Java
License:          LGPLv2+
URL:              http://community.jboss.org/wiki/JBossOSGi

# git clone git://github.com/jbosgi/jbosgi-vfs.git
# cd jbosgi-vfs/ && git archive --format=tar --prefix=jbosgi-vfs-1.1.2.CR1/ 1.1.2.CR1 | xz > jbosgi-vfs-1.1.2.CR1.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    jbosgi-parent
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    felix-osgi-core
BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools
BuildRequires:    jboss-vfs
BuildRequires:    shrinkwrap
BuildRequires:    junit

Requires:         jpackage-utils
Requires:         felix-osgi-core
Requires:         jboss-logging
Requires:         jboss-logging-tools
Requires:         jboss-vfs
Requires:         shrinkwrap
Source44: import.info

%description
This package contains the JBoss OSGi Virtual File System

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
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 api/target/jbosgi-vfs-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-vfs.jar
install -pm 644 vfs30/target/jbosgi-vfs30-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-vfs30.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-parent.pom
install -pm 644 api/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-vfs.pom
install -pm 644 vfs30/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-vfs30.pom

# DEPMAP
%add_maven_depmap JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}-vfs.pom %{name}-vfs.jar
%add_maven_depmap JPP-%{name}-vfs30.pom %{name}-vfs30.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt2_0.4.CR1jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_0.4.CR1jpp7
- new version


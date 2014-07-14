BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbosgi-resolver
%define version 2.0.0
%global namedreltag .Beta2
%global namedversion %{version}%{?namedreltag}

Name:             jbosgi-resolver
Version:          2.0.0
Release:          alt2_0.3.Beta2jpp7
Summary:          Standalone OSGi Resolver 
Group:            Development/Java
License:          LGPLv2+
URL:              http://community.jboss.org/wiki/JBossOSGi

# git clone git://github.com/jbosgi/jbosgi-resolver.git
# cd jbosgi-resolver/ && git archive --format=tar --prefix=jbosgi-resolver-2.0.0.Beta2/ 2.0.0.Beta2 | xz > jbosgi-resolver-2.0.0.Beta2.tar.xz
Source0:          jbosgi-resolver-%{namedversion}.tar.xz

# Shipped osgi.core is outdated, we need to use felix directly
Patch0:           0001-Use-felix-directly.patch
# Support for JDK7
Patch1:           0002-JDK7-support.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    jbosgi-parent
BuildRequires:    mockito
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    felix-osgi-core
BuildRequires:    jboss-logging
BuildRequires:    jboss-modules
BuildRequires:    jboss-logmanager
BuildRequires:    jbosgi-metadata
BuildRequires:    jbosgi-spi
BuildRequires:    jbosgi-vfs
BuildRequires:    felix-osgi-obr-resolver
BuildRequires:    felix-framework

Requires:         jpackage-utils
Requires:         felix-osgi-core
Requires:         jboss-modules
Requires:         jboss-logging
Requires:         jboss-logmanager
Requires:         jbosgi-metadata
Requires:         jbosgi-spi
Requires:         jbosgi-vfs
Requires:         felix-osgi-obr-resolver
Requires:         felix-framework
Source44: import.info

%description
This package contains the JBoss OSGi Resolver.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jbosgi-resolver-%{namedversion}

%patch0 -p1
%patch1 -p1

%build
# No org.jboss.osgi.testing classes available
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

for m in api felix; do
  # JAR
  install -pm 644 ${m}/target/jbosgi-resolver-${m}-v2-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${m}.jar
  # POM
  install -pm 644 ${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom

# DEPMAP
%add_maven_depmap JPP.%{name}-%{name}-parent.pom

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_0.3.Beta2jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_0.3.Beta2jpp7
- new version


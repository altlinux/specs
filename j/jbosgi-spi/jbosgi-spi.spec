BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbosgi-spi
%define version 3.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbosgi-spi
Version:          3.0.1
Release:          alt2_2jpp7
Summary:          JBossOSGi SPI
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/

# git clone git://github.com/jbosgi/jbosgi-spi.git
# cd jbosgi-spi/ && git archive --format=tar --prefix=jbosgi-spi-3.0.1.Final/ 3.0.1.Final | xz > jbosgi-spi-3.0.1.Final.tar.xz
Source0:          jbosgi-spi-%{namedversion}.tar.xz

Patch0:           0001-Remove-osgi.enterprise-dependency.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    jbosgi-parent
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    jboss-logging
BuildRequires:    jbosgi-vfs
BuildRequires:    args4j
BuildRequires:    shrinkwrap
BuildRequires:    felix-osgi-core

Requires:         jpackage-utils
Requires:         jboss-logging
Requires:         jbosgi-vfs
Requires:         args4j
Requires:         shrinkwrap
Requires:         felix-osgi-core
Source44: import.info

%description
This pakcage contains the JBossOSGi SPI.

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
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jbosgi-spi-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
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
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_2jpp7
- new version


# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbosgi-deployment
%define version 1.0.12
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbosgi-deployment
Version:          1.0.12
Release:          alt2_5jpp7
Summary:          JBoss OSGi Deployment
Group:            Development/Java
License:          LGPLv2+
URL:              http://community.jboss.org/wiki/JBossOSGi

# git clone git://github.com/jbosgi/jbosgi-deployment.git
# cd jbosgi-deployment/ && git archive --format=tar --prefix=jbosgi-deployment-1.0.12.Final/ 1.0.12.Final | xz > jbosgi-deployment-1.0.12.Final.tar.xz
Source0:          jbosgi-deployment-%{namedversion}.tar.xz


BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    jbosgi-parent
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    jbosgi-spi
BuildRequires:    jbosgi-vfs
BuildRequires:    jboss-logging
BuildRequires:    felix-osgi-core

Requires:         jpackage-utils
Requires:         jbosgi-spi
Requires:         jbosgi-vfs
Requires:         jboss-logging
Requires:         felix-osgi-core
Source44: import.info

%description
This package contains the JBoss OSGi deployment support.

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
# jbosgi-testing not available
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jbosgi-deployment-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

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
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.12-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.12-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.12-alt1_3jpp7
- new version


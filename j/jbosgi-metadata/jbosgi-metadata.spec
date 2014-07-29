# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbosgi-metadata
%define version 2.0.3
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbosgi-metadata
Version:          2.0.3
Release:          alt2_5jpp7
Summary:          JBoss OSGi Metadata
Group:            Development/Java
License:          LGPLv2+ and LGPLv2 and ASL 2.0
URL:              http://community.jboss.org/wiki/JBossOSGi

# git clone git://github.com/jbosgi/jbosgi-metadata.git
# cd jbosgi-metadata/ && git archive --format=tar --prefix=jbosgi-metadata-2.0.3.Final/ 2.0.3.Final | xz > jbosgi-metadata-2.0.3.Final.tar.xz
Source0:          jbosgi-metadata-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    jbosgi-parent
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    felix-osgi-core
BuildRequires:    jboss-logging

Requires:         jpackage-utils
Requires:         felix-osgi-core
Requires:         jboss-logging
Source44: import.info

%description
This package contains the JBoss OSGi Metadata.

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
install -pm 644 target/jbosgi-metadata-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

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
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt1_3jpp7
- new version


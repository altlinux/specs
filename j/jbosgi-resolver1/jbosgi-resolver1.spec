# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbosgi-resolver1
%define version 1.0.13
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbosgi-resolver1
Version:          1.0.13
Release:          alt2_6jpp7
Summary:          Standalone OSGi Resolver 
Group:            Development/Java
License:          LGPLv2+
URL:              http://community.jboss.org/wiki/JBossOSGi

# git clone git://github.com/jbosgi/jbosgi-resolver.git
# cd jbosgi-resolver/ && git archive --format=tar --prefix=jbosgi-resolver-1.0.13.Final/ 1.0.13.Final | xz > jbosgi-resolver-1.0.13.Final.tar.xz
Source0:          jbosgi-resolver-%{namedversion}.tar.xz

# Missing test dependencies: org.jboss.osgi.testing
Patch0:           0001-Disable-itests-module.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    jbosgi-parent
BuildRequires:    mockito
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    felix-osgi-core
BuildRequires:    jboss-logging
BuildRequires:    jboss-logmanager
BuildRequires:    jbosgi-metadata
BuildRequires:    jbosgi-spi
BuildRequires:    jbosgi-vfs

Requires:         jpackage-utils
Requires:         felix-osgi-core
Requires:         jboss-logging
Requires:         jboss-logmanager
Requires:         jbosgi-metadata
Requires:         jbosgi-spi
Requires:         jbosgi-vfs
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

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

for m in api spi felix; do
  # JAR
  install -pm 644 ${m}/target/jbosgi-resolver-${m}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${m}.jar
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
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_4jpp7
- new version


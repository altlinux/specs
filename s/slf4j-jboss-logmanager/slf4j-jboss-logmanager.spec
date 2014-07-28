# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name slf4j-jboss-logmanager
%define version 1.0.0
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             slf4j-jboss-logmanager
Version:          1.0.0
Release:          alt2_5jpp7
Summary:          SLF4J backend for JBoss LogManager
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org

# git clone git://github.com/jboss-logging/slf4j-jboss-logmanager.git
# cd slf4j-jboss-logmanager/ && git archive --format=tar --prefix=slf4j-jboss-logmanager-1.0.0.GA/ 1.0.0.GA | xz > slf4j-jboss-logmanager-1.0.0.GA.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    jboss-logmanager
BuildRequires:    slf4j

Requires:         jpackage-utils
Requires:         jboss-logmanager
Requires:         slf4j
Source44: import.info

%description
This package contains SLF4J backend for JBoss LogManager

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
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}

# JAR
install -pm 644 target/%{name}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- new version


# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-dmr
%define version 1.1.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-dmr
Version:          1.1.1
Release:          alt2_9jpp7
Summary:          JBoss DMR
Group:            Development/Java
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-dmr

# git clone git://github.com/jbossas/jboss-dmr.git
# cd jboss-dmr/ && git archive --format=tar --prefix=jboss-dmr-1.1.1.Final/ 1.1.1.Final | xz > jboss-dmr-1.1.1.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local

BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    apt-maven-plugin
BuildRequires:    junit4
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    jboss-parent
BuildRequires:    jboss-logmanager
BuildRequires:    cookcc
BuildRequires:    apiviz

Requires:         cookcc
Requires:         jboss-logmanager
Requires:         jpackage-utils
Source44: import.info

%description
This package contains the Dynamic Model Representation.

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
# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# APIDOCS
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_9jpp7
- new release

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_6jpp7
- fixed build

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_6jpp7
- new version


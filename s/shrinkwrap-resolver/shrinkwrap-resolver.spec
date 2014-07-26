# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name shrinkwrap-resolver
%define version 1.0.0
%global namedreltag .beta7
%global upstreamreltag -beta-7
%global namedversion %{version}%{?namedreltag}

Name:             shrinkwrap-resolver
Version:          1.0.0
Release:          alt2_0.2.beta7jpp7
Summary:          ShrinkWrap Resolver
Group:            Development/Java
License:          ASL 2.0
URL:              http://www.jboss.org/shrinkwrap

# git clone git://github.com/shrinkwrap/resolver.git
# cd resolver/ && git archive --format=tar --prefix=shrinkwrap-resolver-1.0.0.beta7/ 1.0.0-beta-7 | xz > shrinkwrap-resolver-1.0.0.beta7.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

Patch0:           0001-Add-support-for-jetty-8.patch
Patch1:           0002-Use-correct-content-type-for-enhanced-repository-man.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    maven-model
BuildRequires:    maven-wagon
BuildRequires:    shrinkwrap
BuildRequires:    junit
BuildRequires:    aether
BuildRequires:    jetty-server

Requires:         jpackage-utils
Requires:         shrinkwrap
Requires:         aether
Requires:         maven
Requires:         maven-model
Requires:         maven-wagon
Source44: import.info

%description
This package contains the ShrinkWrap Resolver.

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
%patch1 -p1

%build
# The build pulls the incorrect maven-model.jar, so we need to explicitly require mvn3 version of it
mvn-rpmbuild -Dmaven.test.skip=true  -Dmaven.local.depmap.file=%{_mavendepmapfragdir}/maven install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

for m in api api-maven impl-maven; do
  # JAR
  install -pm 644 ${m}/target/shrinkwrap-resolver-${m}-%{version}%{upstreamreltag}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${m}.jar
  # POM
  install -pm 644 ${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom
install -pm 644 bom/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-bom.pom

# DEPMAP
%add_maven_depmap JPP.%{name}-%{name}-parent.pom
%add_maven_depmap JPP.%{name}-%{name}-bom.pom

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.2.beta7jpp7
- fixed build

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.2.beta7jpp7
- full build

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies


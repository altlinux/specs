BuildRequires: maven-plugin-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name apt-maven-plugin
%define version 1.0
%global namedreltag .alpha4
%global namedversion %{version}%{?namedreltag}

Name:             apt-maven-plugin
Version:          1.0
Release:          alt3_0.3.alpha4jpp7
Summary:          Apt Maven Plugin
Group:            Development/Java
License:          MIT
URL:              http://mojo.codehaus.org/apt-maven-plugin

# svn export http://svn.codehaus.org/mojo/tags/apt-maven-plugin-1.0-alpha-4/ apt-maven-plugin-1.0.alpha4
# tar cafJ apt-maven-plugin-1.0.alpha4.tar.xz apt-maven-plugin-1.0.alpha4
Source0:          %{name}-%{namedversion}.tar.xz

# Support for Maven 3 and disabling integration tests
Patch0:           %{name}-%{namedversion}-maven3.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    mojo-parent
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-invoker-plugin
BuildRequires:    maven-verifier-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-docck-plugin
BuildRequires:    objectweb-asm

Requires:         objectweb-asm
Requires:         maven
Requires:         maven-invoker-plugin
Requires:         jpackage-utils
Source44: import.info

%description
This plugin provides goals to run the Annotation Processing Tool (apt)
against project sources.

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
# Some deps missing to build integration tests which are required
# to build unit tests
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/%{name}-%{version}-alpha-4.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

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
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Thu Jul 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.3.alpha4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.3.alpha4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.3.alpha4jpp7
- new version


BuildRequires: maven-enforcer-plugin geronimo-jpa geronimo-jta
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name weld-api
%define version 1.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             weld-api
Version:          1.1
Release:          alt2_4jpp7
Summary:          Weld API
Group:            Development/Java
License:          ASL 2.0
URL:              http://seamframework.org/Weld

# git clone git://github.com/weld/api.git weld-api
# cd weld-api/ && git archive --format=tar --prefix=weld-api-1.1.Final/ 1.1.Final | xz > weld-api-1.1.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

# JSF api fix
Patch0:           %{name}-%{namedversion}-pom.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-testng
BuildRequires:    cdi-api
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    jboss-interceptors-1.1-api
BuildRequires:    jboss-ejb-3.1-api
BuildRequires:    jboss-jsf-2.1-api
BuildRequires:    hibernate-jpa-2.0-api
BuildRequires:    jboss-transaction-1.1-api
BuildRequires:    geronimo-annotation
BuildRequires:    weld-parent

Requires:         jpackage-utils
Requires:         cdi-api
Requires:         jboss-servlet-3.0-api
Requires:         jboss-interceptors-1.1-api
Requires:         jboss-ejb-3.1-api
Requires:         jboss-jsf-2.1-api
Requires:         hibernate-jpa-2.0-api
Requires:         jboss-transaction-1.1-api
Requires:         geronimo-annotation
Source44: import.info

%description
Weld specifc extensions to the CDI API

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
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 weld/target/weld-api-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/weld-api.jar
install -pm 644 weld-spi/target/weld-spi-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/weld-spi.jar

# POM
install -pm 644 parent/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-parent.pom
install -pm 644 bom/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-bom.pom
install -pm 644 weld/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-weld-api.pom
install -pm 644 weld-spi/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-weld-spi.pom

# DEPMAP
%add_maven_depmap JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-bom.pom
%add_maven_depmap JPP.%{name}-weld-api.pom %{name}/weld-api.jar
%add_maven_depmap JPP.%{name}-weld-spi.pom %{name}/weld-spi.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4jpp7
- new version


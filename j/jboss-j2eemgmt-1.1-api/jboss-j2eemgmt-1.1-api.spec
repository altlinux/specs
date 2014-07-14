BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-j2eemgmt-1.1-api
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:          jboss-j2eemgmt-1.1-api
Version:       1.0.1
Release:       alt2_3jpp7
Summary:       Java EE Management 1.1 API
Group:         Development/Java
License:       LGPLv2+
URL:           http://www.jboss.org/
# git clone git://github.com/jboss/jboss-j2eemgmt-api_spec.git jboss-j2eemgmt-1.1-api
# cd jboss-j2eemgmt-1.1-api/ && git archive --format=tar --prefix=jboss-j2eemgmt-1.1-api/ jboss-j2eemgmt-api_1.1_spec-1.0.1.Final | xz > jboss-j2eemgmt-1.1-api-1.0.1.Final.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

BuildRequires: jboss-specs-parent
BuildRequires: jpackage-utils

BuildRequires: jboss-ejb-3.1-api

BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin

Requires:      jboss-ejb-3.1-api

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
JSR-77: Java (TM) EE Management 1.1 API.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}

%build

mvn-rpmbuild install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/jboss-j2eemgmt-api_1.1_spec-%{namedversion}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp7
- new version


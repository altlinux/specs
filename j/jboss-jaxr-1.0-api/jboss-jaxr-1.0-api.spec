Epoch: 1
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jaxr-1.0-api
%define version 1.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:          jboss-jaxr-1.0-api
Version:       1.0.2
Release:       alt2_2jpp7
Summary:       Java(TM) API for XML Registries 1.0 (JAXR)
Group:         Development/Java
License:       CDDL or GPLv2 with exceptions
URL:           http://www.jboss.org/
# git clone git://github.com/jboss/jboss-jaxr-api_spec.git jboss-jaxr-1.0-api
# cd jboss-jaxr-1.0-api/ && git archive --format=tar --prefix=jboss-jaxr-1.0-api/ jboss-jaxr-api_1.0_spec-1.0.2.Final  | xz > jboss-jaxr-1.0-api-1.0.2.Final.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

# remove javax.activation
Patch0:        %{name}-%{namedversion}-pom.patch

BuildRequires: jboss-specs-parent
BuildRequires: jpackage-utils

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

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
JSR 93: Java(TM) API for XML Registries 1.0 (JAXR).

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}
%patch0 -p0

%build

mvn-rpmbuild install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/jboss-jaxr-api_1.0_spec-%{namedversion}.jar \
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
%doc LICENSE README

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_2jpp7
- new version

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt4_2jpp6
- fixed build

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt3_2jpp6
- build w/o jms-1.1-api

* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt2_2jpp6
- built with patched assembly plugin

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt1_2jpp6
- new version


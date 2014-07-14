BuildRequires: /proc
BuildRequires: jpackage-compat
%global site_name org.apache.felix.configadmin
%global grp_name  felix

Name:             felix-configadmin
Version:          1.4.0
Release:          alt2_3jpp7
Summary:          Felix Configuration Admin Service
License:          ASL 2.0
Group:            Development/Java
URL:              http://felix.apache.org/site/apache-felix-config-admin.html

Source0:          http://www.fightrice.com/mirrors/apache/felix/%{site_name}-%{version}-source-release.tar.gz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    felix-osgi-compendium >= 1.4.0-10
BuildRequires:    felix-osgi-core
BuildRequires:    aqute-bndlib

Requires:         jpackage-utils
Requires:         felix-osgi-compendium >= 1.4.0-10
Requires:         felix-osgi-core
Requires:         aqute-bndlib
Source44: import.info

%description
Implementation of the OSGi Configuration Admin Service Specification 1.4.

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{site_name}-%{version}

%build
# Pax test dependency unavailable
mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 -Dmaven.test.skip=true package javadoc:aggregate

%install
# jar
install -Dpm 644 target/%{site_name}-%{version}.jar %{buildroot}%{_javadir}/%{grp_name}/%{name}.jar

# pom
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{grp_name}-%{name}.pom

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%add_maven_depmap JPP.%{grp_name}-%{name}.pom %{grp_name}/%{name}.jar

%files
%doc LICENSE NOTICE DEPENDENCIES
%{_javadir}/%{grp_name}/%{name}.jar
%{_mavenpomdir}/JPP.%{grp_name}-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_3jpp7
- new release


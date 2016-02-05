Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global bundle org.apache.felix.framework

Name:           felix-framework
Version:        5.0.0
Release:        alt1_1jpp8
Summary:        Apache Felix Framework
License:        ASL 2.0
URL:            http://felix.apache.org
Source0:        http://www.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

Patch0:         test-ambiguity.patch

BuildArch:      noarch

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:felix-parent:pom:)
BuildRequires: mvn(org.osgi:org.osgi.annotation)
BuildRequires: mvn(org.osgi:org.osgi.compendium)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.apache.felix:org.apache.felix.resolver) >= 1.2.0
Source44: import.info

%description
Apache Felix Framework Interfaces and Classes.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}
%patch0

# This test needs porting to easymock3
rm src/test/java/org/apache/felix/framework/ServiceRegistryTest.java

%mvn_file :%{bundle} "felix/%{bundle}"

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_1jpp8
- java 8 mass update

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1_1jpp7
- new version

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt1_4jpp7
- new version

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt1_3jpp7
- new release

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_3jpp6
- new jpp release


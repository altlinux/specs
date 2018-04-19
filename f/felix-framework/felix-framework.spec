Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global bundle org.apache.felix.framework

Name:           felix-framework
Version:        5.6.0
Release:        alt1_4jpp8
Summary:        Apache Felix Framework
License:        ASL 2.0
URL:            http://felix.apache.org
BuildArch:      noarch

Source0:        http://www.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.resolver) >= 1.8.0
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.osgi:org.osgi.annotation)
BuildRequires:  mvn(org.ow2.asm:asm-all)
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

%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-source-plugin

# This test needs porting to easymock3
rm src/test/java/org/apache/felix/framework/ServiceRegistryTest.java

# This test fails when run on arm builders
rm src/test/java/org/apache/felix/framework/ConcurrencyTest.java

# This test is unstable on Koji
sed -i "/testgetOsNameWithAliases/s//ignore_&/" $(find -name NativeLibraryClauseTest.java)

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE
%doc DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt1_2jpp8
- new jpp release

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 5.4.0-alt1_3jpp8
- new version

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


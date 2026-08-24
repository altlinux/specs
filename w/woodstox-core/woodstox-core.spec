Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global base_name woodstox

Name:           woodstox-core
Summary:        High-performance XML processor
Version:        7.1.1
Release:        alt1
License:        Apache-2.0

Url:            https://github.com/FasterXML/woodstox
Vcs:            https://github.com/FasterXML/woodstox

Source0:        %{url}/archive/%{name}-%{version}.tar.gz

# Port to latest OSGi APIs
Patch0:         0001-Allow-building-against-OSGi-APIs-newer-than-R4.patch
# Drop requirements on defunct optional dependencies: msv and relaxng
Patch1:         0002-Patch-out-optional-support-for-msv-and-relax-schema-.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml:oss-parent:pom:)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.codehaus.woodstox:stax2-api)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.moditect:moditect-maven-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
Source44: import.info

%description
Woodstox is a high-performance validating namespace-aware StAX-compliant
(JSR-173) Open Source XML-processor written in Java.
XML processor means that it handles both input (== parsing)
and output (== writing, serialization)), as well as supporting tasks
such as validation.

%prep
%setup -q -n %{base_name}-%{name}-%{version}
%patch0 -p1
%patch1 -p1

# Patch out optional support for msv and relax schema validation
%pom_remove_dep :relaxngDatatype
%pom_remove_dep net.java.dev.msv:
%pom_remove_dep :isorelax
rm -rf src/main/java/com/ctc/wstx/msv

# Remove tests for msv and relaxng functionality
rm -rf src/main/java/com/ctc/wstx/msv
rm src/test/java/failing/{RelaxNGTest,TestRelaxNG189,TestRelaxNG190,TestW3CSchema189,W3CDefaultValuesTest,W3CSchemaTypesTest}.java
rm src/test/java/stax2/vwstream/{W3CSchemaWrite16Test,W3CSchemaWrite23Test}.java
rm src/test/java/wstxtest/msv/{TestW3CSchema,TestW3CSchemaTypes,TestWsdlValidation}.java
rm src/test/java/wstxtest/vstream/{TestRelaxNG,TestW3CSchemaComplexTypes}.java

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Mon Aug 24 2026 Anton Meleshnikov <alton@altlinux.org> 7.1.1-alt1
- new version (thanks fedora for the spec)
- remove javadoc

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 6.2.3-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 6.2.1-alt1_5jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 6.0.2-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt1_1jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1_6jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.2-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1_2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_3jpp7
- new version


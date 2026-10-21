Name:          jackson-module-jsonSchema
Version:       2.22.1
Release:       alt1

Summary:       Jackson JSON Schema Module
License:       Apache-2.0
Group:         Development/Java
URL:           https://github.com/FasterXML/jackson-module-jsonSchema
VCS:           https://github.com/FasterXML/jackson-module-jsonSchema

Source0:       %name-%version.tar

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:)
BuildRequires:  mvn(org.moditect:moditect-maven-plugin)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(jakarta.validation:jakarta.validation-api)

BuildArch:      noarch

%description
This module supports the creation of a JSON Schema (v3).

%javadoc_package

%prep
%setup

# Build jakarta variant
%pom_disable_module javax

%pom_remove_plugin :gradle-module-metadata-maven-plugin jakarta
%pom_remove_plugin :cyclonedx-maven-plugin jakarta

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE *.md

%changelog
* Wed Oct 21 2026 Evgeniy Serov <scala@altlinux.org> 2.22.1-alt1
- Updated to 2.22.1.
- Returned to Sisyphus.

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.8-alt1_1jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_3jpp8
- fc29 update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_2jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_2jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_2jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- java 8 mass update

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies


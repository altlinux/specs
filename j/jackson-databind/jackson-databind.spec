%define _unpackaged_files_terminate_build 1

Name: jackson-databind
Version: 2.20.1
Release: alt3

Summary: General data-binding package for Jackson (2.x)
License: Apache-2.0
Group: Development/Java
Url: https://github.com/FasterXML/jackson-databind
Vcs: https://github.com/FasterXML/jackson-databind.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: jackson-annotations
BuildRequires: jackson-core
BuildRequires: jackson-bom
BuildRequires: replacer
BuildRequires: maven-plugin-bundle
BuildRequires: moditect-maven-plugin

%description
The general-purpose data-binding functionality and tree-model for Jackson Data
Processor. It builds on core streaming parser/generator package, and uses
Jackson Annotations for configuration.

%prep
%setup

# Remove plugins unnecessary for RPM builds
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin :gradle-module-metadata-maven-plugin
%pom_remove_plugin :cyclonedx-maven-plugin

cp -p src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

# unavailable test deps
%pom_remove_dep javax.measure:jsr-275
rm src/test/java/com/fasterxml/jackson/databind/introspect/NoClassDefFoundWorkaroundTest.java
%pom_xpath_remove pom:classpathDependencyExcludes

# Off test that require connection with the web
rm src/test/java/com/fasterxml/jackson/databind/ser/jdk/JDKTypeSerializationTest.java

%mvn_file : %name

%build
%mvn_build -f -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc --no-dereference LICENSE NOTICE

%changelog
* Thu Apr 02 2026 Anton Meleshnikov <alton@altlinux.org> 2.20.1-alt3
- FTBFS fix.

* Mon Nov 10 2025 Ivan Khanas <xeno@altlinux.org> 2.20.1-alt2
- Add JPMS support.

* Fri Nov 08 2025 Ivan Khanas <xeno@altlinux.org> 2.20.1-alt1
- New version.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 2.11.4-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.11.4-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.11.2-alt1_2jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 2.10.2-alt1_2jpp8
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 2.9.9.3-alt1_1jpp8
- new version

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.8-alt1_1jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_4jpp8
- fc29 update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_3jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_5jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_2jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies


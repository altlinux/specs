%define _unpackaged_files_terminate_build 1

Name: icu4j
Version: 79.1
Release: alt1
Epoch: 1

Summary: International Components for Unicode for Java
License: Unicode-3.0
Group: Development/Java
URL: https://icu.unicode.org/
VCS: https://github.com/unicode-org/icu.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(pl.pragmatists:JUnitParams)
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-shade-plugin
BuildRequires: maven-plugin-build-helper

%description
ICU4J provides Unicode and internationalization services for Java,
including character properties, normalization, collation, transliteration,
locale data, calendars and number and date formatting.

%package charset
Summary: Charset converters for ICU4J
Group: Development/Java

%description charset
Additional charset converters for ICU4J.

%package parent
Summary: Maven parent metadata for ICU4J
Group: Development/Java

%description parent
Parent POMs for the ICU4J Java modules.

%package taglets
Summary: Javadoc taglets for ICU4J
Group: Development/Java

%description taglets
Javadoc extensions used to generate ICU4J API documentation.

%package javadoc
Summary: API documentation for ICU4J
License: Unicode-3.0 AND MIT
Group: Development/Java

%description javadoc
Generated Java API documentation for ICU4J.

%prep
%setup

# Publication and cleanup plugins are unnecessary for an offline RPM build.
%pom_remove_plugin -r :flatten-maven-plugin
%pom_remove_plugin -r :maven-clean-plugin
%pom_remove_plugin -r :maven-deploy-plugin

# Keep every runtime module and its ordinary tests.
# These modules are examples, benchmarks and development/reporting tools.
%pom_disable_module demos icu4j
%pom_disable_module samples icu4j
%pom_disable_module perf-tests icu4j
%pom_disable_module build icu4j/tools
%pom_disable_module errorprone_report icu4j/tools
%pom_disable_module misc icu4j/tools
%pom_disable_module pmd icu4j/tools

# Doclet extensions are build inputs, not an ICU runtime dependency.
%pom_xpath_inject \
  "pom:dependencies/pom:dependency[pom:artifactId='tools_taglets']" \
  "<scope>provided</scope>" icu4j/main/core

%mvn_package :icu-root parent
%mvn_package :icu4j-root parent
%mvn_package :icu4j-main parent
%mvn_package :icu4j-tools parent
%mvn_package :icu4j-charset charset
%mvn_package :tools_taglets taglets
%mvn_package :framework __noinstall
%mvn_package :common_tests __noinstall
%mvn_package :icu4j %name
%mvn_package :core %name
%mvn_package :collate %name
%mvn_package :currdata %name
%mvn_package :langdata %name
%mvn_package :regiondata %name
%mvn_package :translit %name

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-icu4j
%doc LICENSE

%files charset -f .mfiles-charset

%files parent -f .mfiles-parent

%files taglets -f .mfiles-taglets

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 1:79.1-alt1
- New version.


* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1:71.1-alt1_3jpp11
- new version

* Sat Jul 02 2022 Igor Vlasenko <viy@altlinux.org> 1:70.1-alt1_3jpp11
- new version

* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 1:69.1-alt1_1jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:68.2-alt1_1jpp11
- new version

* Sun Oct 11 2020 Igor Vlasenko <viy@altlinux.ru> 1:65.1-alt1_5jpp8
- new version

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1:63.1-alt1_2jpp8
- new version

* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 1:59.1-alt3_3jpp8
- fixed build

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:59.1-alt2_3jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:59.1-alt2_2jpp8
- fixed build

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 1:59.1-alt1_2jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:59.1-alt1_1jpp8
- new version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:54.1.1-alt1_8jpp8
- new fc release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1:54.1.1-alt1_7jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1:54.1.1-alt1_6jpp8
- java 8 mass update

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.4.2.2-alt2_12jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.4.2.2-alt1_12jpp7
- new version

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.4.2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies


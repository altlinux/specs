Name:           snakeyaml
Version:        2.5
Release:        alt2

Summary:        YAML parser and emitter for Java
License:        Apache-2.0
Group:          Development/Java
URL:            https://bitbucket.org/snakeyaml/snakeyaml
VCS:            https://bitbucket.org/snakeyaml/snakeyaml

Source:         %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.openjdk.jmh:jmh-core)
BuildRequires:  mvn(org.openjdk.jmh:jmh-generator-annprocess)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)

BuildArch:      noarch

%description
SnakeYAML features:
    * a complete YAML 1.1 parser. In particular,
      SnakeYAML can parse all examples from the specification.
    * Unicode support including UTF-8/UTF-16 input/output.
    * high-level API for serializing and deserializing
      native Java objects.
    * support for all types from the YAML types repository.
    * relatively sensible error messages.
    * when you plan to feed the parser with untrusted data please study the
      settings which allow to restrict incoming data.

%javadoc_package

%prep
%setup

%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :formatter-maven-plugin
%pom_remove_plugin :maven-source-plugin

%pom_remove_dep :velocity-engine-core
%pom_remove_dep :joda-time
%pom_remove_dep :lombok
%pom_remove_dep :jackson-dataformat-yaml

rm -rf src/test/java/examples/jodatime
rm src/test/java/org/yaml/snakeyaml/reader/ReaderBomTest.java

# Tests using dependencies we don't have/have removed
rm src/test/java/org/yaml/snakeyaml/emitter/template/VelocityTest.java
rm src/test/java/org/yaml/snakeyaml/issues/issue387/YamlExecuteProcessContextTest.java
rm src/test/java/org/yaml/snakeyaml/env/ApplicationProperties.java
rm src/test/java/org/yaml/snakeyaml/env/EnvLombokTest.java
rm src/test/java/org/yaml/snakeyaml/issues/issue527/Fuzzy47047Test.java
rm src/test/java/org/yaml/snakeyaml/issues/issue530/Fuzzy47039Test.java
rm src/test/java/org/yaml/snakeyaml/issues/issue543/Fuzzer50355Test.java
rm src/test/java/org/yaml/snakeyaml/issues/issue525/FuzzyStackOverflowTest.java
rm src/test/java/org/yaml/snakeyaml/issues/issue526/Fuzzy47027Test.java
rm src/test/java/org/yaml/snakeyaml/issues/issue1100/JacksonTest.java

# Problematic test resources for maven-resources-plugin 3.2
rm src/test/resources/issues/issue99.jpeg
rm src/test/resources/reader/unicode-16be.txt
rm src/test/resources/reader/unicode-16le.txt
rm src/test/resources/pyyaml/spec-05-01-utf16be.data
rm src/test/resources/pyyaml/spec-05-01-utf16le.data
rm src/test/resources/pyyaml/spec-05-02-utf16le.data
rm src/test/resources/pyyaml/odd-utf16.stream-error
rm src/test/resources/pyyaml/invalid-character.loader-error
rm src/test/resources/pyyaml/invalid-character.stream-error
rm src/test/resources/pyyaml/invalid-utf8-byte.loader-error
rm src/test/resources/pyyaml/invalid-utf8-byte.stream-error
rm src/test/resources/pyyaml/empty-document-bug.data
rm src/test/resources/pyyaml/spec-05-02-utf16be.data
rm -rf src/test/resources/fuzzer/

# Test using the jpeg data removed above
rm src/test/java/org/yaml/snakeyaml/issues/issue99/YamlBase64Test.java

# This tests uses jackson-dataformats-text. jackson-dataformats-text has been updated
# from version 2.9.8 to 2.20.1 in Sisyphus. jackson-dataformats-text-2.9.8
# has been removed from older repositories due to incompatibility with newer
# versions of jackson, and the new jackson-dataformats-text cannot be built
# without updating snakeyaml, which cannot be updated without updating
# jackson-dataformats-text. This causes problems during backporting.
rm -f src/test/java/org/yaml/snakeyaml/issues/issue1100/JacksonTest.java
rm -f src/test/java/org/yaml/snakeyaml/issues/issue1100/YamlRoot.java


%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Mon May 11 2026 Arseniy Kostevich <faux@altlinux.org> 2.5-alt2
- Build without jackson-dataformats-text.

* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.5-alt1.1
- Cosmetic fixes.

* Sat Dec 27 2025 Evgeniy Serov <scala@altlinux.org> 2.5-alt1
- updated to 2.5
- removed import.info

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.27-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.27-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.26-alt1_4jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.25-alt1_4jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1_1jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_7jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_4jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_3jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_9jpp8
- unbootsrap build

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.13-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_7jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_4jpp7
- new version

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt3_3jpp7
- fixed build

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.9-alt2_3jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_3jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_2jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_1jpp7
- new version


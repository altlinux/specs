%define _unpackaged_files_terminate_build 1

Name: safere
Version: 1.1.0
Release: alt1

Summary: Linear-time regular expression matching library for Java
License: BSD-3-Clause AND Unicode-3.0
Group: Development/Java
URL: https://github.com/eaftan/safere
VCS: https://github.com/eaftan/safere.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-antrun-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: junit5
BuildRequires: assertj-core
BuildRequires: mvn(com.ibm.icu:icu4j)

%description
SafeRE provides linear-time regular expression matching, Java-compatible
pattern and matcher APIs, Unicode support and direct UTF-8 matching.

%package parent
Summary: Maven parent POM for SafeRE
Group: Development/Java

%description parent
Shared Maven project metadata for SafeRE and its Unicode generator.

%package unicode-generator
Summary: Unicode table generator for SafeRE
Group: Development/Java

%description unicode-generator
Tool for generating the Unicode property tables used by SafeRE.

%prep
%setup

# Upstream release.yml sets all POM versions from the stable Git tag.
%pom_xpath_set pom:version %version
%pom_xpath_set pom:parent/pom:version %version safere safere-unicode

# Development-only crosschecks, fuzzing, FFM bindings and benchmarks.
%pom_disable_module safere-crosscheck
%pom_disable_module safere-fuzz
%pom_disable_module safere-exhaustive
%pom_disable_module safere-ffm-re2
%pom_disable_module safere-benchmarks

# Static analysis would introduce a bootstrap cycle with Error Prone.
%pom_remove_plugin com.diffplug.spotless:spotless-maven-plugin
%pom_remove_plugin com.diffplug.spotless:spotless-maven-plugin safere
%pom_remove_plugin :maven-pmd-plugin safere
%pom_remove_plugin :jacoco-maven-plugin safere
%pom_remove_plugin :maven-javadoc-plugin safere
%pom_xpath_remove //pom:annotationProcessorPaths
%pom_xpath_remove //pom:annotationProcessorPaths safere
%pom_xpath_remove //pom:compilerArgs
%pom_xpath_remove //pom:compilerArgs safere
%pom_xpath_inject \
  '//pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration' \
  "<compilerArgs>\
    <arg>--add-modules</arg><arg>jdk.incubator.vector</arg>\
    <arg>--add-reads</arg><arg>org.safere=jdk.incubator.vector</arg>\
  </compilerArgs>" \
  safere

# Test APIs are compatible with the system JUnit Jupiter provider.
%pom_xpath_set pom:properties/pom:junit.version 5.14.4

%mvn_package :safere-parent parent
%mvn_package :safere-unicode-generator unicode-generator

%build
# Keep test compilation, skipping exhaustive execution only on 32-bit x86.
safere_test_flags=
if [ "$(getconf LONG_BIT)" = 32 ]; then
  case "$(uname -m)" in
    i?86|x86_64) safere_test_flags=-DskipTests ;;
  esac
fi
%mvn_build -s -j -- \
  -Dtest.parallelism=2 $safere_test_flags

%install
%mvn_install

%files -f .mfiles-safere
%doc LICENSE safere/src/main/resources/META-INF/LICENSE-Unicode.txt

%files parent -f .mfiles-parent

%files unicode-generator -f .mfiles-unicode-generator

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 1.1.0-alt1
- Initial build for ALT.

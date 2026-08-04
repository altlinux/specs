%global _unpackaged_files_terminate_build 1

Name: jqf
Version: 2.0
Release: alt1
Summary: Coverage-guided semantic fuzzing for Java
License: BSD-2-Clause
Group: Development/Java
Url: https://github.com/rohanpadhye/JQF
Vcs: https://github.com/rohanpadhye/JQF

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: maven-dependency-plugin
BuildRequires: maven-assembly-plugin
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.pholser:junit-quickcheck-core)
BuildRequires: mvn(com.pholser:junit-quickcheck-generators)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.jacoco:org.jacoco.report)
BuildRequires: mvn(org.hamcrest:hamcrest-library)
BuildRequires: mvn(info.picocli:picocli)
BuildRequires: mvn(org.eclipse.collections:eclipse-collections)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)

%description
JQF is a feedback-directed fuzz testing platform for Java.
JQF uses the abstraction of property-based testing, which makes it
easy to write fuzz drivers as parametric JUnit test methods.
JQF enables running junit-quickcheck style parameterized unit tests
with the power of coverage-guided fuzzing algorithms such as Zest.

%package -n jqf-fuzz
Summary: JQF fuzzing engine
Group: Development/Java
Requires: mvn(com.pholser:junit-quickcheck-core)
Requires: mvn(com.pholser:junit-quickcheck-generators)
Requires: mvn(junit:junit)
Requires: mvn(info.picocli:picocli)
Requires: mvn(org.eclipse.collections:eclipse-collections)
Requires: mvn(org.jacoco:org.jacoco.report)

%description -n jqf-fuzz
JQF fuzzing engine module.

%package -n jqf-instrument
Summary: JQF bytecode instrumentation module
Group: Development/Java
Requires: mvn(org.ow2.asm:asm)

%description -n jqf-instrument
JQF bytecode instrumentation module based on janala2.

%package -n jqf-maven-plugin
Summary: JQF Maven plugin
Group: Development/Java
Requires: jqf-fuzz = %EVR
Requires: mvn(org.apache.maven:maven-core)

%description -n jqf-maven-plugin
Maven plugin for running JQF fuzz tests.

%package javadoc
Summary: API documentation for JQF
Group: Development/Java

%description javadoc
API documentation for the JQF library.

%prep
%setup

# Disable examples module
%pom_disable_module examples

# Set Java 17 compiler settings
%pom_xpath_inject "pom:properties" \
    "<maven.compiler.source>17</maven.compiler.source>\
<maven.compiler.target>17</maven.compiler.target>\
<maven.compiler.release>17</maven.compiler.release>"

# Set version of plugins
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-dependency-plugin']" "<version>3.1.2</version>" instrument
%pom_xpath_set "pom:plugin[pom:artifactId='maven-assembly-plugin']/pom:version" 3.3.0 fuzz

# Remove unnecessary plugins
for plugin in maven-release-plugin maven-gpg-plugin jacoco-maven-plugin \
              maven-checkstyle-plugin nexus-staging-maven-plugin; do
    %pom_remove_plugin :$plugin || :
done

# Fix eclipse-collections version to what we have in Sisyphus
%pom_change_dep -r org.eclipse.collections:eclipse-collections:10.4.0 \
    org.eclipse.collections:eclipse-collections:13.0.0

# Add explicit versions for dependencies managed by parent BOM
%pom_change_dep -r junit:junit: junit:junit:4.13.2 fuzz
%pom_change_dep -r org.ow2.asm:asm: org.ow2.asm:asm:9.8 instrument
%pom_change_dep -r org.jacoco:org.jacoco.report: org.jacoco:org.jacoco.report:0.8.14 fuzz
%pom_change_dep -r org.hamcrest:hamcrest-library: org.hamcrest:hamcrest-library:1.3 fuzz

%mvn_package ":jqf-fuzz" jqf-fuzz
%mvn_package ":jqf-instrument" jqf-instrument
%mvn_package ":jqf-maven-plugin" jqf-maven-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files -n jqf-fuzz -f .mfiles-jqf-fuzz

%files -n jqf-instrument -f .mfiles-jqf-instrument

%files -n jqf-maven-plugin -f .mfiles-jqf-maven-plugin

%files javadoc -f .mfiles-javadoc

%changelog
* Thu May 29 2026 Timofei Fedotov <sovtouch@altlinux.org> 2.0-alt1
- Initial built for ALT Sisyphus.

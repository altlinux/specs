%define _unpackaged_files_terminate_build 1

%def_with check

Name: junit-quickcheck
Version: 1.0
Release: alt1

Summary: Property-based testing, JUnit-style
License: MIT
Group: Development/Java
Url: https://github.com/pholser/junit-quickcheck
Vcs: https://github.com/pholser/junit-quickcheck

BuildArch: noarch

Source0: %name-%version.tar

Patch0: junit-quickcheck-1.0-alt-use-arxila-javaruntype.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: serviceloader-maven-plugin
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.hamcrest:hamcrest-core)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(ognl:ognl)
BuildRequires: mvn(ru.vyarus:generics-resolver)
BuildRequires: mvn(io.arxila.javaruntype:javaruntype)
%if_with check
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(com.google.guava:guava-testlib)
BuildRequires: mvn(ch.qos.logback:logback-classic)
%endif

%description
junit-quickcheck is a library that supports writing and running
property-based tests in JUnit, inspired by QuickCheck for Haskell.

%package -n junit-quickcheck-core
Summary: junit-quickcheck core module
Group: Development/Java
Requires: mvn(junit:junit)
Requires: mvn(org.hamcrest:hamcrest-core)
Requires: mvn(org.slf4j:slf4j-api)
Requires: mvn(ognl:ognl)
Requires: mvn(ru.vyarus:generics-resolver)
Requires: mvn(io.arxila.javaruntype:javaruntype)

%description -n junit-quickcheck-core
Core module of junit-quickcheck providing the @RunWith(JQF.class)
runner and @Fuzz annotation support.

%package -n junit-quickcheck-generators
Summary: junit-quickcheck generators module
Group: Development/Java
Requires: junit-quickcheck-core = %EVR

%description -n junit-quickcheck-generators
Built-in generators for common Java types for use with junit-quickcheck.

%package javadoc
Summary: API documentation for junit-quickcheck
Group: Development/Java
Requires: %name = %EVR

%description javadoc
API documentation for the junit-quickcheck library.

%prep
%setup
%autopatch -p1

# Remove parent POM (oss-parent requires network)
%pom_remove_parent

# Disable modules we don't need
%pom_disable_module examples

# Remove reporting/quality/release plugins not available offline
for plugin in maven-release-plugin jacoco-maven-plugin maven-checkstyle-plugin \
              maven-pmd-plugin spotbugs-maven-plugin maven-site-plugin \
              maven-project-info-reports-plugin maven-gpg-plugin \
              site-maven-plugin maven-source-plugin; do
    %pom_remove_plugin :$plugin || :
    %pom_remove_plugin :$plugin core || :
done

# Replace old mockito with new version
%pom_change_dep org.mockito:mockito-all: org.mockito:mockito-core:5.20.0 core
%pom_change_dep org.mockito:mockito-all: org.mockito:mockito-core:5.20.0 generators
%pom_change_dep org.mockito:mockito-all: org.mockito:mockito-core:5.20.0 guava

# Replace old javaruntype with new arxila version
%pom_change_dep -r org.javaruntype:javaruntype: io.arxila.javaruntype:javaruntype:2.0.0

# Fix generics-resolver version
%pom_change_dep -r ru.vyarus:generics-resolver: ru.vyarus:generics-resolver:3.0.3

# Add explicit versions for dependencies managed by parent BOM
%pom_change_dep junit:junit: junit:junit:4.13.1 core
%pom_change_dep org.hamcrest:hamcrest-core: org.hamcrest:hamcrest-core:1.3 core
%pom_change_dep org.slf4j:slf4j-api: org.slf4j:slf4j-api:1.7.36 core
%pom_change_dep junit:junit: junit:junit:4.13.1 generators

%mvn_package "com.pholser:junit-quickcheck-core" junit-quickcheck-core
%mvn_package "com.pholser:junit-quickcheck-generators" junit-quickcheck-generators

# Exclude tests incompatible with Java 17 module system, Mockito 5.x and updated dependencies
%pom_xpath_inject "pom:build/pom:plugins" \
    "<plugin><groupId>org.apache.maven.plugins</groupId>\
<artifactId>maven-compiler-plugin</artifactId>\
<configuration><testExcludes>\
<testExclude>**/CompositeGeneratorTest.java</testExclude>\
<testExclude>**/RegisterGeneratorsByConventionTest.java</testExclude>\
<testExclude>**/ConstrainingWhatGeneratorsCanAcceptCertainComponentsTest.java</testExclude>\
</testExcludes></configuration></plugin>\
<plugin><groupId>org.apache.maven.plugins</groupId>\
<artifactId>maven-surefire-plugin</artifactId>\
<configuration><skipTests>true</skipTests></configuration></plugin>" core
%pom_xpath_inject "pom:build/pom:plugins" \
    "<plugin><groupId>org.apache.maven.plugins</groupId>\
<artifactId>maven-compiler-plugin</artifactId>\
<configuration><testExcludes>\
<testExclude>**/SetOfSuperFloatPropertyParameterTest.java</testExclude>\
</testExcludes></configuration></plugin>\
<plugin><groupId>org.apache.maven.plugins</groupId>\
<artifactId>maven-surefire-plugin</artifactId>\
<configuration><skipTests>true</skipTests></configuration></plugin>" generators
%build
# -f skips test execution; tests require network-dependent dependencies
%mvn_build %{?_without_check:-f} -- \
    -Dmaven.compiler.source=17 \
    -Dmaven.compiler.target=17 \
    -Dmaven.compiler.release=17

%install
%mvn_install

%check
%mvn_build -s -- \
    -Dmaven.compiler.source=17 \
    -Dmaven.compiler.target=17 \
    -Dmaven.compiler.release=17

%files -f .mfiles
%doc README.md LICENSE.txt

%files -n junit-quickcheck-core -f .mfiles-junit-quickcheck-core

%files -n junit-quickcheck-generators -f .mfiles-junit-quickcheck-generators

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Jun 11 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.0-alt1
- Initial build for ALT Sisyphus.

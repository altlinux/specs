%define _unpackaged_files_terminate_build 1

Name: snakeyaml-engine
Version: 3.2
Release: alt1
Summary: YAML 1.2 parser and emitter for Java
License: Apache-2.0
Group: Development/Java
URL: https://codeberg.org/snakeyaml/snakeyaml-engine
VCS: https://codeberg.org/snakeyaml/snakeyaml-engine.git
Source0: %name-%version.tar
Source1: THIRD-PARTY-NOTICES.txt
Patch0: snakeyaml-engine-performance.patch
BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.openjdk.jmh:jmh-core)
BuildRequires: mvn(org.openjdk.jmh:jmh-generator-annprocess)

%description
SnakeYAML Engine is a YAML 1.2 processor for Java. It provides a parser
and emitter for Unicode YAML documents, with configurable loading and
serialization settings. This package preserves the OSGi bundle and the
Java 11 module descriptor of the upstream multi-release JAR.

%javadoc_package

%prep
%setup
%patch0 -p1
cp -p %SOURCE1 THIRD-PARTY-NOTICES.txt

# Distribution builds do not publish to Sonatype or reformat upstream sources.
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
# Benchmark execution is separate from the unit-test suite.
%pom_remove_plugin pw.krejci:jmh-maven-plugin
%pom_remove_plugin com.mycila:license-maven-plugin
%pom_remove_plugin net.revelc.code.formatter:formatter-maven-plugin
# XMvn generates API documentation without Maven site/link resolution.
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
# The site descriptor attachment is for upstream website deployment.
%pom_remove_plugin :maven-site-plugin

# Preserve binary and intentionally malformed YAML fixtures byte for byte.
%pom_xpath_set "pom:build/pom:testResources/pom:testResource/pom:filtering" false

%mvn_file : snakeyaml-engine

%build
# Keep hardware-timed performance measurements outside the unit-test suite.
%mvn_build -s -- -DexcludedGroups=performance

%install
%mvn_install

%files -f .mfiles-snakeyaml-engine
%doc LICENSE.txt THIRD-PARTY-NOTICES.txt

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 3.2-alt1
- Initial build for ALT.

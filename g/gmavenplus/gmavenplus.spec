%define _unpackaged_files_terminate_build 1

Name: gmavenplus
Version: 5.1.0
Release: alt1

Summary: Maven plugin for compiling and running Groovy
License: Apache-2.0
Group: Development/Java
URL: https://groovy.github.io/GMavenPlus/
VCS: https://github.com/groovy/GMavenPlus.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven:maven-archiver)
BuildRequires: mvn(org.apache.maven.shared:file-management)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires: mvn(org.apache.groovy:groovy)
BuildRequires: mvn(org.apache.groovy:groovy-ant)
BuildRequires: mvn(org.apache.groovy:groovy-groovydoc)
BuildRequires: mvn(org.apache.groovy:groovy-templates)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.junit:junit-bom:pom:)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
GMavenPlus integrates Groovy compilation, stub generation, documentation,
script execution and the interactive shell into Maven builds. The consuming
project supplies its Groovy version; the plugin uses reflective support for
multiple Groovy releases.

%javadoc_package

%prep
%setup
# Release automation and bytecode policy checks are outside the offline build.
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_xpath_remove pom:reporting
# The five forked-JVM projects require the unavailable toolchains plugin.
# advancedExecute uses Grape to download commons-lang3 from Maven Central.
%pom_xpath_inject \
    'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-invoker-plugin"]/pom:configuration' \
    '<pomExcludes><pomExclude>forked*/pom.xml</pomExclude><pomExclude>advancedExecute/pom.xml</pomExclude></pomExcludes>'
# Resolve genuine system artifacts through XMvn in the nested offline builds.
find src/it -name invoker.properties -exec \
    sh -c 'printf "\ninvoker.offline = true\n" >> "$1"' sh {} \;
%mvn_file :gmavenplus-plugin %name/gmavenplus-plugin

%build
%mvn_build -- -Dinvoker.mavenExecutable=%_bindir/xmvn

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Tue Nov 10 2026 Ivan Khanas <xeno@altlinux.org> 5.1.0-alt1
- Initial build for ALT.

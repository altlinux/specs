%define _unpackaged_files_terminate_build 1

Name: spdx-java-core
Version: 1.0.5
Release: alt1

Summary: Core libraries for SPDX Java models
License: Apache-2.0
Group: Development/Java
URL: https://github.com/spdx/spdx-java-core
VCS: https://github.com/spdx/spdx-java-core
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.jsoup:jsoup)

%description
Shared core utilities and model objects used by the SPDX Java libraries.

%prep
%setup -q
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.spdx:spdx-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
plugins='pom:project/pom:build/pom:plugins/pom:plugin'
%pom_xpath_set \
    "$plugins[pom:artifactId='maven-compiler-plugin']/pom:version" \
    3.14.0
%pom_xpath_set \
    "$plugins[pom:artifactId='maven-jar-plugin']/pom:version" \
    3.2.2
%pom_xpath_set \
    "$plugins[pom:artifactId='build-helper-maven-plugin']/pom:version" \
    3.6.2
%pom_add_plugin org.apache.maven.plugins:maven-resources-plugin:3.5.0
%pom_add_plugin org.apache.maven.plugins:maven-surefire-plugin:3.5.6
%pom_change_dep org.slf4j:slf4j-api:2.0.19 org.slf4j:slf4j-api:1.7.36
%pom_change_dep \
    org.apache.commons:commons-lang3:3.20.0 \
    org.apache.commons:commons-lang3:3.21.0
%pom_change_dep org.jsoup:jsoup:1.23.2 org.jsoup:jsoup:1.22.2

%build
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles-spdx-java-core
%doc README.md LICENSE

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 1.0.5-alt1
- Initial build for ALT.

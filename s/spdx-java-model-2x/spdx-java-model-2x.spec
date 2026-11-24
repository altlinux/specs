%define _unpackaged_files_terminate_build 1

Name: spdx-java-model-2x
Version: 1.0.5
Release: alt1

Summary: SPDX 2.X Java model
License: Apache-2.0
Group: Development/Java
URL: https://github.com/spdx/spdx-java-model-2_X
VCS: https://github.com/spdx/spdx-java-model-2_X
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
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: mvn(org.spdx:spdx-java-core)

%description
Java implementation of the SPDX 2.X data model and helper functions.

%prep
%setup -q
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.spdx:spdx-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
plugins='pom:project/pom:build/pom:plugins/pom:plugin'
%pom_xpath_set \
    "$plugins[pom:artifactId='maven-compiler-plugin']/pom:version" \
    3.14.0
%pom_xpath_set \
    "$plugins[pom:artifactId='maven-jar-plugin']/pom:version" \
    3.2.2
%pom_add_plugin org.apache.maven.plugins:maven-resources-plugin:3.5.0
%pom_add_plugin org.apache.maven.plugins:maven-surefire-plugin:3.5.6
%pom_change_dep org.slf4j:slf4j-simple:2.0.19 org.slf4j:slf4j-simple:1.7.36
%mvn_package org.spdx:spdx-java-model-2_X spdx-java-model-2x

%build
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles-spdx-java-model-2x
%doc README.md LICENSE

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 1.0.5-alt1
- Initial build for ALT.

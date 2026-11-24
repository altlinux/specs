%define _unpackaged_files_terminate_build 1

Name: spdx-java-library
Version: 2.0.5
Release: alt1

Summary: Java library implementing the SPDX model and utilities
License: Apache-2.0
Group: Development/Java
URL: https://github.com/spdx/Spdx-Java-Library
VCS: https://github.com/spdx/Spdx-Java-Library
Source0: %name-%version.tar
Patch0: remove-unused-concurrentunit-test-scaffolding.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.spdx:spdx-java-core)
BuildRequires: mvn(org.spdx:spdx-java-model-2_X)
BuildRequires: mvn(org.spdx:spdx-java-model-3_0)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.jsoup:jsoup)
BuildRequires: mvn(org.slf4j:slf4j-api)

%description
Java library implementing the SPDX data model and providing useful helpers.

%prep
%setup -q
%patch0 -p1
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin org.spdx:spdx-maven-plugin
%pom_remove_dep net.jodah:concurrentunit
plugins='pom:project/pom:build/pom:plugins/pom:plugin'
%pom_xpath_set \
    "$plugins[pom:artifactId='build-helper-maven-plugin']/pom:version" \
    3.6.2
%pom_add_plugin org.apache.maven.plugins:maven-surefire-plugin:3.5.6
# The web store tests connect to spdx.org.
web_store_test='**/SpdxListedLicenseWebStoreTest.java'
excludes="<excludes><exclude>$web_store_test</exclude></excludes>"
%pom_xpath_inject \
    "$plugins[pom:artifactId='maven-surefire-plugin']" \
    "<configuration>$excludes</configuration>"

%build
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles-java-spdx-library
%doc README.md LICENSE

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 2.0.5-alt1
- Initial build for ALT.

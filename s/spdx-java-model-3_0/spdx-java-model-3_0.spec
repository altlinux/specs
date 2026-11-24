%define _unpackaged_files_terminate_build 1

Name: spdx-java-model-3_0
Version: 1.0.5
Release: alt1

Summary: SPDX 3.0 Java model
License: Apache-2.0
Group: Development/Java
URL: https://github.com/spdx/spdx-java-model-3_0
VCS: https://github.com/spdx/spdx-java-model-3_0
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.spdx:spdx-java-core)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(junit:junit)

%description
Generated Java sources for the SPDX 3.0 model.

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
    "$plugins[pom:artifactId='build-helper-maven-plugin']/pom:version" \
    3.6.2
%pom_xpath_set \
    "$plugins[pom:artifactId='maven-jar-plugin']/pom:version" \
    3.2.2
%pom_add_plugin org.apache.maven.plugins:maven-resources-plugin:3.5.0
%pom_add_plugin org.apache.maven.plugins:maven-surefire-plugin:3.5.6
%pom_change_dep org.slf4j:slf4j-api:2.0.17 org.slf4j:slf4j-api:1.7.36
# All model tests share a helper that needs Generex.
%pom_remove_dep com.github.mifmif:generex
test_pattern='org/spdx/library/model/v3_0_1/**/*.java'
%pom_xpath_inject \
    "$plugins[pom:artifactId='maven-compiler-plugin']/pom:configuration" \
    "<testExcludes><testExclude>$test_pattern</testExclude></testExcludes>"

%build
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles-spdx-java-model-3_0
%doc README.md LICENSE

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 1.0.5-alt1
- Initial build for ALT.

%define _unpackaged_files_terminate_build 1

Name: jetty-toolchain
Version: 1.7
Release: alt1

Summary: Jetty Toolchain parent Maven POM
License: Apache-2.0 or EPL-1.0
Group: Development/Java
Url: https://jetty.org
Vcs: https://github.com/eclipse/jetty.toolchain
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-17-compat
BuildRequires: HdrHistogram
BuildRequires: javaparser
BuildRequires: maven-dependency-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-shade-plugin

%description
Jetty Toolchain parent Maven POM.

%package artifact-remote-resources
Summary: Jetty Toolchain Artifact Remote Resources
Group: Development/Java
Requires: %name = %EVR

%description artifact-remote-resources
Artifact remote resources module for Jetty Toolchain.

%package assembly-descriptors
Summary: Jetty Toolchain Assembly Descriptors
Group: Development/Java
Requires: %name = %EVR

%description assembly-descriptors
Assembly descriptors module for Jetty Toolchain.

%package distribution-remote-resources
Summary: Jetty Toolchain Distribution Remote Resources
Group: Development/Java
Requires: %name = %EVR

%description distribution-remote-resources
Distribution remote resources module for Jetty Toolchain.

%package perf-helper
Summary: Jetty Toolchain Performance Helper
Group: Development/Java
Requires: %name = %EVR

%description perf-helper
Performance helper module for Jetty Toolchain.

%package schemas
Summary: Jetty Toolchain Schemas
Group: Development/Java
Requires: %name = %EVR

%description schemas
Schemas module for Jetty Toolchain.

%package test-helper
Summary: Jetty Toolchain Test Helper
Group: Development/Java
Requires: %name = %EVR

%description test-helper
Test helper module for Jetty Toolchain.

%package test-policy
Summary: Jetty Toolchain Test Policy
Group: Development/Java
Requires: %name = %EVR

%description test-policy
Test policy module for Jetty Toolchain.

%package build-crutch
Summary: Jetty Toolchain build reactor POM metadata
Group: Development/Java
Requires: javapackages-filesystem

%description build-crutch
Build reactor POM metadata for Jetty Toolchain.

%prep
%setup

%pom_disable_module jetty-build-support
%pom_disable_module jetty-servlet-api
%pom_disable_module jetty-xslt-tools

%pom_xpath_set "/*[local-name()='project']/*[local-name()='parent']/*[local-name()='version']" 1.7 jetty-artifact-remote-resources/pom.xml
%pom_xpath_set "/*[local-name()='project']/*[local-name()='parent']/*[local-name()='version']" 1.7 jetty-assembly-descriptors/pom.xml
%pom_xpath_set "/*[local-name()='project']/*[local-name()='parent']/*[local-name()='version']" 1.7 jetty-build-support/pom.xml
%pom_xpath_set "/*[local-name()='project']/*[local-name()='parent']/*[local-name()='version']" 1.7 jetty-distribution-remote-resources/pom.xml
%pom_xpath_set "/*[local-name()='project']/*[local-name()='parent']/*[local-name()='version']" 1.7 jetty-perf-helper/pom.xml
%pom_xpath_set "/*[local-name()='project']/*[local-name()='parent']/*[local-name()='version']" 1.7 jetty-schemas/pom.xml
%pom_xpath_set "/*[local-name()='project']/*[local-name()='parent']/*[local-name()='version']" 1.7 jetty-servlet-api/pom.xml
%pom_xpath_set "/*[local-name()='project']/*[local-name()='parent']/*[local-name()='version']" 1.7 jetty-test-helper/pom.xml
%pom_xpath_set "/*[local-name()='project']/*[local-name()='parent']/*[local-name()='version']" 1.7 jetty-test-policy/pom.xml
%pom_xpath_set "/*[local-name()='project']/*[local-name()='parent']/*[local-name()='version']" 1.7 jetty-xslt-tools/pom.xml

%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-jarsigner-plugin
%pom_remove_plugin -r :maven-pmd-plugin
%pom_remove_plugin -r :maven-remote-resources-plugin
%pom_remove_plugin -r com.mycila:license-maven-plugin
%pom_remove_plugin -r :maven-deploy-plugin

# hamcrest 2.x no longer provides org.hamcrest.Factory annotation
sed -i '/import org.hamcrest.Factory;/d' \
  jetty-test-helper/src/main/java/org/eclipse/jetty/toolchain/test/matchers/RegexMatcher.java
sed -i '/^[[:space:]]*@Factory[[:space:]]*$/d' \
  jetty-test-helper/src/main/java/org/eclipse/jetty/toolchain/test/matchers/RegexMatcher.java

%build
%mvn_build -s -j -- -f pom.xml

%install
%mvn_install

%files -f .mfiles-jetty-toolchain
%doc README.md

%files artifact-remote-resources -f .mfiles-jetty-artifact-remote-resources
%files assembly-descriptors -f .mfiles-jetty-assembly-descriptors
%files distribution-remote-resources -f .mfiles-jetty-distribution-remote-resources
%files perf-helper -f .mfiles-jetty-perf-helper
%files schemas -f .mfiles-jetty-schemas
%files test-helper -f .mfiles-jetty-test-helper
%files test-policy -f .mfiles-jetty-test-policy
%files build-crutch -f .mfiles-jetty-toolchain-build-crutch

%changelog
* Wed Apr 01 2026 Ivan Khanas <xeno@altlinux.org> 1.7-alt1
- Initial build for ALT.

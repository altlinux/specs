%define _unpackaged_files_terminate_build 1

Name: japicmp
Version: 0.25.0
Release: alt2

Summary: Comparison of two versions of a jar archive
License: Apache-2.0
Group: Development/Java
Url: https://siom79.github.io/japicmp
Vcs: https://github.com/siom79/japicmp.git
BuildArch: noarch

Source0: %name-%version.tar

Patch0:	0001-Replace-javax-with-jakarta-xml-bind.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin
BuildRequires: maven-assembly-plugin
BuildRequires: javassist
BuildRequires: jaxb-api
BuildRequires: jaxb-runtime
BuildRequires: mockito-core
BuildRequires: jsoup
BuildRequires: maven-enforcer-plugin
BuildRequires: jacoco-maven-plugin
BuildRequires: ant-testutil

%description
Japicmp is a tool for checking Java API compatibility between different
versions of libraries or applications. It compares two JAR files and reports
changes in the public API, helping developers detect binary and source
incompatible modifications. The tool can be used from the command line or
integrated into automated build and CI workflows.

%package parent
Summary: Parent POM for japicmp modules
Group: Development/Java
BuildArch: noarch

%description parent
This package provides the parent Maven POM for the japicmp project.  It defines
common build configuration, dependency management, and plugin settings shared
across japicmp modules. The parent POM is intended for development and
build-time use.

%package ant-task
Summary: Ant task for japicmp API compatibility checks
Group: Development/Java
BuildArch: noarch

%description ant-task
This package provides an Ant task for japicmp, allowing API compatibility
checks to be integrated into Ant-based build systems. The task compares two
versions of a JAR archive and reports binary and source compatibility changes,
helping detect breaking API modifications during automated builds.

%prep
%setup
%autopatch -p1

%pom_xpath_remove "/*[local-name()='project']/*[local-name()='build']/*[local-name()='extensions']" pom.xml

%pom_disable_module japicmp-testbase
# No groovy.
%pom_disable_module japicmp-maven-plugin

%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :japicmp-maven-plugin japicmp
# Off integration tests, we dont want to download japicmp 0.9.4.
%pom_remove_plugin :maven-failsafe-plugin japicmp-ant-task
%pom_remove_plugin :maven-dependency-plugin japicmp-ant-task

sed -i 's/@{argLine}/${argLine}/g' japicmp/pom.xml

%build
%mvn_build -j -s

%install
%mvn_install

%files parent -f .mfiles-japicmp-base

%files -f .mfiles-japicmp

%files ant-task -f .mfiles-japicmp-ant-task

%changelog
* Thu Feb 12 2026 Evgeniy Serov <scala@altlinux.org> 0.25.0-alt2
- Fixed FTBFS.

* Mon Dec 15 2025 Ivan Khanas <xeno@altlinux.org> 0.25.0-alt1
- First build for ALT.

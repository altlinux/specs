%define _unpackaged_files_terminate_build 1

Name: takari-plugin-testing-project
Version: 3.1.1
Release: alt1

Summary: Takari Maven plugin testing framework
License: EPL-1.0
Group: Development/Java
URL: https://github.com/takari/takari-plugin-testing-project
VCS: https://github.com/takari/takari-plugin-testing-project.git

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-lib
BuildRequires: maven-resolver
BuildRequires: google-guice
BuildRequires: sisu
BuildRequires: junit
BuildRequires: junit5
BuildRequires: slf4j
BuildRequires: plexus-utils
BuildRequires: plexus-classworlds
BuildRequires: apache-commons-exec
BuildRequires: apache-commons-compress
BuildRequires: mvn(io.takari.m2e.workspace:org.eclipse.m2e.workspace.cli)

%description
Takari provides reusable JUnit resources and Maven runtimes for testing
Maven plugins, including embedded and external Maven executions.

%package integration-testing
Summary: Integration testing dependencies for Takari Maven plugins

Group: Development/Java

%description integration-testing
The integration testing POM supplies the dependencies required to execute
external Maven installations with the Takari testing framework.

%package javadoc
Summary: API documentation for Takari Maven plugin testing

Group: Development/Java

%description javadoc
API documentation for the Takari Maven plugin testing framework.

%prep
%setup -q

# Use the distribution Maven lifecycle instead of the Takari build extension.
%pom_remove_parent
# ALT supplies the ordinary Guice artifact, not the upstream classes classifier.
guice_version=$(rpm -q --qf '%%{VERSION}' google-guice)
%pom_xpath_set pom:properties/pom:sisuGuiceVersion "$guice_version"
for pom in pom.xml takari-plugin-testing/pom.xml; do
    %pom_xpath_remove \
        'pom:project//pom:dependency[pom:groupId="com.google.inject"
    and pom:artifactId="guice"]/pom:classifier' \
        "$pom"
done
# Keep all Jupiter/Vintage APIs coherent with the genuine installed JUnit5 line.
junit_version=$(rpm -q --qf '%%{VERSION}' junit5)
%pom_xpath_set \
    'pom:dependencyManagement/pom:dependencies
    /pom:dependency[pom:groupId="org.junit" and pom:artifactId="junit-bom"]
    /pom:version' \
    "$junit_version"
%pom_xpath_set pom:packaging jar takari-plugin-testing
%pom_xpath_set pom:packaging jar takari-plugin-testing-its
%pom_remove_plugin io.takari.maven.plugins:takari-lifecycle-plugin \
    takari-plugin-testing-its
# The unchanged IT suite downloads Maven3.6/3.8/3.9/4-RC distributions
# and forks nested builds; retain and compile it without network execution.
%pom_remove_plugin org.apache.maven.plugins:maven-dependency-plugin \
    takari-plugin-testing-its
%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin . \
    '<configuration><source>8</source><target>8</target></configuration>'

%mvn_package :takari-plugin-testing-project %name
%mvn_package :takari-plugin-testing %name
%mvn_package :takari-plugin-integration-testing integration-testing
%mvn_package :takari-plugin-testing-its __noinstall

%build
# Compile all retained IT sources; installed real Mojo consumers test the
# runtime.
%mvn_build -s -- -DskipTests

%install
%mvn_install

%files -f .mfiles-%name
%doc LICENSE.txt classloading.md reactorpropagation.md testproperties.md

%files integration-testing -f .mfiles-integration-testing

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 3.1.1-alt1
- Initial build for ALT.

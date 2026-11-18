%define _unpackaged_files_terminate_build 1

Name: templating-maven-plugin
Version: 3.2.0
Release: alt1

Summary: Maven plugin for filtering source templates
License: Apache-2.0
Group: Development/Java
URL: https://www.mojohaus.org/templating-maven-plugin/
VCS: https://github.com/mojohaus/templating-maven-plugin.git

Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-filtering
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-provider-junit5
BuildRequires: maven-surefire-provider-testng
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.codehaus.plexus:plexus-xml)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.mockito:mockito-junit-jupiter)
BuildRequires: mvn(net.bytebuddy:byte-buddy)
BuildRequires: mvn(net.bytebuddy:byte-buddy-agent)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.groovy:groovy)
BuildRequires: mvn(org.beanshell:bsh)

%description
Filters Java source templates into generated source directories and registers
both main and test source roots with Maven. Includes both upstream goals.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for the Templating Maven Plugin.

%prep
%setup
# Replace unavailable parent build configuration with its Java8 baseline.
%pom_remove_parent
%pom_xpath_inject pom:project '<groupId>org.codehaus.mojo</groupId>'
%pom_xpath_inject pom:properties '<maven.compiler.source>8</maven.compiler.source><maven.compiler.target>8</maven.compiler.target><maven-compiler-plugin.version>3.14.0</maven-compiler-plugin.version>'
%pom_xpath_inject 'pom:dependencies/pom:dependency[pom:artifactId="maven-plugin-annotations"]' '<version>3.9.0</version>'
%pom_xpath_inject 'pom:dependencies/pom:dependency[pom:artifactId="junit-jupiter-api" or pom:artifactId="junit-jupiter-params"]' '<version>6.0.1</version>'
# Mockito5 core includes the inline mock maker; no separate inline artifact.
%pom_remove_dep org.mockito:mockito-inline
%pom_add_dep org.junit.jupiter:junit-jupiter-engine:6.0.1:test
%pom_xpath_inject 'pom:profiles/pom:profile[pom:id="run-its"]/pom:build/pom:plugins/pom:plugin/pom:configuration/pom:properties' '<maven.compiler.source>8</maven.compiler.source><maven.compiler.target>8</maven.compiler.target>'

%build
%mvn_build -- -Dinvoker.mavenExecutable=/usr/bin/xmvn -Dinvoker.offline=true

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 16 2026 Ivan Khanas <xeno@altlinux.org> 3.2.0-alt1
- Initial build for ALT.

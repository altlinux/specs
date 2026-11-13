%define _unpackaged_files_terminate_build 1

Name: cucumber-parent
Version: 5.8.0
Release: alt1

Summary: Common Maven configuration for Cucumber projects
License: MIT
Group: Development/Java
URL: https://github.com/cucumber/cucumber-parent
VCS: https://github.com/cucumber/cucumber-parent.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-war-plugin)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)

%description
Parent POM with common build configuration for Cucumber Java projects.

%prep
%setup
# Distribution builds do not publish, generate sites or reformat sources.
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-deploy-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-project-info-reports-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin
%pom_remove_plugin org.codehaus.mojo:versions-maven-plugin
%pom_remove_plugin com.diffplug.spotless:spotless-maven-plugin

%install
%mvn_artifact pom.xml
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Thu Nov 12 2026 Ivan Khanas <xeno@altlinux.org> 5.8.0-alt1
- Initial build for ALT.

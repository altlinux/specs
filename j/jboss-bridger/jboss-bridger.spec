%define _unpackaged_files_terminate_build 1

Name: jboss-bridger
Version: 1.8
Release: alt1

Summary: Java bridge method generation library and Maven plugin
License: Apache-2.0
Group: Development/Java
Url: https://github.com/dmlloyd/bridger
VCS: https://github.com/dmlloyd/bridger.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-settings)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.ow2.asm:asm)

%description
Bridger transforms Java class files to generate synthetic bridge methods.
It provides both a command line tool and a Maven plugin used by Groovy.

%javadoc_package

%prep
%setup -q
%pom_remove_parent
%pom_remove_dep org.apache.maven:maven-project
%pom_remove_dep org.apache.maven.shared:maven-filtering
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-jar-plugin
%pom_remove_plugin :maven-plugin-plugin
%pom_xpath_remove 'pom:reporting'
%pom_xpath_remove 'pom:scm'
%pom_xpath_remove 'pom:issueManagement'
%pom_xpath_remove 'pom:nexus.repository.release'
%pom_xpath_set 'pom:properties/pom:maven.compiler.source' 8
%pom_xpath_set 'pom:properties/pom:maven.compiler.target' 8

%mvn_file :bridger jboss-bridger

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-bridger
%doc README.md
%doc LICENSE

%changelog
* Thu Oct 29 2026 Ivan Khanas <xeno@altlinux.org> 1.8-alt1
- Initial build for ALT.

%define _unpackaged_files_terminate_build 1

Name: cucumber-jvm-deps
Version: 1.0.6
Release: alt1

Summary: Relocated dependencies for Cucumber-JVM
License: BSD-3-Clause AND Apache-2.0
Group: Development/Java
URL: https://github.com/cucumber-attic/cucumber-jvm-deps
VCS: https://github.com/cucumber-attic/cucumber-jvm-deps

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(com.thoughtworks.xstream:xstream)
BuildRequires: mvn(com.googlecode.java-diff-utils:diffutils)

BuildArch: noarch

%description
Cucumber-JVM packages selected dependencies in relocated Java packages to
avoid conflicts with other libraries used by applications.

%prep
%setup -q
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_xpath_set \
    'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-shade-plugin"]/pom:version' \
    3.6.2
%pom_xpath_remove 'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-shade-plugin"]/pom:executions/pom:execution/pom:configuration/pom:createSourcesJar'
%pom_xpath_set \
    'pom:project/pom:dependencies/pom:dependency[pom:artifactId="xstream"]/pom:version' \
    1.4.19

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-cucumber-jvm-deps

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 1.0.6-alt1
- Initial build for ALT.

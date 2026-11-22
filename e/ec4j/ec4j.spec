%define _unpackaged_files_terminate_build 1

Name: ec4j
Version: 1.2.0
Release: alt1

Summary: Java EditorConfig parser and tree walker
License: Apache-2.0
Group: Development/Java
URL: https://github.com/ec4j/ec4j
VCS: https://github.com/ec4j/ec4j

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(junit:junit)

BuildArch: noarch

%description
ec4j is a Java implementation of EditorConfig. It parses .editorconfig files
and provides an API for querying properties and validating configuration.

%package javadoc
Summary: API documentation for ec4j
Group: Development/Documentation

%description javadoc
API documentation for the ec4j EditorConfig library.

%prep
%setup -q
%pom_remove_plugin com.mycila:license-maven-plugin
%pom_remove_plugin net.revelc.code.formatter:formatter-maven-plugin
%pom_remove_plugin net.revelc.code:impsort-maven-plugin
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 1.2.0-alt1
- Initial build for ALT.

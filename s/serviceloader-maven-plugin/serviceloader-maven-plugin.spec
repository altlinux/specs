%define _unpackaged_files_terminate_build 1

%def_with check

Name: serviceloader-maven-plugin
Version: 1.4.0
Release: alt1

Summary: Maven plugin to generate META-INF/services files for ServiceLoader
License: Apache-2.0
Group: Development/Java
Url: https://github.com/francisdb/serviceloader-maven-plugin
Vcs: https://github.com/francisdb/serviceloader-maven-plugin

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: java-11-openjdk-devel
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven:maven-project)
BuildRequires: mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)

%description
Maven plugin that locates all classes implementing a certain interface
and generates the META-INF/services/ files required by the Java
ServiceLoader mechanism.

%package javadoc
Summary: API documentation for %name
Group: Development/Java
Requires: %name = %EVR

%description javadoc
API documentation for the serviceloader-maven-plugin.

%prep
%setup

# Remove build extensions and plugins requiring network
%pom_xpath_remove "pom:build/pom:extensions" || :
for plugin in nexus-staging-maven-plugin maven-gpg-plugin \
              maven-release-plugin maven-source-plugin; do
    %pom_remove_plugin :$plugin || :
done
%pom_remove_plugin com.mycila:license-maven-plugin || :
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin || :

%build
%mvn_build %{?_without_check:-f}

%install
%mvn_install

%check
%mvn_build -s

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Jun 11 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.4.0-alt1
- Initial build for ALT Sisyphus.

%define _unpackaged_files_terminate_build 1

Name: maven-toolchains-plugin
Version: 3.3.0
Release: alt1

Summary: Apache Maven Toolchains Plugin
License: Apache-2.0
Group: Development/Java
URL: https://maven.apache.org/plugins/maven-toolchains-plugin/
VCS: https://github.com/apache/maven-toolchains-plugin.git

Source0: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-parent
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires: mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires: mvn(org.codehaus.plexus:plexus-xml)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires: mvn(org.apache.groovy:groovy)

%description
Maven Toolchains shares tool configuration between plugins. It provides JDK
discovery, selection and toolchains XML generation, as well as support for
custom toolchain types.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for the Apache Maven Toolchains Plugin.

%prep
%setup

%build
%mvn_build -s -- -Prun-its

%install
%mvn_install

%files -f .mfiles-%name
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 16 2026 Ivan Khanas <xeno@altlinux.org> 3.3.0-alt1
- Initial build for ALT.

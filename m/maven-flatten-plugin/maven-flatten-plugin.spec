%define _unpackaged_files_terminate_build 1

Name: maven-flatten-plugin
Version: 1.9.0
Release: alt1

Summary: Maven plugin for producing flattened POM files
License: Apache-2.0
Group: Development/Java
URL: https://www.mojohaus.org/flatten-maven-plugin/
VCS: https://github.com/mojohaus/flatten-maven-plugin.git

Source0: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires: mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-model-builder)
BuildRequires: mvn(org.apache.maven:maven-settings)
BuildRequires: mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires: mvn(org.apache.maven.resolver:maven-resolver-util)
BuildRequires: mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires: mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.codehaus.plexus:plexus-xml)
BuildRequires: mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)

%description
The Flatten Maven Plugin resolves and reduces Maven project metadata into
POM files suitable for consumers. It provides the flatten and clean goals.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for the Flatten Maven Plugin.

%prep
%setup -q

%build
%mvn_build -- -Dmaven.compiler.release=8 -Dmaven.source.skip=true

%install
%mvn_install
rm -f %buildroot%_javadocdir/%name/args

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 16 2026 Ivan Khanas <xeno@altlinux.org> 1.9.0-alt1
- Initial build for ALT.

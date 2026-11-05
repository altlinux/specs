%define _unpackaged_files_terminate_build 1

Name: m2e-workspace
Version: 0.4.0
Release: alt1

Summary: Eclipse m2e workspace resolver for Maven
License: EPL-1.0
Group: Development/Java
URL: https://eclipse.dev/m2e/
VCS: https://github.com/eclipse-m2e/org.eclipse.m2e.workspace.git

BuildArch: noarch

Source0: %name-%version.tar
Source1: LICENSE
Patch0: m2e-workspace-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-lib
BuildRequires: maven-resolver
BuildRequires: plexus-containers-component-annotations
BuildRequires: atinject

%description
The m2e workspace resolver lets Maven use projects from an Eclipse workspace
as dependency artifacts during command-line builds.

%prep
%setup -q -n %name-%version
cp %SOURCE1 LICENSE
%patch0 -p1
%pom_xpath_set pom:properties/pom:maven-core.version 3.9.16 \
    org.eclipse.m2e.workspace.cli
%pom_xpath_set pom:packaging jar org.eclipse.m2e.workspace.cli
%pom_remove_dep org.sonatype.aether:aether-api org.eclipse.m2e.workspace.cli
%pom_remove_plugin io.takari.maven.plugins:takari-lifecycle-plugin \
    org.eclipse.m2e.workspace.cli
%pom_remove_plugin org.codehaus.plexus:plexus-component-metadata \
    org.eclipse.m2e.workspace.cli
%pom_remove_plugin org.apache.felix:maven-bundle-plugin \
    org.eclipse.m2e.workspace.cli

%build
cd org.eclipse.m2e.workspace.cli
%mvn_build -s -- -Dmaven.compiler.source=8 -Dmaven.compiler.target=8

%install
cd org.eclipse.m2e.workspace.cli
%mvn_install
cat .mfiles-javadoc >> .mfiles-org.eclipse.m2e.workspace.cli

%files -f org.eclipse.m2e.workspace.cli/.mfiles-org.eclipse.m2e.workspace.cli
%doc LICENSE org.eclipse.m2e.workspace.cli/src/main/resources/about.html

%changelog
* Wed Oct 28 2026 Ivan Khanas <xeno@altlinux.org> 0.4.0-alt1
- Initial build for ALT.

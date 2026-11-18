%define _unpackaged_files_terminate_build 1

Name: glassfish-build-maven-plugin
Version: 4.1.0
Release: alt1

Summary: Maven plugin for GlassFish build tasks
License: EPL-2.0 OR GPL-2.0 WITH Classpath-exception-2.0
Group: Development/Java
URL: https://github.com/eclipse-ee4j/glassfish-build-maven-plugin
VCS: https://github.com/eclipse-ee4j/glassfish-build-maven-plugin.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.eclipse.ee4j:project:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires: mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires: mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(org.apache.maven:maven-model-builder)
BuildRequires: mvn(org.apache.maven:maven-archiver)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.maven.shared:maven-common-artifact-filters)

%description
Maven build goals and lifecycle extensions for GlassFish distribution
assembly, feature-set dependencies, artifact selection and file operations.

%package compat
Summary: GlassFish build goals from the 3.2 compatibility line
Group: Development/Java

%description compat
The genuine GlassFish build Maven plugin 3.2.28, including source unpacking,
POM generation and artifact attachment goals required by Jakarta EE APIs.

%package javadoc
Summary: API documentation for GlassFish build Maven plugin
Group: Development/Java

%description javadoc
API documentation for GlassFish build Maven plugin.

%prep
%setup
%pom_remove_plugin -r -f :maven-checkstyle-plugin
%pom_remove_plugin -r -f org.glassfish.copyright:glassfish-copyright-maven-plugin
%pom_remove_plugin -r -f :maven-source-plugin

pushd legacy3
%pom_remove_plugin -r -f :maven-checkstyle-plugin
%pom_remove_plugin -r -f org.glassfish.copyright:glassfish-copyright-maven-plugin
%pom_remove_plugin -r -f :maven-source-plugin
%mvn_compat_version :glassfishbuild-maven-plugin 3.2.28
%mvn_package :glassfishbuild-maven-plugin compat
popd

%build
java -version
%mvn_build -- -Dinvoker.offline=true
pushd legacy3
%mvn_build -- -Dmaven.compiler.release=8
popd

%install
%mvn_install
pushd legacy3
xmvn-install -R .xmvn-reactor -n %name-compat -d %buildroot
jdir=target/xmvn-apidocs
install -d %buildroot%_javadocdir/%name/compat
cp -a "$jdir"/. %buildroot%_javadocdir/%name/compat/
popd

%files -f .mfiles
%doc LICENSE.md NOTICE.md

%files compat -f legacy3/.mfiles-compat
%doc legacy3/LICENSE.md legacy3/NOTICE.md

%files javadoc
%_javadocdir/%name

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 4.1.0-alt1
- Initial build for ALT.

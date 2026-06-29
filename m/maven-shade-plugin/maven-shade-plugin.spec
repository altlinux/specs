Name:    maven-shade-plugin
Version: 3.6.0
Release: alt3
Summary: Maven plugin for packaging artifacts in an uber-jar

License: Apache-2.0
Group: Development/Java
URL: https://maven.apache.org/plugins/maven-shade-plugin
Source0: https://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch: noarch
 
BuildRequires(pre): rpm-build-java
BuildRequires: maven-local
BuildRequires: /proc
BuildRequires: java-11-openjdk-devel
BuildRequires: unzip
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires: mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.jdom:jdom2)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(org.vafer:jdependency)
BuildRequires: mvn(xmlunit:xmlunit)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(org.apache.commons:commons-collections4)
BuildRequires: mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires: mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires: google-guice
BuildRequires: maven-plugin-testing-harness
 
%description
This plugin provides the capability to package the artifact in an
uber-jar, including its dependencies and to shade - i.e. rename - the
packages of some of the dependencies.

#%%javadoc_package

%prep
%setup
rm src/test/jars/plexus-utils-1.4.1.jar
ln -s $(build-classpath plexus/utils) src/test/jars/plexus-utils-1.4.1.jar
 
%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE
 
%changelog
* Mon Jun 22 2026 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt3
- Built with openjdk11.

* Tue Dec 09 2025 Anton Meleshnikov <alton@altlinux.org> 3.6.0-alt2
- Fixed FTBFS.

* Sun Aug 24 2025 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus (without javadoc).

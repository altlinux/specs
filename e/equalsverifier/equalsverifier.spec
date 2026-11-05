%define _unpackaged_files_terminate_build 1

Name: equalsverifier
Version: 4.5.2
Release: alt1

Summary: Verify Java equals and hashCode contracts
License: Apache-2.0
Group: Development/Java
URL: https://jqno.nl/equalsverifier/
VCS: https://github.com/jqno/equalsverifier.git

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(net.bytebuddy:byte-buddy)
BuildRequires: mvn(org.objenesis:objenesis)
BuildRequires: mvn(org.mockito:mockito-core)
# Core RPM metadata also advertises Jupiter; require the actual integration JAR.
BuildRequires: mockito-junit-jupiter
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(com.tngtech.archunit:archunit-junit5)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(net.jcip:jcip-annotations)
BuildRequires: mvn(jakarta.annotation:jakarta.annotation-api)
BuildRequires: mvn(org.eclipse.jdt:org.eclipse.jdt.annotation)
BuildRequires: mvn(jakarta.persistence:jakarta.persistence-api)
BuildRequires: mvn(com.github.spotbugs:spotbugs-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jarsigner-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
EqualsVerifier verifies the Java equals and hashCode contract, including
inheritance, fields and common third party types. The library uses the
system Byte Buddy and Objenesis implementations.

%javadoc_package

%prep
%setup
%autopatch -p1
# Keep upstream JDK activation: core17 and the Java21 overlay/tests.
# Add only the normal consumer assembly, excluding metadata edges to inactive
# JDK25/26 modules. Their production sources remain in the source archive.
%pom_xpath_inject pom:project \
    '<modules><module>equalsverifier-aggregator</module><module>equalsverifier-release-main</module></modules>'
%pom_remove_dep :equalsverifier-25 equalsverifier-release-main
%pom_remove_dep :equalsverifier-25 equalsverifier-aggregator
%pom_remove_dep :equalsverifier-26 equalsverifier-aggregator
%pom_remove_dep :equalsverifier-test-kotlin equalsverifier-aggregator
%pom_remove_dep :equalsverifier-test-jpms equalsverifier-aggregator
%pom_xpath_remove \
    "//*[local-name()='moduleSet'][*[local-name()='includes']/*[local-name()='include']='nl.jqno.equalsverifier:equalsverifier-25']" \
    equalsverifier-aggregator/src/main/resources/assemblies/assembly.xml
# XMvn provides documentation and source registration locally.
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-deploy-plugin
# The regular release uses external dependencies rather than the shaded variant.
%pom_remove_plugin org.apache.maven.plugins:maven-shade-plugin \
    equalsverifier-core
%pom_remove_plugin com.coderplus.maven.plugins:copy-rename-maven-plugin \
    equalsverifier-release-main
%pom_remove_plugin org.codehaus.mojo:build-helper-maven-plugin \
    equalsverifier-release-main
# XMvn packages the parent POM, so the publication-only flattening is
# unnecessary.
%pom_remove_plugin org.codehaus.mojo:flatten-maven-plugin \
    equalsverifier-release-main
%mvn_package :equalsverifier-parent equalsverifier
%mvn_package :equalsverifier equalsverifier
%mvn_package :equalsverifier-core __noinstall
%mvn_package :equalsverifier-21 __noinstall
%mvn_package :equalsverifier-25 __noinstall
%mvn_package :equalsverifier-26 __noinstall
%mvn_package :equalsverifier-aggregator __noinstall
%mvn_package :equalsverifier-test* __noinstall
%mvn_file :equalsverifier equalsverifier

%build
# This is upstream's supported Java21 reactor plus the normal consumer GAV.
# The universal upstream release additionally contains the Java25 overlay;
# it is intentionally not assembled into this Java<=21 build.
%mvn_build -s -j -- -DdisableStaticAnalysis

# Document the shipped modular API, excluding the mixed test reactor.
xmvn --offline --batch-mode -DdisableStaticAnalysis \
    -pl equalsverifier-core \
    org.fedoraproject.xmvn:xmvn-mojo:javadoc
test -s .xmvn/apidocs/index.html
rm -rf .xmvn/apidocs/module-source-path .xmvn/apidocs/args

%install
%mvn_install

%files -f .mfiles-equalsverifier
%doc LICENSE.md

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 4.5.2-alt1
- Initial build for ALT.

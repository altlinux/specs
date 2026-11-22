%define _unpackaged_files_terminate_build 1

Name: memoryfilesystem
Version: 2.8.4
Release: alt1

Summary: In-memory implementation of the Java NIO file system API
License: MIT
Group: Development/Java
URL: https://github.com/marschall/memoryfilesystem
VCS: https://github.com/marschall/memoryfilesystem.git

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(jakarta.annotation:jakarta.annotation-api)
BuildRequires: mvn(org.junit:junit-bom:pom:)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.apache.lucene:lucene-core)
BuildRequires: mvn(codes.rafael.modulemaker:modulemaker-maven-plugin)
BuildRequires: mvn(io.smallrye:jandex-maven-plugin)

BuildArch: noarch

%description
MemoryFileSystem implements Java NIO.2 file systems in memory, with configurable
Unix, Windows and macOS behavior, file attributes, channels and file operations.

%prep
%setup
# Remote publication and developer reports are not part of local compilation.
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :flatten-maven-plugin
%pom_remove_plugin :jitwatch-jarscan-maven-plugin
%pom_remove_plugin :maven-dependency-plugin
# Do not install an attached source-classifier JAR.
%pom_remove_plugin :maven-source-plugin
# Remove upstream package-phase Javadoc attachment; the module cannot export javax.annotation.
%pom_remove_plugin :maven-javadoc-plugin
# Sisyphus Jakarta API contains both genuine javax and jakarta annotations.
# They belong to one JPMS module; a separate javax API would split packages.
%pom_remove_dep javax.annotation:javax.annotation-api
%pom_xpath_set \
    'pom:project/pom:profiles/pom:profile[pom:id="jdk-9-plus"]/pom:build/pom:plugins/pom:plugin[pom:artifactId="modulemaker-maven-plugin"]/pom:configuration/pom:static-requires' \
    jakarta.annotation
# These suites require unavailable test-only providers; retain all independent tests.
rm -f src/test/java/com/github/marschall/memoryfilesystem/MemoryFileSystemFactoryBeanGeneratedNameTest.java
rm -f src/test/java/com/github/marschall/memoryfilesystem/MemoryFileSystemFactoryBeanTest.java
rm -f src/test/java/com/github/marschall/memoryfilesystem/MemoryFileSystemFactoryBeanTypeTest.java
rm -f src/test/java/com/github/marschall/memoryfilesystem/MemoryInodeIT.java
%pom_remove_dep org.springframework:spring-test
%pom_remove_dep org.springframework:spring-context
%pom_remove_dep org.apache.logging.log4j:log4j-core
%pom_remove_dep org.apache.logging.log4j:log4j-slf4j-impl
%pom_remove_dep org.apache.logging.log4j:log4j-jcl
%pom_remove_dep org.apache.logging.log4j:log4j-jul
%pom_remove_dep com.github.marschall:jol-agent
%pom_remove_dep org.openjdk.jol:jol-core
%pom_remove_dep org.springframework:spring-framework-bom
%pom_remove_dep org.apache.logging.log4j:log4j-bom
# Match the exact AssertJ version available in the Sisyphus Maven repository.
%pom_xpath_set \
    'pom:project/pom:dependencies/pom:dependency[pom:artifactId="assertj-core"]/pom:version' \
    3.27.3
# Use the current Sisyphus versions of the module generator and Lucene test API.
%pom_xpath_set \
    'pom:project/pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:version' \
    3.14.0
%pom_xpath_set \
    'pom:project/pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId="maven-surefire-plugin"]/pom:version' \
    3.5.6
%pom_xpath_set \
    'pom:project/pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId="modulemaker-maven-plugin"]/pom:version' \
    1.9
%pom_xpath_set \
    'pom:project/pom:profiles/pom:profile[pom:id="jdk-9-plus"]/pom:dependencies/pom:dependency[pom:artifactId="lucene-core"]/pom:version' \
    10.4.0
%pom_remove_plugin :maven-failsafe-plugin
%mvn_package : memoryfilesystem

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles-memoryfilesystem
%doc src/main/resources/LICENSE

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 2.8.4-alt1
- Initial build for ALT.

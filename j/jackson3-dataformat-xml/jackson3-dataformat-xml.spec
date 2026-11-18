%define _unpackaged_files_terminate_build 1

Name: jackson3-dataformat-xml
Version: 3.3.0
Release: alt1

Summary: Jackson XML data format module
License: Apache-2.0
Group: Development/Java
URL: https://github.com/FasterXML/jackson-dataformat-xml
VCS: https://github.com/FasterXML/jackson-dataformat-xml.git

Source0: %name-%version.tar
Patch0: 0001-Isolate-JAXB-dependent-tests.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(tools.jackson:jackson-base:pom:)
BuildRequires: mvn(tools.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(tools.jackson.core:jackson-databind)
BuildRequires: mvn(org.codehaus.woodstox:stax2-api)
BuildRequires: mvn(com.fasterxml.woodstox:woodstox-core)
BuildRequires: replacer
BuildRequires: mvn(org.moditect:moditect-maven-plugin)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)

BuildArch: noarch

%description
Data format extension for Jackson to serialize Java objects as XML and
read XML as Java objects.

%javadoc_package

%prep
%setup
%autopatch -p1

# Only isolated JAXB tests need this unavailable test module.
%pom_remove_dep tools.jackson.module:jackson-module-jakarta-xmlbind-annotations
%pom_remove_plugin :gradle-module-metadata-maven-plugin
%pom_remove_plugin :cyclonedx-maven-plugin
# Target Woodstox has an incomplete JPMS descriptor; run tests on classpath.
# Optional MSV schema providers are absent; retain these suites testCompile.
%pom_add_plugin org.apache.maven.plugins:maven-surefire-plugin . \
    "<configuration> \
       <useModulePath>false</useModulePath> \
       <excludes> \
         <exclude>**/RelaxNGValidationTest.java</exclude> \
         <exclude>**/W3CSchemaValidationTest.java</exclude> \
       </excludes> \
     </configuration>"
%mvn_file : %name

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE src/main/resources/META-INF/NOTICE

%changelog
* Sat Nov 14 2026 Ivan Khanas <xeno@altlinux.org> 3.3.0-alt1
- Initial build for ALT.

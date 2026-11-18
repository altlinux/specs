%define _unpackaged_files_terminate_build 1

Name: jackson3-databind
Version: 3.3.0
Release: alt1

Summary: General data binding and tree model for Jackson
License: Apache-2.0
Group: Development/Java
URL: https://github.com/FasterXML/jackson-databind
VCS: https://github.com/FasterXML/jackson-databind.git

Source0: %name-%version.tar
Patch0: 0001-Use-system-test-module-names.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(tools.jackson:jackson-base:pom:)
BuildRequires: mvn(tools.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: replacer
BuildRequires: maven-plugin-bundle
BuildRequires: mvn(org.moditect:moditect-maven-plugin)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(com.google.guava:guava-testlib)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(net.bytebuddy:byte-buddy-agent)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)

BuildArch: noarch

%description
General-purpose data binding and tree model for the Jackson streaming API.

%javadoc_package

%prep
%setup
%autopatch -p1
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :gradle-module-metadata-maven-plugin
%pom_remove_plugin :cyclonedx-maven-plugin
# Use the declared system agent rather than a Maven download-cache path.
%pom_xpath_set -- \
    "//pom:profile[pom:id='java21']/pom:properties/pom:argLine" \
    '--add-opens=java.base/java.lang=tools.jackson.databind
     --add-opens=java.base/java.util=tools.jackson.databind
     --add-opens
     tools.jackson.databind/tools.jackson.databind.jdk21=org.junit.platform.commons
     -javaagent:%_javadir/byte-buddy/byte-buddy-agent.jar'
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

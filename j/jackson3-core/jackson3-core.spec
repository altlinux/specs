%define _unpackaged_files_terminate_build 1

Name: jackson3-core
Version: 3.3.0
Release: alt1

Summary: Core part of Jackson
License: Apache-2.0
Group: Development/Java
URL: https://github.com/FasterXML/jackson-core
VCS: https://github.com/FasterXML/jackson-core.git

Source0: %name-%version.tar
Patch0: 0001-Require-system-FastDoubleParser-module.patch
Patch1: 0002-Use-system-AssertJ-module-name.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(tools.jackson:jackson-base:pom:)
BuildRequires: mvn(ch.randelshofer:fastdoubleparser)
BuildRequires: replacer
BuildRequires: maven-plugin-bundle
BuildRequires: mvn(org.moditect:moditect-maven-plugin)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-failsafe-plugin)

BuildArch: noarch

%description
Core part of Jackson that defines Streaming API as well
as basic shared abstractions.

%javadoc_package

%prep
%setup
%autopatch -p1

%pom_remove_plugin :maven-enforcer-plugin
# The shaded-FDP layout assertion does not apply to the system dependency.
%pom_xpath_inject \
    "//pom:plugin[pom:artifactId='maven-failsafe-plugin']/pom:configuration" \
    '<excludes><exclude>**/FastDoubleParserShadingIT.java</exclude></excludes>'
%pom_remove_plugin :gradle-module-metadata-maven-plugin
%pom_remove_plugin :cyclonedx-maven-plugin

# Use the system FastDoubleParser without shading its classes.
%pom_remove_plugin :maven-shade-plugin
%pom_xpath_set pom:properties/pom:osgi.import '*'

%mvn_file : %name

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE src/main/resources/META-INF/jackson-core-NOTICE

%changelog
* Sat Nov 14 2026 Ivan Khanas <xeno@altlinux.org> 3.3.0-alt1
- Initial build for ALT.

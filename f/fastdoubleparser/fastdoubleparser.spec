%define _unpackaged_files_terminate_build 1

Name: fastdoubleparser
Version: 2.0.1
Release: alt1

Summary: Fast parsers for Java floating point and integer numbers
License: MIT AND BSD-2-Clause
Group: Development/Java
URL: https://github.com/wrandelshofer/FastDoubleParser
VCS: https://github.com/wrandelshofer/FastDoubleParser.git

Source0: %name-%version.tar
Patch0: %name-explicit-arabic-numbering.patch
Patch1: %name-java21.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: maven-assembly-plugin
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.platform:junit-platform-suite-commons)
BuildRequires: mvn(org.openjdk.jmh:jmh-core)
BuildRequires: mvn(org.openjdk.jmh:jmh-generator-annprocess)
BuildArch: noarch

%description
Fast parsers for Java double, float, BigDecimal and BigInteger values,
including JSON numbers and configurable number format symbols.

%prep
%setup

# Keep Arabic-digit fixtures independent of JDK locale-data defaults.
%autopatch -p1

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin io.github.git-commit-id:git-commit-id-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :flatten-maven-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_xpath_set pom:version %version
for module in fastdoubleparser fastdoubleparser-java{8,11,17,21}; do
    %pom_xpath_set pom:parent/pom:version %version "$module"
done

# The release JAR assembles Java 8/11/17/21 modules, not dev/demo JARs.
%pom_disable_module fastdoubleparser-dev
%pom_disable_module fastdoubleparserdemo
%pom_disable_module fastdoubleparserdemo-dev
%pom_disable_module fastdoubleparserdemo-java8
%pom_disable_module fastdoubleparserdemo-java11
%pom_disable_module fastdoubleparserdemo-java17
%pom_disable_module fastdoubleparserdemo-java21
%pom_disable_module fastdoubleparserdemo-java23

%mvn_package :fastdoubleparser-java* __noinstall
%mvn_file :fastdoubleparser %name

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Tue Nov 10 2026 Ivan Khanas <xeno@altlinux.org> 2.0.1-alt1
- Initial build for ALT.

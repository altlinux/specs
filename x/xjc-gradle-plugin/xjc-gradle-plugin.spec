%define _unpackaged_files_terminate_build 1

Name: xjc-gradle-plugin
Version: 1.9.0
Release: alt1

Summary: Gradle plugin for generating Java sources from XML schemas
License: MIT
Group: Development/Java
Url: https://github.com/bjornvester/xjc-gradle-plugin
Vcs: https://github.com/bjornvester/xjc-gradle-plugin.git

BuildArch: noarch

Source0: %name-%version.tar
Patch0: xjc-gradle-plugin-offline.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-17-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: javapackages-filesystem
BuildRequires: mvn(org.glassfish.jaxb:jaxb-xjc)

%description
A Gradle plugin that runs the JAXB XJC compiler to generate Java sources
from XML schema definitions.

%prep
%setup -q -n %name-%version
%patch0 -p1

%build
%gradle_publish --warning-mode=summary

%install
%gradle_register --artifacts=xjc-gradle-plugin-
marker_dir=$HOME/.m2/repository/com/github/bjornvester/xjc
marker_dir=$marker_dir/com.github.bjornvester.xjc.gradle.plugin/%version
%mvn_artifact \
    "$marker_dir/com.github.bjornvester.xjc.gradle.plugin-%version.pom"
%mvn_file com.github.bjornvester:xjc-gradle-plugin %name/xjc-gradle-plugin
%mvn_file com.github.bjornvester.xjc:com.github.bjornvester.xjc.gradle.plugin \
    %name/com.github.bjornvester.xjc.gradle.plugin
%gradle_install

%check
# The only upstream suite runs downloaded TestKit distributions and fixtures.
%gradle_check -x test

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 1.9.0-alt1
- Initial build for ALT.

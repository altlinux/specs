%define _unpackaged_files_terminate_build 1

Name: badass-jar-plugin
Version: 2.0.0
Release: alt1

Summary: Plugin that lets you seamlessly create modular jars that target a Java release before 9
License: Apache-2.0
Group: Development/Java
Url: https://github.com/beryx/badass-jar
Vcs: https://github.com/beryx/badass-jar-plugin.git
BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: /proc
BuildRequires: dos2unix
BuildRequires: rpm-build-java
BuildRequires: jpackage-11-compat
BuildRequires: shadow-gradle-plugin
BuildRequires: javaparser
BuildRequires: objectweb-asm

Source0: %name-%version.tar
Patch0: 0001-Remove-unwanted-plugins-alt-patch.patch

%description
This plugin lets you seamlessly create modular jars that target a Java release
before 9. This way, your library can be used not only by people who build JPMS
applications, but also by people who are still using Java 8 or older releases.

%prep
%setup
dos2unix build.gradle
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register
%mvn_artifact $(find %_mavenrepolocal -name org.beryx.jar.gradle.plugin-%version.pom)

%gradle_install

%files -f .mfiles
%changelog
* Thu Nov 06 2025 Ivan Khanas <xeno@altlinux.org> 2.0.0-alt1
- First build for ALT.

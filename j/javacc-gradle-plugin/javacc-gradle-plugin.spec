%define _unpackaged_files_terminate_build 1

Name: javacc-gradle-plugin
Version: 4.0.3
Release: alt1

Summary: JavaCC Compiler Plugin for Gradle
Group: Development/Java
License: MIT
Url: https://github.com/javacc/javaccPlugin
Vcs: https://github.com/javacc/javaccPlugin
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: java-11-openjdk-devel
BuildRequires: xgradle
BuildRequires: javacc
BuildRequires: hamcrest-core
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang3
BuildRequires: shadow-gradle-plugin
Requires: javacc

%package javadoc
Summary: API documentation for JavaCC Gradle plugin
Group: Development/Java

%description
JavaCC Gradle plugin provides the ability to use JavaCC via Gradle.

%description javadoc
This package contains API documentation for the JavaCC Gradle plugin.
JavaCC Gradle plugin provides the ability to use JavaCC via Gradle.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register
%gradle_register_javadoc
%gradle_install
# Related to the groupId change
find ~/.m2 -iname *javacc.gradle.plugin-%version.pom -exec \
    install -Dm 644 {} \
    %buildroot%_datadir/maven-poms/javacc-gradle-plugin/org.javacc.javacc.gradle.plugin.pom \;

%files -f .mfiles
%_datadir/maven-poms/javacc-gradle-plugin/org.javacc.javacc.gradle.plugin.pom

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Mar 23 2026 Arseniy Kostevich <faux@altlinux.org> 4.0.3-alt1
- Initial build for ALT.

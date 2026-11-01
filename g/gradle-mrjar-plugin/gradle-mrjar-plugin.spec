%define _unpackaged_files_terminate_build 1

Name: gradle-mrjar-plugin
Version: 0.1.1
Release: alt1

Summary: Gradle plugin for building multi-release JARs
License: Apache-2.0
Group: Development/Java
Url: https://github.com/melix/gradle-mrjar-plugin
VCS: https://github.com/melix/gradle-mrjar-plugin.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-21-openjdk-devel
BuildRequires: xgradle

%description
A Gradle plugin that configures source sets and toolchains for building
multi-release JARs.

%prep
%setup -q
%patch0 -p1

%build
# Upstream tests require Spock 2 and Groovy 3, which introduce a
# build-order cycle before the new Groovy package is available.
%gradle_publish

%install
install -d %buildroot%_javadir/%name %buildroot%_mavenpomdir/%name
%gradle_install_plugin --artifacts=plugin-,me.champeau.mrjar.gradle.plugin-

%files
%_javadir/%name/plugin.jar
%_mavenpomdir/%name/plugin.pom
%_mavenpomdir/%name/me.champeau.mrjar.gradle.plugin.pom
%doc LICENSE README.md

%changelog
* Thu Oct 29 2026 Ivan Khanas <xeno@altlinux.org> 0.1.1-alt1
- Initial build for ALT.
- Publish implementation and plugin marker with Java 8-compatible bytecode.

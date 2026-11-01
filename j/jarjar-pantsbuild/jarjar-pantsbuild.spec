%define _unpackaged_files_terminate_build 1

Name: jarjar-pantsbuild
Version: 1.7.2
Release: alt1

Summary: Pants Jar Jar Links Java library repackaging tool
License: Apache-2.0
Group: Development/Java
Url: https://github.com/pantsbuild/jarjar
VCS: https://github.com/pantsbuild/jarjar.git

Source0: %name-%version.tar
Patch0: %name-%version-alt-build.patch
BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: java-21-openjdk-devel
BuildRequires: rpm-build-java-osgi
BuildRequires: xgradle
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-commons)

%description
Jar Jar Links repackages Java libraries and rewrites class references.
This package provides the org.pantsbuild artifact and namespace used
by the Groovy build, with external system ASM and Ant dependencies.

%package javadoc
Summary: API documentation for Pants Jar Jar Links
Group: Development/Documentation

%description javadoc
API documentation for the Pants Jar Jar Links repackaging library.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register --artifacts=jarjar-
%gradle_register_javadoc --artifacts=jarjar-
%gradle_install

%check
# The upstream integration suite compiles Java 6, 7 and 8 class fixtures.
%gradle_check

%files -f .mfiles
%doc COPYING LICENSE README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 1.7.2-alt1
- Initial build for ALT.

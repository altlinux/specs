%define _unpackaged_files_terminate_build 1

Name: jbr-api
Version: 1.12.0
Release: alt1

Summary: API for JetBrains Runtime extensions
License: Apache-2.0
Group: Development/Java
Url: https://github.com/JetBrains/JetBrainsRuntimeApi
VCS: https://github.com/JetBrains/JetBrainsRuntimeApi.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: generated-JBR.sha256

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java javapackages-local
BuildRequires: java-21-openjdk-devel

%description
Standalone interfaces for JetBrains Runtime features. Applications can compile
against these interfaces with a standard JDK and query feature availability
when running on JetBrains Runtime.

%prep
%setup

%build
# Keep the upstream generator, compiler plugin and multi-release JAR layout.
# Full mode uses the release API snapshot rather than overriding version checks.
bash tools/build.sh full %_jvmdir/java-21-openjdk
%mvn_artifact out/jbr-api-%version.pom out/jbr-api-%version.jar

%install
%mvn_install

%check
# Validate regenerated source against the IDE-pinned upstream source archive.
sha256sum -c %SOURCE1
test "$(cat out/version.txt)" = "%version"
# JBR-specific jtreg and graphical tests require the matching JBR runtime.

%files -f .mfiles
%doc LICENSE CONTRIBUTING.md

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 1.12.0-alt1
- Initial build for ALT.

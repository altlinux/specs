%define _unpackaged_files_terminate_build 1

Name: kotlinx-html
Version: 0.12.0
Release: alt1

Summary: Kotlin HTML builder DSL for the JVM
License: Apache-2.0
Group: Development/Java
URL: https://github.com/Kotlin/kotlinx.html
VCS: https://github.com/Kotlin/kotlinx.html.git

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-jvm.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: rpm-build-java-osgi
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlin-build-statistics
BuildRequires: kotlin-maven
BuildRequires: kotlin-tooling-core
BuildRequires: kotlin-stdlib
BuildRequires: kotlin-test
BuildRequires: junit

%description
Kotlin DSL for building HTML with JVM Writer, Appendable and DOM support.
This package provides the kotlinx-html-jvm library for JVM consumers.

%prep
%setup -q
%patch0 -p1
# Preserve the explicit generator sources without automatic buildSrc
# compilation.
# Checked-in common sources were verified against the pinned sources artifact.
mv buildSrc buildSrc.alt-generator
# Use system Gradle instead of the archived wrapper binary.
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete

%build
%gradle_publish \
    -x publishKotlinMultiplatformPublicationToMavenLocal

%install
%gradle_register --artifacts=kotlinx-html-jvm-
%gradle_install

%check
# Run common and JVM tests.
%gradle_check

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 0.12.0-alt1
- Initial build for ALT.

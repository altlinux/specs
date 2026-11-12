%define _unpackaged_files_terminate_build 1

Name: perfmark
Version: 0.27.0
Release: alt1

Summary: Low-overhead Java tracing library
License: Apache-2.0 AND BSD-3-Clause AND MIT AND GPL-2.0-only WITH Classpath-exception-2.0
Group: Development/Java
URL: https://www.perfmark.io/
VCS: https://github.com/perfmark/perfmark.git

BuildArch: noarch

Source0: %name-%version.tar
Source1: settings-alt.gradle
Source2: build-alt.gradle

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(com.google.errorprone:error_prone_annotations)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(org.openjdk.jmh:jmh-core)

%description
PerfMark records low-overhead tracing events. This package includes the API,
implementation, Java-specific backends, trace writer and HTML trace viewer.

%prep
%setup -q
cp %SOURCE1 settings.gradle
cp %SOURCE2 build.gradle
# Select the ALT Groovy settings file without deleting the original KTS.
mv settings.gradle.kts settings-upstream.gradle.kts
mkdir third-party-licenses
install -m644 \
    traceviewer/src/main/resources/io/perfmark/traceviewer/third_party/polymer/LICENSE \
    third-party-licenses/Polymer-LICENSE
install -m644 \
    traceviewer/src/main/resources/io/perfmark/traceviewer/third_party/catapult/LICENSE \
    third-party-licenses/Catapult-LICENSE

%build
%gradle_publish -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk

%install
%gradle_register --artifacts=perfmark-
%gradle_register_javadoc --artifacts=perfmark-
%gradle_install
cat .mfiles-javadoc >> .mfiles

%check
%gradle_check -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk test

%files -f .mfiles
%doc LICENSE NOTICE third-party-licenses

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 0.27.0-alt1
- Initial build for ALT.

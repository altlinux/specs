%define _unpackaged_files_terminate_build 1

Name: jediterm
Version: 3.76
Release: alt1

Summary: Terminal emulator core and Swing components for Java
License: LGPL-3.0-only or Apache-2.0
Group: Development/Java
URL: https://github.com/JetBrains/jediterm
VCS: https://github.com/JetBrains/jediterm.git
BuildArch: noarch

Source: %name-%version.tar
Patch: current-jvm.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-compiler
BuildRequires: kotlin-gradle-plugin
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: slf4j2
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.jetbrains.pty4j:pty4j)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.ibm.icu:icu4j)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: mvn(org.slf4j:slf4j-jdk14)

%description
JediTerm provides a terminal emulator, terminal buffers and Swing terminal
components. It implements escape sequences, Unicode text handling, terminal
input and rendering for Java applications.

%prep
%setup
%patch -p1

%build
%gradle_publish :JediTerm:classes --no-daemon \
    -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk \
    -Pkotlin.compiler.execution.strategy=in-process

%install
%gradle_register --artifacts=jediterm-core-,jediterm-ui-
%gradle_install

%check
%gradle_check --no-daemon \
    -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk \
    -Pkotlin.compiler.execution.strategy=in-process

%files -f .mfiles
%doc LICENSE-APACHE-2.0.txt LICENSE-LGPLv3.txt

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 3.76-alt1
- Initial build for ALT.

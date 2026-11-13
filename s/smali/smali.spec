%define _unpackaged_files_terminate_build 1

Name: smali
Version: 3.0.10
Release: alt1

Summary: Assembler, disassembler and library for Dalvik bytecode
License: BSD-2-Clause AND BSD-3-Clause AND Apache-2.0
Group: Development/Java
URL: https://github.com/google/smali
VCS: https://github.com/google/smali.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: system-gradle.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(org.jcommander:jcommander)
BuildRequires: mvn(org.antlr:antlr)
BuildRequires: mvn(org.antlr:antlr-runtime)
BuildRequires: mvn(org.antlr:stringtemplate)
BuildRequires: mvn(org.antlr:ST4)
BuildRequires: mvn(de.jflex:jflex)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.mockito:mockito-core)

%description
Smali and baksmali assemble and disassemble Android Dalvik bytecode.
Dexlib2 provides the complete bytecode model, reader and writer API.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for the Smali, Baksmali, Dexlib2 and utility libraries.

%prep
%setup
%autopatch -p1

%build
%gradle_publish -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk

%install
%gradle_register --artifacts=smali-
%gradle_register_javadoc --artifacts=smali-
%gradle_install

%check
%gradle_check -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk

%files -f .mfiles
%doc LICENSE third_party/NOTICE

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 10 2026 Ivan Khanas <xeno@altlinux.org> 3.0.10-alt1
- Initial build for ALT.

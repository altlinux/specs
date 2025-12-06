%define _unpackaged_files_terminate_build 1
%def_with check

Name: picocli
Version: 4.7.7
Release: alt1

Summary: Picocli is a modern Java cli framework
License: Apache-2.0
Group: Development/Java
Url: https://picocli.info
Vcs: https://github.com/remkop/picocli.git
BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-17-compat
BuildRequires: biz-aQute-bnd-gradle-plugins
BuildRequires: badass-jar-plugin
BuildRequires: system-rules
BuildRequires: jansi
BuildRequires: pragmatists-junitparams
BuildRequires: jline2
BuildRequires: hawtjni-runtime
%if_with check
BuildRequires: system-lambda
BuildRequires: junit5
%endif

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

%description
Picocli is a modern framework for building powerful, user-friendly,
GraalVM-enabled command line apps with ease. It supports colors,
autocompletion, subcommands, and more. In 1 source file so apps can include as
source & avoid adding a dependency. Written in Java, usable from Groovy,
Kotlin, Scala, etc.

%package shell-jline2
Summary: Picocli integration with JLine2 shell framework
Group: Development/Java
Requires: picocli = %EVR

%description shell-jline2
This module provides integration between picocli and JLine2, allowing you to
build interactive shells with features like tab-completion, command history,
and line editing. It includes the `picocli-shell-jline2` library which combines
picocli's command line parsing with JLine2's terminal capabilities.

%package codegen
Summary: Picocli annotation processor for code generation
Group: Development/Java
Requires: picocli = %EVR

%description codegen
This module provides the annotation processor for picocli, which generates
GraalVM native-image configuration files and other metadata at compile time.
It includes the `picocli-codegen` library used for automatic generation of
completion scripts, man pages, and GraalVM configuration for native
compilation.

%{?javadoc_package}

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register
%gradle_register_javadoc

%gradle_install

%check
%gradle_check -Dfile.encoding=UTF-8

%files
%_mavenmetadatadir/picocli.xml
%_javadir/picocli/picocli.jar
%_mavenpomdir/picocli/picocli.pom

%files shell-jline2
%_javadir/picocli/picocli-shell-jline2.jar
%_mavenpomdir/picocli/picocli-shell-jline2.pom

%files codegen
%_javadir/picocli/picocli-codegen.jar
%_mavenpomdir/picocli/picocli-codegen.pom

%changelog
* Wed Dec 03 2025 Ivan Khanas <xeno@altlinux.org> 4.7.7-alt1
- First build for ALT.


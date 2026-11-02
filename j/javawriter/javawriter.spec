%define _unpackaged_files_terminate_build 1

Name: javawriter
Version: 2.5.1
Release: alt2

Summary: Utility for generating Java source files
License: Apache-2.0
Group: Development/Java
Url: https://github.com/square/javawriter
VCS: https://github.com/square/javawriter.git

Source: %name-%version.tar
Source1: javawriter-toolchains.xml
Patch0: javawriter-use-system-assertj.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: sonatype-oss-parent
BuildRequires: maven-javadoc-plugin
BuildRequires: junit
BuildRequires: assertj-core

%description
JavaWriter is a utility for generating Java source files with consistent
indentation, imports, declarations and escaped string literals.

%package javadoc
Summary: API documentation for %name
Group: Development/Documentation
Requires: %name = %EVR

%description javadoc
API documentation for %name.

%prep
%setup -q
%autopatch -p1

# Use the distro Java8 compiler through Maven's normal toolchain support,
# preserving the original Java6 classfile target without environment selectors.
mkdir -p .mvn
cp -p %SOURCE1 .mvn/toolchains.xml
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration" "<jdkToolchain><version>[1.8,1.9)</version></jdkToolchain>"
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_dep org.easytesting:fest-assert-core
%pom_add_dep org.assertj:assertj-core:3.27.3:test
%mvn_package :javawriter %name

%build
%mvn_build -s -- --toolchains .mvn/toolchains.xml -Dmaven.javadoc.source=8 -Ddoclint=none

%install
%mvn_install
mkdir -p licenses
cp -p LICENSE.txt licenses/
if [ -d %buildroot%_javadocdir/%name/legal ]; then
    mv %buildroot%_javadocdir/%name/legal licenses/javadoc
    ln -s %_docdir/%name-%version/licenses/javadoc %buildroot%_javadocdir/%name/legal
fi

%files -f .mfiles-%name
%doc licenses

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 2.5.1-alt2
- Initial build for ALT.

%define _unpackaged_files_terminate_build 1

Name: asm-jdk-bridge
Version: 0.0.13
Release: alt1

Summary: A first approach to trial the JDK API for generation and reading of class files by adapting the ASM API
License: Apache-2.0
Group: Development/Java
Url: https://github.com/raphw/asm-jdk-bridge
Vcs: https://github.com/raphw/asm-jdk-bridge.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: jpackage-default

%description
A first approach to trial the JDK API for generation and reading of class files
by adapting the ASM API. This should serve as a first prof of concept by
plugging the reader/writer into existing ASM-based code without much change of
code. This also serves as an adapter concept for Byte Buddy where ASM is used
vastly.

In order to use the adapter, simply replace an instance of ASM's ClassReader or
ClassWriter with JdkClassReader or JdkClassWriter. The latter use the Class
File API internally, but expose equal APIs to ASM. If the availability of the
Class File API is unclear, ProbingClassReader and ProbingClassWriter can be
used, which will discover the underlying JVM and delegate to ASM or the Class
File API, depending on capability.

%prep
%setup
%pom_remove_parent

%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin asm-jdk-bridge

# We don't have java-24.
%pom_xpath_remove '//pom:execution[pom:id="java24-compile"]' asm-jdk-bridge
rm -rf asm-jdk-bridge/asm-jdk-bridge/src/main/java-24
%pom_disable_module asm-jdk-bridge-test

%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles

%changelog
* Thu Nov 13 2025 Ivan Khanas <xeno@altlinux.org> 0.0.13-alt1
- Fist build for ALT.

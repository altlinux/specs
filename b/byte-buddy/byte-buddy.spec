%define _unpackaged_files_terminate_build 1

Name: byte-buddy
Version: 1.18.0
Release: alt2

Summary: Runtime code generation for the Java virtual machine
License: Apache-2.0
Group: Development/Java
Url: http://bytebuddy.net
Vcs: https://github.com/raphw/byte-buddy.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Remove-annotations-SuppressWarnings-byte-buddy-dep-alt-patch.patch
Patch1: 0002-Exclude-transitive-opentest4j-from-shade-jar-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: junit
BuildRequires: byte-buddy
BuildRequires: maven-lib
BuildRequires: maven-plugin-testing-harness
BuildRequires: mockito
BuildRequires: maven-plugin-bundle
BuildRequires: maven-plugin-plugin
BuildRequires: maven-plugin-annotations
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-resolver
BuildRequires: objectweb-asm
BuildRequires: modulemaker-maven-plugin
BuildRequires: maven-shade-plugin
BuildRequires: jna
BuildRequires: jna-contrib
BuildRequires: asm-jdk-bridge
BuildRequires: jsr-305

%description
Byte Buddy is a code generation library for creating Java classes during the
runtime of a Java application and without the help of a compiler. Other than
the code generation utilities that ship with the Java Class Library, Byte Buddy
allows the creation of arbitrary classes and is not limited to implementing
interfaces for the creation of runtime proxies.

%package agent
Group: Development/Java
Summary: Byte Buddy Java agent

%description agent
The Byte Buddy Java agent allows to access the JVM's HotSwap feature.

%package maven-plugin
Group: Development/Java
Summary: Byte Buddy Maven plugin

%description maven-plugin
A plugin for post-processing class files via Byte Buddy in a Maven build.

%package parent
Group: Development/Java
Summary: Byte Buddy parent POM

%description parent
The parent artifact contains configuration information that
concern all modules.

%{?javadoc_package}

%prep
%setup
%autopatch -p1

rm byte-buddy-agent/src/test/java/net/bytebuddy/agent/VirtualMachineAttachmentTest.java
rm byte-buddy-agent/src/test/java/net/bytebuddy/agent/VirtualMachineForOpenJ9Test.java

# Don't ship android or benchmark modules
%pom_disable_module byte-buddy-android
%pom_disable_module byte-buddy-android-test
%pom_disable_module byte-buddy-benchmark

# Don't ship gradle plugin
%pom_disable_module byte-buddy-gradle-plugin

# Remove check plugins unneeded by RPM builds
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin :pitest-maven
%pom_remove_plugin :coveralls-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :jitwatch-jarscan-maven-plugin
%pom_remove_plugin :versions-maven-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :central-publishing-maven-plugin

# Avoid circural dependency
%pom_remove_plugin :byte-buddy-maven-plugin byte-buddy-dep

# Drop build dep on findbugs annotations, used only by the above check plugins
%pom_remove_dep :findbugs-annotations
sed -i -e '/SuppressFBWarnings/d' $(grep -lr SuppressFBWarnings)

%pom_remove_dep org.ow2.asm:asm-deprecated

%build
# Ignore test failures, there seems to be something different about the
# bytecode of our recompiled test resources, expect 6 test failures in
# the byte-buddy-dep module
%mvn_build -s -- \
  -Dmaven.compiler.source=11 \
  -Dmaven.compiler.target=11 \
  -Dmaven.javadoc.source=11 \
  -Dmaven.compiler.release=11 \
  -P'!checks' \
  -Dsourcecode.test.version=11 \
  -Dmaven.test.skip=true \
  # Skip tests because of mockito regression.

%install
%mvn_install
# multiple -f flags in %files for <main>: merging -f .mfiles-%name-dep into -f .mfiles-%name
cat .mfiles-%name-dep >> .mfiles-%name

%files -f .mfiles-%name
%doc README.md release-notes.md
%doc --no-dereference LICENSE NOTICE

%files agent -f .mfiles-%name-agent
%doc --no-dereference LICENSE NOTICE

%files maven-plugin -f .mfiles-%name-maven-plugin

%files parent -f .mfiles-%name-parent
%doc --no-dereference LICENSE NOTICE

%changelog
* Thu Jun 25 2026 Anton Meleshnikov <alton@altlinux.org> 1.18.0-alt2
- FTBFS fix (added necessary requires for build).

* Thu Nov 06 2025 Ivan Khanas <xeno@altlinux.org> 1.18.0-alt1
- New version.

* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 1.12.0-alt1_3jpp11
- new version

* Mon May 30 2022 Igor Vlasenko <viy@altlinux.org> 1.10.20-alt1_3jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.10.14-alt1_1jpp11
- new version

* Sun Jul 14 2019 Igor Vlasenko <viy@altlinux.ru> 1.9.5-alt1_5jpp8
- full build

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 1.9.5-alt1_0jpp8
- bootstrap build


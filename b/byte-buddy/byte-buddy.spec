%define _unpackaged_files_terminate_build 1
%define gradle_plugin_id net.bytebuddy.byte-buddy-gradle-plugin

Name: byte-buddy
Version: 1.18.17
Release: alt1

Summary: Runtime code generation for the Java virtual machine
License: Apache-2.0
Group: Development/Java
URL: http://bytebuddy.net
VCS: https://github.com/raphw/byte-buddy.git

BuildArch: noarch

Source0: %name-%version.tar
Source1: fix-shaded-metadata.py
Patch0: 0001-Remove-annotations-SuppressWarnings-byte-buddy-dep-alt-patch.patch
Patch1: 0002-Exclude-transitive-opentest4j-from-shade-jar-alt-patch.patch
Patch2: 0003-module-main-class-internal-name.patch
Patch3: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: maven-local
BuildRequires: python3
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: junit
BuildRequires: byte-buddy
BuildRequires: byte-buddy-maven-plugin
BuildRequires: jarjar-pantsbuild
BuildRequires: objenesis
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

%package gradle-plugin
Group: Development/Java
Summary: Byte Buddy JVM Gradle plugin

%description gradle-plugin
Gradle integration for enhancing Java and Kotlin JVM classes with Byte Buddy.

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

# Don't ship android or benchmark modules
%pom_disable_module byte-buddy-android
%pom_disable_module byte-buddy-android-test
%pom_disable_module byte-buddy-benchmark

# Build the JVM Gradle plugin below with the system Gradle.
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

# Use the installed plugin to generate the upstream equals/hashCode and cache
# methods.

# Drop build dep on findbugs annotations, used only by the above check plugins
%pom_remove_dep :findbugs-annotations
sed -i -e '/SuppressFBWarnings/d' $(grep -lr SuppressFBWarnings)

%pom_remove_dep org.ow2.asm:asm-deprecated

# Mockito is built against shaded ASM, whereas byte-buddy-dep exposes ordinary
# ASM types. Remap only the build-time test copy, retaining system
# ASM/Objenesis.
mkdir -p target
printf 'rule net.bytebuddy.jar.asm.** org.objectweb.asm.@1\n' \
  > target/mockito.rules
java -cp \
  "%{_javadir}/jarjar-pantsbuild/jarjar.jar:%{_javadir}/objectweb-asm/*" \
  org.pantsbuild.jarjar.Main process target/mockito.rules \
  %{_javadir}/mockito/mockito-core.jar target/mockito-unshaded.jar
# Compile against the system Mockito API, and replace its runtime JAR only in
# Surefire. Keep ordinary test scope so XMvn installs valid published POMs.
%pom_add_plugin org.apache.maven.plugins:maven-surefire-plugin byte-buddy-dep \
  '<configuration>
     <classpathDependencyExcludes>
       <classpathDependencyExclude>
         org.mockito:mockito-core
       </classpathDependencyExclude>
     </classpathDependencyExcludes>
     <additionalClasspathElements>
       <additionalClasspathElement>
         ${project.basedir}/../target/mockito-unshaded.jar
       </additionalClasspathElement>
     </additionalClasspathElements>
   </configuration>'
%pom_add_dep org.objenesis:objenesis::test byte-buddy-dep
mock_maker=org.mockito.plugins.MockMaker
mkdir -p byte-buddy-dep/src/test/resources/mockito-extensions
printf 'mock-maker-subclass\n' \
  > byte-buddy-dep/src/test/resources/mockito-extensions/$mock_maker
# This suite targets Mockito 2 subclass semantics, without inline agent
# attachment.
mkdir -p byte-buddy-maven-plugin/src/test/resources/mockito-extensions
printf 'mock-maker-subclass\n' \
  > byte-buddy-maven-plugin/src/test/resources/mockito-extensions/$mock_maker

%pom_xpath_inject \
  "pom:profile[pom:id='shade-current']
   //pom:execution[pom:goals/pom:goal='shade']
   /pom:configuration" \
  "<artifactSet>
     <includes>
       <include>net.bytebuddy:byte-buddy-dep</include>
       <include>codes.rafael.asmjdkbridge:asm-jdk-bridge</include>
       <include>org.ow2.asm:*</include>
     </includes>
   </artifactSet>" \
  byte-buddy

%build
%mvn_build -s -- \
  -Dmaven.compiler.source=11 \
  -Dmaven.compiler.target=11 \
  -Dmaven.javadoc.source=11 \
  -Dmaven.compiler.release=11 \
  -P'!checks' \
  -Dsourcecode.test.version=11 \
  -Dbytecode.test.version=11

# XMvn snapshots reactor dependencies before Shade writes its reduced POM.
# The shaded artifact contains byte-buddy-dep already; do not expose it twice.
python3 %SOURCE1

pushd byte-buddy-gradle-plugin
%gradle_publish --dependency-verification=off --no-daemon --max-workers=4
popd

%install
%mvn_install
if [ -d %buildroot%_javadocdir/%name/legal ]; then
    mv %buildroot%_javadocdir/%name/legal javadoc-legal
    legal_target=$(realpath -m --relative-to="%_javadocdir/%name" \
        "%_defaultdocdir/%name-%version/javadoc-legal")
    ln -s "$legal_target" %buildroot%_javadocdir/%name/legal
fi
# multiple -f flags in %files for <main>: merging -f .mfiles-%name-dep into -f
# .mfiles-%name
cat .mfiles-%name-dep >> .mfiles-%name

pushd byte-buddy-gradle-plugin
%gradle_register --artifacts=byte-buddy-gradle-plugin-
marker_base=%_mavenrepolocal/repository/net/bytebuddy/%name-gradle-plugin
marker_id=%gradle_plugin_id.gradle.plugin
marker_dir="$marker_base/$marker_id/%version-jdk5"
%mvn_artifact "$marker_dir/$marker_id-%version-jdk5.pom"
%mvn_package net.bytebuddy:byte-buddy-gradle-plugin gradle-plugin
%mvn_package \
  %gradle_plugin_id:%gradle_plugin_id.gradle.plugin \
  gradle-plugin
%mvn_file net.bytebuddy:byte-buddy-gradle-plugin %name/gradle-plugin
%mvn_file \
  %gradle_plugin_id:%gradle_plugin_id.gradle.plugin \
  %name/gradle-plugin-marker
%gradle_install
popd

%check
pushd byte-buddy-gradle-plugin
%gradle_check --dependency-verification=off --no-daemon --max-workers=4
popd

%files -f .mfiles-%name
%doc release-notes.md javadoc-legal
%doc --no-dereference LICENSE NOTICE

%files agent -f .mfiles-%name-agent

%files maven-plugin -f .mfiles-%name-maven-plugin

%files gradle-plugin -f byte-buddy-gradle-plugin/.mfiles-gradle-plugin

%files parent -f .mfiles-%name-parent

%changelog
* Tue Nov 03 2026 Ivan Khanas <xeno@altlinux.org> 1.18.17-alt1
- New version.

* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 1.18.16-alt2
- Align shaded artifact XMvn dependencies with its reduced POM.

* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 1.18.16-alt1
- New version.
- Encode the module main class as an internal name for modulemaker 1.9.
- Enable unit tests.

* Thu Aug 27 2026 Evgeniy Serov <scala@altlinux.org> 1.18.8-alt1
- Automatically updated to 1.18.8.
- Excluded test dependencies from the shaded JAR.

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


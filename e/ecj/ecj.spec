%define _unpackaged_files_terminate_build 1
%define ecj_version 3.46.100
%define annotation_version 2.4.100
%define batch_src org.eclipse.jdt.core.compiler.batch/src
%define ecj_main org.eclipse.jdt.internal.compiler.batch.Main

# The legacy OSGi scanner misreads standard 72-byte manifest wrapping.
%filter_from_provides /^osgi(org[.]ecli)$/d

Name: ecj
Epoch: 1
Version: 4.41
Release: alt1

Summary: Eclipse Compiler for Java
License: EPL-2.0
Group: Development/Java
URL: https://www.eclipse.org/jdt/
VCS: https://github.com/eclipse-jdt/eclipse.jdt.core.git

Source0: %name-%version.tar
Source1: ecj-gcj.tar.bz2
Source2: ecj-%ecj_version.pom
Source3: org.eclipse.jdt.annotation-%annotation_version.pom
Source4: rpm-build.xml
Source5: EcjRuntimeSmoke.java
Source6: CompilerConsumer.java
Source7: ChecksSmoke.java
Source8: DebugInfoInput.java
Patch0: ecj-force-debug-info.patch
Patch1: eclipse-gcj-nodummysymbol.patch
Patch2: ecj-gcj-for-current-api.patch
Patch3: ecj-gcj-java8.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: rpm-build-java-osgi
BuildRequires: java-21-openjdk-devel
BuildRequires: ant

%description
ECJ is the Java compiler of the Eclipse Platform. It provides the JDT Core
batch compiler, Java compiler tool API, annotation processing and Ant adapter.

%package -n eclipse-jdt-annotations
Version: %annotation_version
Summary: Eclipse JDT nullness and ownership annotations
Group: Development/Java

%description -n eclipse-jdt-annotations
The JDT annotations describe nullness and ownership contracts in Java source
and class files. The bundle also provides the Checks utility.

%javadoc_package

%prep
%setup -q -a1
%autopatch -p1
cp %SOURCE4 rpm-build.xml
# Preserve the existing ALT GCJ adapter with the current compiler API.
cp eclipse-gcj/org/eclipse/jdt/internal/compiler/batch/GCCMain.java \
    %batch_src/org/eclipse/jdt/internal/compiler/batch/
cat eclipse-gcj/gcc.properties >> \
    %batch_src/org/eclipse/jdt/internal/compiler/batch/messages.properties
# Retain the genuine legacy compiler coordinate used by Tomcat.
%mvn_alias org.eclipse.jdt:ecj org.eclipse.jdt.core.compiler:ecj
%mvn_file org.eclipse.jdt:ecj ecj/ecj
%mvn_file org.eclipse.jdt:org.eclipse.jdt.annotation eclipse-jdt-annotations
# Classifier mappings precede the broader annotation bundle mapping.
%mvn_package org.eclipse.jdt:ecj:jar:javadoc:%ecj_version javadoc
%mvn_package :org.eclipse.jdt.annotation:jar:javadoc:%annotation_version \
    javadoc
%mvn_package org.eclipse.jdt:org.eclipse.jdt.annotation annotations

%build
# The original javax23api.jar is a compile-only upstream API compatibility
# input. It is not copied into either runtime JAR or its classpath.
%ant -f rpm-build.xml -Dant.jar=%_javadir/ant/ant.jar \
    -Decj.version=%ecj_version -Dannotations.version=%annotation_version

%install
%mvn_artifact %SOURCE2 build/ecj.jar
%mvn_artifact %SOURCE3 build/annotations.jar
%mvn_artifact org.eclipse.jdt:ecj:jar:javadoc:%ecj_version \
    build/ecj-javadoc.jar
%mvn_artifact \
    org.eclipse.jdt:org.eclipse.jdt.annotation:jar:javadoc:%annotation_version \
    build/annotations-javadoc.jar
%mvn_install
%jpackage_script %ecj_main '' '' ecj ecj true
install -Dpm644 org.eclipse.jdt.core/scripts/ecj.1 \
    %buildroot%_mandir/man1/ecj.1

%check
mkdir -p build/runtime-smoke build/compiled-consumer build/debug-info
mkdir -p build/default-cli
javac --release 17 -cp build/ecj.jar -d build/runtime-smoke %SOURCE5
java -cp build/ecj.jar:build/runtime-smoke EcjRuntimeSmoke \
    %SOURCE6 build/compiled-consumer
java -cp build/compiled-consumer CompilerConsumer
java -cp build/compiled-consumer LegacyCompilerConsumer
# An ordinary invocation keeps upstream's Java 8 default on the Java 21 host.
java -cp build/ecj.jar org.eclipse.jdt.internal.compiler.batch.Main \
    -d build/default-cli build/compiled-consumer/LegacyCompilerConsumer.java
java -cp build/default-cli LegacyCompilerConsumer
javap -v build/default-cli/LegacyCompilerConsumer.class > build/default-cli.txt
grep -q 'major version: 52' build/default-cli.txt
javac --release 8 -cp build/annotations.jar -d build/runtime-smoke %SOURCE7
java -cp build/annotations.jar:build/runtime-smoke ChecksSmoke
java -cp build/ecj.jar org.eclipse.jdt.internal.compiler.batch.Main \
    -version > build/compiler-version.txt
grep -Fq '%ecj_version' build/compiler-version.txt
# The retained ALT patch forces complete debug information for RPM builds.
java -cp build/ecj.jar org.eclipse.jdt.internal.compiler.batch.Main \
    -g:none --release 17 -d build/debug-info %SOURCE8
javap -v build/debug-info/DebugInfoInput.class > build/debug-info.txt
grep -q LocalVariableTable build/debug-info.txt
grep -q LineNumberTable build/debug-info.txt
grep -q SourceFile build/debug-info.txt

%files -f .mfiles
%doc LICENSE NOTICE org.eclipse.jdt.annotation/about.html
%_bindir/ecj
%_mandir/man1/ecj.1*

%files -n eclipse-jdt-annotations -f .mfiles-annotations

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 1:4.41-alt1
- New version.
- Build the JDT annotations as a binary subpackage.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1:4.23-alt1_3jpp11
- new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1:4.22-alt1_3jpp11
- new version

* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 1:4.21-alt1_1jpp11
- new version

* Fri Jul 02 2021 Igor Vlasenko <viy@altlinux.org> 1:4.19-alt2_1jpp11
- added BR: unzip

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:4.19-alt1_1jpp11
- new version

* Sun Jun 06 2021 Igor Vlasenko <viy@altlinux.org> 1:4.16-alt2_4jpp11
- removed compat symlink for gradle

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1:4.16-alt1_4jpp11
- new version

* Mon May 10 2021 Igor Vlasenko <viy@altlinux.org> 1:4.14-alt1_3jpp11
- new version

* Sun Oct 11 2020 Igor Vlasenko <viy@altlinux.ru> 1:4.12-alt1_2jpp8
- new version

* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.11-alt1_0.1jpp9
- rebuild with java 9

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.11-alt1_0.1jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:4.7.3a-alt1_1jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.7.1-alt1_1jpp8
- new version

* Mon Nov 28 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.2-alt2_3jpp8
- merged eclipse-gcj code && native by glebfm@

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.2-alt1_3jpp8
- new version

* Wed Feb 03 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:4.5.1-alt2_1jpp8
- Reenabled eclipse-gcj code.
- Updated eclipse-gcj to CVS 2013-12-11.
- Restored native subpackage.

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.1-alt1_1jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.2.1-alt1_7jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt5_7jpp6.qa1
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1:3.4.2-alt4_7jpp6.qa1
- NMU: rebuilt for debuginfo.

* Thu Aug 19 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt4_7jpp6
- removed Req: java-gcj-compat (closes: #23902)

* Thu Aug 19 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt3_7jpp6
- BR:java-gcj-compat reduced to fastjar (#23902)

* Sat Feb 20 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt2_7jpp6
- removed poms as it breaks too much builds

* Tue Jan 26 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt1_7jpp6
- replaces ecj-standalone


%def_without check

Name: gluegen
Version: 2.6.0
Release: alt1
Epoch: 1
%global src_name gluegen-v%{version}
Summary: Java/JNI glue code generator to call out to ANSI C

License: BSD
Group: Development/Java
URL: https://github.com/sgothel/gluegen
VCS: https://github.com/sgothel/gluegen

Source0: %name-%version.tar
Source1: jcpp.tar

Patch0: disable-static-linking.patch
Patch1: cc-attributes-in-build.patch
Patch2: jcpp-remove-javax-api.patch
Patch3: alt-system-japicmp.patch
Patch4: alt-disable-tests-build-and-release-archive.patch
Patch5: alt-disable-archive-7z.patch
Patch6: use-system-jni.patch

ExcludeArch: armh %ix86

BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
BuildRequires: jpackage-utils
BuildRequires: ant-antlr
BuildRequires: ant-contrib
BuildRequires: ant-junit
BuildRequires: cpptasks
BuildRequires: maven-local
BuildRequires: japicmp

Provides: gluegen2 = %EVR
Obsoletes: gluegen2 < %EVR
Requires: jpackage-utils

%filter_from_requires /profile.ant/d
%filter_from_requires /android-tools/d
%filter_from_requires /scp/d

%description
GlueGen is a tool which automatically generates the Java and JNI
code necessary to call C libraries. It reads as input ANSI C header
files and separate configuration files which provide control over
many aspects of the glue code generation. GlueGen uses a complete
ANSI C parser and an internal representation (IR) capable of
representing all C types to represent the APIs for which it
generates interfaces.

%package devel
Group: Development/Other
Summary: GlueGen devel utilities required to build JOGL
Provides: gluegen2-devel = %EVR
Obsoletes: gluegen2-devel < %EVR

Requires: %{name} = %{version}-%{release}
Requires: ant-antlr
Requires: ant-contrib
Requires: ant-junit
Requires: cpptasks

%description devel
GlueGen devel utilities provide some ant targets and shared files to build
application.

%package javadoc
Group: Development/Java
Summary: Javadoc for GlueGen
Provides: gluegen2-javadoc = %EVR
Obsoletes: gluegen2-javadoc < %EVR

%description javadoc
Javadoc for GlueGen.

%package doc
Group: Development/Java
Summary: GlueGen's user manual
Provides: gluegen2-doc = %EVR
Obsoletes: gluegen2-doc < %EVR

%description doc
GlueGen's user manual.

%prep
%setup -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
sed -e "s|%%{_libdir}|%{_libdir}|;s|%%{name}|%{name}|" %{PATCH6} \
    >use-system-jni.patch
/usr/bin/patch -s -p1 --fuzz=0 <use-system-jni.patch

# Remove bundled dependencies
find -name "*.jar" -type f -exec rm {} \;
find -name "*.apk" -type f -exec rm {} \;
rm -fr make/lib

# Fix wrong-script-end-of-line-encoding
rm make/scripts/*.bat

# Fix non-executable-script
find make/scripts -type f -name "*.sh" -exec chmod +x {} +

# Fix script-without-shebang
find make/scripts -type f -name "*.sh" -exec sed -i -e '1i#!/bin/sh' {} +

%build

cd make
ant \
 -verbose \
 -Dc.compiler.debug=true \
 -Djavacdebug=false \
%ifarch x86_64
 -Djavac.memorymax=1024m \
%else
 -Djavac.memorymax=256m \
%endif
 -Dtarget.sourcelevel=1.8 \
 -Dtarget.targetlevel=1.8 \
 -Dantlr.jar=%{_javadir}/antlr.jar \
 -Djunit.jar=%{_javadir}/junit.jar \
 -Dant.jar=%{_javadir}/ant.jar \
 -Dant-junit.jar=%{_javadir}/ant/ant-junit.jar \
 -Djavadoc.link=%{_javadocdir}/java \
 all \
 javadoc \
 maven.install

%install
mkdir -p %{buildroot}%{_javadir}/%{name} \
    %{buildroot}%{_libdir}/%{name} \
    %{buildroot}%{_jnidir}

install build/gluegen.jar %{buildroot}%{_javadir}/%{name}.jar
install build/gluegen-rt.jar %{buildroot}%{_jnidir}/%{name}-rt.jar
ln -s ../../..%{_jnidir}/%{name}-rt.jar %{buildroot}%{_libdir}/%{name}/
install build/obj/libgluegen_rt.so %{buildroot}%{_libdir}/%{name}/lib%{name}_rt.so

# Provide JPP pom
mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 build/pom-gluegen.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 build/pom-gluegen-rt.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-rt.pom

# Make the devel package. This package is needed to build JOGL2
%global gluegen_devel_dir %{_datadir}/gluegen
%global inst_srcdir %{buildroot}%{gluegen_devel_dir}
mkdir -p %{inst_srcdir} %{inst_srcdir}/build
cp -rdf -t %{inst_srcdir} make
cp build/artifact.properties %{inst_srcdir}/build/artifact.properties

# Make the javadoc package
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rdf build/javadoc/gluegen/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# Make the doc package
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -rdf doc/manual/* %{buildroot}%{_docdir}/%{name}
cp LICENSE.txt %{buildroot}%{_docdir}/%{name}/
cp LICENSE.txt %{buildroot}%{_javadocdir}/%{name}/

%check
cd make
_JAVA_OPTIONS="-Djogamp.debug=true -Djava.library.path=../build/test/build/natives" xargs -t ant <<EOF
 -verbose
 -Djavacdebug=true
 -Dc.compiler.debug=true
 -Djavacdebuglevel=lines,vars,source
 -Dcommon.gluegen.build.done=true
 -Dtarget.sourcelevel=1.8
 -Dtarget.targetlevel=1.8
 -Dantlr.jar=%{_javadir}/antlr.jar
 -Djunit.jar=%{_javadir}/junit.jar
 -Dant.jar=%{_javadir}/ant.jar
 -Dant-junit.jar=%{_javadir}/ant/ant-junit.jar
 -Dgluegen.jar=%{buildroot}%{_javadir}/%{name}.jar
 -Dgluegen-rt.jar=%{buildroot}%{_libdir}/%{name}/%{name}-rt.jar
 -Dswt.jar=%{_libdir}/eclipse/swt.jar

 junit.run
EOF

rm -fr %{buildroot}%{_jnidir}/test

%files
%doc LICENSE.txt
%{_jnidir}/%{name}-rt.jar
%{_libdir}/%{name}
%{_mavenpomdir}/JPP-%{name}-rt.pom

%files devel
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{gluegen_devel_dir}

%files javadoc
%exclude %{_docdir}/%{name}/LICENSE.txt
%{_javadocdir}/%{name}

%files doc
%{_docdir}/%{name}

%changelog
* Fri Jun 12 2026 Andrey Cherepanov <cas@altlinux.org> 1:2.6.0-alt1
- New version.
- Built from upstream Git https://github.com/sgothel/gluegen.
- Renamed to gluegen.
- Removed autorequirements of android-tools and scp (ALT #49642).

* Wed Jun 10 2026 Arseniy Kostevich <faux@altlinux.org> 2.5.0-alt2
- fixed runtime native library loading from %%_libdir/gluegen2
- installed native library as libgluegen2_rt.so to match Java loader name (Closes: #59491)

* Sat Feb 22 2025 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- new version

* Sat Nov 27 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt3_11jpp8.gitg0b441cfc
- build from upstream/master

* Tue Apr 20 2021 Slava Aseev <ptrnine@altlinux.org> 2.3.2-alt2_11jpp8
- fix build with gcc-10 (-fno-common)

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_11jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_10jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_7jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_5jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_4jpp8
- new version

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt2_3jpp8
- %%_jnidir set to /usr/lib/java

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_1jpp7
- new release

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_8jpp7
- build with ant-junit

* Thu Jul 24 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_7jpp7
- merged junit-junit4

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_7jpp7
- fixed build with new junit

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_7jpp7
- new release

* Tue Jan 15 2013 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_6jpp7
- initial build

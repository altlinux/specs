# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /.opt-share.etc.profile.ant/d
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           gluegen2
Version:        2.3.2
Release:        alt1_4jpp8
%global src_name gluegen-v%{version}
Summary:        Java/JNI glue code generator to call out to ANSI C

Group:          Development/Other
License:        BSD
URL:            http://jogamp.org/
Source0:        http://jogamp.org/deployment/v%{version}/archive/Sources/%{src_name}.tar.xz
Source1:        http://jogamp.org/deployment/v%{version}/archive/Sources/jcpp-v%{version}.tar.xz
Patch1:         %{name}-0001-renamed-library.patch
# gluegen2.spec: W: patch-not-applied Patch2: 0002-use-fedora-jni.patch
#                Applied with %%{_libdir} and %%{name} resolved
Patch2:         %{name}-0002-use-fedora-jni.patch
Patch3:         %{name}-0003-disable-executable-tmp-tests.patch
Patch4:         %{name}-0004-add-antlr-jar-to-all-targets.patch
Patch5:         %{name}-0005-use-system-antlib.patch
Patch6:         %{name}-0006-disable-static-libgcc.patch
Patch7:         %{name}-0007-add-ppc64-aarch64.patch
Patch8:         %{name}-0008-jcpp-remove-javax-api.patch

BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  ant-antlr
BuildRequires:  ant-contrib
BuildRequires:  ant-junit
BuildRequires:  cpptasks
BuildRequires:  maven-local

Requires:       jpackage-utils
Source44: import.info

%description
GlueGen is a tool which automatically generates the Java and JNI
code necessary to call C libraries. It reads as input ANSI C header
files and separate configuration files which provide control over
many aspects of the glue code generation. GlueGen uses a complete
ANSI C parser and an internal representation (IR) capable of
representing all C types to represent the APIs for which it
generates interfaces.

%package devel
Summary:        GlueGen2 devel utilities required to build JOGL2
Group:          Development/Other
BuildArch:      noarch

Requires:       %{name} = %{version}
Requires:       ant-antlr
Requires:       ant-contrib
Requires:       ant-junit
Requires:       cpptasks

%description devel
GlueGen devel utilities provide some ant targets and shared files to build
application.

%package javadoc
Summary:        Javadoc for GlueGen2
Group:          Development/Java
BuildArch:      noarch

%description javadoc
Javadoc for GlueGen2.

%package doc
Summary:        GlueGen's user manual
Group:          Development/Java
BuildArch:      noarch

%description doc
GlueGen's user manual.

%prep
%setup -n %{src_name}
tar -xJf %{SOURCE1} -C jcpp --strip 1

%patch1 -p1
sed -e "s|%%{_libdir}|%{_libdir}|;s|%%{name}|%{name}|" %{PATCH2} \
    >use-fedora-jni.patch
/usr/bin/patch -s -p1 --fuzz=0 <use-fedora-jni.patch
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

# Remove bundled dependencies
find -name "*.jar" -type f -exec rm {} \;
find -name "*.apk" -type f -exec rm {} \;
rm -fr make/lib

# Fix wrong-script-end-of-line-encoding
rm make/scripts/*.bat

# Fix spurious-executable-perm
chmod -x LICENSE.txt
chmod -x doc/manual/index.html
chmod -x src/native/*/*
find src/java/ -type f -exec chmod -x {} +
find make/scripts -type f -not -name "*.sh" -exec chmod -x {} +

# Fix non-executable-script
find make/scripts -type f -name "*.sh" -exec chmod +x {} +

# Fix script-without-shebang
find make/scripts -type f -name "*.sh" -exec sed -i -e '1i#!/bin/sh' {} +

# Remove hardcoded classpath
sed -i '/Class-Path/I d' make/Manifest

# git executable should not be used, use true (to avoid checkout) instead
sed -i 's/executable="git"/executable="true"/' make/build.xml

# 7z executable is not provided, use true (to avoid archive) instead
sed -i 's/executable="7z"/executable="true"/' make/jogamp-archivetasks.xml

# mvn executable should not be used, use true (to avoid install) instead
sed -i 's/executable="mvn"/executable="true"/' make/build.xml

%build

# Clean up some tests
rm -f src/junit/com/jogamp/common/util/TestVersionSemantics.java src/junit/com/jogamp/junit/util/VersionSemanticsUtil.java

cd make
xargs -t ant <<EOF
 -verbose
 -Dc.compiler.debug=true
 -Djavacdebug=false
%ifarch x86_64
 -Djavac.memorymax=1024m
%else
 -Djavac.memorymax=256m
%endif

 -Dantlr.jar=%{_javadir}/antlr.jar
 -Djunit.jar=%{_javadir}/junit.jar
 -Dant.jar=%{_javadir}/ant.jar
 -Dant-junit.jar=%{_javadir}/ant/ant-junit.jar

 -Djavadoc.link=%{_javadocdir}/java

 all
 javadoc
 maven.install
EOF

%install
mkdir -p %{buildroot}%{_javadir}/%{name} \
    %{buildroot}%{_libdir}/%{name} \
    %{buildroot}%{_jnidir}

install build/gluegen.jar %{buildroot}%{_javadir}/%{name}.jar
install build/gluegen-rt.jar %{buildroot}%{_jnidir}/%{name}-rt.jar
ln -s ../../..%{_jnidir}/%{name}-rt.jar %{buildroot}%{_libdir}/%{name}/
install build/obj/libgluegen-rt.so %{buildroot}%{_libdir}/%{name}/lib%{name}-rt.so

# Provide JPP pom
mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 build/pom-gluegen.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 build/pom-gluegen-rt.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-rt.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap JPP-%{name}-rt.pom %{name}-rt.jar

# Make the devel package. This package is needed to build JOGL2
%global gluegen_devel_dir %{_datadir}/gluegen2
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
%{_docdir}/%{name}/LICENSE.txt
%{_jnidir}/%{name}-rt.jar
%{_libdir}/%{name}
%{_mavenpomdir}/JPP-%{name}-rt.pom

%files devel
%{_docdir}/%{name}/LICENSE.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_datadir}/maven-metadata/%{name}.xml
%{gluegen_devel_dir}

%files javadoc
%{_javadocdir}/%{name}

%files doc
%{_docdir}/%{name}

%changelog
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


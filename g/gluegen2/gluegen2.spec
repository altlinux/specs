# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /.opt-share.etc.profile.ant/d
BuildRequires: /proc
BuildRequires: jpackage-compat
# baserelease defines which build revision of this version we're building.
# The magical name baserelease is matched by the rpmdev-bumpspec tool, which
# you should use.
%global baserelease 7

%global pkg_name gluegen
%global pkg_version 2.0
%global pkg_rc rc11

%if 0%{?pkg_rc:1}
%global pkg_release 0.%{baserelease}.%{pkg_rc}
%global src_name %{pkg_name}-v%{pkg_version}-%{pkg_rc}
%else
%global pkg_release %{baserelease}
%global src_name %{pkg_name}-v%{pkg_version}
%endif

Name:           gluegen2
Version:        %{pkg_version}
Release:        alt1_7jpp7
Summary:        Java/JNI glue code generator to call out to ANSI C

Group:          Development/Java
License:        BSD
URL:            http://jogamp.org/
Source0:        http://jogamp.org/deployment/jogamp-current/archive/Sources/%{src_name}.tar.7z
Patch1:         %{name}-0001-renamed-library.patch
# gluegen2.spec: W: patch-not-applied Patch2: 0002-use-fedora-jni.patch
#                Applied with %%{_libdir} and %%{name} resolved
Patch2:         %{name}-0002-use-fedora-jni.patch
Patch3:         %{name}-0003-disable-executable-tmp-tests.patch

BuildRequires:  jpackage-utils
BuildRequires: p7zip-standalone p7zip
BuildRequires:  ant-antlr
BuildRequires:  ant-contrib
BuildRequires:  ant-junit4
BuildRequires:  cpptasks
BuildRequires:  maven

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
Group:          Development/Java
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
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

Requires:       jpackage-utils

%description javadoc
Javadoc for GlueGen2.

%package doc
Summary:        GlueGen's user manual
Group:          Development/Java
BuildArch:      noarch

%description doc
GlueGen's user manual.

%prep
# inline %%setup as 7z archive are not supported
%setup -c -T -n %{src_name}
cd ..
7za e -y %{SOURCE0}
tar -xf %{src_name}.tar
rm %{src_name}.tar
cd %{src_name}
chmod -Rf a+rX,u+w,g-w,o-w .

%patch1 -p1
sed -e "s|%%{_libdir}|%{_libdir}|;s|%%{name}|%{name}|" %{PATCH2} \
    >use-fedora-jni.patch
/usr/bin/patch -s -p1 --fuzz=0 <use-fedora-jni.patch
%patch3 -p1

# Fix wrong-script-end-of-line-encoding
rm make/scripts/*.bat

# Fix spurious-executable-perm
chmod -x LICENSE.txt
chmod -x doc/manual/index.html
chmod -x make/stub_includes/*/*
chmod -x src/native/*/*
find src/java/ -type f -exec chmod -x {} +
find make/ -type f -exec chmod -x {} +

# Fix non-executable-script
chmod +x make/scripts/*.sh

# Fix script-without-shebang
sed -i -e '1i#!/bin/sh' make/scripts/*.sh

# Remove bundled dependencies
find -name "*.jar" -type f -exec rm {} \;
find -name "*.apk" -type f -exec rm {} \;
rm -fr make/lib

# Remove hardcoded classpath
sed -i '/Class-Path/I d' make/Manifest

# git executable should not be used, use true (to avoid checkout) instead
sed -i 's/executable="git"/executable="true"/' make/build.xml

# 7z executable is not provided, use true (to avoid archive) instead
sed -i 's/executable="7z"/executable="true"/' make/jogamp-archivetasks.xml

# mvn executable should not be used, use true (to avoid install) instead
sed -i 's/executable="mvn"/executable="true"/' make/build.xml

%build
cd make
ant -Djavacdebug=true \
    -Djavacdebuglevel=lines,vars,source \
    -Dc.compiler.debug=true \
    \
    -Dantlr.jar=%{_javadir}/antlr.jar \
    -Djunit.jar=%{_javadir}/junit4.jar \
    -Dant.jar=%{_javadir}/ant.jar \
    -Dant-junit.jar=%{_javadir}/ant/ant-junit4.jar \
    \
    -Djavadoc.link=%{_javadocdir}/java \
    \
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

%check
cd make
_JAVA_OPTIONS="-Djogamp.debug=true -Djava.library.path=../build/test/build/natives" ant -Djavacdebug=true \
    -Dc.compiler.debug=true \
    -Djavacdebug=true \
    -Djavacdebuglevel=lines,vars,source \
    -Dcommon.gluegen.build.done=true \
    \
    -Dantlr.jar=%{_javadir}/antlr.jar \
    -Djunit.jar=%{_javadir}/junit.jar \
    -Dant.jar=%{_javadir}/ant.jar \
    -Dant-junit.jar=%{_javadir}/ant/ant-junit.jar \
    -Dgluegen.jar=%{buildroot}%{_javadir}/%{name}.jar \
    -Dgluegen-rt.jar=%{buildroot}%{_libdir}/%{name}/%{name}-rt.jar \
    -Dswt.jar=%{_libdir}/eclipse/swt.jar \
    \
    junit.run

%files
%doc LICENSE.txt
%{_jnidir}/%{name}-rt.jar
%{_libdir}/%{name}
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}-rt.pom

%files devel
%doc LICENSE.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{gluegen_devel_dir}

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%files doc
%doc LICENSE.txt
%{_docdir}/%{name}

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_7jpp7
- new release

* Tue Jan 15 2013 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_6jpp7
- initial build


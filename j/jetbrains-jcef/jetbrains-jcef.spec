%define _unpackaged_files_terminate_build 1
%define _cmake__builddir jcef_build
%define upstream_rev 9036bb1727ab5e1b8108ba3a90326ce3dfc463a8
%define upstream_count 1235
%define jcef_revision 263-b18
%define jcef_api 1.21
%define cef_root %_datadir/cef
%define jcef_libdir %_libdir/%name
%define jcef_maven_base %version-g7c1aa68-chromium-150.0.7871.129
%define jcef_maven_version %jcef_maven_base-api-%jcef_api-%jcef_revision

Name: jetbrains-jcef
Version: 150.0.14
Release: alt1

Summary: JetBrains Java bindings for Chromium Embedded Framework
License: BSD-3-Clause AND Apache-2.0
Group: Development/Java
URL: https://github.com/JetBrains/jcef
VCS: https://github.com/JetBrains/jcef.git

Source0: %name-%version.tar
Source1: jetbrains-jcef-check.sh
Source2: thrift-NOTICE
Patch0: jetbrains-jcef-system.patch
ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-java
BuildRequires(pre): rpm-macros-python3
BuildRequires(pre): rpm-macros-cmake
BuildRequires: java-21-openjdk-devel
BuildRequires: ant
BuildRequires: maven-local
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libcef-devel
BuildRequires: libgtk+3-devel
BuildRequires: libX11-devel
BuildRequires: thrift
BuildRequires: thrift-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-interprocess-devel
BuildRequires: python3
BuildRequires: mvn(org.jogamp.jogl:jogl-all)
BuildRequires: mvn(org.jogamp.gluegen:gluegen-rt)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(org.jetbrains.runtime:jbr-api)
BuildRequires: mvn(org.junit.platform:junit-platform-console)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(info.picocli:picocli)
BuildRequires: xvfb-run
BuildRequires: fonts-ttf-dejavu
BuildRequires: dbus
BuildRequires: openbox-base

%description
JetBrains JCEF provides Java browser APIs and private JNI libraries for Chromium
Embedded Framework. This package includes both the in-process and remote
browser implementations and uses the system CEF runtime and resources.

%prep
%setup
%autopatch -p1
cp -p %SOURCE2 thrift-NOTICE
sed -i 's|@JCEF_LIBDIR@|%jcef_libdir|g' \
    java/org/cef/SystemBootstrap.java
%pom_xpath_set pom:properties/pom:revision %jcef_revision
%pom_xpath_set /pom:project/pom:version %jcef_maven_version
%mvn_file org.jetbrains.intellij.deps.jcef:jcef %name/%name

%build
%ifarch aarch64
%define jcef_arch arm64
%else
%define jcef_arch %_arch
%endif
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DPROJECT_ARCH=%jcef_arch \
    -DCEF_ROOT=%cef_root \
    -Dapi_version=15000 \
    -DPython_EXECUTABLE=%__python3 \
    -DJCEF_COMMIT_HASH=%upstream_rev \
    -DJCEF_COMMIT_NUMBER=%upstream_count
%cmake_build

cef_runtime_version=$(sed -n \
    's/^#define CEF_VERSION "\([^"]*\)"/\1/p' \
    %cef_root/include/cef_version.h | tr '+' '-')
test -n "$cef_runtime_version"
%ant \
    -Dout.path=out \
    -Dant.build.javac.source=17 \
    -Dant.build.javac.target=17 \
    -Djcef.version=%jcef_maven_version \
    -Djcef.runtime.version="$cef_runtime_version-api-%jcef_api-%jcef_revision" \
    -Djogl.jar=%_jnidir/jogl.jar \
    -Dgluegen.jar=%_jnidir/gluegen-rt.jar \
    -Dgson.jar=%_javadir/google-gson/gson.jar \
    -Djunit.jar="$(build-classpath junit5/junit-jupiter-api \
        junit5/junit-platform-console junit5/junit-platform-commons \
        junit5/junit-platform-engine junit5/junit-platform-launcher \
        apiguardian opentest4j)" \
    -Djbrapi.jar=%_javadir/jbr-api/jbr-api.jar \
    jar tests-jar
%mvn_artifact pom.xml out/jcef.jar

%install
%mvn_install
install -dm755 %buildroot%jcef_libdir
install -m755 %_cmake__builddir/native/Release/libjcef.so \
    %_cmake__builddir/native/Release/jcef_helper \
    %_cmake__builddir/remote/Release/cef_server \
    %_cmake__builddir/remote/Release/libshared_mem_helper.so \
    %buildroot%jcef_libdir/
OS=%_os JCEF_ROOT_DIR="$PWD" OUT_CLS_DIR="$PWD/out" \
    bash jb/tools/common/create_version_file.sh %buildroot%jcef_libdir
ln -s jcef.version %buildroot%jcef_libdir/version.info

%check
xvfb-run -a -s '-screen 0 1280x1024x24 -nolisten tcp +extension GLX' \
    dbus-run-session -- sh %SOURCE1 \
    %buildroot%jcef_libdir out/jcef.jar out/jcef-tests.jar

%files -f .mfiles
%doc LICENSE.txt tools/yapf/LICENSE thrift-NOTICE
%dir %jcef_libdir
%jcef_libdir/libjcef.so
%jcef_libdir/libshared_mem_helper.so
%jcef_libdir/jcef_helper
%jcef_libdir/cef_server
%jcef_libdir/jcef.version
%jcef_libdir/version.info

%changelog
* Sat Nov 07 2026 Ivan Khanas <xeno@altlinux.org> 150.0.14-alt1
- Initial build for ALT.

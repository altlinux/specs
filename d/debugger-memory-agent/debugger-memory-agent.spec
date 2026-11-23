%define _unpackaged_files_terminate_build 1

Name: debugger-memory-agent
Version: 1.0.51
Release: alt1

Summary: JVMTI memory analysis and allocation sampling agent
License: Apache-2.0
Group: Development/Java
URL: https://github.com/JetBrains/debugger-memory-agent
VCS: https://github.com/JetBrains/debugger-memory-agent.git

Source: %name-%version.tar
Patch0: 0001-Publish-the-Linux-agent-with-system-Gradle.patch
Patch1: 0002-Run-native-tests-outside-TeamCity.patch
Patch2: 0003-Avoid-wall-clock-assumptions-in-timeout-tests.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires(pre): rpm-macros-java
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel-static
BuildRequires: java-21-openjdk-devel
BuildRequires: python3
BuildRequires: xgradle

%description
Native JVMTI agent and Java API for JVM heap diagnostics, object reachability,
retained-size analysis, and allocation sampling.

%prep
%setup -q
%autopatch -p1

%build
# The upstream FindJNI11 module uses JDK_11 to locate the JNI headers.
export JDK_11=%_jvmdir/java-21-openjdk
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

mkdir -p bin classes
install -pm755 %_cmake__builddir/libmemory_agent.so bin/libmemory_agent.so
rm -f %_cmake__builddir/libmemory_agent.so
find test_data/proxy/src -type f -name '*.java' -print0 \
    | xargs -0 %_jvmdir/java-21-openjdk/bin/javac --release 8 -d classes

cd publish
%gradle_publish --no-daemon \
    -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk \
    -PrpmVersion=%version \
    -PnativeBinaries=libmemory_agent.so

%install
cd publish
%gradle_register --artifacts=debugger-memory-agent
%gradle_install

%check
cd publish
%gradle_check --no-daemon -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk
cd ..
JDK_21=%_jvmdir/java-21-openjdk python3 test_runner.py JDK_21

%files -f publish/.mfiles
%doc LICENSE

%changelog
* Fri Nov 13 2026 Ivan Khanas <xeno@altlinux.org> 1.0.51-alt1
- Initial build for ALT.

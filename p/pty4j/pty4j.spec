%define _unpackaged_files_terminate_build 1
%def_with check

Name: pty4j
Version: 0.14.0
Release: alt1

Summary: Pseudo terminal implementation for Java
License: EPL-1.0 and Apache-2.0
Group: Development/Java
URL: https://github.com/JetBrains/pty4j
VCS: https://github.com/JetBrains/pty4j.git

Source: %name-%version.tar
Patch: alt-linux-native.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: gcc
BuildRequires: make
BuildRequires: java-17-openjdk-devel
BuildRequires: kotlin-compiler
BuildRequires: kotlin-gradle-plugin
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: slf4j2
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(net.java.dev.jna:jna)
BuildRequires: mvn(net.java.dev.jna:jna-platform)
%if_with check
BuildRequires: /dev/pts
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.jetbrains.format-ripper:format-ripper)
BuildRequires: kotlinx-coroutines
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.slf4j:slf4j-simple)
%endif

%ifarch x86_64
%define native_arch x86-64
%define native_target linux_x86_64
%else
%ifarch %ix86
%define native_arch x86
%define native_target linux_x86
%else
%define native_arch %_arch
%define native_target linux_%_arch
%endif
%endif

%description
Pty4j runs child processes connected to a pseudo terminal. It provides
terminal input and output, window sizing, process lifetime and signal
handling through a Java API and a native Linux library built from source.

%prep
%setup
%patch -p1
subst 's|@PTY4J_NATIVE_DIR@|%_jnidir/%name|' src/com/pty4j/util/PtyUtil.java

%build
%make_build -B -C native -f Makefile_linux %native_target \
    CFLAGS="%optflags -fPIC -D_REENTRANT -D_GNU_SOURCE"
%gradle_publish --no-daemon \
    -Dorg.gradle.java.home=%_jvmdir/java-17-openjdk \
    -PnativeResourcePath=linux/%native_arch \
    -Pkotlin.compiler.execution.strategy=in-process

%install
%gradle_register --artifacts=pty4j-
%gradle_install
install -Dpm755 os/linux/%native_arch/libpty.so \
    %buildroot%_jnidir/%name/linux/%native_arch/libpty.so

%check
%if_with check
%gradle_check --no-daemon \
    -Dorg.gradle.java.home=%_jvmdir/java-17-openjdk \
    -PnativeResourcePath=linux/%native_arch \
    -Pkotlin.compiler.execution.strategy=in-process
%endif

%files -f .mfiles
%_jnidir/%name/linux
%doc LICENSE NOTICE

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 0.14.0-alt1
- Initial build for ALT.

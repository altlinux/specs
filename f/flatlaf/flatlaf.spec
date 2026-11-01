%define _unpackaged_files_terminate_build 1

# The running JVM supplies libjawt; its versioned directory is not a public ABI.
%filter_from_requires \|^%_jvmdir/java-[^/]*/lib/libjawt[.]so.*$|d
%filter_from_requires \|^/usr/lib/debug%_jvmdir/java-[^/]*/lib/libjawt[.]so[.]debug.*$|d

Name: flatlaf
Version: 3.7.1
Release: alt5

Summary: Flat Look and Feel
Group: Development/Java
License: Apache-2.0
Url: https://www.formdev.com/flatlaf/
Vcs: https://github.com/JFormDesigner/FlatLaf

%ifarch %ix86
%define flatlaf_native_arch i386
%else
%ifarch aarch64
%define flatlaf_native_arch arm64
%else
%define flatlaf_native_arch %_arch
%endif
%endif

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: java-17-openjdk-devel
BuildRequires: gcc-c++
BuildRequires: xgradle
BuildRequires: libgtk+3-devel
BuildRequires: fontconfig-devel
BuildRequires: fonts-ttf-dejavu
BuildRequires: jsvg
BuildRequires: jna
BuildRequires: jna-contrib
BuildRequires: junit5

%package core
Summary: Flat Look and Feel Core
Group: Development/Java
BuildArch: noarch
Requires: %name-native = %EVR

%package extras
Summary: Flat Look and Feel Extras
Group: Development/Java
BuildArch: noarch

%package fonts
Summary: Flat Look and Feel Fonts Pack
Group: Development/Java
BuildArch: noarch

%package intellij-themes
Summary: FlatLaf IntelliJ Themes Pack
Group: Development/Java
BuildArch: noarch

%package native
Summary: FlatLaf Linux JNI library
Group: Development/Java
Requires: java

%description native
Linux JNI support for FlatLaf dialogs and window integration, built for
the installed JVM architecture and loaded from beside the FlatLaf JAR.

%{?javadoc_package}

%description
FlatLaf is a modern open-source cross-platform Look and Feel for Java
Swing desktop applications. It looks almost flat (no shadows or
gradients), clean, simple and elegant. FlatLaf comes with Light, Dark,
IntelliJ and Darcula themes, scales on HiDPI displays and runs on
Java 8 or newer (LTS and latest).

%description core
FlatLaf is a modern open-source cross-platform Look and Feel for Java
Swing desktop applications. It looks almost flat (no shadows or
gradients), clean, simple and elegant. FlatLaf comes with Light, Dark,
IntelliJ and Darcula themes, scales on HiDPI displays and runs on
Java 8 or newer (LTS and latest).

This package contains Flat Look and Feel core module.

%description extras
FlatLaf is a modern open-source cross-platform Look and Feel for Java
Swing desktop applications. It looks almost flat (no shadows or
gradients), clean, simple and elegant. FlatLaf comes with Light, Dark,
IntelliJ and Darcula themes, scales on HiDPI displays and runs on
Java 8 or newer (LTS and latest).

This package contains Flat Look and Feel extras module.

%description fonts
FlatLaf is a modern open-source cross-platform Look and Feel for Java
Swing desktop applications. It looks almost flat (no shadows or
gradients), clean, simple and elegant. FlatLaf comes with Light, Dark,
IntelliJ and Darcula themes, scales on HiDPI displays and runs on
Java 8 or newer (LTS and latest).

This package contains Flat Look and Feel fonts pack.

%description intellij-themes
FlatLaf is a modern open-source cross-platform Look and Feel for Java
Swing desktop applications. It looks almost flat (no shadows or
gradients), clean, simple and elegant. FlatLaf comes with Light, Dark,
IntelliJ and Darcula themes, scales on HiDPI displays and runs on
Java 8 or newer (LTS and latest).

This package contains Flat Look and Feel themes pack.

%prep
%setup
%autopatch -p1

%build
gradle :flatlaf-natives-linux:build-natives -Prelease -Dtoolchain=17 \
  -PaltJvmLibraryPath=%_jvmdir/jre/lib \
  -Ddisable.xgradle=true --offline
%gradle_publish -Prelease -Dtoolchain=17

%check
%gradle_check -Prelease -Dtoolchain=17

%install
%gradle_register
%gradle_register_javadoc

%mvn_package :flatlaf flatlaf-core
%mvn_package :flatlaf-extras flatlaf-extras
%mvn_package :flatlaf-fonts-inter flatlaf-fonts
%mvn_package :flatlaf-fonts-jetbrains-mono flatlaf-fonts
%mvn_package :flatlaf-fonts-roboto flatlaf-fonts
%mvn_package :flatlaf-fonts-roboto-mono flatlaf-fonts
%mvn_package :flatlaf-intellij-themes flatlaf-intellij-themes

%mvn_file :flatlaf flatlaf %_javadir/flatlaf

%gradle_install

install -Dpm755 \
  flatlaf-core/src/main/resources/com/formdev/flatlaf/natives/libflatlaf-linux-%flatlaf_native_arch.so \
  %buildroot%_libdir/%name/libflatlaf-linux-%flatlaf_native_arch.so
native_rel=$(realpath -m --relative-to=%_javadir %_libdir/%name)
ln -s "$native_rel/libflatlaf-linux-%flatlaf_native_arch.so" \
  %buildroot%_javadir/flatlaf-linux-%flatlaf_native_arch.so
install -d %buildroot%_jnidir
native_jni_rel=$(realpath -m --relative-to=%_jnidir %_libdir/%name)
ln -s "$native_jni_rel/libflatlaf-linux-%flatlaf_native_arch.so" \
  %buildroot%_jnidir/flatlaf-linux-%flatlaf_native_arch.so

%files core -f .mfiles-flatlaf-core
%doc LICENSE
%files extras -f .mfiles-flatlaf-extras
%files fonts -f .mfiles-flatlaf-fonts
%files intellij-themes -f .mfiles-flatlaf-intellij-themes

%files native
%doc LICENSE
%dir %_libdir/%name
%_libdir/%name/libflatlaf-linux-%flatlaf_native_arch.so
%_javadir/flatlaf-linux-%flatlaf_native_arch.so
%_jnidir/flatlaf-linux-%flatlaf_native_arch.so

%changelog
* Sat Oct 31 2026 Ivan Khanas <xeno@altlinux.org> 3.7.1-alt5
- Split the Linux JNI library into an architecture-specific subpackage.
- Build Java artifacts as noarch and support Linux i586 JNI.

* Thu Sep 10 2026 Anton Meleshnikov <alton@altlinux.org> 3.7.1-alt4
- Fixed ftbfs: used java-17.

* Mon Jul 06 2026 Arseniy Kostevich <faux@altlinux.org> 3.7.1-alt3
- Fixed ftbfs: changed jpackage-default jpackage-11-compat.
- Build only for %%java_arches.

* Fri Apr 24 2026 Arseniy Kostevich <faux@altlinux.org> 3.7.1-alt2
- Add core symlink to javadir.

* Fri Apr 17 2026 Arseniy Kostevich <faux@altlinux.org> 3.7.1-alt1
- Initial build for ALT.

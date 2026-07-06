%define _unpackaged_files_terminate_build 1

Name: flatlaf
Version: 3.7.1
Release: alt3

Summary: Flat Look and Feel
Group: Development/Java
License: Apache-2.0
Url: https://www.formdev.com/flatlaf/
Vcs: https://github.com/JFormDesigner/FlatLaf
ExclusiveArch: %java_arches

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: jpackage-11-compat
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

%package extras
Summary: Flat Look and Feel Extras
Group: Development/Java

%package fonts
Summary: Flat Look and Feel Fonts Pack
Group: Development/Java

%package intellij-themes
Summary: FlatLaf IntelliJ Themes Pack
Group: Development/Java

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

%ifarch aarch64
sed -i '/linux-x86_64/ d' flatlaf-core/build.gradle.kts
%endif

%ifarch x86_64
sed -i '/linux-arm64/ d' flatlaf-core/build.gradle.kts
%endif

%build
gradle :flatlaf-natives-linux:build-natives -Prelease -Dtoolchain=11 -Ddisable.xgradle=true --offline
%gradle_build -Prelease -Dtoolchain=11
%gradle_publish -Prelease -Dtoolchain=11

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

%files core -f .mfiles-flatlaf-core
%files extras -f .mfiles-flatlaf-extras
%files fonts -f .mfiles-flatlaf-fonts
%files intellij-themes -f .mfiles-flatlaf-intellij-themes

%changelog
* Mon Jul 06 2026 Arseniy Kostevich <faux@altlinux.org> 3.7.1-alt3
- Fixed ftbfs: changed jpackage-default jpackage-11-compat.
- Build only for %%java_arches.

* Fri Apr 24 2026 Arseniy Kostevich <faux@altlinux.org> 3.7.1-alt2
- Add core symlink to javadir.

* Fri Apr 17 2026 Arseniy Kostevich <faux@altlinux.org> 3.7.1-alt1
- Initial build for ALT.

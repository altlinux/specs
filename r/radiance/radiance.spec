%define _unpackaged_files_terminate_build 1

Name: radiance
Version: 8.5.0
Release: alt1

Summary: Modern libraries for building Swing applications
License: BSD-3-Clause
Group: Development/Java
Url: https://github.com/kirill-grouchnikov/radiance
Vcs: https://github.com/kirill-grouchnikov/radiance.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: xgradle
BuildRequires: ephemeral
BuildRequires: jgoodies-common
BuildRequires: jgoodies-forms
BuildRequires: batik
BuildRequires: jhlabs-filters

%description
Radiance is a collection of libraries for building modern Swing applications.
This template builds and installs the core Java and Kotlin modules.

%package common
Summary: Common utilities for Radiance modules
Group: Development/Java

%description common
Common utility classes shared by Radiance libraries.

%package animation
Summary: Animation library for Swing applications
Group: Development/Java

%description animation
Animation APIs and timeline infrastructure from Radiance.

%package theming
Summary: Radiance Swing look-and-feel
Group: Development/Java

%description theming
Core look-and-feel implementation from Radiance.

%package theming-extras
Summary: Extra theming features for Radiance
Group: Development/Java

%description theming-extras
Supplementary theming APIs and add-ons for Radiance.

%package component
Summary: Additional Swing components for Radiance
Group: Development/Java

%description component
Extra Swing UI components built on top of Radiance theming.

%package tools-laf-benchmark
Summary: Benchmark tool for Swing look-and-feels
Group: Development/Java

%description tools-laf-benchmark
Utility for benchmarking Swing look-and-feel startup and rendering.

%package theming-debugger
Summary: Debug utilities for Radiance theming
Group: Development/Java

%description theming-debugger
Runtime debugging helpers for Radiance look-and-feel internals.

%package svg-transcoder
Summary: SVG transcoder used by Radiance tooling
Group: Development/Java

%description svg-transcoder
Library that converts SVG assets for use with Radiance components.

%package svg-transcoder-gradle-plugin
Summary: Gradle plugin for Radiance SVG transcoder
Group: Development/Java

%description svg-transcoder-gradle-plugin
Gradle plugin integrating the Radiance SVG transcoder into builds.

%prep
%setup
%autopatch -p1

%mvn_package :radiance-common common
%mvn_package :radiance-animation animation
%mvn_package :radiance-theming theming
%mvn_package :radiance-theming-extras theming-extras
%mvn_package :radiance-component component
%mvn_package :radiance-tools-laf-benchmark tools-laf-benchmark
%mvn_package :radiance-theming-debugger theming-debugger
%mvn_package :radiance-svg-transcoder svg-transcoder
%mvn_package :radiance-svg-transcoder-gradle-plugin svg-transcoder-gradle-plugin
%mvn_package :svg-transcoder-gradle-plugin svg-transcoder-gradle-plugin

%build
%gradle_publish

%install
%gradle_register

%gradle_install

%files common -f .mfiles-common
%files animation -f .mfiles-animation
%files theming -f .mfiles-theming
%files theming-extras -f .mfiles-theming-extras
%files component -f .mfiles-component
%files tools-laf-benchmark -f .mfiles-tools-laf-benchmark
%files theming-debugger -f .mfiles-theming-debugger
%files svg-transcoder -f .mfiles-svg-transcoder
%files svg-transcoder-gradle-plugin -f .mfiles-svg-transcoder-gradle-plugin

%changelog
* Thu Apr 16 2026 Ivan Khanas <xeno@altlinux.org> 8.5.0-alt1
- First build for ALT.

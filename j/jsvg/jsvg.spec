%define _unpackaged_files_terminate_build 1

Name: jsvg
Version: 2.0.0
Release: alt2

Summary: Java SVG renderer
Group: Development/Java
License: MIT
Url: https://github.com/weisJ/jsvg
Vcs: https://github.com/weisJ/jsvg
ExclusiveArch: %java_arches

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: biz-aQute-bnd-gradle-plugins
BuildRequires: jetbrains-annotations

%description
JSVG is an SVG user agent using AWT graphics. Its aim is to provide a small
and fast implementation. This implementation only tries to be a static user
agent meaning it won't support any scripting languages or interaction.
Partial animations exists and will be extended in future versions.

This library aims to be as lightweight as possible. Generally JSVG uses ~50%%
less memory than svgSalamander and ~98%% less than Batik.

%{?javadoc_package}

%prep
%setup
%autopatch -p1

%build
%gradle_publish -Prelease -x test

%install
%gradle_register
%gradle_register_javadoc

%gradle_install

%files -f .mfiles

%changelog
* Mon Jul 06 2026 Arseniy Kostevich <faux@altlinux.org> 2.0.0-alt2
- Build only for %%java_arches.

* Tue Apr 14 2026 Arseniy Kostevich <faux@altlinux.org> 2.0.0-alt1
- Initial build for ALT.

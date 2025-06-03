%define _unpackaged_files_terminate_build 1

Name: ignis
Version: 0.5.1
Release: alt1

ExcludeArch: %ix86

Summary: A widget framework for building desktop shells
License: LGPL-2.1-only
Group: Graphical desktop/Other
Url: https://ignis-sh.github.io/ignis
VCS: https://github.com/ignis-sh/ignis

Requires: libgtk4-layer-shell-devel
Requires: grass-sass

# Source-url: https://github.com/ignis-sh/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Patch1: alt-remove-git-start.patch
Patch2: alt-remove-empty-fields.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: libpulseaudio-devel
BuildRequires: libgtk4-devel
BuildRequires: libgtk4-layer-shell-devel
BuildRequires: gobject-introspection-devel

%description
A widget framework for building desktop shells, written and
configurable in Python.
* Easy to use
* GTK4-based
* Batteries Included (a lot of built-in Services and Utilities!)
* Flexible work with widgets

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%meson \
    --wrap-mode=nodownload \
    #
%meson_build

%install
%meson_install

%files
%_bindir/%name
%python3_sitelibdir/%{name}*

%changelog
* Tue Jun 03 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 0.5.1-alt1
- Initial build for ALT Linux

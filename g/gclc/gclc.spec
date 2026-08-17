%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: gclc
Version: 2026.08
Release: alt1

Summary: Visualize and explore geometry
License: MIT
Group: Publishing
Url: https://github.com/ADG-Foundation/gclc

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(cups)

%description
GCLC (Geometry Constructions to LaTeX Converter) is a mathematical
software tool for visualizing geometry and producing high-quality
digital mathematical illustrations.

GCLC was initially built as a tool for converting formal descriptions
of geometric constructions into LaTeX form, but now it is much more
than that. For instance, there is support for symbolic expressions,
for drawing parametric curves, for program loops, user-defined
procedures, etc. Built-in theorem provers can automatically prove
a range of complex theorems, and the graphical interface makes GCLC
a tool for teaching geometry and other mathematical fields as well.

%prep
%setup

%build
%cmake \
       -Dgui=ON
%cmake_build

%install
%cmake_install

%files
%doc LICENSE.md README.md DOC/*.pdf samples working_example
%_bindir/gclc
%_bindir/gclc-gui
%_desktopdir/io.github.ADG_Foundation.gclc.desktop
%_iconsdir/hicolor/*/apps/io.github.ADG_Foundation.gclc.png
%_datadir/metainfo/io.github.ADG_Foundation.gclc.metainfo.xml

%changelog
* Mon Aug 17 2026 Nikolay Strelkov <snk@altlinux.org> 2026.08-alt1
- Initial build for Sisyphus

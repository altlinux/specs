%define        _unpackaged_files_terminate_build 1
%define        oname ImGuiColorTextEdit

Name:          lib%oname
Version:       1.93.0
Release:       alt1
Summary:       Colorizing text editor for ImGui
License:       MIT
Group:         Sciences/Mathematics
Url:           https://github.com/goossens/ImGuiColorTextEdit
Vcs:           https://github.com/malbajun/ImGuiColorTextEdit.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: cmake(imgui)
BuildRequires: libimgui-devel >= 1.93.0

%description
Syntax highlighting text editor for ImGui.

This started as my attempt to write a relatively simple widget which provides
text editing functionality with syntax highlighting. Now there are other
contributors who provide valuable additions.

While it relies on Omar Cornut's https://github.com/ocornut/imgui, it does not
follow the "pure" one widget - one function approach. Since the editor has to
maintain a relatively complex and large internal state, it did not seem to be
practical to try and enforce fully immediate mode. It stores its internal state
in an object instance which is reused across frames.

Main features:
* approximates typical code editor look and feel (essential mouse/keyboard
  commands work - I mean, the commands I normally use :))
* undo/redo
* UTF-8 support
* works with both fixed and variable-width fonts
* extensible syntax highlighting for multiple languages
* identifier declarations: a small piece of description can be associated with
  an identifier. The editor displays it in a tooltip when the mouse cursor is
  hovered over the identifier
* error markers: the user can specify a list of error messages together the line
  of occurence, the editor will highligh the lines with red backround and
  display error message in a tooltip when the mouse cursor is hovered over the
  line
* large files: there is no explicit limit set on file size or number of lines
  (below 2GB, performance is not affected when large files are loaded (except
  syntax coloring, see below)
* color palette support: you can switch between different color palettes, or
  even define your own
* whitespace indicators (TAB, space)


%package       devel
Group:         Development/C++
Summary:       Colorizing text editor for ImGui development files

Requires:      %name = %EVR
Requires:      cmake(imgui)
Requires:      libimgui-devel >= 1.93.0

%description   devel
Colorizing text editor for ImGui development files.

Syntax highlighting text editor for ImGui.

This started as my attempt to write a relatively simple widget which provides
text editing functionality with syntax highlighting. Now there are other
contributors who provide valuable additions.

While it relies on Omar Cornut's https://github.com/ocornut/imgui, it does not
follow the "pure" one widget - one function approach. Since the editor has to
maintain a relatively complex and large internal state, it did not seem to be
practical to try and enforce fully immediate mode. It stores its internal state
in an object instance which is reused across frames.

Main features:
* approximates typical code editor look and feel (essential mouse/keyboard
  commands work - I mean, the commands I normally use :))
* undo/redo
* UTF-8 support
* works with both fixed and variable-width fonts
* extensible syntax highlighting for multiple languages
* identifier declarations: a small piece of description can be associated with
  an identifier. The editor displays it in a tooltip when the mouse cursor is
  hovered over the identifier
* error markers: the user can specify a list of error messages together the line
  of occurence, the editor will highligh the lines with red backround and
  display error message in a tooltip when the mouse cursor is hovered over the
  line
* large files: there is no explicit limit set on file size or number of lines
  (below 2GB, performance is not affected when large files are loaded (except
  syntax coloring, see below)
* color palette support: you can switch between different color palettes, or
  even define your own
* whitespace indicators (TAB, space)


%prep
%setup

%build
%cmake \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo \
   -DENABLE_GEOGRAM=ON \
   -DENABLE_BALAZS=ON \
   -DBUILD_SHARED_LIBS=ON \
   -DCMAKE_INSTALL_LIBDIR=%_lib \
   -DBUILD_TESTING=ON \
   %nil
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%doc README.md CONTRIBUTING LICENSE
%_libdir/lib%{oname}.so.*

%files         devel
%doc README.md CONTRIBUTING LICENSE
%_includedir/%{oname}/
%_cmakedir/%{oname}/
%_libdir/lib%{oname}.so


%changelog
* Tue Nov 10 2026 Pavel Skrylev <majioa@altlinux.org> 1.93.0-alt1
- ^ 1.0.0 -> 1.93.0
- * rebased to current goossens upstream with optional standalone Geogram
    and Balazs support.
- * Check the ImGui version through libimgui-devel while retaining its CMake
    requirement.
- * required the separate ctest package for the build-time regression checks.
- + installed modular language headers and exported CMake targets.
- * run editor regression checks during package build.

* Thu Nov 28 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus

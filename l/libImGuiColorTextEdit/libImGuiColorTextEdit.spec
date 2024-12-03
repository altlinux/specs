%define        _unpackaged_files_terminate_build 1
%define        oname ImGuiColorTextEdit

Name:          lib%oname
Version:       1.0.0
Release:       alt1
Summary:       Colorizing text editor for ImGui
License:       MIT
Group:         Sciences/Mathematics
Url:           https://github.com/BalazsJako/ImGuiColorTextEdit
Vcs:           https://github.com/BalazsJako/ImGuiColorTextEdit.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libimgui-devel

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
Summary:       Development files for %name

Requires:      cmake
Requires:      gcc-c++
Requires:      libimgui-devel

%description   devel
Development files for %name.

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
%cmake -DARCH:STRING=%_arch \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \

%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md CONTRIBUTING LICENSE
%_libdir/%{name}.*so.*
%_libdir/%{name}*.*so.*

%files         devel
%doc README.md CONTRIBUTING LICENSE
%_includedir/%{oname}*
%_cmakedir/*
%_libdir/%{name}*.*so


%changelog
* Thu Nov 28 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus

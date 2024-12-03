%define        _unpackaged_files_terminate_build 1
%define        oname imgui

Name:          lib%oname
Version:       1.91.5
Release:       alt1
Summary:       Dear ImGui: Bloat-free Graphical User interface for C++ with minimal dependencies
License:       MIT
Group:         Sciences/Mathematics
Url:           https://www.dearimgui.com/
Vcs:           https://github.com/ocornut/imgui.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: liballegro5.2-devel
BuildRequires: libfreeglut-devel
BuildRequires: libglfw3-devel
BuildRequires: libSDL2-devel
BuildRequires: libvulkan-devel
Conflicts:     imgui

%description
Dear ImGui is a bloat-free graphical user interface library for C++. It outputs
optimized vertex buffers that you can render anytime in your 3D-pipeline-enabled
application. It is fast, portable, renderer agnostic, and self-contained (no
external dependencies).

Dear ImGui is designed to enable fast iterations and to empower programmers to
create content creation tools and visualization / debug tools (as opposed to UI
for the average end-user). It favors simplicity and productivity toward this
goal and lacks certain features commonly found in more high-level libraries.
Among other things, full internationalization (right-to-left text, bidirectional
text, text shaping etc.) and accessibility features are not supported.

Dear ImGui is particularly suited to integration in game engines (for tooling),
real-time 3D applications, fullscreen applications, embedded applications, or
any applications on console platforms where operating system features are
non-standard.

* Minimize state synchronization.
* Minimize UI-related state storage on user side.
* Minimize setup and maintenance.
* Easy to use to create dynamic UI which are the reflection of a dynamic data
  set.
* Easy to use to create code-driven and data-driven tools.
* Easy to use to create ad hoc short-lived tools and long-lived, more elaborate
  tools.
* Easy to hack and improve.
* Portable, minimize dependencies, run on target (consoles, phones, etc.).
* Efficient runtime and memory consumption.
* Battle-tested, used by many major actors in the game industry.


%package       devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      cmake
Requires:      gcc-c++
Requires:      liballegro-devel
Requires:      liballegro5.2-devel
Requires:      libfreeglut-devel
Requires:      libglfw3-devel
Requires:      libSDL2-devel
Requires:      libvulkan-devel
Conflicts:     imgui-devel

%description   devel
Development files for %name.

Dear ImGui is a bloat-free graphical user interface library for C++. It outputs
optimized vertex buffers that you can render anytime in your 3D-pipeline-enabled
application. It is fast, portable, renderer agnostic, and self-contained (no
external dependencies).

Dear ImGui is designed to enable fast iterations and to empower programmers to
create content creation tools and visualization / debug tools (as opposed to UI
for the average end-user). It favors simplicity and productivity toward this
goal and lacks certain features commonly found in more high-level libraries.
Among other things, full internationalization (right-to-left text, bidirectional
text, text shaping etc.) and accessibility features are not supported.

Dear ImGui is particularly suited to integration in game engines (for tooling),
real-time 3D applications, fullscreen applications, embedded applications, or
any applications on console platforms where operating system features are
non-standard.

* Minimize state synchronization.
* Minimize UI-related state storage on user side.
* Minimize setup and maintenance.
* Easy to use to create dynamic UI which are the reflection of a dynamic data
  set.
* Easy to use to create code-driven and data-driven tools.
* Easy to use to create ad hoc short-lived tools and long-lived, more elaborate
  tools.
* Easy to hack and improve.
* Portable, minimize dependencies, run on target (consoles, phones, etc.).
* Efficient runtime and memory consumption.
* Battle-tested, used by many major actors in the game industry.


%prep
%setup

%build
%cmake -DARCH:STRING=%_arch \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \

%cmake_build

%install
%cmakeinstall_std

%files
%doc docs/README*
%_libdir/%{name}.*so.*
%_libdir/%{name}*.*so.*

%files         devel
%_includedir/%{oname}*
%_cmakedir/*
%_libdir/%{name}*.*so


%changelog
* Mon Nov 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.91.5-alt1
- initial build for Sisyphus

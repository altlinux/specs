Name:           imgui
Version:        1.89.8
Release:        alt1
Summary:        Immediate Mode Graphical User interface for C++ with minimal dependencies
License:        MIT
Group:          System/Libraries
URL:            https://www.dearimgui.org
Source:         %name-%version.tar
BuildRequires:  gcc-c++
BuildRequires:  make

%description
ImGui is a bloat-free graphical user interface library for C++. It outputs optimized vertex buffers that you can render anytime in your 3D-pipeline enabled application. It is fast, portable, renderer agnostic and self-contained (no external dependencies).

ImGui is designed to enable fast iteration and empower programmers to create content creation tools and visualization/ debug tools (as opposed to UI for the average end-user). It favors simplicity and productivity toward this goal, and thus lacks certain features normally found in more high-level libraries.

ImGui is particularly suited to integration in realtime 3D applications, fullscreen applications, embedded applications, games, or any applications on consoles platforms where operating system features are non-standard.

%package devel
Summary:        Development files for ImGui
Group:          Development/C

%description devel
ImGui is self-contained within a few files that you can easily copy and compile into your application/engine.

No specific build process is required. You can add the .cpp files to your project or #include them from an existing file.

%prep
%setup -q

%build

%install
mkdir -p %buildroot%_includedir/imgui
cp *.h %buildroot%_includedir/imgui

%files devel
%_includedir/imgui

%changelog
* Fri Sep  1 2023 Artyom Bystrov <arbars@altlinux.org> 1.89.8-alt1
- update to new version

* Wed Sep 25 2019 Artyom Bystrov <arbars@altlinux.org> 1.88-alt1
- initial build for ALT Sisyphus

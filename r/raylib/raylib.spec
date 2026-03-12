%define _unpackaged_files_terminate_build 1

%define abiversion 5

Name:    raylib
Version: 5.5
Release: alt2

Summary: A simple and easy-to-use library to enjoy videogames programming
License: Zlib
Group:   Development/C
Url:     https://www.raylib.com
Vcs:     https://github.com/raysan5/raylib.git

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: libXcursor-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libGL-devel
BuildRequires: wayland-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libglfw3-devel

%description
%summary.

raylib is highly inspired by Borland BGI graphics lib and by XNA framework and
it's especially well suited for prototyping, tooling, graphical applications,
embedded systems and education.

NOTE for ADVENTURERS: raylib is a programming library to enjoy videogames
                      programming; no fancy interface, no visual helpers,
                      no debug button
                      ...just coding in the most pure spartan-programmers way.
Ready to learn? Jump to https://www.raylib.com/examples.html

%package -n lib%name
Summary: A simple and easy-to-use library to enjoy videogames programming
Group: System/Libraries

%description -n lib%name
%summary.

raylib is highly inspired by Borland BGI graphics lib and by XNA framework and
it's especially well suited for prototyping, tooling, graphical applications,
embedded systems and education.

NOTE for ADVENTURERS: raylib is a programming library to enjoy videogames
                      programming; no fancy interface, no visual helpers,
                      no debug button
                      ...just coding in the most pure spartan-programmers way.
Ready to learn? Jump to https://www.raylib.com/examples.html

%package -n lib%name-devel
Summary: Devel files for %name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
The %name-devel package contains header files for developing with %name.

%prep
%setup

%build
%cmake \
	-DBUILD_EXAMPLES=ON \
	-DBUILD_SHARED_LIBS=ON \
	-DUSE_EXTERNAL_GLFW=ON \
	-DOpenGL_GL_PREGERENCE=GLVND \
	-DUSE_WAYLAND=ON \
	-DPLATFORM=Desktop
%cmake_build

%install
%cmake_install

%files -n lib%name
%doc *.md LICENSE
%_libdir/lib%name.so.%{abiversion}*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
%_cmakedir/raylib/

%changelog
* Wed Mar 11 2026 Nikita Shmatko <nash@altlinux.org> 5.5-alt2
- Renamed raylib package to libraylib.
- Added ABI versioning.

* Tue Oct 21 2025 Nikita Shmatko <nash@altlinux.org> 5.5-alt1
- Initial build for Sisyphus.

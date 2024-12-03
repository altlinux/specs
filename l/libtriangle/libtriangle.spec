%define        _unpackaged_files_terminate_build 1
%define        oname triangle

Name:          lib%oname
Version:       1.6.0
Release:       alt1
Summary:       A Two-Dimensional Quality Mesh Generator and Delaunay Triangulator
License:       MIT
Group:         Sciences/Mathematics
Url:           http://www.cs.cmu.edu/~quake/triangle.research.html
Vcs:           https://github.com/libigl/triangle.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%description
A Two-Dimensional Quality Mesh Generator and Delaunay Triangulator.


%package       devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      cmake
Requires:      gcc-c++

%description   devel
Development files for %name.

A Two-Dimensional Quality Mesh Generator and Delaunay Triangulator.

%prep
%setup

%build
%cmake -DARCH:STRING=%_arch \
       -DBUILD_EXECUTABLE=OFF \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \

%cmake_build

%install
%cmakeinstall_std

%files
%doc README*
%_libdir/%{name}.*so.*
%_libdir/%{name}*.*so.*

%files         devel
%doc README*
%_includedir/%{oname}*
%_cmakedir/*
%_libdir/%{name}*.*so


%changelog
* Fri Nov 29 2024 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- initial build for Sisyphus

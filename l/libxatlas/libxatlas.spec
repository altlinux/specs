%define        _unpackaged_files_terminate_build 1
%define        oname xatlas

Name:          lib%oname
Version:       0.4
Release:       alt1
Summary:       Mesh parameterization / UV unwrapping library
License:       MIT
Group:         Sciences/Mathematics
Url:           https://github.com/jpcy/xatlas
Vcs:           https://github.com/guycalledfrank/xatlasLib.git
# Vcs1:        https://github.com/jpcy/xatlas.git
# Vcs2:        https://github.com/cpp-pm/xatlas.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%description
xatlas is a small C++11 library with no external dependencies that generates
unique texture coordinates suitable for baking lightmaps or texture painting.

It is an independent fork of thekla_atlas.


%package       devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      cmake
Requires:      gcc-c++

%description   devel
Development files for %name.

xatlas is a small C++11 library with no external dependencies that generates
unique texture coordinates suitable for baking lightmaps or texture painting.

It is an independent fork of thekla_atlas.


%prep
%setup

%build
%cmake -DARCH:STRING=%_arch \
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
* Fri Nov 29 2024 Pavel Skrylev <majioa@altlinux.org> 0.4-alt1
- initial build for Sisyphus

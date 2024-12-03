%define        _unpackaged_files_terminate_build 1

Name:          libmeshb
Version:       7.80
Release:       alt1
Summary:       A library to handle the *.meshb file format
License:       MIT
Group:         Sciences/Mathematics
Url:           https://github.com/LoicMarechal/libMeshb
Vcs:           https://github.com/LoicMarechal/libMeshb.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gcc-fortran

%description
A library to handle the *.meshb file format.

The Gamma Mesh Format (GMF) and the associated library libMeshb provide
programers of simulation and meshing software with an easy way to store their
meshes and physical solutions. The GMF features more than 200 kinds of data
types, like vertex, polyhedron, normal vector or vector solution field.
The libMeshb provides a convenient way to move data between those files, via
keyword tags, and the user's own structures. Transparent handling of ASCII &
binary files. Transparent handling of little & big endian files. Optional ultra
fast asynchronous and low level transfers. Can call user's own pre and post
processing routines in a separate thread while accessing a file.


%package       devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      cmake
Requires:      gcc-c++
Requires:      gcc-fortran

%description   devel
Development files for %name.

The Gamma Mesh Format (GMF) and the associated library libMeshb provide
programers of simulation and meshing software with an easy way to store their
meshes and physical solutions. The GMF features more than 200 kinds of data
types, like vertex, polyhedron, normal vector or vector solution field.
The libMeshb provides a convenient way to move data between those files, via
keyword tags, and the user's own structures. Transparent handling of ASCII &
binary files. Transparent handling of little & big endian files. Optional ultra
fast asynchronous and low level transfers. Can call user's own pre and post
processing routines in a separate thread while accessing a file.


%package       -n meshb7
Group:         Sciences/Mathematics
Summary:       libmeshb7 executables

%description   -n meshb7
Binaries to handle the *.meshb file format.

The Gamma Mesh Format (GMF) and the associated library libMeshb provide
programers of simulation and meshing software with an easy way to store their
meshes and physical solutions. The GMF features more than 200 kinds of data
types, like vertex, polyhedron, normal vector or vector solution field.
The libMeshb provides a convenient way to move data between those files, via
keyword tags, and the user's own structures. Transparent handling of ASCII &
binary files. Transparent handling of little & big endian files. Optional ultra
fast asynchronous and low level transfers. Can call user's own pre and post
processing routines in a separate thread while accessing a file.


%prep
%setup

%build
%cmake -DARCH:STRING=%_arch \
       -DLIBNAME:STRING=%name \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_Fortran_COMPILER=/usr/bin/gfortran \
       -DWITH_GMF_AIO=ON \
       -DCMAKE_HOST_SYSTEM_NAME=Linux

%cmake_build

%install
%cmakeinstall_std

%files         -n meshb7
%doc README*
%_bindir/*
%_libdir/%name
%_datadir/%name

%files
%doc README*
%_libdir/%{name}.*so.*

%files         devel
%_includedir/%{name}7*
%_cmakedir/*
%_libdir/%{name}.*so


%changelog
* Fri Nov 22 2024 Pavel Skrylev <majioa@altlinux.org> 7.80-alt1
- initial build for Sisyphus

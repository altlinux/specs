%define        _unpackaged_files_terminate_build 1
%define        Nomen OpenNL
%define        nomen opennl

Name:          lib%nomen
Version:       0.0.1
Release:       alt0.1
Summary:       OpenNL a library of linear solvers for sparse matrices on the CPU and the GPU
License:       Unlicense
Group:         Sciences/Mathematics
Url:           https://github.com/BrunoLevy/OpenNL
Vcs:           https://github.com/brunolevy/opennl.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%add_optflags -lm

%description
OpenNL a library of linear solvers for sparse matrices on the CPU and the GPU.

%package       devel
Group:         Development/C
Summary:       Development files for %name

%description   devel
OpenNL a library of linear solvers for sparse matrices on the CPU and the GPU.


%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmakeinstall_std


%files
%doc README.md
%_libdir/lib%{nomen}.*so.*

%files         devel
%doc README*
%_includedir/%Nomen
%_cmakedir/*
%_libdir/lib%{nomen}.so

%changelog
* Sun May 03 2026 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt0.1
- initial build for Sisyphus

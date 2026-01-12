%define _unpackaged_files_terminate_build 1
%define soversion 2

Name: gz-tools
Version: 2.0.3
Release: alt1

Summary: Entrypoint to Gazebo's command line interface
License: Apache-2.0
Group: Other
Url: https://gazebosim.org/libs/tools/
Vcs: https://github.com/gazebosim/gz-tools

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: gz-cmake >= 3.0.0

%description
Gazebo Tools provide the gz command line tool that accepts multiple
subcommands. Each subcommand is implemented in a plugin that belongs to a
specific Gazebo project. For example, all the commands that start with gz topic
... are implemented by the Gazebo Transport library.

%package -n libgz-tools%soversion-backward%soversion
Summary: Library files for libgz-tools%soversion-backward
Group: System/Libraries
Conflicts: gz-tools < 2.0.3

%description -n libgz-tools%soversion-backward%soversion
Library files for the gz-tools.

%package devel
Summary: Development files for gz-tools
Group: Development/C++

%description devel
Development files for building against gz-tools.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS README.md
%_bindir/gz
%_datadir/bash-completion/completions/gz
%_datadir/gz/gz.completion

%files -n libgz-tools%soversion-backward%soversion
%_libdir/libgz-tools%soversion-backward.so.%soversion
%_libdir/libgz-tools%soversion-backward.so.%version

%files -n gz-tools-devel
%_libdir/cmake/gz-tools%soversion-all
%_libdir/libgz-tools%soversion-backward.so

%changelog
* Tue Dec 23 2025 Pavel Petrykin <silverducks@altlinux.org> 2.0.3-alt1
- New version.

* Mon Nov 11 2024 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version.

* Thu Aug 03 2023 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt2
- Moved .so files to main package.

* Wed May 17 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus.

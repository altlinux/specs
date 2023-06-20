Name:    gz-tools
Version: 1.5.0
Release: alt1

Summary: Command line tools for the Gazebo libraries
License: Apache-2.0
Group:   Other
Url:     https://github.com/gazebosim/gz-tools

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
Gazebo tools provide the ign command line tool that accepts multiple
subcommands. Each subcommand is implemented in a plugin that belongs to a
specific Gazebo project. For example, all the commands that start with ign
topic ... will be implemented by the Gazebo Transport library.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS README.md
%_bindir/ign
%_datadir/bash-completion/completions/ign
%_datadir/gz/gz1.completion

%files devel
%_libdir/cmake/ignition-tools
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc

%changelog
* Wed May 17 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus.

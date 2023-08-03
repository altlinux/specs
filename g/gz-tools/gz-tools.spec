Name:    gz-tools
Version: 2.0.0
Release: alt1

Summary: Entrypoint to Gazebo's command line interface
License: Apache-2.0
Group:   Other
Url:     https://github.com/gazebosim/gz-tools

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: gz-cmake >= 3.0.0

%description
Gazebo Tools provide the gz command line tool that accepts multiple
subcommands. Each subcommand is implemented in a plugin that belongs to a
specific Gazebo project. For example, all the commands that start with gz topic
... are implemented by the Gazebo Transport library.

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
%_bindir/gz
%_datadir/bash-completion/completions/gz
%_datadir/gz/gz.completion
%_libdir/lib*.so

%files devel
%_libdir/cmake/gz-tools*

%changelog
* Thu Aug 03 2023 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt2
- Moved .so files to main package.

* Wed May 17 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus.

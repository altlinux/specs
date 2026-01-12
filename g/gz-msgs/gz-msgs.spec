%define _unpackaged_files_terminate_build 1
%define soversion 12

Name: gz-msgs
Version: 12.0.0
Release: alt1

Summary: Messages for Gazebo robot simulation
License: Apache-2.0
Group: Development/C++
Url: https://gazebosim.org/libs/msgs/
Vcs: https://github.com/gazebosim/gz-msgs

Source: %name-%version.tar

Conflicts: libgz-msgs

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libprotobuf-devel
BuildRequires: libtinyxml2-devel
BuildRequires: libgz-math-devel
BuildRequires: protobuf-compiler
BuildRequires: ctest

%add_python3_path %_libdir/python/gz/msgs*
%filter_from_requires /python3(gz.msgs)/d

%description
Gazebo Messages: Protobuf messages and functions for robot applications.

%package -n libgz-msgs%soversion
Summary: Library of gz-msgs
Group: System/Libraries

%description -n libgz-msgs%soversion
%summary

%package -n libgz-msgs-devel
Summary: Development files for gz-msgs
Group: Development/C++

%description -n libgz-msgs-devel
%summary

%prep
%setup
ln -s /usr/include/google proto/google

%build
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%check
%ctest \
    --exclude-regex ".*\.py"

%files
%doc AUTHORS README.md
%_bindir/gz-msgs_generate.py
%_bindir/gz-msgs_generate_factory.py
%_bindir/gz-msgs_protoc_plugin
%_libexecdir/ruby/gz/cmdmsgs%soversion.rb
%_datadir/gz/gz2.completion.d/msgs%soversion.bash_completion.sh
%_datadir/gz/msgs%soversion.yaml
%_datadir/gz/gz-msgs/protos
%_datadir/gz/protos/gz-msgs%soversion.gz_desc
%_libdir/python/gz/msgs
%_prefix/libexec/gz/msgs/gz-msgs

%files -n libgz-msgs%soversion
%_libdir/libgz-msgs.so.%soversion
%_libdir/libgz-msgs.so.%version

%files -n libgz-msgs-devel
%_includedir/gz/msgs%soversion
%_libdir/cmake/gz-msgs
%_libdir/cmake/gz-msgs-all
%_libdir/pkgconfig/gz-msgs.pc
%_libdir/libgz-msgs.so

%changelog
* Mon Dec 22 2025 Pavel Petrykin <silverducks@altlinux.org> 12.0.0-alt1
- New version.

* Mon Nov 11 2024 Andrey Cherepanov <cas@altlinux.org> 11.0.1-alt1
- New version.

* Tue Apr 02 2024 Andrey Cherepanov <cas@altlinux.org> 10.1.1-alt1
- New version.

* Mon Oct 02 2023 Andrey Cherepanov <cas@altlinux.org> 10.0.0-alt1
- New version.

* Wed Aug 02 2023 Andrey Cherepanov <cas@altlinux.org> 9.4.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 8.7.0-alt2
- Moved .so files to main package.

* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 8.7.0-alt1
- New version.

* Thu May 18 2023 Andrey Cherepanov <cas@altlinux.org> 5.11.0-alt1
- Initial build for Sisyphus.

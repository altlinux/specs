%define _unpackaged_files_terminate_build 1

Name: uid_wrapper
Version: 1.3.0
Release: alt2

Summary: A wrapper for privilege separation
License: GPLv3+
Group: Development/Other
Url: http://cwrap.org

# Source-git: git://git.samba.org/uid_wrapper.git
Source: %name-%version.tar
Patch0: skip_test_syscall_swrap_for_arm.patch

BuildRequires: cmake
BuildRequires: ctest
BuildRequires: libcmocka-devel

%description
Some projects like a file server need privilege separation to be able to switch
to the connection user and do file operations. uid_wrapper convincingly lies
to the application letting it believe it is operating as root and even
switching between UIDs and GIDs as needed.

To use it set the following environment variables:

LD_PRELOAD=libuid_wrapper.so
UID_WRAPPER=1

This package doesn't have a devel package cause this project is for
development/testing.

%prep
%setup
%patch0 -p2

%build
%cmake \
  -DUNIT_TESTING=ON

%cmake_build

%install
%cmake_install

%check
pushd %_cmake__builddir
LD_LIBRARY_PATH=$(pwd)/tests %make test || \
    { find Testing -name "*.log" | xargs cat; exit 2; }
popd

%files
%doc AUTHORS README.md CHANGELOG LICENSE
%_libdir/libuid_wrapper.so*
%dir %_libdir/cmake/uid_wrapper
%_libdir/cmake/uid_wrapper/uid_wrapper-config-version.cmake
%_libdir/cmake/uid_wrapper/uid_wrapper-config.cmake
%_libdir/pkgconfig/uid_wrapper.pc
%_man1dir/uid_wrapper.1*

%changelog
* Fri Mar 24 2023 Evgeny Sinelnikov <sin@altlinux.org> 1.3.0-alt2
- Skip test_syscall_swrap for arm archicture

* Fri Mar 24 2023 Evgeny Sinelnikov <sin@altlinux.org> 1.3.0-alt1
- Added support to interact with socket_wrapper syscall()
- Fixed deadlocks with threads
- Improved log output

* Sun Feb 27 2022 Evgeny Sinelnikov <sin@altlinux.org> 1.2.9-alt1
- Update to latest release with support for getgroups_chk()

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 1.2.8-alt1.1
- NMU: spec: adapted to new cmake macros.

* Sun Feb 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.2.8-alt1
- Update to latest release

* Fri Jul 20 2018 Stanislav Levin <slev@altlinux.org> 1.2.4-alt1
- Initial build for Sisyphus


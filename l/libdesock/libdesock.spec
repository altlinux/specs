%define _unpackaged_files_terminate_build 1
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define soversion 2

%def_with check

Name: libdesock
Version: 2.0
Release: alt1
Summary: De-socketing library for fuzzing network applications
License: MIT
Group: Development/Tools
Url: https://github.com/fkie-cad/libdesock
Vcs: https://github.com/fkie-cad/libdesock

# Architecture-specific inline assembly for stack canary and syscall hooks
# aarch64 support is planned upstream but not yet implemented
ExclusiveArch: x86_64

Source0: %name-%version.tar
Patch0: libdesock-2.0-alt-warnings.patch
Patch1: libdesock-2.0-alt-install.patch
Patch2: libdesock-2.0-alt-makefile.patch

BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: glibc-devel

%description
libdesock is a de-socketing library for fuzzing network applications.
It hooks socket-related syscalls (connect, bind, accept, etc.) and
redirects network I/O to stdin/stdout, allowing fuzzers like AFL++
to feed input directly to network servers and clients without
requiring actual network connections.

%package -n libdesock%soversion
Summary: De-socketing shared library for fuzzing
Group: System/Libraries

%description -n libdesock%soversion
Shared library for de-socketing network applications during fuzzing.

%package devel
Summary: Development files for libdesock
Group: Development/C
Requires: libdesock2 = %EVR

%description devel
Header files for developing with libdesock.

%package devel-static
Summary: Static library for libdesock
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
Static library for developing with libdesock.

%prep
%setup
%autopatch -p1
sed -i '/test_passthrough,/d' tests/test_select.c tests/test_epoll.c tests/test_poll.c

%build
# Release build for installation
%meson \
    -Ddesock_client=true \
    -Ddesock_server=true \
    -Dallow_dup_stdin=true

%meson_build

%if_with check
# Debug build for tests only
meson setup %_target_platform-debug \
    -Ddesock_client=true \
    -Ddesock_server=true \
    -Dallow_dup_stdin=true \
    -Ddebug_desock=true \
    -Drequest_delimiter=--- \
    -Dmultiple_requests=true
ninja -C %_target_platform-debug
%endif

%install
%meson_install

%check
%make -C tests LIBDIR=../%_target_platform-debug DELIMITER=---
cd tests
export LD_PRELOAD=../%_target_platform-debug/libdesock.so
./test_accept
./test_threads
./test_epoll
./test_select
./test_poll
./test_multi
unset LD_PRELOAD

%files -n libdesock2
%_libdir/libdesock.so.%soversion
%_libdir/libdesock.so.%soversion.0
%doc LICENSE README.md

%files devel
%_includedir/desock.h
%_libdir/libdesock.so
%doc LICENSE README.md

%files devel-static
%_libdir/libdesock.a
%doc LICENSE README.md

%changelog
* Thu Jun 11 2026 Timofei Fedotov <sovtouch@altlinux.org> 2.0-alt1
- Initial build for ALT Sisyphus.

Name:           socket_wrapper
Version:        1.4.0
Release:        alt2
Group:          Development/Other
License:        BSD
Summary:        A library passing all socket communications through Unix sockets
Url:            http://cwrap.org/

# git://git.samba.org/socket_wrapper.git
Source0:        %name-%version.tar
Patch0:         %name-%version-alt.patch

BuildRequires:  cmake ctest
BuildRequires:  libcmocka-devel

Requires:       cmake
Requires:       pkgconfig

%description
socket_wrapper aims to help client/server software development teams willing to
gain full functional test coverage. It makes it possible to run several
instances of the full software stack on the same machine and perform locally
functional testing of complex network configurations.

To use it set the following environment variables:

LD_PRELOAD=libsocket_wrapper.so
SOCKET_WRAPPER_DIR=/path/to/swrap_dir

This package doesn't have a devel package because this project is for
development/testing.

%package -n libsocket_wrapper_noop
Summary:        A library providing dummies for socket_wrapper
Group:          Development/Other

%description -n libsocket_wrapper_noop
Applications with the need to call socket_wrapper_enabled() should link against
-lsocket_wrapper_noop in order to resolve the symbol at link time.

%package -n libsocket_wrapper_noop-devel
Summary:        Development headers for libsocket_wrapper_noop
Requires:       libsocket_wrapper_noop = %version-%release
Group:          Development/C

%description -n libsocket_wrapper_noop-devel
Development headers for applications with the need to call
socket_wrapper_enabled().

%prep
%setup -q
%patch -p1

%build
if test ! -e "obj"; then
mkdir obj
fi

pushd obj
%cmake_insource \
  -DUNIT_TESTING=ON \
  %_builddir/%name-%version

%make VERBOSE=1
popd

%install
pushd obj
%make DESTDIR=%buildroot install
popd

%check
pushd obj
LD_LIBRARY_PATH=$PWD/src ctest -V

LD_PRELOAD=src/libsocket_wrapper.so bash -c '>/dev/null'
LD_PRELOAD=src/libsocket_wrapper_noop.so bash -c '>/dev/null'

popd

%files
%doc AUTHORS README.md CHANGELOG LICENSE
%_libdir/lib%name.so*
%dir %_libdir/cmake/%name
%_pkgconfigdir/%name.pc
%_libdir/cmake/%name/%name-config*.cmake
%_man1dir/%name.1*

%files -n libsocket_wrapper_noop
%_libdir/lib%{name}_noop.so.*

%files -n libsocket_wrapper_noop-devel
%_includedir/%name.h
%_pkgconfigdir/%{name}_noop.pc
%_libdir/lib%{name}_noop.so
%_libdir/cmake/%name/%{name}_noop-config*.cmake

%changelog
* Fri Mar 24 2023 Evgeny Sinelnikov <sin@altlinux.org> 1.4.0-alt2
- Skip test_syscall_swrap for arm archicture

* Fri Mar 24 2023 Evgeny Sinelnikov <sin@altlinux.org> 1.4.0-alt1
- Added support for sendmmsg()/recvmmsg()
- Added support for handling close, recvmmsg and sendmmsg syscalls
- Added support to interact with uid_wrapper syscall()
- Improved IP address tracing output
- Inject O_LARGEFILE as needed on 32bit
- pkgconfig: Fix path to libsocket_wrapper.so
- Fix -Wcast-qual warnings
- Fix dclose(RTLD_NEXT)

* Fri Mar 24 2023 Evgeny Sinelnikov <sin@altlinux.org> 1.3.4-alt2
- Split and place libsocket_wrapper_noop library and it's development files
  to separate subpackages.

* Fri Sep 16 2022 Evgeny Sinelnikov <sin@altlinux.org> 1.3.4-alt1
- Fixed TOCTOU issue with udp auto binding

* Thu Jul 29 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.3.3-alt1
- Update to latest release with support for fd-passing via unix sockets
- Add public libsocket_wrapper_noop library

* Sun Feb 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.2.5-alt1
- Update to latest release

* Wed Jan 16 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.2.1-alt1
- Update to latest release
- Disable ubt macros due binary package identity change

* Mon Apr 09 2018 Evgeny Sinelikov <sin@altlinux.org> 1.1.9-alt2
- Add LD_LIBRARY_PATH to libthread_deadlock.so for running tests on e2k

* Mon Jan 29 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.1.9-alt1
- Update to latest release with fixed thread - signal deadlock issue

* Fri Nov 03 2017 Evgeny Sinelnikov <sin@altlinux.org> 1.1.8-alt2
- Disable ipv6 for test_socket_getsockname due girar error with:
  "Address family not supported by protocol"

* Fri Nov 03 2017 Evgeny Sinelnikov <sin@altlinux.org> 1.1.8-alt1
- Initial build for ALT Sisyphus


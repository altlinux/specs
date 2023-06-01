Name:           priv_wrapper
Version:        1.0.1
Release:        alt1

Summary:        A library to disable resource limits and other privilege dropping
License:        GPL-3.0-or-later
Group:          Development/Other
Url:            http://cwrap.org/

# git://git.samba.org/priv_wrapper.git
Source:         %name-%version.tar
Patch:          %name-%version-alt.patch

BuildRequires:  gcc
BuildRequires:  cmake ctest
BuildRequires:  libcmocka-devel >= 1.1.0

Requires:       cmake
Requires:       pkgconfig

%description
priv_wrapper aims to help running processes which are dropping privileges or
are restricting resources in test environments.
It can disable chroot, prctl, pledge and setrlmit system calls. A disabled call
always succeeds (i.e. returns 0) and does nothing.
The system call pledge exists only on OpenBSD.

To use it, set the following environment variables:

LD_PRELOAD=libpriv_wrapper.so
PRIV_WRAPPER_CHROOT_DISABLE=1

This package does not have a devel package, because this project is for
development/testing.

%prep
%setup
%patch -p1

%build
%cmake \
  -DUNIT_TESTING=ON
%cmake_build

%install
%cmake_install

%check
pushd %_cmake__builddir
%make test
popd

%files
%doc AUTHORS README.md CHANGELOG.md LICENSE
%_libdir/libpriv_wrapper.so*
%dir %_libdir/cmake/priv_wrapper
%_libdir/cmake/priv_wrapper/priv_wrapper-config-version.cmake
%_libdir/cmake/priv_wrapper/priv_wrapper-config.cmake
%_libdir/pkgconfig/priv_wrapper.pc
%_man1dir/priv_wrapper.*

%changelog
* Mon May 29 2023 Evgeny Sinelnikov <sin@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.


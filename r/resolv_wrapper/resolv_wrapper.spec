Name:           resolv_wrapper
Version:        1.1.8
Release:        alt1

Summary:        A wrapper for dns name resolving or dns faking
License:        BSD
Group:          Development/Other
Url:            http://cwrap.org/

# git://git.samba.org/resolv_wrapper.git
Source:        %name-%version.tar
Patch:         %name-%version-alt.patch

BuildRequires:  cmake ctest
BuildRequires:  libcmocka-devel
BuildRequires:  socket_wrapper

Requires:       cmake
Requires:       pkgconfig

%description
It is likely that if you have a server/client architecture, you need to do DNS
queries or a third party library, like Kerberos needs to be able to do queries.
In the case of Kerberos the client needs to look the address of the KDC up via a
SRV record. resolv_wrapper is able to either redirect all DNS queries to your
DNS server implementation, or fake DNS replies!

To use it set the following environment variables:

LD_PRELOAD=libresolv_wrapper.so
RESOLV_WRAPPER_CONF=./my_resolv.conf

This package doesn't have a devel package because this project is for
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
%doc AUTHORS README.md CHANGELOG LICENSE
%_libdir/libresolv_wrapper.so*
%dir %_libdir/cmake/resolv_wrapper
%_libdir/cmake/resolv_wrapper/resolv_wrapper-config-version.cmake
%_libdir/cmake/resolv_wrapper/resolv_wrapper-config.cmake
%_libdir/pkgconfig/resolv_wrapper.pc
%_man1dir/resolv_wrapper.1*

%changelog
* Fri Mar 24 2023 Evgeny Sinelnikov <sin@altlinux.org> 1.1.8-alt1
- Fix issues with glibc >= 2.34

* Thu Jan 27 2022 Evgeny Sinelnikov <sin@altlinux.org> 1.1.7-alt2
- Fix detection of a fully seperate libresolv. With glibc 2.24 all res_
  symbols moved from libresolv to libc, so only DNS faking avaialble now.

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 1.1.7-alt1.1
- NMU: spec: adapted to new cmake macros.

* Sun Feb 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.1.7-alt1
- Initial build for ALT Sisyphus


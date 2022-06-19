%define oname crc32c

Name: libcrc32c
Version: 1.1.2
Release: alt1

Summary: CRC32C implementation with support for CPU-specific acceleration instructions

License: BSD
Group: System/Libraries
Url: https://github.com/google/crc32c

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/google/crc32c/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%description
This project collects a few CRC32C implementations under an umbrella that
dispatches to a suitable implementation based on the host computer's hardware
capabilities. CRC32C is specified as the CRC that uses the iSCSI polynomial in
RFC 3720. The polynomial was introduced by G. Castagnoli, S. Braeuer and M.
Herrmann. CRC32C is used in software such as Btrfs, ext4, Ceph and leveldb.

%package devel
Summary: Development files for %oname
Requires: %name = %EVR
Group: Development/C

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %oname.

%prep
%setup

%build
# NOTE(mhayden): Thanks to the Arch Linux developers for providing ideas on how
# to compile this properly. https://aur.archlinux.org/packages/google-crc32c/
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=yes \
    -DCRC32C_BUILD_BENCHMARKS=OFF \
    -DCRC32C_BUILD_TESTS=OFF \
    -DCRC32C_USE_GLOG=OFF
%cmake_build

%install
%cmake_install

%check
#ctest

%files
%_libdir/lib%oname.so.*

%files devel
%doc LICENSE
%doc README.md
%_libdir/lib%oname.so
%_libdir/cmake/Crc32c/
%_includedir/%oname/

%changelog
* Wed Jun 15 2022 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- initial build for ALT Sisyphus

* Fri Jun 03 2022 Major Hayden <major@redhat.com> 1.1.2-3
- Drop period from cmake line

* Tue May 10 2022 Major Hayden <major@mhtx.net> 1.1.2-1
- Update to 1.1.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 09 2021 Major Hayden <major@mhtx.net> 1.1.1-2
- Move to rpmautospec

* Mon Aug 23 2021 Major Hayden <major@mhtx.net> 1.1.1-1
- Initial import (#1983175)

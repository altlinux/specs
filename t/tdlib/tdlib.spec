# TODO: use system sqlite

# Enable or disable clang compiler...
%def_with clang

Name: tdlib
Version: 1.3.0
Release: alt2

Summary: Cross-platform library for building Telegram clients

License: Boost
Group: Development/C++
Url: https://github.com/tdlib/td

ExcludeArch: %ix86

# Source-url: %url/archive/v%version.tar.gz#/%name-%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

Patch: %name-system-crypto.patch

BuildRequires(pre): rpm-macros-ninja-build
BuildRequires: gperftools-devel
BuildRequires: libssl-devel
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: gperf
BuildRequires: zlib-devel
BuildRequires: cmake

BuildRequires(pre): rpm-build-intro >= 2.1.5

%if_with clang
BuildRequires: clang
BuildRequires: llvm
%remove_optflags -frecord-gcc-switches
%endif

# Building with default settings require at least 16 GB of free RAM.
# Builds on ARM and other low-memory architectures are failing.
#ExclusiveArch: %ix86 x86_64

# use no more than system_memory/2300 build procs (see https://bugzilla.altlinux.org/show_bug.cgi?id=35112)
%_tune_parallel_build_by_procsize 6300

%description
TDLib (Telegram Database library) is a cross-platform library for
building Telegram clients. It can be easily used from almost any
programming language.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%package static
Summary: Static libraries for %name
Group: Development/C++
Requires: %name = %EVR
Requires: %name-devel = %EVR

%description devel
%summary.

%description static
%summary.

%prep
%setup
%patch -p1

# Adding missing SOVERSION for shared libraries...
echo "set_property(TARGET tdclient PROPERTY SOVERSION \${TDLib_VERSION})" >> CMakeLists.txt
echo "set_property(TARGET tdjson PROPERTY SOVERSION \${TDLib_VERSION})" >> CMakeLists.txt

# Patching LIBDIR path...
sed -e 's@DESTINATION lib@DESTINATION %_lib@g' -e 's@lib/@%_lib/@g' -i CMakeLists.txt
%__subst 's@DESTINATION lib@DESTINATION %_lib@g' {sqlite,tdactor,tddb,tdnet,tdutils}/CMakeLists.txt

%build
%if_with clang
export CC=clang
export CXX=clang++
%endif

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release

%ninja_build -C BUILD

%install
%ninja_install -C BUILD
# disable static
rm -fv %buildroot%_libdir/*.a

%files
%doc LICENSE_1_0.txt
%doc README.md CHANGELOG.md
%_libdir/libtd*.so.%version

%files devel
%_includedir/td
%_libdir/libtd*.so
%_libdir/cmake/Td

#%files static
#%_libdir/libtd*.a

%changelog
* Sun Dec 16 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt2
- build with clang
- disable i586 build

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- initial build for ALT Sisyphus

* Sun Sep 16 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3.0-2
- Fixed issue with crypto policies.

* Sat Sep 15 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3.0-1
- Initial SPEC release.

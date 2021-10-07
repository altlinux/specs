Name: libleveldb
Version: 1.23
Release: alt1

Summary: A fast and lightweight key/value database library by Google

License: BSD
Group: Development/Databases
Url: https://github.com/google/leveldb

Packager: Alexei Takaseev <taf@altlinux.ru>

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

## patches from Fedora
Patch0001: 0001-Allow-leveldbjni-build.patch
Patch0002: 0002-Added-a-DB-SuspendCompations-and-DB-ResumeCompaction.patch
Patch0003: 0003-allow-Get-calls-to-avoid-copies-into-std-string.patch
Patch0004: 0004-bloom_test-failure-on-big-endian-archs.patch
Patch0006: 0006-revert-no-rtti.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libsnappy-devel
# Can't build ceph with external crc32c libs
#BuildRequires: libcrc32c-devel

%description
LevelDB is a fast key-value storage library written at Google that provides an
ordered mapping from string keys to string values.

%package devel
Summary: The development files for %name
Group: Development/Databases
Requires: %name = %version-%release

%description devel
Additional header files for development with %name.

%prep
%setup
%autopatch -p1

cat > leveldb.pc << EOF
prefix=%prefix
exec_prefix=%prefix
libdir=%_libdir
includedir=%_includedir

Name: leveldb
Description: %summary
Version: %version
Libs: -lleveldb
EOF

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DLEVELDB_BUILD_TESTS:BOOL=OFF \
	-DLEVELDB_BUILD_BENCHMARKS:BOOL=OFF
%cmake_build

%install
%cmakeinstall_std

mkdir -p %buildroot%_pkgconfigdir
cp -a leveldb.pc %buildroot%_pkgconfigdir/

%files
%doc AUTHORS LICENSE README.md
%_libdir/%name.so.*

%files devel
%doc doc
%_includedir/leveldb
%_libdir/%name.so
%_pkgconfigdir/*
%_libdir/cmake/leveldb

%changelog
* Thu Oct 07 2021 Alexey Shabalin <shaba@altlinux.org> 1.23-alt1
- 1.23

* Tue May 07 2019 Alexei Takaseev <taf@altlinux.org> 1.22-alt2
- Fix leveldb.pc file

* Mon May 06 2019 Alexei Takaseev <taf@altlinux.org> 1.22-alt1
- 1.22
- Remove unneeded patch leveldb-0002-Add-memory-barrier-on-PowerPC.patch
- Re-applay Fedore patches:
    * leveldb-0003-bloom_test-failure-on-big-endian-archs.patch
    * leveldb-0004-Allow-leveldbjni-build.patch
    * leveldb-0005-Added-a-DB-SuspendCompations-and-DB-ResumeCompaction.patch
    * leveldb-0006-allow-Get-calls-to-avoid-copies-into-std-string.patch
- Use CMAKE build system

* Mon Sep 25 2017 Alexei Takaseev <taf@altlinux.org> 1.20-alt1
- 1.20 (ALT#33915)

* Fri Aug 12 2016 Alexei Takaseev <taf@altlinux.org> 1.19-alt1
- 1.19

* Sat May 28 2016 Alexei Takaseev <taf@altlinux.org> 1.18-alt1
- 1.18

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.17-alt3
- NMU: added fedora patches for
  * leveldbjni support
  * arm/ppc support

* Thu May 28 2015 Alexei Takaseev <taf@altlinux.org> 1.17-alt2
- rebuild with gcc-c++ 5.1

* Fri May 02 2014 Alexei Takaseev <taf@altlinux.org> 1.17-alt1
- 1.17

* Tue Mar 04 2014 Alexei Takaseev <taf@altlinux.org> 1.16-alt1
- 1.16

* Tue Apr 16 2013 Alexei Takaseev <taf@altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus

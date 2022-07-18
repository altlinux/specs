Name: libmanticore-columnar
Version: 1.15.4
Release: alt1

Summary: Manticore Columnar Library is a column-oriented storage library, aiming to provide decent performance with low memory footprint at big data volume

License: Apache-2.0
Group: Text tools
Url: https://github.com/manticoresoftware/columnar

# Source-url: https://github.com/manticoresoftware/columnar/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Patch1: %name.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

BuildRequires: libfastpfor-devel
BuildRequires: libpgm-index-devel

ExclusiveArch: x86_64

%description
Manticore Columnar Library is a column-oriented storage library,
aiming to provide decent performance with low memory footprint at big data volume.
When used in combination with Manticore Search can be beneficial for faster / lower
resource consumption log/metrics analytics and running log / metric analytics in docker / kubernetes.

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Header files for %name.

%prep
%setup
%patch1 -p2
# fix for use libpgm-index-devel
subst "s|.*GetPGM.*||" secondary/CMakeLists.txt
subst "s|pgmindexlib||" secondary/CMakeLists.txt

%build
%cmake_insource

%install
%makeinstall_std
mkdir -p %buildroot%_libdir/
# TODO: fix MODULES_DIR
mv %buildroot/usr/share/manticore/modules/lib_manticore_columnar.so %buildroot%_libdir
mv %buildroot/usr/share/manticore/modules/lib_manticore_secondary.so %buildroot%_libdir
subst "s|/share/manticore/modules/|/%_lib/|" %buildroot%_libdir/cmake/columnar/columnar-targets*.cmake

%files
%doc README.md
%_libdir/lib*.so

%files devel
%_includedir/manticore-columnar-lib/
%_libdir/cmake/columnar/

%changelog
* Mon Jun 27 2022 Vitaly Lipatov <lav@altlinux.ru> 1.15.4-alt1
- new version 1.15.4 (with rpmrb script)

* Tue Dec 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.12.2-alt1
- initial build for ALT Sisyphus

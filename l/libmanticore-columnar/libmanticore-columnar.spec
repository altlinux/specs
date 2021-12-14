Name: libmanticore-columnar
Version: 1.12.2
Release: alt1

Summary: Manticore Columnar Library is a column-oriented storage library, aiming to provide decent performance with low memory footprint at big data volume

License: Apache-2.0
Group: Text tools
Url: https://github.com/manticoresoftware/columnar

# untagged 1.12.2
# Source-url: https://github.com/manticoresoftware/columnar/archive/69d37801adfaa2d6bc91d41cd6794a7fa7ae19f3.zip
Source: %name-%version.tar

Patch1: %name.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

BuildRequires: libfastpfor-devel

ExclusiveArch: x86_64

%description
Manticore Columnar Library is a column-oriented storage library,
aiming to provide decent performance with low memory footprint at big data volume.
When used in combination with Manticore Search can be beneficial for faster / lower
resource consumption log/metrics analytics and running log / metric analytics in docker / kubernetes

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Header files for %name.

%prep
%setup
%patch1 -p2

%build
%cmake_insource

%install
%makeinstall_std
mkdir -p %buildroot%_libdir/
mv %buildroot/usr/share/manticore/modules/lib_manticore_columnar.so %buildroot%_libdir
subst "s|/share/manticore/modules/|/%_lib/|" %buildroot%_libdir/cmake/columnar/columnar-targets-relwithdebinfo.cmake

%files
%doc README.md
%_libdir/lib*.so

%files devel
%_includedir/manticore-columnar-lib/
%_libdir/cmake/columnar/

%changelog
* Tue Dec 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.12.2-alt1
- initial build for ALT Sisyphus

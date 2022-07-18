Name: libpgm-index
Version: 1.0
Release: alt1

Summary: State-of-the-art learned data structure that enables fast lookup, predecessor, range searches and updates in arrays

License: Apache-2.0
Group: Text tools
Url: https://github.com/tomatolog/PGM-index

# latest
# Source-url: https://github.com/tomatolog/PGM-index/archive/refs/heads/master.zip
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

ExclusiveArch: x86_64

%description
The Piecewise Geometric Model index (PGM-index) is a data structure that enables fast lookup,
predecessor, range searches and updates in arrays of billions of items using orders of magnitude
less space than traditional indexes while providing the same worst-case query time guarantees.

%package devel
Summary: Header files for %name
Group: Development/C
#Requires: %name = %EVR

%description devel
The Piecewise Geometric Model index (PGM-index) is a data structure that enables fast lookup,
predecessor, range searches and updates in arrays of billions of items using orders of magnitude
less space than traditional indexes while providing the same worst-case query time guarantees.

%prep
%setup

%build
%cmake_insource

%install
#makeinstall_std
mkdir -p %buildroot/%_includedir/
cp -a include/pgm %buildroot/%_includedir/

%files devel
%doc README.md
#_libdir/cmake/
%_includedir/pgm/

%changelog
* Mon Jun 27 2022 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus

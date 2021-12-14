%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Name: libfastpfor
Version: 0.1.9
Release: alt1

Summary: The FastPFOR C++ library: Fast integer compression

License: Apache-2.0
Group: Text tools
Url: https://github.com/lemire/FastPFor

# latest
# Source-url: https://github.com/lemire/FastPFor/archive/refs/heads/master.zip
Source: %name-%version.tar

Source1: CMakeLists.txt

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

BuildRequires: libsnappy-devel

ExclusiveArch: x86_64

%add_optflags -fPIC


%description
The FastPFOR C++ library: Fast integer compression.

%package devel
Summary: Header files for %name
Group: Development/Other
#Requires: %name = %EVR

%description devel
Header files for %name.

%prep
%setup
cp -fv %SOURCE1 .

%build
%cmake_insource

%install
%makeinstall_std
# hack
mv %buildroot/usr/lib %buildroot%_libdir/
mv %buildroot/%_libdir/Release/*.a %buildroot%_libdir/
subst "s|/lib/Release|/%_lib|" %buildroot%_libdir/cmake/FastPFOR/*.cmake

%files devel
%doc AUTHORS README.md TODO.md
%_libdir/*.a
%_libdir/cmake/
%_includedir/fastpfor/

%changelog
* Tue Dec 14 2021 Vitaly Lipatov <lav@altlinux.ru> 0.1.9-alt1
- initial build for ALT Sisyphus

Name:     libchdr
Version:  0.1
Release:  alt1

Summary:  Standalone library for reading MAME's CHDv1-v5 formats
License:  GPL2
Group:    Emulators
Url:      https://github.com/rtissera/libchdr

Packager: Artyom Bystrov <arbars@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ zlib-devel

%description
Standalone library for reading MAME's CHDv1-v5 formats

%package devel
Summary:  Standalone library for reading MAME's CHDv1-v5 formats devel headers
License:  GPL2
Group:    Emulators


%description devel
Standalone library for reading MAME's CHDv1-v5 formats - devel headers

%prep
%setup

%build
%cmake  -DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_C_FLAGS_RELEASE="-DNDEBUG" \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DWITH_SYSTEM_ZLIB=ON \
		-Wno-dev
%cmake_build

%install

%cmake_install

%files

%doc LICENSE.txt
%_includedir/%name/*

%files devel
%doc LICENSE.txt
%_libdir/%name.so*
%_libdir/pkgconfig/%name.pc
%changelog
* Sun Jan 15 2022 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial build for Sisyphus

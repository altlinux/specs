Name: alacenc
Version: 0.4.1
Release: alt1

Summary: encode audio into the Apple Lossless Audio Codec (ALAC) format
License: MIT
Group: Sound

URL: https://github.com/flacon/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/flacon/%name/archive/v%version/%name-%version.tar.gz
Source: https://github.com/flacon/%name/archive/v%version/%name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++

%description
%name - encode audio into the Apple Lossless Audio Codec (ALAC) format

%prep
%setup
%ifarch %e2k
# should be named WhitelistedUnportable
sed -i "s/__aarch64__/__e2k__/" vendor/alac/codec/EndianPortable.c
%endif

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name

%changelog
* Sun Jun 02 2024 Nazarov Denis <nenderus@altlinux.org> 0.4.1-alt1
- New version 0.4.1.

* Thu Oct 05 2023 Nazarov Denis <nenderus@altlinux.org> 0.4.0-alt1
- New version 0.4.0.

* Sat Jul 01 2023 Nazarov Denis <nenderus@altlinux.org> 0.3.0-alt1.2
- Fix FTBFS

* Wed May 18 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.3.0-alt1.1
- Fixed build for Elbrus

* Mon May 16 2022 Nazarov Denis <nenderus@altlinux.org> 0.3.0-alt1
- Initial build for ALT Linux

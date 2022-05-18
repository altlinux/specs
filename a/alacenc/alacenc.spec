Name: alacenc
Version: 0.3.0
Release: alt1.1

Summary: encode audio into the Apple Lossless Audio Codec (ALAC) format
License: MIT
Group: Sound

URL: https://github.com/flacon/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: %arm ppc64le

# https://github.com/flacon/%name/archive/v%version/%name-%version.tar.gz
Source: https://github.com/flacon/%name/archive/v%version/%name-%version.tar

# Automatically added by buildreq on Mon May 16 2022 (-bi)
# optimized out: cmake-modules debugedit elfutils glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libgpg-error libsasl2-3 libstdc++-devel rpm-build-file sh4
BuildRequires: cmake gcc-c++

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
* Wed May 18 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.3.0-alt1.1
- Fixed build for Elbrus

* Mon May 16 2022 Nazarov Denis <nenderus@altlinux.org> 0.3.0-alt1
- Initial build for ALT Linux

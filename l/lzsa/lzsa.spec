Name:    lzsa
Version: 1.4.1
Release: alt1

Summary: Byte-aligned, efficient lossless packer that is optimized for fast decompression on 8-bit micros
License: zlib
Group:   System/Libraries
Url:     https://github.com/emmanuel-marty/lzsa

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires: clang make

%description
%summary

%prep
%setup

%build
%make_build

%install
mkdir -p %buildroot%_bindir
install -p -m 0775 %name %buildroot%_bindir/%name

%files
%doc *.md
%_bindir/*

%changelog
* Mon Feb 05 2024 Artyom Bystrov <arbars@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus

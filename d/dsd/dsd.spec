Name:     dsd
Version:  1.7.0
Release:  alt1.20150806%ubt

Summary:  Digital Speech Decoder
License:  GPLv2+
Group:    Engineering
Url:      https://github.com/szechyjs/dsd

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-build-ubt
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(sndfile)
BuildRequires: mbelib-devel
BuildRequires: pkgconfig(itpp)
BuildRequires: pkgconfig(portaudio-2.0)

%description
DSD is able to decode several digital voice formats
from discriminator tap audio and synthesize the
decoded speech. Speech synthesis requires mbelib,
which is a separate package.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/%name

%changelog
* Thu Jan 25 2018 Anton Midyukov <antohami@altlinux.org> 1.7.0-alt1.20150806%ubt
- Initial build for Sisyphus

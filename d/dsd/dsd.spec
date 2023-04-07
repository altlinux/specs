Name:     dsd
Version:  1.7.0
Release:  alt4.git59423fa

Summary:  Digital Speech Decoder
License:  GPL-2.0+
Group:    Engineering
Url:      https://github.com/szechyjs/dsd

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
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
* Fri Apr 07 2023 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt4.git59423fa
- Returned to Sisyphus.
- Updated from upstream repository.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt3.20150806.1
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt2.20150806.1
- NMU: remove %ubt from release

* Wed Jun 27 2018 Anton Midyukov <antohami@altlinux.org> 1.7.0-alt1.20150806%ubt.1
- Rebuilt for aarch64

* Thu Jan 25 2018 Anton Midyukov <antohami@altlinux.org> 1.7.0-alt1.20150806%ubt
- Initial build for Sisyphus

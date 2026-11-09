Name: spi-tools
Version: 1.2.0
Release: alt1

Summary: Simple command line tools to help using Linux spidev devices
License: GPL-2.0-only
Group: System/Kernel and hardware
URL: https://github.com/cpb-/spi-tools
VCS: https://github.com/cpb-/spi-tools

Source:   %name-%version.tar

Buildrequires(pre): rpm-macros-cmake
Buildrequires: rpm-build-cmake
Buildrequires: help2man

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/*
%_man1dir/*.1.*
%doc README.md LICENSE

%changelog
* Mon Nov 09 2026 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- New version 1.2.0.

* Wed Jul 15 2026 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- New version 1.1.0.

* Mon Nov 10 2025 Anton Midyukov <antohami@altlinux.org> 1.0.2-alt1
- New version 1.0.2.

* Sat Oct 02 2021 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- new version 1.0.0
- fix Group tag

* Sun Jun 27 2021 Anton Midyukov <antohami@altlinux.org> 0.8.7-alt1
- new version 0.8.7

* Sun Mar 22 2020 Anton Midyukov <antohami@altlinux.org> 0.8.4-alt1
- new version 0.8.4

* Thu Apr 25 2019 Anton Midyukov <antohami@altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus

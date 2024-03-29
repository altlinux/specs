Name: mesaflash
Version: 3.4.9
Release: alt2
Summary: Configuration and diagnostic tool for Mesa Electronics boards
License: GPL-2.0-or-later
Group: Engineering
Url: https://github.com/LinuxCNC/mesaflash
Source0: %name-%version.tar

ExcludeArch: ppc64le

BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(libmd)

%description
Configuration and diagnostic tool for Mesa Electronics
PCI(E)/ETH/EPP/USB/SPI boards.

%prep
%setup
# Remove binary files
rm -rf *.dll *.sys libpci

%build
%make_build OWNERSHIP=""

%install
%makeinstall DESTDIR="%buildroot%_prefix" OWNERSHIP=""

%files
%doc README.md
%_bindir/%name
%_mandir/man1/*.1*

%changelog
* Mon Oct 23 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 3.4.9-alt2
- Build on more architectures. Note that PCI and EPP cards are supported
  on x86_64 (and i586) only (as ever).
- Simplified spec (USE_STUBS has been removed in commit
  7b2cb3abcdd17502a7625a7efd)

* Mon Oct 23 2023 Anton Midyukov <antohami@altlinux.org> 3.4.9-alt1
- new version 3.4.9

* Mon Sep 11 2023 Anton Midyukov <antohami@altlinux.org> 3.4.6-alt1
- new version 3.4.6

* Sun Jun 13 2021 Anton Midyukov <antohami@altlinux.org> 3.4.0-alt1.20210527
- Initial build

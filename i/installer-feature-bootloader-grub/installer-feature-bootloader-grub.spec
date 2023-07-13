Name: installer-feature-bootloader-grub
Version: 0.1.0
Release: alt4

Summary: Installer bootloader step for stage 3 (alterator-grub)
License: GPL-2.0-or-later
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

ExcludeArch: %arm

Requires: alterator-grub

%description
This used in mkimage-profiles (feature bootloader),
to explicitly not install the alterator-grub package.

%files

%changelog
* Thu Jul 13 2023 Anton Midyukov <antohami@altlinux.org> 0.1.0-alt4
- ExcludeArch: %%arm
- fix typo in summary (Closes: 46901)

* Wed May 24 2023 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt3
- Bump the release in order to allow other versions in branches.

* Fri Sep 11 2020 Michael Shigorin <mike@altlinux.org> 0.1.0-alt2
- It's not noarch if ExclusiveArch: is specified (see also #38919)

* Fri Jun 05 2020 Anton Midyukov <antohami@altlinux.org> 0.1.0-alt1
- Initial build

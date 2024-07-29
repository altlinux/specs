%define _unpackaged_files_terminate_build 1

Name: fwupd-efi
Version: 1.6
Release: alt1
License: LGPLv2+

Group: System/Configuration/Hardware
Url: https://github.com/fwupd/fwupd-efi
Summary: EFI Application used by uefi-capsule plugin in fwupd

Source: %name-%version.tar
Patch0: %name-%version-alt.patch
ExclusiveArch: x86_64 aarch64

BuildRequires: meson
BuildRequires: gnu-efi
BuildRequires: python3-module-pefile

%description
fwupd-efi is the UEFI binary used with fwupd for installing UEFI
firmware updates.

%package checkinstall
Group: System/Configuration/Hardware
Summary: Verify EFI signature
Requires: %name = %EVR
Requires(post): rpm-pesign-checkinstall

%description checkinstall
fwupd-efi is the UEFI binary used with fwupd for installing UEFI
firmware updates.

This package enables EFI signature verification.

%prep
%setup
%patch0 -p1

%build
%meson \
    -Defi-ldsdir="%_libdir" \
    -Defi_sbat_distro_id="altlinux" \
    -Defi_sbat_distro_summary="ALT Linux" \
    -Defi_sbat_distro_pkgname="%name" \
    -Defi_sbat_distro_version="%version-%release" \
    -Defi_sbat_distro_url="http://git.altlinux.org/gears/f/%{name}.git"

%meson_build

%install
%meson_install

%files
%_libdir/efi/fwupd*.efi
%_libdir/pkgconfig/fwupd-efi.pc

%files checkinstall

%changelog
* Mon Jul 22 2024 Egor Ignatov <egori@altlinux.org> 1.6-alt1
- 1.6

* Wed May 15 2024 Egor Ignatov <egori@altlinux.org> 1.5-alt2
- bumped release to pesign with the new key

* Mon Mar 25 2024 Egor Ignatov <egori@altlinux.org> 1.5-alt1
- 1.5

* Wed Jun 14 2023 Egor Ignatov <egori@altlinux.org> 1.4-alt2
- add fwupd-efi-checkinstall subpackage for automatic EFI signature
  verification

* Wed Feb 01 2023 Egor Ignatov <egori@altlinux.org> 1.4-alt1
- 1.4

* Wed May 04 2022 Nikolai Kostrigin <nickel@altlinux.org> 1.3-alt1
- new version

* Tue Jan 25 2022 Nikolai Kostrigin <nickel@altlinux.org> 1.2-alt1
- new version
- spec: revert sbat-clarify-project-URL patch addition

* Thu Sep 16 2021 Nikolai Kostrigin <nickel@altlinux.org> 1.1-alt2
- add sbat-clarify-project-URL patch

* Wed Jun 23 2021 Egor Ignatov <egori@altlinux.org> 1.1-alt1
- first build for ALT

%define orig_name gnu-efi

Name: gnu-efi-3.0.5
Version: 3.0.5
Release: alt0.1

Summary: Building EFI applications using the GNU toolchain
# Intel and HP's BSD-like license, except setjmp code coming from GRUB
License: GPL v2+ (setjmp code), BSD-like (all the rest)
Group: Development/Other

Url: http://gnu-efi.sourceforge.net/
Source: %orig_name-%version.tar.bz2
Patch01: 0001-arm64-efi-remove-pointless-dummy-.reloc-section.patch
Patch02: 0001-Mark-our-explicit-fall-through-so-Wextra-will-work-i.patch
Patch03: 0002-Fix-some-types-gcc-doesn-t-like.patch
Patch04: 0003-Fix-arm-build-paths-in-the-makefile.patch
Patch05: 0004-Work-around-Werror-maybe-uninitialized-not-being-ver.patch
Patch06: 0005-Fix-a-sign-error-in-the-debughook-example-app.patch
Patch07: 0006-Fix-typedef-of-EFI_PXE_BASE_CODE.patch
Patch08: 0007-make-clang-not-complain-about-fno-merge-constants.patch
Patch09: 0008-Fix-another-place-clang-complains-about.patch
Patch10: 0009-route80h-remove-some-dead-code.patch
Patch11: 0010-Make-clang-not-complain-about-the-debughook-s-optimi.patch
Patch12: 0011-Nerf-Werror-pragma-away.patch
Patch13: 0012-Make-ia32-use-our-own-div-asm-on-gnu-C-as-well.patch
Patch14: 0013-Call-ar-in-deterministic-mode.patch

BuildRequires: binutils >= 2.17.50.0.14
BuildRequires: gcc >= 4.1.1
Requires: binutils >= 2.17.50.0.14
Requires: gcc >= 4.1.1
ExclusiveArch: %ix86 x86_64 aarch64

%description
GNU-EFI development environment allows to create EFI applications
for IA-64 and x86 platforms using the GNU toolchain.

%prep
%setup -n %orig_name-%version
%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch04 -p1
%patch05 -p1
%patch06 -p1
%patch07 -p1
%patch08 -p1
%patch09 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

%build
%make
%make apps

%install
%make install INSTALLROOT=%buildroot PREFIX=%prefix LIBDIR=%_libdir

%files
%doc ChangeLog README.* apps
%_libdir/libefi.a
%_libdir/libgnuefi.a
%_libdir/crt0-efi-*.o
%_libdir/elf_*_efi.lds
%_includedir/efi

%changelog
* Thu Nov 23 2017 L.A. Kostis <lakostis@altlinux.ru> 3.0.5-alt0.1
- Downgrade to 3.0.5 (3.0.6 probably broken again).
- Sync with fc27 3.0.5-11.

* Mon Nov 20 2017 L.A. Kostis <lakostis@altlinux.ru> 1:3.0.6-alt0.1
- Updated to 3.0.6.
- No more drugs: renamed back to gnu-efi.
- Added aarch64/Remove ia64 targets.

* Wed Mar 01 2017 Michael Shigorin <mike@altlinux.org> 3.0u-alt4
- FTBFS workaround: use gcc4.7

* Mon Nov 25 2013 Michael Shigorin <mike@altlinux.org> 3.0u-alt3
- renamed to gnu-efi-3.0u to be packaged along with 3.0r

* Fri Nov 15 2013 Michael Shigorin <mike@altlinux.org> 3.0u-alt2
- drop extra options (both build and defaults) as per:
  + upstream recommendations regarding defaults;
  + gentoo portage's 3.0u build;
  + architectures supported by ALT Linux
- refind-0.7.x built with this gnu-efi doesn't hang anymore ;-)

* Mon Jul 29 2013 Michael Shigorin <mike@altlinux.org> 3.0u-alt1
- 3.0u

* Thu Feb 28 2013 Michael Shigorin <mike@altlinux.org> 3.0t-alt1
- 3.0t: works again

* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 3.0s-alt1
- 3.0s: results in broken elilo build (silent hang, reported upstream)

* Wed Oct 17 2012 Michael Shigorin <mike@altlinux.org> 3.0r-alt1
- 3.0r

* Wed Oct 17 2012 Michael Shigorin <mike@altlinux.org> 3.0q-alt1
- built for Sisyphus; these PLD people worked on the spec:
  baggins glen qboosh

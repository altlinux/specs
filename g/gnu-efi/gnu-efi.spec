%define _unpackaged_files_terminate_build 1
%define efidir altlinux

Name: gnu-efi
Version: 3.0.18
Release: alt2
Epoch: 1

Summary: Building EFI applications using the GNU toolchain
License: BSD-2-Clause AND BSD-2-Clause-Patent AND BSD-3-Clause AND BSD-4-Clause AND GPL-2.0-or-later AND GPL-2.0-only
Group: Development/Other

Url: http://gnu-efi.sourceforge.net/
VCS: https://git.code.sf.net/p/gnu-efi/code
Source: %name-%version.tar
Patch: %name-%version-%release.patch
ExclusiveArch: %ix86 x86_64 armh aarch64
Conflicts: gnu-efi-3.0r gnu-efi-3.0u gnu-efi-3.0.5

BuildRequires: gcc-c++

%description
GNU-EFI development environment allows to create EFI applications
for IA-64 and x86 platforms using the GNU toolchain.

%prep
%setup
%patch0 -p1

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
%_libdir/gnuefi
%_includedir/efi
%_pkgconfigdir/gnu-efi.pc

%changelog
* Wed Jul 24 2024 Egor Ignatov <egori@altlinux.org> 1:3.0.18-alt2
- disable 32-bit gni-efi toolchain on x86_64

* Wed May 15 2024 Egor Ignatov <egori@altlinux.org> 1:3.0.18-alt1
- 3.0.18

* Fri Oct 23 2020 Nikolai Kostrigin <nickel@altlinux.org> 1:3.0.12-alt1
- 3.0.12
  + rediff armh patch

* Sat Oct 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:3.0.9-alt2
- rebuilt for armh

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1:3.0.9-alt1
- up to 3.0.9 with fixes from git

* Tue Aug 07 2018 Anton Farygin <rider@altlinux.ru> 1:3.0.8-alt2
- rebuilt for aarch64

* Tue Apr 24 2018 Anton Farygin <rider@altlinux.ru> 1:3.0.8-alt1
- added ubt

* Wed Mar 28 2018 Anton Farygin <rider@altlinux.ru> 1:3.0.8-alt1
- 3.0.8

* Mon Mar 05 2018 Anton Farygin <rider@altlinux.ru> 1:3.0.6-alt2
- built 32-bit gni-efi toolchain on x86_64

* Sun Nov 26 2017 Anton Farygin <rider@altlinux.ru> 1:3.0.6-alt1
- 3.0.6

* Fri Nov 24 2017 Anton Farygin <rider@altlinux.ru> 1:3.0.5-alt1
- 3.0.5
- drop wrapping

* Wed Mar 01 2017 Michael Shigorin <mike@altlinux.org> 3.0u-alt4
- FTBFS workaround: use gcc4.7

* Mon Nov 25 2013 Michael Shigorin <mike@altlinux.org> 3.0r-alt2
- turned into a wrapper package

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

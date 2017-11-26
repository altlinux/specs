Name: gnu-efi
Version: 3.0.6
Release: alt1
Epoch: 1
Summary: Building EFI applications using the GNU toolchain
# Intel and HP's BSD-like license, except setjmp code coming from GRUB
License: GPL v2+ (setjmp code), BSD-like (all the rest)
Group: Development/Other

Url: http://gnu-efi.sourceforge.net/
# git https://git.code.sf.net/p/gnu-efi/code
Source: %name-%version.tar
Patch1: gnu-efi-3.0.6-redhat-fix-some-types-gcc-doesn-t-like.patch
ExclusiveArch: %ix86 x86_64 aarch64
Conflicts: gnu-efi-3.0r gnu-efi-3.0u gnu-efi-3.0.5

%description
GNU-EFI development environment allows to create EFI applications
for IA-64 and x86 platforms using the GNU toolchain.

%prep
%setup
%patch1 -p1

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

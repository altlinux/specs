%define origname gnu-efi
%define flavour 3.0u

Name: %origname-%flavour
Version: %flavour
Release: alt3

Summary: Building EFI applications using the GNU toolchain
# Intel and HP's BSD-like license, except setjmp code coming from GRUB
License: GPL v2+ (setjmp code), BSD-like (all the rest)
Group: Development/Other

Url: http://gnu-efi.sourceforge.net/
Source: http://downloads.sourceforge.net/gnu-efi/%{origname}_%version.orig.tar.gz

BuildRequires: binutils >= 2.17.50.0.14
BuildRequires: gcc >= 4.1.1
Requires: binutils >= 2.17.50.0.14
Requires: gcc >= 4.1.1
ExclusiveArch: %ix86 x86_64 ia64

Summary(pl.UTF-8): Tworzenie aplikacji EFI przy użyciu narzędzi GNU

%description
GNU-EFI development environment allows to create EFI applications
for IA-64 and x86 platforms using the GNU toolchain.

%description -l pl.UTF-8
Rodowisko programistyczne GNU-EFI umożliwia tworzenie aplikacji EFI
dla platform IA-64 i x86 przy użyciu narzędzi GNU.

%prep
%setup -n %origname-3.0
# upstream recommendation as of 20130130
sed -i 's/-DGNU_EFI_USE_MS_ABI -maccumulate-outgoing-args//' Make.defaults

%build
%make -j1 \
	ARCH=$(arch | sed -e 's/i.86/ia32/') \
	CFLAGS="%optflags -fpic -Wall -fno-stack-protector" \
	OBJCOPY=objcopy

%install
%make install INSTALLROOT=%buildroot PREFIX=%prefix

%if "%_lib" != "lib"
mv -f %buildroot%prefix/{lib,%_lib}
%endif

%files
%doc ChangeLog README.* apps
%_libdir/libefi.a
%_libdir/libgnuefi.a
%_libdir/crt0-efi-*.o
%_libdir/elf_*_efi.lds
%_includedir/efi

%changelog
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

# NOTE: don't use 3.1, it doesn't support EFI x86_64

Name: gnu-efi
Version: 3.0r
Release: alt2

Summary: wrapper for GNU EFI toolchain
License: public domain
Group: Development/Other

Url: http://altlinux.org/UEFI
ExclusiveArch: x86_64
Requires: %name-%version

%description
GNU-EFI development environment allows to create EFI applications
for IA-64 and x86 platforms using the GNU toolchain.

It comes in different versions which can be useful/required
for various EFI software and so far there's no single version
that would be good for anything EFI in Sisyphus without
regressions for anything else there.

This package requires the version that's considered most stable
so that packages that benefit from newer toolchain can BR: that
explicitly.

%prep

%files

%changelog
* Mon Nov 25 2013 Michael Shigorin <mike@altlinux.org> 3.0r-alt2
- turned into a wrapper package

* Wed Oct 17 2012 Michael Shigorin <mike@altlinux.org> 3.0r-alt1
- 3.0r

* Wed Oct 17 2012 Michael Shigorin <mike@altlinux.org> 3.0q-alt1
- built for Sisyphus; these PLD people worked on the spec:
  baggins glen qboosh

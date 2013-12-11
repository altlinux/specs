Name: rpm-macros-uefi
Version: 0.5
Release: alt1

Summary: A set of RPM macros to help package UEFI related things
License: Public domain
Group: Development/Other

Url: http://www.altlinux.org/UEFI
Requires: pesign
# NB: it's *not* noarch due to %%_libdir in a macro

%define macrofile %_rpmmacrosdir/uefi

%description
This package carries helpful macros to package
(and probably sign before that) UEFI binaries.

%prep

%build

%install
mkdir -p %buildroot%_rpmmacrosdir
cat > %buildroot%macrofile << EOF
%%_efi_bootdir /boot/efi
%%_efi_bindir %_libdir/efi
%%_efi_keydir %_sysconfdir/pki/uefi

%ifarch x86_64
%%_efi_arch x64
%endif
%ifarch %ix86
%%_efi_arch ia32
%endif
EOF

%files
%macrofile

%changelog
* Wed Dec 11 2013 Michael Shigorin <mike@altlinux.org> 0.5-alt1
- restored %%_efi_keydir to provide cacert

* Wed Nov 20 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt2
- explicit R: pesign

* Wed Nov 20 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- dropped sbsign support (pesign carries its macros along,
  sbsign should do the same or be used manually anyways)
- added de facto pesign BR for hasher mountpoint

* Sat Jan 12 2013 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- added %%_efi_arch (reworked refind's implementation)

* Sat Jan 12 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- extended %%_efi_sign a bit to allow for key and suffix options
  (the trivial form of its use hasn't changed though)

* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release


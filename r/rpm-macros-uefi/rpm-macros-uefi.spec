Name: rpm-macros-uefi
Version: 0.7
Release: alt2

Summary: A set of RPM macros to help package UEFI related things
License: ALT-Public-Domain
Group: Development/Other

Url: http://www.altlinux.org/UEFI
# NB: it's *not* noarch due to %%_libdir in a macro

%define macrofile %_rpmmacrosdir/uefi

%package -n rpm-build-uefi
Summary: macros and tools to help package UEFI related things
Group: Development/Other
Requires: rpm-macros-uefi = %EVR
%ifnarch loongarch64
Requires: pesign
%endif

%description -n rpm-macros-uefi
This package carries helpful macros to package UEFI binaries.

%description -n rpm-build-uefi
This package carries the build environment and helpful macros
to package (and probably sign before that) UEFI binaries.

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
%ifarch aarch64
%%_efi_arch aa64
%endif
%ifarch loongarch64
%%_efi_arch loongarch64
%endif
EOF

%files -n rpm-macros-uefi
%macrofile

%files -n rpm-build-uefi

%changelog
* Tue Nov 28 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.7-alt2
- added %%_efi_arch definition for loongarch64
- do NOT require pesing on LoongArch (restricted boot is not available)
- note: release is -alt2 so this version is newer than the one in
  sisyphus_loongarch64

* Sat Apr 16 2022 Igor Vlasenko <viy@altlinux.org> 0.6-alt2
- NMU: moved deps to rpm-build-uefi

* Wed Sep 08 2021 Nikolai Kostrigin <nickel@altlinux.org> 0.6-alt1
- added %%_efi_arch definition for aarch64
- spec: clarified the license (mike@)

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


Name: shim
Version: 0.4
Release: alt1.2

Summary: First-stage UEFI bootloader
License: BSD
Group: System/Kernel and hardware

Url: http://www.codon.org.uk/~mjg59/shim/
Source0: http://www.codon.org.uk/~mjg59/shim/shim-%version.tar
Source1: altlinux-ca.cer

# incorporate mokutil for packaging simplicity
%global mokutilver 0.1.0
Source2: http://www.codon.org.uk/~mjg59/mokutil/mokutil-%mokutilver.tar.bz2

Patch0: 0001-Fix-grub-path.patch
Patch2: mokutil-correct-moklistrt-size.patch
Patch4: 0001-Fix-some-pointer-casting-issues.patch

BuildRequires: openssl-devel openssl
BuildRequires: pesign >= 0.106
BuildRequires: gnu-efi-3.0u

# Shim is only required on platforms implementing the UEFI secure boot
# protocol. The only one of those we currently wish to support is 64-bit x86.
# Adding further platforms will require adding appropriate relocation code.
ExclusiveArch: x86_64

# Figure out the right file path to use
%global efidir altlinux

%description
Initial UEFI bootloader that handles chaining to a trusted
full bootloader under secure boot environments.

%package -n shim-unsigned
Summary: First-stage UEFI bootloader (unsigned data)
Group: System/Kernel and hardware

%description -n shim-unsigned
Initial UEFI bootloader that handles chaining to a trusted
full bootloader under secure boot environments.

%package -n mokutil
Summary: Utilities for managing Secure Boot/MoK keys
Group: System/Kernel and hardware

%description -n mokutil
Utilities for managing the "Machine's Own Keys" list.

%prep
%setup -n shim-%version
%setup -a 2 -D -T
%patch0 -p1
%patch2 -p1
%patch4 -p1

find -name Makefile | xargs sed -i 's,/usr/lib64/gnuefi,%_libdir,g'

%build
MAKEFLAGS=""
if [ -f "%SOURCE1" ]; then
	MAKEFLAGS="VENDOR_CERT_FILE=%SOURCE1"
fi
make ${MAKEFLAGS} shim.efi MokManager.efi fallback.efi
cd mokutil-%mokutilver
%configure
%make_build
cd ..

%install
pesign -h -P -i shim.efi -h > shim.hash
install -D -d -m 0755 %buildroot%_datadir/shim/
install -m 0644 shim.efi %buildroot%_datadir/shim/shim.efi
install -m 0644 shim.hash %buildroot%_datadir/shim/shim.hash
install -m 0644 fallback.efi %buildroot%_datadir/shim/fallback.efi
install -m 0644 MokManager.efi %buildroot%_datadir/shim/MokManager.efi
cd mokutil-%mokutilver
make PREFIX=%prefix LIBDIR=%_libdir DESTDIR=%buildroot install
cd ..

%files -n shim-unsigned
%doc
%dir %_datadir/shim
%_datadir/shim/*

%files -n mokutil
%_bindir/mokutil
%_man1dir/mokutil.1*

%changelog
* Tue Dec 17 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt1.2
- rebuilt for Sisyphus

* Thu Aug 01 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt1.1
- replaced fedora-ca.cer with altlinux-ca.cer

* Mon Jul 29 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- actually built for ALT Linux
  + based on fedora's 0.3-2 spec by pjones@

* Fri Jun 07 2013 Peter Jones <pjones@redhat.com> - 0.3-2
- Require gnu-efi-3.0q for now.
- Don't allow mmx or sse during compilation.
- Re-organize this so all real signing happens in shim-signed instead.
- Split out mokutil

* Wed Dec 12 2012 Peter Jones <pjones@redhat.com> - 0.2-3
- Fix mokutil's idea of signature sizes.

* Wed Nov 28 2012 Matthew Garrett <mjg59@srcf.ucam.org> - 0.2-2
- Fix secure_mode() always returning true

* Mon Nov 26 2012 Matthew Garrett <mjg59@srcf.ucam.org> - 0.2-1
- Update shim
- Include mokutil
- Add debuginfo package since mokutil is a userspace executable

* Mon Oct 22 2012 Peter Jones <pjones@redhat.com> - 0.1-4
- Produce an unsigned shim

* Tue Aug 14 2012 Peter Jones <pjones@redhat.com> - 0.1-3
- Update how embedded cert and signing work.

* Mon Aug 13 2012 Josh Boyer <jwboyer@redhat.com> - 0.1-2
- Add patch to fix image size calculation

* Mon Aug 13 2012 Matthew Garrett <mjg@redhat.com> - 0.1-1
- initial release

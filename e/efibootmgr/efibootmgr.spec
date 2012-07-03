Name: efibootmgr
Version: 0.5.4
Release: alt1

Summary: EFI Boot Manager
Group: System/Kernel and hardware
License: GPLv2+
URL: http://linux.dell.com/efibootmgr/

# EFI/UEFI don't exist on PPC
ExclusiveArch: i386 i586 i686 x86_64 ia64

Source0: http://linux.dell.com/efibootmgr/permalink/%name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Fri Apr 11 2008
BuildRequires: libpci-devel zlib-devel

%description
efibootmgr displays and allows the user to edit the Intel Extensible
Firmware Interface (EFI) Boot Manager variables.  Additional
information about EFI can be found at
http://developer.intel.com/technology/efi/efi.htm and http://uefi.org/.

%prep
%setup -q

%build
%make_build EXTRA_CFLAGS="%optflags"

%install
mkdir -p %buildroot%_sbindir/ %buildroot%_man8dir/
install -p -m755 src/%name/%name %buildroot%_sbindir/
install -p -m644 src/man/man8/%name.8 %buildroot%_man8dir/

%files
%doc AUTHORS README INSTALL doc/ChangeLog doc/TODO
%_sbindir/%name
%_man8dir/%name.*

%changelog
* Fri Apr 11 2008 Igor Zubkov <icesik@altlinux.org> 0.5.4-alt1
- build for Sisyphus

* Thu Jan  3 2008 Matt Domsch <Matt_Domsch@dell.com> 0.5.4-1
- split efibootmgr into its own RPM for Fedora/RHEL.

* Thu Aug 24 2004 Matt Domsch <Matt_Domsch@dell.com>
- new home linux.dell.com

* Fri May 18 2001 Matt Domsch <Matt_Domsch@dell.com>
- See doc/ChangeLog

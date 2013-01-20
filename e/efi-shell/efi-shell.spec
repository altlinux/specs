Name: efi-shell
Version: 2.0
Release: alt2

Summary: Native UDK implementations of UEFI Shell 2.0
License: BSD-like
Group: System/Kernel and hardware

Url: http://sourceforge.net/apps/mediawiki/tianocore/index.php?title=ShellPkg
# https://edk2.svn.sourceforge.net/svnroot/edk2/trunk/edk2/ShellBinPkg
Source0: https://edk2.svn.sourceforge.net/svnroot/edk2/trunk/edk2/ShellBinPkg/UefiShell/X64/Shell.efi
Source1: Contributions.txt
Source2: License.txt
Source3: ReadMe.txt
Packager: Michael Shigorin <mike@altlinux.org>

# x86 might be added but the sense is quite faint
ExclusiveArch: x86_64

BuildRequires: rpm-macros-uefi
BuildRequires: sbsigntools alt-uefi-keys-private

Summary(pl.UTF-8): Natywne implementacje UDK powłoki UEFI Shell 2.0

%description
Native UDK implementations of UEFI Shell 2.0 prebuilt binaries.

%description -l pl.UTF-8
Natywne implementacje UDK powłoki UEFI Shell 2.0.

%package signed
Summary: Native UDK implementations of UEFI Shell 2.0 (signed variant)
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description signed
Native UDK implementations of UEFI Shell 2.0 prebuilt binaries.

This package provides means to cope with UEFI SecureBoot
(better described as Restricted Boot) firmware when one
can't disable it easily, doesn't want to, or needs not to.

%prep

%install
install -pDm644 %SOURCE0 %buildroot%_efi_bindir/shell.efi

# autocreates signed.manifest
%_efi_sign %buildroot%_efi_bindir/shell.efi

install %SOURCE1 %SOURCE2 %SOURCE3 .

%files
%doc License.txt ReadMe.txt Contributions.txt
%_efi_bindir/shell.efi

%files -f signed.manifest signed

# TODO:
# - native EDK build, anyone?

%changelog
* Sun Jan 20 2013 Michael Shigorin <mike@altlinux.org> 2.0-alt2
- added signed subpackage
- dropped ia32
- further spec cleanup

* Sat Jan 19 2013 Michael Shigorin <mike@altlinux.org> 2.0-alt1
- built for ALT Linux based on PLD spec by Jacek Konieczny
- dropped subpackages and efi-boot-update scripts for now

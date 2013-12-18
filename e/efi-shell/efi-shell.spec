Name: efi-shell
Version: 2.0
Release: alt4

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
BuildRequires: pesign >= 0.109-alt4

Obsoletes: efi-shell-signed

AutoReqProv: no

Summary(pl.UTF-8): Natywne implementacje UDK powłoki UEFI Shell 2.0

%description
Native UDK implementations of UEFI Shell 2.0 prebuilt binaries.

Please note that the official build is signed; this shouldn't
intervene in any way but rather provides means to cope with
UEFI SecureBoot (better described as Restricted Boot) firmware
when one can't disable it easily, doesn't want to, or needs not to.

%description -l pl.UTF-8
Natywne implementacje UDK powłoki UEFI Shell 2.0.

%prep

%install
install -pDm644 %SOURCE0 %buildroot%_efi_bindir/shell.efi
%pesign -s -i %buildroot%_efi_bindir/shell.efi

install %SOURCE1 %SOURCE2 %SOURCE3 .

%files
%doc License.txt ReadMe.txt Contributions.txt
%_efi_bindir/shell.efi

# TODO:
# - native EDK build, anyone?

%changelog
* Tue Dec 17 2013 Michael Shigorin <mike@altlinux.org> 2.0-alt4
- updated pesign macros use, reworked binaries installation
- prepare for production signing

* Fri Nov 22 2013 Michael Shigorin <mike@altlinux.org> 2.0-alt3
- pesign with ALT key
- turn automated R:/P: search off as there are none

* Sun Jan 20 2013 Michael Shigorin <mike@altlinux.org> 2.0-alt2
- added signed subpackage
- dropped ia32
- further spec cleanup

* Sat Jan 19 2013 Michael Shigorin <mike@altlinux.org> 2.0-alt1
- built for ALT Linux based on PLD spec by Jacek Konieczny
- dropped subpackages and efi-boot-update scripts for now

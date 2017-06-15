Name: shim-signed
Version: 0.4
Release: alt6

Summary: UEFI RestrictedBoot shim signed by Microsoft
License: BSD
Group: System/Kernel and hardware

Url: http://www.codon.org.uk/~mjg59/shim-signed/
Source: %url/%name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: rpm-macros-uefi
ExclusiveArch: x86_64

%description
This package contains shim and MokManager binaries
signed by "Microsoft Windows UEFI Driver Publisher" key
and provided by Matthew Garrett.

See http://mjg59.dreamwidth.org/20303.html for details.

%prep
%setup

%install
mkdir -p %buildroot%_efi_bindir %buildroot%_libexecdir/shim
install -p *.efi %buildroot%_efi_bindir/
# both should end up within /usr
ln %buildroot%_efi_bindir/shim.efi \
	%buildroot%_libexecdir/shim/shimx64.efi.signed
ln %buildroot%_efi_bindir/MokManager.efi \
	%buildroot%_libexecdir/shim/mmx64.efi.signed
ln %buildroot%_efi_bindir/fallback.efi \
	%buildroot%_libexecdir/shim/fbx64.efi.signed

%files
%attr(0644,root,root) %_efi_bindir/*.efi
%attr(0644,root,root) %_libexecdir/shim/*x64.efi.signed

%changelog
* Fri Jun 09 2017 Michael Shigorin <mike@altlinux.org> 0.4-alt6
- built for sisyphus

* Wed Jun 07 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt5
- made shim binaries accessible also by debian'ish paths

* Sat Apr 01 2017 Michael Shigorin <mike@altlinux.org> 0.4-alt4
- removed ALT signature (closes: #33314)

* Tue Dec 10 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt3
- added ALT signature

* Fri Nov 22 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt2
- added fallback.efi
- signed supplementary binaries with ALT key for versatility

* Tue Nov 19 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- ALT build

* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt2
- only makes sense for x86_64

* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- initial release

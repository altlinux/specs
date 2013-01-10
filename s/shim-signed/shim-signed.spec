Name: shim-signed
Version: 0.2
Release: alt2

Summary: UEFI RestrictedBoot shim signed by Microsoft
License: BSD
Group: System/Kernel and hardware

Url: http://www.codon.org.uk/~mjg59/shim-signed/
Source: %url/%name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: rpm-macros-uefi

ExclusiveArch: x86_64

# not noarch due to %%_libdir anyways

%description
This package contains shim and MokManager binaries
signed by "Microsoft Windows UEFI Driver Publisher" key
and provided by Matthew Garrett.

See http://mjg59.dreamwidth.org/20303.html for details.

%prep
%setup

%build

%install
mkdir -p %buildroot%_efi_bindir
install -p *.efi %buildroot%_efi_bindir/

%files
%_efi_bindir/*.efi

%changelog
* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt2
- only makes sense for x86_64

* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- initial release


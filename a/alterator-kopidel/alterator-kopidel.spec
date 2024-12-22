%define _unpackaged_files_terminate_build 1

Name: alterator-kopidel
Version: 0.0.2
Release: alt1

Summary: Creating a bootable iso that copies the file system
License: GPL
Group: System/Configuration/Other
Url: https://www.altlinux.org/Alterator
# grub-pc architectures:
ExclusiveArch: x86_64 %ix86

Source: %name-%version.tar

Requires: alterator
Requires: alterator-setup
Requires: alterator-sh-functions
Requires: alterator-l10n
Requires: rsync
Requires: grub-pc
Requires: grub-common
Requires: mtools
Requires: squashfs-tools
Requires: xorriso
Requires: make-initrd-bootchain
Requires: alt-uefi-certs

# Dependencies of the altinst squashfs image:
Requires: alterator-vm
Requires: alterator-preinstall
Requires: alterator-grub
Requires: libevms
Requires: installer-alterator-fs
Requires: installer-common-stage2
Requires: installer-scripts-remount-stage2
Requires: installer-feature-alterator-setup-stage2
Requires: console-scripts
Requires: kbd

BuildRequires(pre): rpm-macros-alterator
%ifarch %e2k
BuildRequires: guile20-devel libguile20-devel
%else
BuildRequires: guile22-devel
%endif
BuildRequires: alterator-fbi

%description
If you want to make a complete copy of the file system and install
it on other machines, then you have found what you were looking for!

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_alterator_backend3dir/kopidel
%_alterator_datadir/applications/kopidel.desktop
%_datadir/alterator-kopidel/
%_datadir/alterator/ui/kopidel/
%_sbindir/kopidel
%_sysconfdir/bash_completion.d/alterator-kopidel
%_libexecdir/alterator-kopidel/

%changelog
* Sun Dec 22 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.0.2-alt1
- Fix the creation of a workdir for the first use.

* Sat Dec 21 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.0.1-alt1
- The first version of the new alterator module!

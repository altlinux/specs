%define _unpackaged_files_terminate_build 1

Name: installer-alterator-fs
Version: 1.0.1
Release: alt1

Summary: Installing a file system
License: GPL
Group: System/Configuration/Other
Url: https://www.altlinux.org/Installer
Vcs: https://altlinux.space/rauty/installer-alterator-fs
BuildArch: noarch

Source: %name-%version.tar

Requires: alterator
Requires: alterator-sh-functions
Requires: alterator-lookout
Requires: installer-scripts-remount-stage2
Requires: libshell

BuildRequires(pre): rpm-macros-alterator
BuildRequires: alterator

%description
This step takes the file system, which is packed in tar
and divided into parts, and puts it on the target system.

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_alterator_backend3dir/install-fs

%changelog
* Thu Mar 26 2026 Ajrat Makhmutov <rauty@altlinux.org> 1.0.1-alt1
- Add a check for mounting destdir before installation.

* Tue Aug 12 2025 Ajrat Makhmutov <rauty@altlinux.org> 1.0.0-alt1
- Improve logging.
- Stop installer and print error message if failed to mount_chroot.
- Check archive availability also in /usr/share/install2/metadata.
- Remove installing grub action.
- Add Vcs tag to the spec file.
- Stop joining the parts in copied-fs.tar (thx to alterator-kopidel 1.0.0):
  + Increase the speed of system installation.
  + Reduce the required disk space.

* Sat Dec 21 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.0.1-alt1
- The first version of the new installer step!

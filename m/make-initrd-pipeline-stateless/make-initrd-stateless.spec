%add_findreq_skiplist /usr/share/make-initrd/features/*

Name: make-initrd-pipeline-stateless
Version: 0.3
Release: alt1

Summary: Stateless rootfs feature for make-initrd's pipeline mechanism
License: GPL-2.0-or-later
Group: System/Base

Source0: %name-%version.tar

# Due to pipeline feature support.
Requires: make-initrd >= 2.7.0

# Programs packed into an initrd image.
Requires: tar zstd

BuildArch: noarch

%description
This package provides stateless method for pipeline mechanism.

%prep
%setup

%install
mkdir -p %buildroot/usr/share/make-initrd/features/
cp -a feature %buildroot/usr/share/make-initrd/features/pipeline-stateless

%files
%_datadir/make-initrd/features/pipeline-stateless

%changelog
* Thu Nov 16 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3-alt1
- Modified the stateless pipeline method as follows:
  + Actually deactivate LUKS-encrypted host devices;
  + Extract file extended attributes (e.g. capabilities).

* Tue Jun 06 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2-alt1
- Modified the stateless pipeline method as follows:
  + Avoid attempting to unmount the host filesystem in overlay mode;
  + Deactivate LUKS-encrypted host devices that are unmounted;
  + Treat comma (,) in the same way as the pipe symbol (|) when processing the
  STATELESS_IMAGES variable;
  + When unpacking subsequent image layers, use the /etc/passwd and /etc/group
  files from preceding image layers.

* Fri Mar 25 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt1
- Initial build.

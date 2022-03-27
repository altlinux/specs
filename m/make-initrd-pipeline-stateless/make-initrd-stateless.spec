%add_findreq_skiplist /usr/share/make-initrd/features/*

Name: make-initrd-pipeline-stateless
Version: 0.1
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
* Fri Mar 25 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt1
- Initial build.

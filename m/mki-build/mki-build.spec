Name: mki-build
Version: 0.1.1
Release: alt1
License: GPL-2.0-or-later
Group: Development/Other
Summary: Scripts used to build mkimage-based images
BuildArch: noarch

Source: %name-%version.tar

Requires: mkimage

%description
This package contains scripts that are used to build mkimage-based images.

%prep
%setup
sed 's/@PROG_VERSION@/%version/' -i mki-build

%install
mkdir -p %buildroot%_bindir
cp mki-build -t %buildroot%_bindir
mkdir -p %buildroot%_datadir/%name
cp prepare-vm -t %buildroot%_datadir/%name

%add_findreq_skiplist %_datadir/%name/*

%files
%_bindir/mki-build
%_datadir/%name

%changelog
* Tue Feb 21 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.1-alt1
- Changed sctipts:
  + prepare-vm: copy resolver configuration from the host to the vm;
  + mki-build: export BRANCH variable (based on rpm's
  %%_priority_distbranch variable);
  + Pass --mem=max to vm-run to fix build for aarch64.

* Mon Nov 21 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.0-alt1
- Initial build.

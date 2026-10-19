%define _unpackaged_files_terminate_build 1
%define oname openbfdd

Name: kube-ovn-openbfdd
# commit `e35f43ad8d2b` is version used in kube-ovn v1.15.26 OCI image
# git describe --tags --abbrev=1
Version: 0.5.3.0.6.e35f
Release: alt1
Summary: OpenBFDD BFD daemon with the Kube-OVN patches
License: BSD-3-Clause
Group: Networking/Other
Url: https://github.com/dyninc/OpenBFDD

Source0: %name-%version.tar

# Kube-OVN patches, applied in the order of dist/images/Dockerfile.base
# kube-ovn: v1.15.26
Patch1: OpenBFDD-compile.patch
Patch2: OpenBFDD-allow-ttl-254.patch
Patch3: OpenBFDD-control-hardening.patch

BuildRequires: gcc-c++

%description
OpenBFDD is a software implementation of the Bidirectional Forwarding
Detection (BFD) protocol. 

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

# kubeovn's Dockerfile.base drop this file 
rm -f missing

%build
%autoreconf
%configure --enable-silent-rules
%make_build

%install
%makeinstall_std

%files
%doc LICENSE README AUTHORS
%_bindir/bfdd-beacon
%_bindir/bfdd-control
%_man8dir/bfdd-beacon.8*
%_man8dir/bfdd-control.8*

%changelog
* Mon Oct 19 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.5.3.0.6.e35f-alt1
- Initial build for ALT.



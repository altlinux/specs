# The source directory.
%global source_directory 2.4-stable

Name: virt-v2v
Version: 2.4.0
Release: alt1
Summary: Convert a virtual machine to run on KVM
Group: Development/Other
License: GPLv2+
Url: https://github.com/libguestfs/virt-v2v

Source0: http://download.libguestfs.org/virt-v2v/%source_directory/%name-%version.tar.gz
Patch1: fixes-common.patch

BuildRequires(pre): rpm-build-ocaml
BuildRequires: /usr/bin/pod2man
BuildRequires: gcc
BuildRequires: ocaml >= 4.01 ocaml-findlib ocaml-ocamlbuild
BuildRequires: ocaml-libguestfs-devel ocaml-libvirt-devel ocaml-libnbd-devel
BuildRequires: ocaml-gettext-devel
BuildRequires: ocaml-fileutils-devel
BuildRequires: ocaml-ounit-devel
BuildRequires: libguestfs-devel
BuildRequires: libnbd-devel
BuildRequires: libaugeas-devel
BuildRequires: bash-completion
BuildRequires: gettext-tools
BuildRequires: libjansson-devel
BuildRequires: libosinfo-devel
BuildRequires: libvirt-devel
BuildRequires: libvirt-kvm
BuildRequires: libxml2-devel
BuildRequires: libpcre2-devel
BuildRequires: perl-Sys-Guestfs
BuildRequires: /usr/bin/virsh
BuildRequires: genisoimage zip unzip db4-utils
#BuildRequires: nbdkit-python-plugin


Requires: guestfs-tools
Requires: gawk
Requires: gzip
Requires: unzip
Requires: curl
Requires: /usr/bin/virsh
Requires: qemu-kvm-core >= 5.2.0

%description
Virt-v2v converts a single guest from a foreign hypervisor to run on
KVM.  It can read Linux and Windows guests running on VMware, Xen,
Hyper-V and some other hypervisors, and convert them to KVM managed by
libvirt, OpenStack, oVirt, Red Hat Virtualisation (RHV) or several
other targets.  It can modify the guest to make it bootable on KVM and
install virtio drivers so it will run quickly.


%prep
%setup
pushd common
%patch1 -p1
popd

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

# Delete libtool crap.
find %buildroot -name '*.la' -delete

# Find locale files.
%find_lang %name

%files -f %name.lang
%doc COPYING README
%_bindir/virt-v2v*
%_man1dir/virt-v2v*
#%%_datadir/virt-tools
%_datadir/bash-completion/completions/virt-v2v*

%changelog
* Fri Jan 12 2024 Alexey Shabalin <shaba@altlinux.org> 2.4.0-alt1
- new version 2.4.0

* Tue Mar 01 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.44.2-alt1
- new version 1.44.2

* Tue Sep 07 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.44.0-alt1
- new version 1.44.0

* Wed Apr 07 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.43.4-alt1
- new version 1.43.4

* Tue Dec 08 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.43.1-alt3
- Set LANG=C in parse_ova (Closes: 39366)
- Fix qemu options used in --qemu-boot

* Thu Sep 03 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.43.1-alt2
- Refactor (after discussions with upstream) ALT support

* Mon Aug 24 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.43.1-alt1
- update to 1.43.1
- Add ALT support

* Sun May 10 2020 Alexey Shabalin <shaba@altlinux.org> 1.42.0-alt1
- Initial release of separate virt-v2v program, was part of libguestfs.

%filter_from_requires /NetworkManager-applet-gtk/d
%filter_from_requires /icewm/d
%filter_from_requires /metacity3.0/d
%filter_from_requires /\/.kconfig/d
%filter_from_requires /\/.profile/d
%filter_from_requires /^.usr.bin.virt-p2v/d
%filter_from_requires /^.etc.os-release/d

Name: virt-p2v
Version: 1.42.0
Release: alt1
Summary: Convert a physical machine to run on KVM
Group: Development/Other
License: GPLv2+

Url: http://libguestfs.org/
Source0: http://download.libguestfs.org/%name/%name-%version.tar.gz

# Basic build requirements.
BuildRequires: gcc
BuildRequires: perl-Pod-Simple
BuildRequires: perl-podlators
BuildRequires: perl-List-MoreUtils
BuildRequires: /usr/bin/pod2text
BuildRequires: libxml2-devel
BuildRequires: libpcre-devel
BuildRequires: bash-completion
BuildRequires: xz
BuildRequires: libgtk+3-devel
BuildRequires: libdbus-devel
# Test suite requirements.
BuildRequires: /usr/bin/qemu-nbd

Requires: gawk
Requires: gzip
Requires: libguestfs-tools
Requires: binutils

# Migrate from the old virt-p2v-maker:
Provides: virt-p2v-maker = %EVR
Obsoletes: virt-p2v-maker < 1.41.5

%description
Virt-p2v converts (virtualizes) physical machines so they can be run
as virtual machines under KVM.

This package contains the tools needed to make a virt-p2v boot CD or
USB key which is booted on the physical machine to perform the
conversion.  You also need virt-v2v installed somewhere else to
complete the conversion.

To convert virtual machines from other hypervisors, see virt-v2v.

%prep
%setup

%build
%autoreconf
%configure \
  --with-extra="ALTLinux,release=%version-%release" \
  --disable-gnulib-tests

%make_build

%install
%makeinstall_std

# Delete the development man pages.
rm -f %buildroot%_man1dir/p2v-building.1*
rm -f %buildroot%_man1dir/p2v-hacking.1*
rm -f %buildroot%_man1dir/p2v-release-notes.1*

%files
%doc README COPYING
%_bindir/virt-p2v*
%_datadir/bash-completion/completions/virt-*
%_datadir/virt-p2v
%_libdir/virt-p2v
%_man1dir/virt-p2v*

%changelog
* Sun May 10 2020 Alexey Shabalin <shaba@altlinux.org> 1.42.0-alt1
- Initial release of separate virt-v2v program, was part of libguestfs.


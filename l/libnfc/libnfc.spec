%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

# Tests require cutter (https://github.com/clear-code/cutter)
# but it isn't in ALT Sisyphus and I don't think that a good
# idea to package such almost dead project...
%def_without check

%define abiversion 6
Name: libnfc
Version: 1.8.0
Release: alt1.79.g3fa0751

Summary: Platform independent Near Field Communication (NFC) library
Group: Networking/Other
License: LGPL-3.0
Url: https://github.com/nfc-tools/libnfc
Vcs: https://github.com/nfc-tools/libnfc

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: libusb-compat-devel
BuildRequires: libpcsclite-devel
BuildRequires: doxygen

%description
A library which allows userspace application access to NFC devices.

%package -n %name%abiversion
Summary: Library files for libnfc
Group: System/Libraries

%description -n %name%abiversion
%summary.

%package devel
Summary: Development files for libnfc
Group: Development/C
Requires: %name%abiversion = %EVR

%description devel
%summary.

%package doc
Summary: Documentation for libnfc
Group: Development/Documentation
BuildArch: noarch

%description doc
%summary.

%package utils
Summary: Utilities for libnfc
Group: Development/Tools
Requires: %name%abiversion = %EVR

%description utils
%summary.

%package examples
Summary: Examples (with descriptions in man-pages) for libnfc
Group: Development/Other
Requires: %name%abiversion = %EVR

%description examples
%summary.

%package pn53x-examples
Summary: Examples (with descriptions in man-pages) for libnfc (for pn53x)
Group: Development/Other
Requires: %name%abiversion = %EVR

%description pn53x-examples
%summary.

%prep
%setup
%autopatch -p1

%build
%autoreconf
%configure \
    --disable-static \
    --with-drivers=all \
    --enable-doc
%make_build
%make_build doc

%install
%makeinstall_std \
    install \
    install-html

# Use sample config as dummy for real config
install -Dpm0644 libnfc.conf.sample %buildroot%_sysconfdir/nfc/libnfc.conf

# Create (to own further) pre-device config directory
mkdir -p %buildroot%_sysconfdir/nfc/devices.d/

# Udev-rule to grant permissions to your to drive nfc-device
install -Dpm0644 contrib/udev/93-pn53x.rules %buildroot%_udevrulesdir/93-pn53x.rules

%check
%make_build check

%files -n %name%abiversion
%dir %_sysconfdir/nfc/
%dir %_sysconfdir/nfc/devices.d/
%config(noreplace) %_sysconfdir/nfc/libnfc.conf
%_udevrulesdir/93-pn53x.rules
%_libdir/libnfc.so.%abiversion
%_libdir/libnfc.so.%abiversion.*

%files devel
%_includedir/nfc/
%_pkgconfigdir/libnfc.pc
%_libdir/libnfc.so

%files utils
%_bindir/nfc-barcode
%_bindir/nfc-emulate-forum-tag4
%_bindir/nfc-jewel
%_bindir/nfc-list
%_bindir/nfc-mfclassic
%_bindir/nfc-mfultralight
%_bindir/nfc-read-forum-tag3
%_bindir/nfc-relay-picc
%_bindir/nfc-scan-device
%_man1dir/nfc-barcode.1.xz
%_man1dir/nfc-emulate-forum-tag4.1.xz
%_man1dir/nfc-jewel.1.xz
%_man1dir/nfc-list.1.xz
%_man1dir/nfc-mfclassic.1.xz
%_man1dir/nfc-mfultralight.1.xz
%_man1dir/nfc-read-forum-tag3.1.xz
%_man1dir/nfc-relay-picc.1.xz
%_man1dir/nfc-scan-device.1.xz

%files doc
%doc doc/html

%files examples
%doc contrib/linux/blacklist-libnfc.conf
%_bindir/nfc-anticol
%_bindir/nfc-dep-initiator
%_bindir/nfc-dep-target
%_bindir/nfc-emulate-forum-tag2
%_bindir/nfc-emulate-tag
%_bindir/nfc-emulate-uid
%_bindir/nfc-mfsetuid
%_bindir/nfc-poll
%_bindir/nfc-relay
%_bindir/nfc-st25tb
%_man1dir/nfc-anticol.1*
%_man1dir/nfc-dep-initiator.1*
%_man1dir/nfc-dep-target.1*
%_man1dir/nfc-emulate-forum-tag2.1*
%_man1dir/nfc-emulate-tag.1*
%_man1dir/nfc-emulate-uid.1*
%_man1dir/nfc-mfsetuid.1*
%_man1dir/nfc-poll.1*
%_man1dir/nfc-relay.1*

%files pn53x-examples
%_bindir/pn53x-diagnose
%_bindir/pn53x-sam
%_bindir/pn53x-tamashell
%_man1dir/pn53x-diagnose.1*
%_man1dir/pn53x-sam.1*
%_man1dir/pn53x-tamashell.1*

%changelog
* Fri Jul 18 2025 Anton Zhukharev <ancieg@altlinux.org> 1.8.0-alt1.79.g3fa0751
- Packaged for ALT Sisyphus.

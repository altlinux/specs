Name: virtualsmartcard
Version: 0.9
Release: alt1

Summary: Virtual Smart Card

License: GPLv3
Group: System/Configuration/Hardware
Url: https://github.com/frankmorgner/vsmartcard

# Source0-url: https://github.com/frankmorgner/vsmartcard/releases/download/%name-%version/%name-%version.tar.gz
Source0: %name-%version.tar

BuildRequires: libpcsclite-devel
BuildRequires: help2man
BuildRequires: rpm-build-python3

# The main package needs vpcd, but vpcd can work with other tools
Requires: vpcd = %EVR

%description
Virtual Smart Card emulates a smart card and makes it accessible through PC/SC.

%package -n vpcd
Summary: Virtual smart card reader
Group: System/Configuration/Hardware

%description -n vpcd
Virtual smart card reader to be used for smart card emulation vith
virtualsmartcard (vicc).

%prep
%setup
# The deprecated patchN is needed for RHEL 7 compatibility
#patch -P 0 -p1 -b .prefix
sed -ie 's|serialdropdir="${prefix}|serialdropdir="|' configure.ac
sed -ie 's|serialconfdir="${prefix}|serialconfdir="|' configure.ac

%build
rm py-compile
%autoreconf
%configure --enable-vpcdslots=1 --enable-vpcdhost=127.0.0.1
%make_build

sed -ie 's|^#! %_bindir/python$|#! %_bindir/python3|' src/vpicc/vicc

%install
%makeinstall_std V=1

# needs chat, eac
rm -v %buildroot%python3_sitelibdir_noarch/%name/cards/nPA.py

%files
%_bindir/vicc
%python3_sitelibdir_noarch/%name/*
%_man1dir/vicc.1*

%files -n vpcd
%_bindir/vpcd-config
%_libdir/pcsc/drivers/serial/libifdvpcd.so
%_libdir/pcsc/drivers/serial/libifdvpcd.so.0.*
%config(noreplace) %_sysconfdir/reader.conf.d/vpcd

%changelog
* Sat Mar 22 2025 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- initial build for ALT Sisyphus

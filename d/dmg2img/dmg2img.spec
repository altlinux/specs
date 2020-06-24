Summary: Uncompress the Apple compressed disk image files
Name: dmg2img
Version: 1.6.7
Release: alt1
# dmg2img is GPL without specific version
# vfdecrypt is MIT licensed
License: GPL and MIT
Group: File tools
Url: http://vu1tur.eu.org/tools/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
# Patch0: dmg2img-1.6.2-nostrip.patch

BuildRequires: bzlib-devel
BuildRequires: libssl-devel
BuildRequires: zlib-devel

%description
This package contains dmg2img utility that is able to uncompress compressed dmg
files into plain disk or filesystem images.

%prep
%setup
# %%patch0 -p1

%build
%make_build CC="%__cc" CFLAGS="%optflags"

%install
install -d %buildroot%_man1dir
install -d %buildroot%_bindir

install dmg2img %buildroot%_bindir
install vfdecrypt %buildroot%_bindir
install -pm644 vfdecrypt.1 %buildroot%_man1dir

%files
%doc README COPYING
%_bindir/dmg2img
%_bindir/vfdecrypt
%_man1dir/vfdecrypt.1*

%changelog
* Wed Jun 24 2020 Artyom Bystrov <arbars@altlinux.org> 1.6.7-alt1
- initial build for ALT Sisyphus

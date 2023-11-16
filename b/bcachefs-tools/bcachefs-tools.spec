Name: bcachefs-tools
Version: 1.3.3
Release: alt1

Summary: Userspace tools and docs for bcachefs
License: GPLv2
Group: System/Kernel and hardware

Url: https://bcachefs.org/
Source: %name-%version-%release.tar

BuildRequires: pkgconfig(blkid)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(liburcu)
BuildRequires: pkgconfig(libsodium)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libkeyutils)
BuildRequires: libaio-devel

%description
Userspace tools and docs for bcachefs.
Bcachefs is an advanced new filesystem for Linux, with an emphasis
on reliability and robustness and the complete set of features
one would expect from a modern filesystem.

%prep
%setup
sed -ri '/^VERSION/ s,v0.1-nogit,v%version,'  Makefile

%build
%make_build NO_RUST=please EXTRA_CFLAGS='%optflags'

%install
%make_install NO_RUST=please PREFIX=%_prefix DESTDIR=%buildroot install
rm -v %buildroot/sbin/*.fuse.*

%files
%doc COPYING README*
/sbin/*
%_man8dir/*

%changelog
* Thu Nov 16 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.3-alt1
- initial

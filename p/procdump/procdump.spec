Name:     procdump
Version:  1.0
Release:  alt1

Summary:  A Linux version of the ProcDump Sysinternals tool

License:  MIT
Group:    Other
Url:      https://github.com/Microsoft/ProcDump-for-Linux

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Microsoft/ProcDump-for-Linux/archive/%version.tar.gz
Source:   %name-%version.tar

#BuildRequires:

Requires: gdb >= 7.7.1

BuildRequires: zlib-devel

%description
ProcDump is a Linux reimagining of the classic ProcDump tool from the Sysinternals suite of tools for Windows.
ProcDump provides a convenient way for Linux developers to create core dumps of their application based on performance triggers.

%prep
%setup

%__subst "s|^INSTALLDIR=.*|INSTALLDIR=%buildroot%_bindir|g" Makefile
%__subst "s|^MANDIR=.*|MANDIR=%buildroot%_man1dir|g" Makefile
%__subst "s|^CFLAGS=\(.*\)|CFLAGS=\1 %optflags|g" Makefile

%build
#configure
%make_build build

%install
mkdir -p %buildroot%_bindir/ %buildroot%_man1dir/
%makeinstall_std

#check
#make_build check

%files
%_bindir/*
%_man1dir/*
%doc CONTRIBUTING.md README.md

%changelog
* Tue Dec 12 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus

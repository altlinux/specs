Name: statifier
Version: 1.7.4
Release: alt1

Summary: Convert dynamically-linked ELF binaries to "pseudo-static" binaries

License: GPLv2
Group: Development/Other
URL: http://statifier.sourceforge.net/

Source: http://prdownloads.sourceforge.net/statifier/%{name}-%{version}.tar

# Not autodetected
Requires: gdb

ExclusiveArch: %ix86 x86_64

# This is rare situation when glibc-devel-static is REALLY required for package
# build! :)
# Automatically added by buildreq on Sat Oct 21 2017
# optimized out: glibc-kernheaders-x86 i586-glibc-core i586-glibc-devel i586-libgcc1 python-base python-modules python3 python3-base sssd-client
#BuildRequires: glibc-kernheaders-generic i586-gcc6

BuildRequires: glibc-devel-static

%description
Statifier create from dynamically linked ELF executable
and all it's libraries (and all LD_PRELOAD libraries if any)
one file. This file can be copied and run on another machine
without need to drag all it's libraries.

%prep
%setup
# Fix for correct 64-bit build installation
%__subst 's@/usr/lib@%_libdir@' src/Makefile src/%name
%ifarch x86_64
%__subst "s@ELF32.*@ELF := no@g" configs/config.x86_64
%endif
#__subst "s@SUPPORTED_CPU_LIST :=.*@SUPPORTED_CPU_LIST := %_arch@g" Makefile.common

%build
%make all

%install
%makeinstall_std


%files
%doc AUTHORS ChangeLog INSTALL LICENSE NEWS README TODO
%_bindir/statifier
%_libdir/%name/
%_man1dir/*

%changelog
* Thu Oct 19 2017 Vitaly Lipatov <lav@altlinux.ru> 1.7.4-alt1
- new version 1.7.4 (with rpmrb script)
- cleanup spec

* Thu Nov 27 2008 Victor Forsyuk <force@altlinux.org> 1.6.14-alt1
- Initial build.

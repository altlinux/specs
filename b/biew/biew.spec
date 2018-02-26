# -*- rpm-spec -*-
# $Id: biew,v 1.7 2004/10/04 12:26:46 grigory Exp $

%define src_version	610

Name: biew
Version: 6.1.0
Release: alt1
Packager: Fr. Br. George <george@altlinux.ru>
Summary: %name - console hex viewer/editor and disassembler
License: GPL
Group: Development/Other
URL: http://biew.sourceforge.net
Source0: %name-%src_version-src.tar.bz2
Patch: biew-5.6.2-alt-lvalue.patch.gz
#ExclusiveArch: i586
# Automatically added by buildreq on Sat Apr 11 2009
BuildRequires: libgpm-devel

%description
BIEW (Binary vIEW) is a free, portable, advanced file viewer with
built-in editor for binary, hexadecimal and disassembler modes.

It contains a highlight PentiumIV/K7-Athlon/Cyrix-M2 disassembler,
full preview of MZ, NE, PE, LE, LX, DOS.SYS, NLM, ELF, a.out, arch,
coff32, PharLap, rdoff executable formats, a code guider, and lot of
other features, making it invaluable for examining binary code.

Linux, Unix, QNX, BeOS, DOS, Win32, OS/2 versions are available.

%prep
%setup -q -n %name-%src_version
#patch -p2

%build
find . -type f|xargs sed -i "s|<slang.h>|<slang/slang.h>|g"
sed 's/|| die "Please upgrade your compiler"//' configure
# This CFLAGS hackaround is for 6.1.0 only
CFLAGS='-O2 -mmmx -msse' %configure
%make_build TARGET_PLATFORM=%_target_cpu USE_MOUSE=y

%install 
install -d %buildroot/{%_bindir,%_datadir/%name,%_man1dir}
install %name %buildroot/%_bindir/%name
install doc/%name.1 %buildroot/%_man1dir
cp -a bin_rc/{xlt,skn,*.hlp} %buildroot/%_datadir/%name

%files
%doc doc/*.txt doc/*.ru doc/*en
%_bindir/*
%_datadir/%name
%_man1dir/*

%changelog
* Sat Feb 27 2010 Fr. Br. George <george@altlinux.ru> 6.1.0-alt1
- Version up

* Wed Sep 23 2009 Fr. Br. George <george@altlinux.ru> 6.0.0.0-alt1
- Version up

* Sat Apr 11 2009 Fr. Br. George <george@altlinux.ru> 5.7.3.1-alt1
- Version up

* Mon Dec 18 2006 Grigory Batalov <bga@altlinux.ru> 5.6.2-alt2
- remove lvalue type cast

* Mon Oct  4 2004 Grigory Milev <week@altlinux.ru> 5.6.2-alt1
- new version released

* Tue Feb 24 2004 Grigory Milev <week@altlinux.ru> 5.5.0-alt1
- new version released
- fix used variable name

* Wed Oct 23 2002 Grigory Milev <week@altlinux.ru> 5.3.2-alt1
- new version released
- remover perl from build requires
- rebuild with gcc3

* Thu Jan 24 2002 Grigory Milev <week@altlinux.ru> 5.3.1-alt1
- new version released

* Tue Nov 13 2001 Grigory Milev <week@altlinux.ru>  5.3.0-alt1
- Initial build for ALT Linux distribution.


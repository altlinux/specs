Name: libgsm
Version: 1.0.13
Release: alt5

Summary: GSM audio encoding/decoding library
License: Free/Copyright Technische Universitaet Berlin
Group: System/Libraries

Url: http://user.cs.tu-berlin.de/~jutta/toast.html

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: ftp://ftp.cs.tu-berlin.de/pub/local/kbs/tubmik/gsm/gsm-%version.tar.gz
Patch: %name-1.0.10-pld-makefile.patch
Patch1: %name.link.patch

%description
This is a free and public implementation of GSM audio encoding and
decoding. GSM encoding has specific uses in transmission of packetized
audio over the Internet.

%package utils
Summary: Utilities for compress/decompress audio files using GSM format
Group: Sound

%description utils
This package contains utilities - tost, untoast and tcat (works without
installation libgsm) for compress/decompress files using GSM format.

%package devel
Summary: Header files and development documentation for libgsm
Group: Development/C
Requires: %name = %version

%description devel
Header files and development documentation for libgsm.

%package devel-static
Summary: GSM Audio Encoding/decoding static library
Group: Development/C
Requires: %name-devel = %version

%description devel-static
GSM Audio Encoding/decoding static library.

%prep
%setup -q -n gsm-1.0-pl13
%patch -p1
%patch1 -p0

%build
sed -i "s!ROOT)/lib!ROOT)/%_lib!" Makefile
%make_build OPTFLAGS="${CFLAGS:-%optflags}" WAV49="-DWAV49"
%make addtst

%install
install -d %buildroot{%_bindir,%_mandir/man{1,3},%_includedir,%_libdir}
%makeinstall INSTALL_ROOT=%buildroot

echo .so toast.1 >%buildroot%_man1dir/tcat.1
echo .so toast.1 >%buildroot%_man1dir/untoast.1

%files
%doc COPYRIGHT ChangeLog MACHINES MANIFEST README
%_libdir/%name.so.*

%files utils
%_bindir/*
%_man1dir/*

%files devel
%_libdir/%name.so
%_includedir/*
%_man3dir/*

%files devel-static
%_libdir/%name.a

%changelog
* Mon Aug 08 2011 Denis Smirnov <mithraen@altlinux.ru> 1.0.13-alt5
- rebuild

* Wed May 25 2011 Denis Smirnov <mithraen@altlinux.ru> 1.0.13-alt4
- rebuild

* Sat Apr 02 2011 Denis Smirnov <mithraen@altlinux.ru> 1.0.13-alt3
- rebuild

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0.13-alt2
- auto rebuild

* Thu Nov 12 2009 Denis Smirnov <mithraen@altlinux.ru> 1.0.13-alt1
- update to 1.0pl13

* Mon Dec 08 2008 Denis Smirnov <mithraen@altlinux.ru> 1.0.10-alt8
- cleanup spec 

* Wed May 10 2006 Denis Smirnov <mithraen@altlinux.ru> 1.0.10-alt7
- x86_64 build fixed

* Wed May 03 2006 Denis Smirnov <mithraen@altlinux.ru> 1.0.10-alt6
- fix x86_64 build

* Sat Mar 18 2006 Denis Smirnov <mithraen@altlinux.ru> 1.0.10-alt5
- fix for --as-needed

* Thu Jul 01 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.10-alt4
- fixed %files section.

* Thu Jul 01 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.10-alt3
- fix source files permissions.

* Mon Oct 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.10-alt2
- Rebuild with gcc-3.2.

* Wed Dec 12 2001 Yuri N. Sedunov <aris@altlinux.ru> 1.0.10-alt1
- PLD Team package 1.0.10-5 adopted for Sisyphus.

Name: libgsm
Version: 1.0.17
Release: alt1

Summary: GSM audio encoding/decoding library
License: Free/Copyright Technische Universitaet Berlin
Group: System/Libraries
Url: http://www.quut.com/gsm/
Packager: Denis Smirnov <mithraen@altlinux.ru>

# http://www.quut.com/gsm/gsm-%version.tar.gz
Source: gsm-%version.tar
Patch1: gsm-pld-alt-makefile.patch
Patch2: gsm-rh-warnings.patch

%description
This is a free and public implementation of GSM audio encoding and
decoding. GSM encoding has specific uses in transmission of packetized
audio over the Internet.

%package utils
Summary: Utilities for compress/decompress audio files using GSM format
Group: Sound
Requires: %name = %version-%release

%description utils
This package contains utilities - tost, untoast and tcat (works without
installation libgsm) for compress/decompress files using GSM format.

%package devel
Summary: Header files and development documentation for libgsm
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files and development documentation for libgsm.

%package devel-static
Summary: GSM Audio Encoding/decoding static library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
GSM Audio Encoding/decoding static library.

%prep
%setup -n gsm-1.0-pl13
sed -i 's/^\(CCFLAGS[[:space:]]*=[[:space:]]*\)-c -O2\(.*\)/\1 $(OPTFLAGS) \2/' Makefile
%patch1 -p1
#patch2 -p1

%build
%make_build SLIB=%_lib OPTFLAGS='%optflags -D_REENTRANT'

%install
mkdir -p %buildroot{%_bindir,%_mandir/man{1,3},%_includedir/gsm,%_libdir}
%makeinstall_std SLIB=%_lib INSTALL_ROOT=%buildroot
ln -s gsm/gsm.h %buildroot%_includedir/

echo .so toast.1 >%buildroot%_man1dir/tcat.1
echo .so toast.1 >%buildroot%_man1dir/untoast.1

%check
LD_LIBRARY_PATH=%buildroot%_libdir make tst addtst SLIB=%_lib

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

%changelog
* Tue Apr 10 2018 Denis Smirnov <mithraen@altlinux.ru> 1.0.17-alt1
- 1.0.17

* Mon Mar 27 2017 Denis Smirnov <mithraen@altlinux.ru> 1.0.16-alt1
- 1.0.16

* Sun Apr 14 2013 Dmitry V. Levin <ldv@altlinux.org> 1.0.13-alt8
- Fixed build.
- Fixed debuginfo.
- Dropped libgsm-devel-static.

* Wed Feb 20 2013 Denis Smirnov <mithraen@altlinux.ru> 1.0.13-alt7
- add symlink %_includedir/gsm/gsm.h (ALT #28579)

* Fri Jan 25 2013 Denis Smirnov <mithraen@altlinux.ru> 1.0.13-alt6
- fix requires in subpackages

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

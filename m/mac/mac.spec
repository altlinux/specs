# [for (x)emacs] -*-  mode: RPM-SPEC; coding: utf-8 -*-
Name: mac
Version: 7.09
Release: alt1

Summary: Monkey's Audio Codec
License: Distributable (see license.html)
Group: Sound

Url: http://www.monkeysaudio.com
Source0: %name-%version.zip
Source1: MAC-ALTLinux-permission.html
Source2: license.html

# Automatically added by buildreq on Sun Oct 03 2021
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libstdc++-devel python3-base sh4
BuildRequires: gcc-c++ unzip

%description
Monkey's Audio Codec is a lossless audio codec w/ good
correspondence of compression (and decompresssion) ratio
and time.

%package -n libmac
Summary: Monkey's Audio Codec shared libraries
Group: System/Libraries
%description -n libmac
Monkey's Audio Codec is a lossless audio codec w/ good
correspondence of compression (and decompresssion) ratio
and time.

This package contains shared libraries from
Monkey's Audio Codec SDK

%package -n libmac-devel
Summary: Headers from Monkey's Audio Codec SDK
Summary(ru_RU.UTF-8): Заголовочные файлы SDK кодека Monkey's Audio
Group: Development/C++
Requires: libmac = %version-%release

%description -n libmac-devel
Monkey's Audio Codec is a lossless audio codec w/ good
correspondence of compression (and decompresssion) ratio
and time.

This package contains header files from
Monkey's Audio Codec SDK

%prep
%setup -c
cp %SOURCE1 %SOURCE2 .
sed -i 's@(includedir)/MAC@(includedir)/mac@;s@libMAC@libmac@g' Source/Projects/NonWindows/Makefile
sed -i '1i#define PLATFORM_LINUX' Shared/All.h
sed -i '/\\\r*$/{N; s/\\\r*\n//}' Shared/All.h

%build
%make -f Source/Projects/NonWindows/Makefile libdir=%_libdir

%install
%makeinstall -f Source/Projects/NonWindows/Makefile libdir=%buildroot%_libdir

%files
%doc *html *txt
%_bindir/mac

%files -n libmac
%doc *html *txt
%_libdir/libmac.so.*

%files -n libmac-devel
%doc *html *txt
%_libdir/libmac.so
%_includedir/*

%changelog
* Sun Oct 03 2021 Fr. Br. George <george@altlinux.ru> 7.09-alt1
- Major version update
- License updated (it's permissive now)

* Mon Jul 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.99.u4-alt6.b5.4
- Patch console application to print error code descriptions

* Fri Jun 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.99.u4-alt6.b5.3
- Fix building with gcc-6

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.99.u4-alt6.b5.2.qa1
- NMU: rebuilt for updated dependencies.

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.99.u4-alt6.b5.2
- Rebuilt for debuginfo

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.99.u4-alt6.b5.1
- Rebuilt for soname set-versions

* Tue May 19 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 3.99.u4-alt6.b5
- Fix building with gcc4.4 (patches from rpmfusion)

* Wed Jan 16 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 3.99.u4-alt5.b5
- Fix building

* Fri Jun 23 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 3.99.u4-alt4.b5
- Resurrected from orphaned
- Updated to 3.99-u4 build 5

* Thu Jan 20 2005 Dmitry V. Levin <ldv@altlinux.org> 3.99.u4-alt3
- Fixed compilation issues detected by g++-3.4.3.
- Corrected interpackage dependencies.

* Fri Jul  9 2004 Alexey Morozov <morozov@altlinux.org> 3.99.u4-alt2
- First 'official' release
- Added Matthew T. Ashland permission to distribute the codec
- Package group changed to Sound

* Sat Jun 12 2004 Alexey Morozov <morozov@altlinux.org> 3.99.u4-alt1
- Initial build for ALT Linux

Name: upx
Version: 3.08
Release: alt1

Summary: The Ultimate Packer for eXecutables
License: GPLv2+
Group: Archiving/Compression

Url: http://upx.sourceforge.net
Source: %name-%version-src.tar.bz2

# Automatically added by buildreq on Tue Dec 23 2008
BuildRequires: gcc-c++ libucl-devel zlib-devel
BuildRequires: perl-podlators
# TODO: build with LZMA SDK from http://www.7-zip.org/sdk.html

%description
UPX is an advanced executable packer for several different executable formats.
It achieves an excellent compression ratio and offers very fast decompression.
Your executables suffer no memory overhead or other drawbacks.

%prep
%setup -n %name-%version-src

sed -i 's/-O2/%optflags/' src/Makefile
sed -i 's/-Werror//' src/Makefile
sed -i 's/\(char [*]delim\)/const \1/g' src/pefile.cpp

%build
%make_build -C src exeext=
%make_build -C doc

%install
install -pD -m755 src/upx %buildroot%_bindir/upx
install -pD -m644 doc/upx.1 %buildroot%_man1dir/upx.1

%files
%doc *[A-FH-Z] doc/*.txt
%_bindir/upx
%_man1dir/upx*

%changelog
* Wed Jan 11 2012 Fr. Br. George <george@altlinux.ru> 3.08-alt1
- Autobuild version bump to 3.08

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 3.07-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 25 2010 Fr. Br. George <george@altlinux.ru> 3.07-alt1
- Autobuild version bump to 3.07

* Thu May 13 2010 Fr. Br. George <george@altlinux.ru> 3.05-alt1
- New version

* Fri May 29 2009 Fr. Br. George <george@altlinux.ru> 3.03-alt2
- Quick'n'dirty GCC4.4 build fixup

* Tue Dec 23 2008 Victor Forsyuk <force@altlinux.org> 3.03-alt1
- 3.03

* Tue Oct 24 2006 Fr. Br. George <george@altlinux.ru> 2.02-alt1
- GEAR adapted
- Version up

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.25-alt1.1
- Rebuilt with libstdc++.so.6.

* Fri Oct 08 2004 Dmitry V. Levin <ldv@altlinux.org> 1.25-alt1
- Specfile cleanup.

* Wed Jun 30 2004 Götz Waschk <waschk@linux-mandrake.com> 1.25-2mdk
- enable parallel build
- fix used build flags
- fix description (Stef)

* Wed Jun 30 2004 Götz Waschk <waschk@linux-mandrake.com> 1.25-1mdk
- requires new ucl
- drop prefix
- download URL
- New release 1.25

* Mon Jun  7 2004 Götz Waschk <waschk@linux-mandrake.com> 1.24-3mdk
- rebuild for new g++

* Sun Apr  6 2003 Götz Waschk <waschk@linux-mandrake.com> 1.24-2mdk
- fix for new ucl header location

* Wed Nov 13 2002 Götz Waschk <waschk@linux-mandrake.com> 1.24-1mdk
- new version

* Mon Oct 28 2002 Götz Waschk <waschk@linux-mandrake.com> 1.23-1mdk
- new version

* Thu Aug 15 2002 Laurent Culioli <laurent@pschit.net> 1.22-3mdk
- Rebuild with gcc3.2

* Mon Jul 29 2002 Götz Waschk <waschk@linux-mandrake.com> 1.22-2mdk
- gcc 3.2 build

* Fri Jun 28 2002 Götz Waschk <waschk@linux-mandrake.com> 1.22-1mdk
- new version
- minor spec file fixes

* Fri Jun  7 2002 Götz Waschk <waschk@linux-mandrake.com> 1.21-1mdk
- update URL
- License instead of Copyright
- fix build, link with g++
- quiet tar
- 1.21

* Mon Jun 18 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 1.20-1mdk
- Ugly perl -pi -e to include the correct headers from ucl.
- Ugly perl -pi -e to take care of a difficult Makefile.
- Initial packaging.
- TODO see if need NRZ or not

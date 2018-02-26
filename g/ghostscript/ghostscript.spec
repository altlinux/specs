%define gsver	9.05
%define ijsver	0.35

Name: ghostscript
Version: %gsver
Release: alt1

%define esp_name esp-ghostscript
%define gnu_name gnu-ghostscript

URL: http://www.ghostscript.com

# Included CMap data is Redistributable, no modification permitted, 
License: GPLv3+ and Redistributable, no modification permitted

Summary: PostScript interpreter and renderer, most printer drivers
Group: Publishing

Source: http://ghostscript.com/releases/%name-%version.tar

Patch1: ghostscript-rh-cups-filters.patch
Patch2: ghostscript-rh-Fontmap.local.patch
Patch3: ghostscript-rh-gdevcups-debug-uninit.patch
Patch4: ghostscript-rh-iccprofiles-initdir.patch
Patch5: ghostscript-rh-multilib.patch
Patch6: ghostscript-rh-noopt.patch
Patch7: ghostscript-rh-runlibfileifexists.patch
Patch8: ghostscript-rh-scripts.patch
Patch9: ghostscript-alt-ijs-version.patch
Patch10: ghostscript-rh-ijs-automake-ver.patch
Patch11: ghostscript-alt-gstoraster-avoid-buidroot.patch

#compatibility requires
Requires: %name-classic = %gsver-%release
Provides: %esp_name = %gsver, %gnu_name = %gsver
Obsoletes: %gnu_name, %esp_name

BuildPreReq: libcairo-devel zlib-devel fontconfig-devel libjasper-devel libpaper-devel

# Automatically added by buildreq on Fri Aug 03 2007 (-bi)
BuildRequires: gcc-c++ glibc-devel-static imake libcups-devel libgtk+2-devel libjpeg-devel libgnutls-devel  libssl-devel libtiff-devel libXext-devel libXt-devel xorg-cf-files libpng-devel

%package -n libijs
Version: %{ijsver}_%gsver
Summary: Dynamic library for the IJS printer driver plug-in interface
Group: Publishing
Url: http://www.linuxprinting.org/ijs/
Provides: libespijs = %{ijsver}_%gsver, libgnuijs = %{ijsver}_%gsver
Obsoletes: libgnuijs, libespijs

%package -n libijs-devel
Version: %{ijsver}_%gsver
Summary: Headers and links for compiling against
Group: Development/C
Url: http://www.linuxprinting.org/ijs/
Requires: libijs = %{ijsver}_%gsver-%release
Provides: libespijs-devel = %{ijsver}_%gsver, libgnuijs-devel = %{ijsver}_%gsver
Obsoletes: libgnuijs-devel, libespijs-devel

%package module-X
Summary: PostScript interpreter and renderer (additional support for X)
Version: %gsver
Group: Publishing
PreReq: %name-classic = %gsver-%release
Provides: %esp_name-module-X = %gsver, %gnu_name-module-X = %gsver
Obsoletes: %gnu_name-module-X, %esp_name-module-X

%package utils
Summary: Additional tools for configuring printers
Version: %gsver
Group: Publishing
PreReq: %name-classic = %gsver-%release
Provides: %esp_name-utils = %gsver, %gnu_name-utils = %gsver
Obsoletes: %gnu_name-utils, %esp_name-utils
BuildArch: noarch

%package -n libgs
Summary: Shared library for %name
Version: %gsver
Group: Publishing
Provides: %esp_name-lib = %gsver, %gnu_name-lib = %gsver, %name-lib = %gsver
Obsoletes: %gnu_name-lib, %esp_name-lib, %name-lib

%package -n libgs-devel
Summary: Development library for %name
Version: %gsver
Group: Development/C

%package classic
Summary: classic edition of %name
Version: %gsver
Group: Publishing
PreReq: %name-common = %gsver-%release libgs = %gsver-%release
Provides: %esp_name-classic = %gsver, %gnu_name-classic = %gsver, %name-minimal = %gsver
Obsoletes: %gnu_name-classic, %esp_name-classic, %name-minimal

%package gtk
Summary: %name with gtk
Version: %gsver
Group: Publishing
PreReq: %name-lib = %gsver-%release, %name-common = %gsver-%release
Provides: %esp_name-gtk = %gsver, %gnu_name-gtk = %gsver
Obsoletes: %gnu_name-gtk, %esp_name-gtk

%package common
Summary: Common files for the %name
Version: %gsver
Group: Publishing
Requires: urw-fonts >= 1.1
Requires: %name-classic = %gsver-%release
Provides: %esp_name-common = %gsver, %gnu_name-common = %gsver
Obsoletes: %gnu_name-common, %esp_name-common
BuildArch: noarch

%package cups
Summary: CUPS specific files %name
Version: %gsver
Group: Publishing
Requires: %name = %gsver-%release
Requires: bc
Provides: %esp_name-cups = %gsver

%description
Ghostscript is a set of software that provides a PostScript(TM) interpreter,
a set of C procedures (the Ghostscript library, which implements the
graphics capabilities in the PostScript language) and an interpreter for
Portable Document Format (PDF) files. Ghostscript translates PostScript code
into many common, bitmapped formats, like those understood by your printer
or screen. Ghostscript is normally used to display PostScript files and to
print PostScript files to non-PostScript printers.
Most applications use PostScript for printer output.

In addition, the package contains filters which transfer the raw
bitmap of GhostScript into the protocol of some additional printer
models.

You should install ghostscript if you need to display PostScript files, or
if you have a non-PostScript printer.

%description module-X
Ghostscript is a PostScript interpreter. It can render both PostScript
and PDF compliant files to devices which include an X window, many printer
formats (including support for colour printers), and popular graphics
file formats.
This version enhances ghostscript with X windows support.

%description utils
Tools for printer maintenance: Setting default options for most laser
printers (PJL-capable printers), cartridge changing and head aligning
for inkjet winprinters.

%description -n libijs
This is the API library for programs using the IJS printer driver
plug-in interface. Printer drivers using this interface can be added
to GhostScript (6.53 or newer) without needing to rebuild
GhostScript. Application programs providing an IJS interface can make
use of IJS printer drivers directly, without needing GhostScript.

%description -n libijs-devel
This package contains the static library and the header files needed
to compile applications using this library.

%description -n libgs
Shared library for %name

%description -n libgs-devel
Development library for %name

%description classic
Classic edition of %name

%description gtk
%name with gtk

%description common
Common files for the %name

%description cups
CUPS specific files %name

%prep
%setup -q

# force system library usage
rm -rf -- libpng zlib jpeg jasper

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p2

%autoreconf

%build
export CFLAGS=-DA4

%configure --enable-dynamic \
	   --with-system-libtiff \
           --with-ijs \
	   --with-drivers=ALL \
	   --disable-compile-inits \
	   --with-install-cups \
	   --with-fontpath=/usr/share/fonts/default:\
/usr/share/fonts/type1:\
/usr/share/fonts/type1/urw:\
/usr/share/fonts:\
%_datadir/ghostscript/conf.d \
#

#NO SMP
%make
%make so

cd ijs
    ./autogen.sh
    %configure --enable-shared --enable-static
    %make
cd -

%install

make install soinstall \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	gsincludedir=$RPM_BUILD_ROOT%{_includedir}/ghostscript/ \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	docdir=$RPM_BUILD_ROOT%{_docdir}/%{name}-%gsver \
	gsdir=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	gsdatadir=$RPM_BUILD_ROOT%{_datadir}/%{name}/%gsver \
	gssharedir=$RPM_BUILD_ROOT%{_libdir}/%{name}/%gsver \
	CUPSSERVERROOT=$RPM_BUILD_ROOT`cups-config --serverroot` \
	CUPSSERVERBIN=$RPM_BUILD_ROOT`cups-config --serverbin` \
	CUPSDATA=$RPM_BUILD_ROOT`cups-config --datadir`

# replace classic ghostscript with more modern version
mv -f -- $RPM_BUILD_ROOT%_bindir/gsc $RPM_BUILD_ROOT%_bindir/gs

cd ijs
    %makeinstall
cd -

rm -rf -- %buildroot%_mandir/de
rm -rf -- %buildroot%_datadir/ghostscript/%gsver/Resource/Font
rm -f  -- %buildroot%_bindir/ijs_{client,server}_example

# X11.so always gets loaded, even with 'gs --help'
mkdir -p %buildroot/etc/buildreqs/packages/ignore.d
echo %name-module-X >%buildroot/etc/buildreqs/packages/ignore.d/%name-module-X

mkdir -p %buildroot/%_datadir/ghostscript/conf.d

%files

%files common
%doc %_docdir/%name-%gsver
%_datadir/ghostscript
%_datadir/ghostscript/conf.d
%_bindir/pdf2dsc
%_bindir/pdf2ps
%_bindir/gsnd

%files cups
/usr/lib/cups/filter/*
%_datadir/cups/model/*
%_datadir/cups/mime/*

%files classic
%_bindir/gs

%files gtk
%_bindir/gsx

%files utils
%_bindir/*
#common excludes
%exclude %_bindir/gs
%exclude %_bindir/gsx
%exclude %_bindir/*ijs*
%exclude %_bindir/pdf2dsc
%exclude %_bindir/pdf2ps
%exclude %_bindir/gsnd
%_man1dir/*

%files module-X
%_libdir/ghostscript
/etc/buildreqs/packages/ignore.d/%name-module-X

%files -n libgs
%_libdir/libgs.so.*

%files -n libgs-devel
%_libdir/libgs.so
%_includedir/%name

%files -n libijs
%_libdir/libijs.so.*

%files -n libijs-devel
%doc ijs/README
%_bindir/ijs-config
%_libdir/pkgconfig/*
%_libdir/libijs.so
%_includedir/ijs

%changelog
* Wed Feb 15 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 9.05-alt1
- 9.05

* Thu Sep 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.04-alt2
- resurrect ghostscript-alt-gstoraster-avoid-buidroot.patch (ALT #25465)

* Wed Aug 10 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.04-alt1
- 9.04
- update fedora patches

* Mon Aug 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.02-alt3
- add %_datadir/%name/conf.d to fontpath (ALT #25997)

* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.02-alt2
- avoid buildroot-ed paths in gstoraster (ALT #25465)

* Mon Apr 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.02-alt1
- 9.02
- update fedora patches
- add ghostscript-classic to ghostscript-common Requires (ALT #25373)

* Thu Mar 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.01-alt2
- add libpng-devel to BuildRequires

* Mon Feb 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.01-alt1
- 9.01
- update fedora patches

* Mon Jan 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.00-alt2
- Add fedora patches:
    ghostscript-rh-gdevcups-691733.patch (ALT #24832)
    ghostscript-rh-icc-fix.patch
    ghostscript-rh-scan_token.patch

* Tue Oct 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 9.00-alt1
- 9.00
- CVE-2010-2055

* Sat Mar 13 2010 Stanislav Ievlev <inger@altlinux.org> 8.71-alt1
- 8.71

* Mon Nov 02 2009 Stanislav Ievlev <inger@altlinux.org> 8.70-alt3
- fix deps:
  * drop unused ghostscript-rip provides
  * module-X and utils subpackage now require ghostscript-classic instead of ghostscript-rip

* Thu Oct 01 2009 Stanislav Ievlev <inger@altlinux.org> 8.70-alt2
- fix header files names in ghostscript devel library

* Mon Sep 14 2009 Stanislav Ievlev <inger@altlinux.org> 8.70-alt1
- 8.70
- join minimal and classic subpackages
- drop espgs-alt-visibility patch, because X11.so driver uses some
  internal symbols from the library

* Fri Apr 17 2009 Stanislav Ievlev <inger@altlinux.org> 8.64-alt4
- CVE-2009-0196, CVE-2009-0792

* Fri Mar 20 2009 Stanislav Ievlev <inger@altlinux.org> 8.64-alt3
- CVE-2009-0583, CVE-2009-0584

* Wed Mar 11 2009 Kirill Maslinsky <kirill@altlinux.ru> 8.64-alt2
- rebuilt to eliminate dependency on tetex-dvips (closes: #19128)
- removed calls to %%post(un)_ldconfig

* Fri Feb 27 2009 Stanislav Ievlev <inger@altlinux.org> 8.64-alt1
- 8.64

* Sat Nov 22 2008 Fr. Br. George <george@altlinux.ru> 8.63-alt1.1
- A4 definition added

* Fri Oct 03 2008 Stanislav Ievlev <inger@altlinux.org> 8.63-alt1
- 8.63

* Thu May 08 2008 Stanislav Ievlev <inger@altlinux.org> 8.62-alt1
- 8.62
- rename ghostscript-lib to libgs, add devel part

* Thu Mar 27 2008 Stanislav Ievlev <inger@altlinux.org> 8.60-alt3
- build for Sisyphus with changes from at@: spec: ghostscript-module-X11 ignore file for buildreq

* Thu Feb 28 2008 Stanislav Ievlev <inger@altlinux.org> 8.60-alt2
- CVE-2008-0411

* Thu Nov 08 2007 Stanislav Ievlev <inger@altlinux.org> 8.60-alt1
- remove deps on ghostscript-drivers

* Mon Aug 06 2007 Stanislav Ievlev <inger@altlinux.org> 8.60-alt0.3
- improve latest hack

* Mon Aug 06 2007 Stanislav Ievlev <inger@altlinux.org> 8.60-alt0.2
- fix build on i586

* Fri Aug 03 2007 Stanislav Ievlev <inger@altlinux.org> 8.60-alt0.1
- 8.60 (test build)
- disable jasper library (ghostscript can work with internal copy of library)

* Thu Jun 28 2007 Kirill A. Shutemov <kas@altlinux.ru> 8.15.4-alt1.1
- Drop BuildPreReq: kernel-headers-std

* Thu Mar 15 2007 Stanislav Ievlev <inger@altlinux.org> 8.15.4-alt1
- 8.15.4 (bugfix release)

* Thu Jan 25 2007 Stanislav Ievlev <inger@altlinux.org> 8.15.3-alt0.3
- apply 64 fix from RH (bug #177763 in bugzilla.redhat.com)

* Fri Dec 29 2006 Stanislav Ievlev <inger@altlinux.org> 8.15.3-alt0.2
- Change default visibility for the libraries (avm)

* Fri Oct 13 2006 Stanislav Ievlev <inger@altlinux.org> 8.15.3-alt0.1
- 8.15.3

* Wed May 24 2006 Stanislav Ievlev <inger@altlinux.org> 8.15.2-alt0.1
- 8.15.2

* Thu Mar 23 2006 Stanislav Ievlev <inger@altlinux.org> 8.15.1-alt0.1
- 8.15.1

* Fri May 13 2005 Stanislav Ievlev <inger@altlinux.org> 8.15.0-alt0.1
- 8.15
- all additional drivers are in separate package now

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 7.07.1-alt6.1
- Rebuilt with libstdc++.so.6.

* Thu Oct 07 2004 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt6
- turn off fontconfig patch (author of this patch RH has been discovered some strange problems)

* Wed Sep 22 2004 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt5
- driver updates

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 7.07.1-alt4.1.1
- Rebuilt with libtiff.so.4.

* Tue May 11 2004 ALT QA Team Robot <qa-robot@altlinux.org> 7.07.1-alt4.1
- Rebuilt with openssl-0.9.7d.

* Tue May 11 2004 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt4
- fix bootstrap

* Wed May 05 2004 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt3
- added ppmtomd driver
- added support for KRGB (from hpijs 1.6)
- don't build cat files (was problems with building in hasher)

* Mon Mar 15 2004 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt2
- update epsonepl driver to add support for EPL6200L

* Fri Feb 13 2004 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt1
- fix requires (urw-fonts) in common package.

* Tue Feb 10 2004 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt0.4
- rename back to ghostscript (to minor problems on update)
- added pentaxpj driver for Pentax PocketJet printers

* Thu Dec 25 2003 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt0.3
- correct fontpath (was problems with printing Japanese)
- added lexmark Z11 driver

* Tue Dec 02 2003 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt0.2
- added epsonepl driver
- Daedalus release

* Thu Nov 06 2003 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt0.1
- 7.07.1
- change font path
- fix requires module-X and drivers (added virtual providing %name-rip)
	 

* Fri May 16 2003 Stanislav Ievlev <inger@altlinux.ru> 7.05.6-alt0.8
- added pnm2ppa and pbm2ppa (old version of pnm2ppa) drivers for HP PPA WinPrinters
- fix requires (classic doesn't need lib)

* Wed May 07 2003 Stanislav Ievlev <inger@altlinux.ru> 7.05.6-alt0.7
- added CID support

* Wed Apr 30 2003 Stanislav Ievlev <inger@altlinux.ru> 7.05.6-alt0.6
- added module X11 feature
- pdf2dsc, pdf2ps moved to common like in gnu ghostscript (gv need it)
- added ml85p driver (Samsung ML-85G and QL-85G winprinters)

* Mon Apr 07 2003 Stanislav Ievlev <inger@altlinux.ru> 7.05.6-alt0.5
- Initial release


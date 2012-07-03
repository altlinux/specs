Name: bochs
Version: 2.5.1
Release: alt1

Summary: Bochs Project x86 PC Emulator
Summary(ru_RU.KOI8-R): Проект Bochs -- эмулятор x86 PC

License: LGPL
Group: Emulators
Url: http://bochs.sourceforge.net

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: %name-%version.tar.gz
Source1: bochs.sh

# Automatically added by buildreq on Fri Sep 15 2006
BuildRequires: docbook-utils gcc-c++ libgtk+2-devel imake libpcap-devel libreadline-devel libXpm-devel libXt-devel wget wxGTK-devel libwxGTK-devel xorg-cf-files zlib-devel libXau-devel libXdmcp-devel libXrandr-devel

#uildRequires: OpenSP XFree86-libs docbook-dtds docbook-style-dsssl docbook-utils gcc-c++ glib gtk+-devel hostinfo libjpeg libncurses-devel libpcap-devel libreadline-devel libstdc++-devel libtiff openjade sgml-common wxGTK-devel xml-common

%description
Bochs is a portable x86 PC emulation software package that emulates enough of
the x86 CPU, related AT hardware, and BIOS to run DOS, Windows '95, Minix 2.0,
and other OS's, all on your workstation.

%description -l ru_RU.KOI8-R
Bochs -- это не зависящий от аппаратной платформы эмулятор x86 PC,
который эмулирует процессор x86, необходимое аппаратное обеспечение AT
и BIOS для запуска DOS, Windows '95, Minix 2.0, и других операционных
систем на вашей рабочей станции.

%prep
%setup -q
%__cp %SOURCE1 bochs.sh
%__subst "s|bios/|/usr/share/bochs/|" ./.bochsrc
%__subst "s|#config_interface: wx|config_interface: wx|" ./.bochsrc
%__subst "s|#display_library: wx|display_library: wx|" ./.bochsrc

%build
%configure --enable-fpu --enable-cdrom --enable-sb16=linux  --enable-split-hd  --enable-ne2000 --with-x11 --with-wx --enable-pci --enable-usb 

%make

%install
%makeinstall

install -p -m755 bochs.sh $RPM_BUILD_ROOT/%_bindir/%name-gui
install -D -m 644 gui/icon_%name.xpm $RPM_BUILD_ROOT/%_niconsdir/%name.xpm

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Bochs
Comment=Bochs Project x86 PC Emulator
GenericName=Emulator
Icon=%name
Exec=%name-gui
Terminal=false
Categories=System;Emulator;
EOF


%files
%_bindir/*
%_datadir/%name
%_man1dir/*
%_man5dir/*
%_docdir/%name
%_desktopdir/%name.desktop
%_niconsdir/*

%changelog
* Thu Jan 12 2012 Ilya Mashkin <oddity@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Sun Dec 04 2011 Ilya Mashkin <oddity@altlinux.ru> 2.5-alt1
- 2.5

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 2.4.6-alt1.qa1
- NMU: converted menu to desktop file

* Mon Feb 28 2011 Ilya Mashkin <oddity@altlinux.ru> 2.4.6-alt1
- 2.4.6
- Update requires

* Sun May 02 2010 Ilya Mashkin <oddity@altlinux.ru> 2.4.5-alt1
- 2.4.5

* Wed Mar 10 2010 Ilya Mashkin <oddity@altlinux.ru> 2.4.2-alt2
- rebuild with current wxGTK

* Sun Nov 15 2009 Ilya Mashkin <oddity@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.4-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for bochs
  * postclean-05-filetriggers for spec file

* Mon May 11 2009 Ilya Mashkin <oddity@altlinux.ru> 2.4-alt1
- 2.4

* Thu Jul 03 2008 Ilya Mashkin <oddity at altlinux.ru> 2.3.7-alt1
- 2.3.7

* Wed Dec 26 2007 Ilya Mashkin <oddity at altlinux.ru> 2.3.6-alt1
- New version 2.3.6
+ More than 25%% emulation speedup vs Bochs 2.3.5 release
+ Up to 40%% speedup vs Bochs 2.3.5 release with trace cache optimization
+ Added emulation of Intel SSE4.2 instruction set
+ Bochs benchmarking support

* Tue Sep 18 2007 Ilya Mashkin <oddity at altlinux.ru> 2.3.5-alt1
- New version  2.3.5 
- Brief summary :
- Critical problems fixed for x86-64 support in CPU and Bochs internal debugger
- ACPI support
- The release compiled with x86-64 and ACPI
- Hard disk emulation supports ATA-6 (LBA48 addressing, UDMA modes)
- Added emulation of Intel SSE4.1 instruction set

* Sat Dec 23 2006 Ilya Mashkin <oddity at altlinux.ru> 2.3-alt3
- rebuild with wxGTK2u

* Tue Nov 07 2006 Ilya Mashkin <oddity at altlinux.ru> 2.3-alt2
- fix build

* Fri Sep 15 2006 Ilya Mashkin <oddity at altlinux.ru> 2.3-alt1
- New version 2.3

* Mon Feb 06 2006 Ilya Mashkin <oddity at altlinux.ru> 2.2.6-alt1
- New version 2.2.6

* Wed Jan 18 2006 Ilya Mashkin <oddity at altlinux.ru> 2.2.5-alt1
- New version 2.2.5

* Sat Nov 20 2005 Ilya Mashkin <oddity at altlinux.ru> 2.2.1-alt1
- New version 2.2.1

* Wed Jan 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.1.1-alt2.1.1
- Rebuilt with libstdc++.so.6.

* Tue Jun 22 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt2.1
- move to Applications/Emulators menu section

* Sun Jun 20 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt2
- rebuild
- add icon

* Wed Feb 18 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version
- build with --enable-vbe --enable-pci --enable-usb --enable-mmx

* Mon Jan 05 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt0.1pre3
- CVS version
- build with gcc 3.3

* Thu Jun 26 2003 Stanislav Ievlev <inger@altlinux.ru> 2.0.2-alt2.1
- really rebuild with new wxGTK

* Fri Jun 20 2003 Andrey Astafiev <andrei@altlinux.ru> 2.0.2-alt2
- rebuilt with new wxGTK

* Mon Apr 07 2003 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- new version
- fixed bug #2489 (condrestart for xfs)
- build with wxWindows support
- add menu entry
- add shell wrapper for start from menu
- update buildreq

* Fri Jan 10 2003 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- cleanup spec
- new version
- add buildrequires

* Fri Nov 02 2002 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- first build for Sisyphus
- spec adapted
- dlxlinux disabled

* Sat Aug 31 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.4.1-2mdk
- rebuild

* Wed Jul 24 2002 Sylvestre Taburet <staburet@mandrakesoft.com> 1.4.1-1mdk
- upgraded to 1.4.1 (service release)

* Tue May 28 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.4-3mdk
- rebuild against new libstdc++

* Mon Apr 08 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.4-2mdk
- fix %post & %pre by adding %version to cure problem when
  version changes ( thx Quel Qun )

* Sat Mar 30 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.4-1mdk
- 1.4

* Tue Feb 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.3-1mdk
- new


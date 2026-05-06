Name: usbview
Version: 3.1
Release: alt1
Epoch: 1

Summary: USB topology and device viewer
Group: System/Kernel and hardware
License: GPL
Url: http://www.kroah.com/linux-usb

Source: https://github.com/gregkh/usbview/archive/refs/tags/v3.1.tar.gz#/%name-%version.tar.gz

BuildRequires: libgtk+3-devel /usr/bin/convert


%description
USBView is a GTK program that displays the topography of the devices that are
plugged into the USB bus on a Linux machine. It also displays information on
each of the devices. This can be useful to determine if a device is working
properly or not.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS ChangeLog* README*
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_man8dir/usbview.8*
%_datadir/metainfo/*.xml

%changelog
* Sun May 03 2026 Ildar Mulyukov <ildar@altlinux.ru> 1:3.1-alt1
- new version

* Sun Jun 01 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.0-alt1
- new version

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_1deb
- new version

* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt2_11deb
- converted debian menu to freedesktop

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_11deb.1
- NMU (by repocop): the following fixes applied:
 * update_menus for usbview

* Mon Apr 28 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_11deb
- resurrected from orphaned
- Epoch++ due to ipl3mdk
- fixed *iconsdir
- debian stuff merged using debian2spec 
- gtk2 build (debian -11 patchset)

* Mon Oct 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0-ipl3mdk
- Rebuilt in new environment

* Thu Nov 29 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0-ipl2mdk
- Rebuild for Sisyphus
- Some spec cleanup

* Sat Dec 16 2000 Dmitry V. Levin <ldv@fandra.org> 1.0-ipl1mdk
- RE adaptions.

* Thu Dec  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0-1mdk
- 1.0.

* Sat Dec  2 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.9.0-2mdk
- Add icons.

* Sun Sep 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.9.0-1mdk
- 0.9.0

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.8.1-3mdk
- automatically added BuildRequires

* Fri Jul 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.8.1-2mdk
- BM
- more macros

* Fri Jun 30 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.8.1-1mdk
- macros everywhere.
- 0.8.1.

* Fri Jun 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.8.0-2mdk
- Add menu.

* Fri Jun 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.8.0-1mdk
- 0.8.0.
- Clean up specs.

* Sat Mar 25 2000 Daouda Lo <daouda@mandrakesoft.com> 0.5.0-3mdk
- ready for 7.1

* Wed Dec  8 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- small specs tweaks.

* Tue Dec 07 1999 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- first specfile

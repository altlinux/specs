Name: usbview
Version: 1.1
Release: alt1_1deb
Epoch: 1

Summary: USB topology and device viewer
Group: System/Kernel and hardware
License: GPL
Url: http://www.kroah.com/linux-usb
Packager: Igor Vlasenko <viy@altlinux.ru>

Source: %url/%name-%version.tar
Source1: %name-icons.tar

Patch0: usbview_1.1-1.diff.gz

# Automatically added by buildreq on Mon Apr 28 2008 (-bi)
BuildRequires: libgtk+2-devel
# packagereq: optimized out:
BuildRequires: fontconfig fontconfig-devel glib2-devel libatk-devel libcairo-devel libfreetype-devel libgtk+2-common libgtk+2-common-devel libpango-devel pkg-config zlib-devel


%description
USBView is a GTK program that displays the topography of the devices that are
plugged into the USB bus on a Linux machine. It also displays information on
each of the devices. This can be useful to determine if a device is working
properly or not.

%prep
%setup -q
%patch0 -p1

%build
#autoreconf -fisv
%configure
%make_build

%install
%makeinstall

pushd %buildroot
tar xf %SOURCE1
popd

mkdir -p $RPM_BUILD_ROOT%_desktopdir
cat > $RPM_BUILD_ROOT%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=UsbView
GenericName=USB viewver
Comment=USB topology and device viewer
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=Settings;HardwareSettings;
EOF

# installing debian man pages
install -d ${RPM_BUILD_ROOT}%_man8dir
install -m644 usbview.8 ${RPM_BUILD_ROOT}%_man8dir/

%files
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*.png
%_man8dir/usbview.8*

%changelog
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

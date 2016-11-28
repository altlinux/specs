Name: virt-viewer
Version: 5.0
Release: alt1

Summary: Virtual Machine Viewer
Group: System/Configuration/Other
License: GPL
Url: http://virt-manager.org/

Source: %name-%version.tar

Obsoletes: spice-client < 0.12.5-alt3

BuildRequires: glib2-devel >= 2.38.0 libgio-devel
BuildRequires: libxml2-devel
BuildRequires: libvirt-devel >= 0.9.7 libvirt-glib-devel >= 0.1.8
BuildRequires: libgtk+3-devel >= 3.10
BuildRequires: perl-podlators intltool
BuildRequires: libspice-gtk3-devel >= 0.33 libspice-glib-devel spice-protocol >= 0.12.7
BuildRequires: libgtk3vnc-devel >= 0.4.0
BuildRequires: libgovirt-devel >= 0.3.2

%description
Virt Viewer provides a graphical viewer for the guest OS
display. At this time is supports guest OS using the VNC
or SPICE protocols. Further protocols may be supported in
the future as user demand dicatates. The viewer can connect
directly to both local and remotely hosted guest OS, optionally
using SSL/TLS encryption.

%prep
%setup

%build
mkdir -p m4
touch ChangeLog AUTHORS
intltoolize --force
%autoreconf
%configure \
	--disable-static \
	--disable-update-mimedb \
	--with-buildid=-%release

%make_build

%install
%make_install install  DESTDIR=%buildroot
%find_lang %name

%files -f %name.lang
%doc README COPYING AUTHORS ChangeLog NEWS
%_bindir/*
%_man1dir/*
%_datadir/mime/packages/*.xml
%_desktopdir/*.desktop
%_datadir/appdata/remote-viewer.appdata.xml
%_iconsdir/hicolor/*/apps/*
%_iconsdir/hicolor/*/devices/*

%changelog
* Mon Nov 28 2016 Alexey Shabalin <shaba@altlinux.ru> 5.0-alt1
- 5.0

* Mon Jul 04 2016 Alexey Shabalin <shaba@altlinux.ru> 4.0-alt1
- 4.0

* Mon Jun 27 2016 Alexey Shabalin <shaba@altlinux.ru> 3.1-alt2
- rebuild with spice-gtk-0.32-alt1

* Mon Jan 11 2016 Alexey Shabalin <shaba@altlinux.ru> 3.1-alt1
- 3.1

* Tue Dec 08 2015 Alexey Shabalin <shaba@altlinux.ru> 3.0-alt1
- 3.0

* Tue Jan 27 2015 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.7-alt1.1
- rebuild with new libgovirt

* Wed Aug 07 2013 Alexey Shabalin <shaba@altlinux.ru> 0.5.7-alt1
- 0.5.7

* Mon May 06 2013 Alexey Shabalin <shaba@altlinux.ru> 0.5.6-alt1
- 0.5.6
- build with oVirt support

* Wed Sep 19 2012 Alexey Shabalin <shaba@altlinux.ru> 0.5.4-alt1
- 0.5.4

* Thu Apr 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Tue Nov 15 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Mon Aug 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt1
- 0.4.1
- build with gtk+3

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt2
- rebuild with new libspice-gtk-devel

* Mon Feb 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Thu Feb 17 2011 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1.hg20110211
- snapshot 20110211

* Tue Jan 18 2011 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1.hg20110112
- snapshot 20110112

* Thu Dec 30 2010 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1.hg20101221
- snapshot 20101221
- build with spice support

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jul 31 2009 Ilya Mashkin <oddity@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Sun Apr 13 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.0.3-alt1
- Initial build for ALTLinux

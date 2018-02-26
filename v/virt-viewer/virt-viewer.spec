Name: virt-viewer
Version: 0.5.2
Release: alt1

Summary: Virtual Machine Viewer
Group: System/Configuration/Other
License: GPL
Url: http://virt-manager.org/

Source: %name-%version.tar

BuildRequires: libxml2-devel glib2-devel
BuildRequires: libvirt-devel >= 0.9.7
BuildRequires: perl-podlators intltool
BuildRequires: libspice-gtk-devel >= 0.11 spice-protocol >= 0.10.1
# BuildRequires: libgtkvnc-devel >= 0.3.8
BuildRequires: libgtk3vnc-devel >= 0.4.0

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
%autoreconf
%configure --with-gtk=3.0
%make

%install
%make_install install  DESTDIR=%buildroot
%find_lang %name

%files -f %name.lang
%doc README COPYING AUTHORS ChangeLog NEWS
%_bindir/*
%_man1dir/*
%_datadir/%name/ui/*.xml
%_iconsdir/hicolor/*/apps/%name.png

%changelog
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

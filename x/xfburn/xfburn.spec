Name: xfburn
Version: 0.4.3
Release: alt3

Summary: CD-R/CD-RW disc writing application
Url: http://www.xfce.org/projects/xfburn/ 
License: %gpl2plus
Packager: XFCE Team <xfce@packages.altlinux.org>
Group: Archiving/Cd burning

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: xfce4-dev-tools rpm-build-xfce4
BuildPreReq: libxfce4ui-devel libexo-devel
BuildRequires: libdbus-glib-devel xsltproc docbook-style-xsl
BuildRequires: gst-plugins-devel libburn-devel libisofs-devel libgio-devel libgudev-devel


%description
Xfburn is a simple CD burning tool based on libburn/libisofs.


%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-dbus \
	--enable-gudev \
	--enable-gstreamer \
	--enable-final \
	--disable-profiling \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_iconsdir/hicolor/*/stock/media/*
%_desktopdir/*
%_datadir/Thunar/sendto/*.desktop
/usr/share/man/man1/*

%changelog
* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt3
- Fix build: Add missing header.
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Mon Mar 21 2011 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt2
- Patches from upstream's bug tracker (Xfce bug #7355):
    + Port to libxfce4ui.
    + Port to gio/udev, remove HAL support.

* Mon Jan 31 2011 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt1
- Spec update & cleanup.
- Updated to 0.4.3.

* Tue Apr 14 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.1-alt1
- new version 

* Mon Apr 13 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.0-alt2
- build fixed 

* Mon Jan 12 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.4.0-alt1
- new version

* Mon Oct 13 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3.3.svn5595-alt1
- new version
- git-svn imported repo

* Thu Mar 20 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3.0.svn20080320-alt1
- new version
- fixed build on Sisyphus 

* Wed Jan 16 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.3.0.svn20080117-alt1
- new version
- patch for build with libburn-0.4.0

* Thu Sep 20 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3.0.svn20070826-alt2
- fixed requires 

* Thu Sep 20 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3.0.svn20070826-alt1
- first build 


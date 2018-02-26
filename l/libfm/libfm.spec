Name: libfm
Summary: core part of pcmanfm-ng
Version: 0.1.17
Release: alt1
License: GPL
Group: File tools
Url: http://pcmanfm.sourceforge.net/

Source: %name-%version.tar.gz
#Source1: %name.watch

BuildPreReq: rpm-build-xdg
BuildRequires: intltool libgtk+2-devel libmenu-cache-devel gtk-doc
BuildRequires: libdbus-glib-devel udisks-devel

%description
Description: LibFM is a GIO-based library used to develop file
manager-like programs. It is developed as the core of next generation
PCManFM and takes care of all file-related operations such as
copy & paste, drag & drop, file associations or thumbnail support. By
utilizing glib/gio and gvfs, libfm can access remote filesystems
supported by gvfs.

%package devel
Summary: devel files for libmanfm
Group: Development/Other

%description devel
This package contains files needed to build libfm-dependent applications

%package devel-static
Summary: static devel
Group: Development/Other

%description devel-static
This package contains files needed to statically link to libfm

%prep
%setup

%build
%autoreconf
%configure \
    --enable-largefile \
    --enable-udisks \
    --sysconfdir=/etc

%make

%install
make DESTDIR=%buildroot install
%find_lang %name

%files -f %name.lang
%_xdgconfigdir/*
%_bindir/*
%_libdir/*.so.*

%_xdgmimedir/packages/*
%_datadir/%name/
%_desktopdir/*

%files devel
%_libdir/*.so
%_includedir/%name
%_pkgconfigdir/*

%files devel-static
%_libdir/*.a

%changelog
* Tue Jan 31 2012 Radik Usupov <radik@altlinux.org> 0.1.17-alt1
- new version (0.1.17)

* Wed Aug 31 2011 Radik Usupov <radik@altlinux.org> 0.1.16-alt1
- new snapshot

* Thu Jul 14 2011 Mykola Grechukh <gns@altlinux.ru> 0.1.15-alt6
- new upstream snapshot
- fixed bug with DnD folder to bookmarks

* Wed Jul 06 2011 Mykola Grechukh <gns@altlinux.ru> 0.1.15-alt5
- new upstream snapshot

* Tue May 31 2011 Mykola Grechukh <gns@altlinux.ru> 0.1.15-alt4
- new snapshot

* Tue Apr 26 2011 Mykola Grechukh <gns@altlinux.ru> 0.1.15-alt3
- new snapshot

* Tue Mar 01 2011 Timur Aitov <timonbl4@altlinux.org> 0.1.15-alt1
- new snapshot

* Mon Oct 25 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.14-alt1
- new snapshot

* Thu Sep 23 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.13-alt3
- new snapshot

* Fri Aug 27 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.13-alt2
- udisks support activated

* Wed Jul 21 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.13-alt1
- new upstream version

* Sun May 30 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.12-alt1
- new upstream version

* Tue May 04 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.11-alt1
- new upstream version

* Mon Apr 26 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.10-alt1
- new version

* Mon Apr 12 2010 Nick S. Grechukh <gns@altlinux.ru> 0.1.9-alt1
- new version

* Fri Mar 12 2010 Nick S. Grechukh <gns@altlinux.ru> 0.1.5-alt1
- first build

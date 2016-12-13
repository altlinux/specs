%define soname 4
%define gtkver 2

Name: libfm
Version: 1.2.5
Release: alt1

Summary: Core library of PCManFM file manager
License: GPL
Group: System/Libraries

Url: http://lxqt.org
Source: %name-%version.tar

BuildPreReq: rpm-build-xdg
BuildRequires: intltool libmenu-cache-devel
BuildRequires: libdbus-glib-devel libudisks2-devel
BuildRequires: glib2-devel libgtk+%gtkver-devel gtk-doc
BuildRequires: vala >= 0.13.0
BuildRequires: libexif-devel
BuildRequires: libxslt-devel

BuildRequires: gcc-c++ cmake rpm-macros-cmake
#BuildRequires: qt5-base-devel
#BuildRequires: libqtxdg-devel

%description
LibFM is a core library of PCManFM file manager.

%package -n %name%soname
Summary: %summary
Group: System/Libraries
Requires: gvfs wm-common-freedesktop
Conflicts: libfm2

%description -n %name%soname
LibFM is a core library of PCManFM file manager.

It is developed as the core of next generation PCManFM and takes care
of all file-related operations such as copy & paste, drag & drop, file
associations or thumbnail support. By utilizing glib/gio and gvfs
libfm can access remote filesystems supported by gvfs.

%package devel
Summary: Development files for %name
Group: Development/Other
Conflicts: libfm2-devel

%description devel
This package contains files needed to build applications using LibFM.

%package -n lxde-lxshortcut
Summary: Application shortcuts editor
Group: Graphical desktop/Other

%description -n lxde-lxshortcut
LXShortcut is a small program used to edit application shortcuts
created with freedesktop.org Desktop Entry spec.

%prep
%setup
sed -ri '/AM_INIT_AUTOMAKE/s,-Werror,\0 -Wno-portability,' configure.ac
%autoreconf

%build
%configure \
    --disable-static \
    --disable-silent-rules \
    --with-gtk=%gtkver \
    --enable-gtk-doc \
    --enable-largefile \
    --enable-udisks \
    --sysconfdir=%_sysconfdir

%make_build

# FIXME: tilda versions don't work with RPM in general
sed -i 's,\~[a-z0-9]*,,g' libfm*.pc

%install
%makeinstall_std
%find_lang libfm

# Remove unnecessary files
rm -f %buildroot%_libdir/%name/modules/*.la
%if %gtkver==3
    rm -f %buildroot%_pkgconfigdir/libfm-gtk.pc
%endif
%if %gtkver==2
    rm -f %buildroot%_pkgconfigdir/libfm-gtk3.pc
%endif

%files -n %name%soname -f libfm.lang
%_xdgconfigdir/*
%_libdir/*.so.*
%dir %_libdir/%name
%dir %_libdir/%name/modules
%_libdir/%name/modules/*.so
%_xdgmimedir/packages/*
%_datadir/%name/
%_desktopdir/libfm-pref-apps.desktop
%_bindir/libfm-pref-apps
%_man1dir/libfm-pref-apps.1*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%doc %_datadir/gtk-doc/html/%name

%files -n lxde-lxshortcut
%_bindir/lxshortcut
%_desktopdir/lxshortcut.desktop
%_man1dir/lxshortcut.1*

%changelog
* Tue Dec 13 2016 Anton Midyukov <antohami@altlinux.org> 1.2.5-alt1
- new version 1.2.5

* Tue Oct 04 2016 Michael Shigorin <mike@altlinux.org> 1.2.4-alt1
- 1.2.4

* Mon Mar 02 2015 Michael Shigorin <mike@altlinux.org> 1.2.3-alt3
- added missing Requires: wm-common-freedesktop to %name%soname
  as per http://www.altlinux.org/Window_Manager_Policy
  (MIME type handling should work now)

* Mon Dec 08 2014 Michael Shigorin <mike@altlinux.org> 1.2.3-alt2
- added Requires: gvfs (closes: #30514)

* Tue Oct 14 2014 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1
- 1.2.3

* Wed Aug 27 2014 Michael Shigorin <mike@altlinux.org> 1.2.2.1-alt1
- 1.2.2.1

* Thu May 22 2014 Michael Shigorin <mike@altlinux.org> 1.2.0-alt5
- moved lxshortcut desktop file and manpage to appropriate subpackage

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 1.2.0-alt4
- separate lxde-lxshortcut for proper dist-upgrade

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 1.2.0-alt3
- merged 1.1.2-alt0.2.1 changelog record to please the buildsystem

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 1.2.0-alt2
- re-enabled gtk support (reverted to gtk2 though) for pcmanfm

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1
- 1.2.0
- disabled gtk support (upstream chose Qt instead of GTK3)
  + thus dropped libfm-pref-apps, lxshortcut
- renamed main subpackage according to shared libs policy

* Fri Mar 07 2014 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt0.rc1.1
- Build libfm 1.2.0 as separate package

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt0.2.1
- Fixed build

%define _name garcon

%def_without builtin_menu
%def_enable introspection

Name: lib%_name
Version: 4.17.2
Release: alt1

Summary: Implementation of the freedesktop.org menu specification
License: LGPLv2+
Group: System/Libraries
URL: https://docs.xfce.org/xfce/garcon/start
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/xfce/garcon.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildRequires: libxfce4util-devel >= 4.15.6-alt1 libxfce4ui-gtk3-devel >= 4.15.7-alt1
BuildRequires: glib2-devel >= 2.14
BuildRequires: libgtk+3-devel
BuildRequires: gtk-doc
BuildRequires: intltool
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel libxfce4util-gir-devel libxfce4ui-gtk3-gir-devel}

Obsoletes: libxfce4menu
Requires: xfce-freedesktop-menu
Requires: exo-utils

%define _unpackaged_files_terminate_build 1

%description
Garcon is an implementation of the freedesktop.org menu specification
replacing the former Xfce menu library libxfce4menu. It is based on
GLib/GIO only and aims at covering the entire specification except
for legacy menus.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files for
developing applications that use %name.

%if_enabled introspection
%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for %name.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for %name.
%endif

%package devel-doc
Summary: Development files for %name
License: GFDL-1.1+
Group: Development/C
Conflicts: %name-devel < %version
BuildArch: noarch

%description devel-doc
This package contains development documentation for %name.

%package gtk3
Summary: Common GTK+3 part of %name
Group: Graphical desktop/XFce
Requires: %name = %version-%release

%description gtk3
%summary

%package gtk3-devel
Summary: Development files for %name-gtk3
Group: Development/C
Requires: %name-gtk3 = %version-%release
Requires: %name-devel = %version-%release
Requires: libgtk+3-devel >= 2.12.0
Requires: libxfce4ui-gtk3-devel

%description gtk3-devel
%summary

%if_enabled introspection
%package gtk3-gir
Summary: GObject introspection data for %name-gtk3
Group: System/Libraries
Requires: %name-gtk3 = %EVR

%description gtk3-gir
GObject introspection data for %name-gtk3.

%package gtk3-gir-devel
Summary: GObject introspection devel data for %name-gtk3
Group: System/Libraries
BuildArch: noarch
Requires: %name-gtk3-gir = %EVR
Requires: %name-gtk3-devel = %EVR

%description gtk3-gir-devel
GObject introspection devel data for %name-gtk3.
%endif

%package freedesktop-menu
Summary: xfce menu shipped by default with %name
Group: Graphical desktop/XFce
Provides: xfce-freedesktop-menu
# because of %%_datadir/desktop-directories/xfce-*
Conflicts: xfdesktop <= 4.6.2
# to avoid conflicts during update
Requires: %name = %version-%release
BuildArch: noarch

%description freedesktop-menu
%summary

%package settings-manager-menu
Summary: Xfce menu directories for use with xfce4-settings.
Group: Graphical desktop/XFce
Requires: %name = %version-%release
BuildArch: noarch

%description settings-manager-menu
%summary

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
    --disable-static \
	%{subst_enable introspection} \
    --enable-gtk-doc \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std

# Remove uz@Latn: it is the same as uz and
# glibc not support such language in any case.
rm -rf %buildroot%_datadir/locale/uz@Latn/

%find_lang %_name

%files -f %_name.lang
%doc AUTHORS NEWS README.md
%_libdir/%name-1.so.*

%if_with builtin_menu
%files freedesktop-menu
%_datadir/desktop-directories/*
%config(noreplace) %_sysconfdir/xdg/menus/xfce-applications.menu
%else
%exclude %_datadir/desktop-directories/*
%exclude %_sysconfdir/xdg/menus/xfce-applications.menu
%endif

%files settings-manager-menu
%_datadir/desktop-directories/xfce-hardware.directory
%_datadir/desktop-directories/xfce-personal.directory
%_datadir/desktop-directories/xfce-other.directory
%_datadir/desktop-directories/xfce-system.directory

%files devel
%_includedir/%_name-1/
%_libdir/%name-1.so
%_libdir/pkgconfig/%_name-1.pc

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/Garcon-*.typelib

%files gir-devel
%_datadir/gir-1.0/Garcon-*.gir
%endif

%files devel-doc
%doc %_datadir/gtk-doc/html/%_name

%files gtk3
%_libdir/%name-gtk3-1.so.*
%_niconsdir/*.*

%files gtk3-devel
%_includedir/%_name-gtk3-1/
%_libdir/%name-gtk3-1.so
%_libdir/pkgconfig/%_name-gtk3-1.pc

%if_enabled introspection
%files gtk3-gir
%_libdir/girepository-1.0/GarconGtk-*.typelib

%files gtk3-gir-devel
%_datadir/gir-1.0/GarconGtk-*.gir
%endif


%changelog
* Tue Nov 01 2022 Mikhail Efremov <sem@altlinux.org> 4.17.2-alt1
- Updated to 4.17.2.

* Mon Jul 11 2022 Mikhail Efremov <sem@altlinux.org> 4.17.1-alt1
- Updated to 4.17.1.

* Mon May 16 2022 Mikhail Efremov <sem@altlinux.org> 4.17.0-alt1
- Updated Url tag.
- Updated to 4.17.0.

* Fri Jan 15 2021 Mikhail Efremov <sem@altlinux.org> 4.16.1-alt1
- Updated to 4.16.1.

* Wed Dec 23 2020 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- devel-doc: Fixed License tag.
- Updated to 0.8.0.

* Wed Dec 16 2020 Mikhail Efremov <sem@altlinux.org> 0.7.3-alt1
- Updated BR.
- Updated to 0.7.3.

* Mon Nov 09 2020 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1
- Updated to 0.7.2.

* Wed Sep 02 2020 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Enabled GObject introspection support.
- Updated Vcs tag.
- Updated to 0.7.1.

* Sun Apr 05 2020 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1
- Dropped gtk2 packages.
- Added Vcs tag.
- Fixed docs license.
- Don't use rpm-build-licenses.
- Updated to 0.7.0.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 0.6.4-alt1
- Updated to 0.6.4.

* Mon Jul 01 2019 Mikhail Efremov <sem@altlinux.org> 0.6.3-alt1
- Updated to 0.6.3.

* Mon Dec 10 2018 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt1
- Updated to 0.6.2.

* Tue Aug 07 2018 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1
- Patch from upstream:
  + fix: some menu icons are too big (Bug #13785)
- Update url.
- Use _unpackaged_files_terminate_build.
- gtk* subpackages: require exo-utils.
- Enable debug (minimum level).
- Build GTK+3 library.
- Move libgtk+2-devel dependeces to gtk2-devel subpackage.
- Updated to 0.6.1.

* Thu Mar 05 2015 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1
- Updated to 0.4.0.

* Mon Feb 24 2014 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt2
- Updated to 0.3.0.

* Mon Feb 17 2014 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.git20140217
- Add libgarcon-gtk2 subpackage.
- Don't package wrong uz@Latn locale.
- Drop obsoleted patch.
- Upstream git snapshot (master branch).

* Tue Dec 03 2013 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt2
- Fix crash with empty directory-files.
- Fix Xfce name (XFCE -> Xfce).

* Mon May 06 2013 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Updated to 0.2.1.

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Updated to 0.2.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 0.1.12-alt1
- Updated to 0.1.12.

* Mon Apr 09 2012 Mikhail Efremov <sem@altlinux.org> 0.1.11-alt2
- New subpackage %name-settings-manager-menu.

* Mon Apr 02 2012 Mikhail Efremov <sem@altlinux.org> 0.1.11-alt1
- Updated to 0.1.11.

* Fri Feb 17 2012 Mikhail Efremov <sem@altlinux.org> 0.1.10-alt1
- Updated to 0.1.10.

* Fri Oct 07 2011 Mikhail Efremov <sem@altlinux.org> 0.1.9-alt1
- Updated to 0.1.9.

* Mon Aug 15 2011 Mikhail Efremov <sem@altlinux.org> 0.1.8-alt2
- Updated Russian (ru) translation (by Artem Zolochevskiy).

* Fri Jun 24 2011 Mikhail Efremov <sem@altlinux.org> 0.1.8-alt1
- Updated to 0.1.8.

* Sat Apr 16 2011 Mikhail Efremov <sem@altlinux.org> 0.1.7-alt1
- Updated to 0.1.7.

* Mon Apr 11 2011 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt1
- Drop obsoleted patch.
- Updated to 0.1.6.

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.5-alt5
- disabled built-in menu in favor of system menu

* Tue Mar 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.5-alt4
- added BuildArch: noarch to libgarcon-freedesktop-menu

* Mon Mar 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.5-alt3
- preparations for future migration on freedesktop menu:
  added libgarcon-freedesktop-menu subpackage that provides
  virtual xfce-freedesktop-menu.

* Wed Mar 09 2011 Mikhail Efremov <sem@altlinux.org> 0.1.5-alt2
- Patch from upstream:
    + Also try the garcon install sysconfigdir for config lookups.
- Don't provide libxfce4menu.

* Thu Jan 20 2011 Mikhail Efremov <sem@altlinux.org> 0.1.5-alt1
- Initial build (slightly based on FC spec).


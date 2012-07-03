%define _name garcon

%def_without builtin_menu

Name: lib%_name
Version: 0.2.0
Release: alt1

Summary: Implementation of the freedesktop.org menu specification
License: %lgpl2plus
Group: System/Libraries
URL: http://xfce.org/
Packager: XFCE Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/xfce/garcon
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildPreReq: libxfce4util-devel
BuildRequires: glib2-devel >= 2.14
BuildRequires: libgtk+2-devel >= 2.12.0
BuildRequires: gtk-doc
BuildRequires: intltool

Obsoletes: libxfce4menu
Requires: xfce-freedesktop-menu

%description
Garcon is an implementation of the freedesktop.org menu specification
replacing the former Xfce menu library libxfce4menu. It is based on
GLib/GIO only and aims at covering the entire specification except
for legacy menus.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: libgtk+2-devel >= 2.12.0

%description devel
This package contains libraries and header files for
developing applications that use %name.

%package devel-doc
Summary: Development files for %name
License: GFDLv1.1
Group: Development/C
Conflicts: %name-devel < %version
BuildArch: noarch

%description devel-doc
This package contains development documentation for %name.

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
    --enable-gtk-doc
%make_build

%install
%makeinstall_std
%find_lang %_name

%files -f %_name.lang
%doc AUTHORS NEWS README
%_libdir/*.so.*

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
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files devel-doc
%doc HACKING STATUS TODO
%doc %_datadir/gtk-doc/html/%_name

%changelog
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


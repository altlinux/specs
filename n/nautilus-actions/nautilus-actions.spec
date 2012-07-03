%define ver_major 3.2
%define _libexecdir %_prefix/libexec
%def_disable gtk_doc
%def_enable html_manuals

%set_verify_elf_method unresolved=relaxed

Name: nautilus-actions
Version: %ver_major.2
Release: alt1

Summary: Nautilus extension for customizing the context menu
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://www.grumz.net/node/8

Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: %name-data = %version-%release

BuildPreReq: gnome-common intltool
BuildRequires: libnautilus-devel libuuid-devel gettext libxml2-devel libdbus-glib-devel
BuildRequires: libunique3-devel libGConf-devel libgtop-devel libSM-devel libICE-devel
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_html_manuals:BuildRequires: gtk-doc gnome-doc-utils}

%description
Nautilus-actions is an extension for Nautilus file manager which
allows the user to add arbitrary program to be launched through the
Nautilus file manager popup menu of selected files.

%package data
Summary: Arch independent files for Nautilus-actions
Group: Graphical desktop/GNOME
BuildArch: noarch

%description data
This package provides noarch data needed for Nautilus-actions to work.

%package devel
Summary: Development package for Nautilus-actions
Group: Development/C
Requires: %name = %version-%release

%description devel
Nautilus-actions is an extension for Nautilus file manager which
allows the user to add arbitrary program to be launched through the
Nautilus file manager popup menu of selected files.

This package provides development files needed to write extensions for
Nautilus-actions

%package devel-doc
Group: Development/C
Summary: Development documentation for Nautilus-actions
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
This package contains documentation needed to develop extensions for
Nautilus-actions.

%prep
%setup -q

%build
%autoreconf
export LDFLAGS="$LDFLAGS -luuid `pkg-config --libs gobject-2.0`"
%configure --disable-schemas-install \
	--enable-compile-warnings=maximum \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{?_enable_html_manuals:--enable-html-manuals}

%make_build

%install
make DESTDIR=%buildroot install

%find_lang --with-gnome --output=%name.lang %name %name-config-tool

%files
%_bindir/*
%dir %_libdir/%name
%_libdir/%name/*.so
%dir %_libexecdir/%name
%_libexecdir/%name/na-delete-xmltree
%_libexecdir/%name/na-gconf2key.sh
%_libexecdir/%name/na-print-schemas
%_libexecdir/%name/na-set-conf
%_libdir/nautilus/extensions-3.0/*.so
%doc AUTHORS ChangeLog README TODO

%exclude %_libdir/%name/*.la
%exclude %_libdir/nautilus/extensions-3.0/*.la

%files data -f %name.lang
%_datadir/%name/
%_iconsdir/hicolor/*/apps/nautilus-actions.*
%_datadir/applications/nact.desktop

%files devel
%_includedir/%name/

%files devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Thu Mar 08 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Wed Feb 29 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sat Dec 10 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.5-alt1
- 3.1.5

* Thu Dec 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.4-alt1
- 3.1.4

* Tue Jun 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.3-alt1
- 3.1.3

* Fri Jun 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Sat Mar 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Sat Nov 07 2009 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3

* Tue Aug 04 2009 Yuri N. Sedunov <aris@altlinux.org> 1.11.2-alt1
- first build for Sisyphus


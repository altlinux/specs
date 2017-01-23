%define ver_major 3.22
%define api_ver 1.0
%def_enable python

Name: gitg
Version: %ver_major.0
Release: alt2

Summary: git repository viewer targeting gtk+/GNOME
Group: Development/Other
License: GPL
Url: https://wiki.gnome.org/Apps/Gitg

#Source: %name-%version.tar
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
# hack to avoid break of non-SMP build
Patch: gitg-3.18.0-alt-makefile.patch

PreReq: lib%name = %version-%release
# gitg/gitg-plugins-engine.vala: repo.require("PeasGtk", "1.0", 0);
Requires: typelib(PeasGtk)

%define gitg_pluginsdir %_libdir/%name/plugins

%if_enabled python
# use python3
AutoReqProv: nopython
%define __python %nil
%endif

%define glib_ver 2.38
%define gtk_ver 3.20
%define gtksourceview_ver 3.10
%define git2_ver 0.24.3
%define webkit_ver 2.6.0
%define gtkspell_ver 3.0.3
%define peas_ver 1.5.0

BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgit2-glib-devel >= %git2_ver
BuildPreReq: libgtksourceview3-devel >= %gtksourceview_ver
BuildPreReq: libwebkit2gtk-devel >= %webkit_ver
BuildPreReq: libgtkspell3-devel >= %gtkspell_ver
BuildPreReq: libpeas-devel >= %peas_ver
BuildRequires: gnome-common intltool desktop-file-utils
BuildRequires: libgee0.8-devel libjson-glib-devel libsecret-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel libxml2-devel
BuildRequires: libgit2-glib-gir-devel libwebkit2gtk-gir-devel libgee0.8-gir-devel
BuildRequires: vala-tools
BuildRequires: gsettings-desktop-schemas-devel
%{?_enable_python:BuildRequires: python3-devel rpm-build-python3 python3-module-pygobject3-devel}

%description
Gitg is a graphical user interface for git. It aims at being a small,
fast and convenient tool to visualize the history of git repositories.
Besides visualization, gitg also provides several utilities to manage your
repository and commit your work.

%package -n lib%name
Summary: lib%name library
Group: System/Libraries

%description -n lib%name
Gitg is a graphical user interface for git. It aims at being a small,
fast and convenient tool to visualize the history of git repositories.
Besides visualization, gitg also provides several utilities to manage your
repository and commit your work.

This package provides shared Gitg library.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
PreReq: lib%name = %version-%release

%description -n lib%name-devel
Gitg is a graphical user interface for git. It aims at being a small,
fast and convenient tool to visualize the history of git repositories.
Besides visualization, gitg also provides several utilities to manage your
repository and commit your work.

This package provides headers and libraries to develop plugins for Gitg
or other applications

%package -n lib%name-gir
Summary: GObject introspection data for the Gitg library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
This package provides GObject introspection data for the Gitg
library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Gitg library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
This package provides GObject introspection devel data for the Gitg
library.

%prep
%setup
%patch

%build
%autoreconf
%configure --disable-static \
	%{subst_enable python}
%make

%install
%makeinstall_std
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=RevisionControl \
	%buildroot%_desktopdir/gitg.desktop

%check
%make check

%files -f %name.lang
%_bindir/%name
%gitg_pluginsdir/
%_datadir/glib-2.0/schemas/org.gnome.gitg.gschema.xml
%_desktopdir/%name.desktop
%_datadir/%name/
%_man1dir/%{name}*
%_iconsdir/hicolor/*x*/apps/*
%_iconsdir/hicolor/scalable/apps/%name-symbolic.svg
%_datadir/appdata/%name.appdata.xml
%{?_enable_python:%python3_sitelibdir/gi/overrides/*}
%doc AUTHORS NEWS README

%exclude %gitg_pluginsdir/*.la

%files -n lib%name
%_libdir/lib%name-%api_ver.so.*
%_libdir/lib%name-ext-%api_ver.so.*

%files -n lib%name-devel
%_includedir/lib%name-%api_ver/
%_includedir/lib%name-ext-%api_ver/
%_libdir/lib%name-%api_ver.so
%_libdir/lib%name-ext-%api_ver.so
%_libdir/pkgconfig/lib%name-%api_ver.pc
%_libdir/pkgconfig/lib%name-ext-%api_ver.pc
%_vapidir/lib%name-%api_ver.vapi
%_vapidir/lib%name-ext-1.0.vapi

%files -n lib%name-gir
%_typelibdir/Gitg-%api_ver.typelib
%_typelibdir/GitgExt-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Gitg-%api_ver.gir
%_girdir/GitgExt-%api_ver.gir

%changelog
* Mon Jan 23 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt2
- reqs: + typelib(PeasGtk)

* Sun Sep 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Sep 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Sat Aug 27 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Wed Jun 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Wed Mar 23 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Thu Apr 30 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Dec 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Sun Nov 30 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt3
- fixed buildreqs
- %%check section

* Mon Oct 06 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt2
- rebuilt with libwebkit2gtk-4.0

* Wed Sep 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Jul 01 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gitg

* Fri Feb 18 2011 Vladimir Lettiev <crux@altlinux.ru> 0.1.0-alt1
- New version 0.1.0
- Updated buildreqs

* Mon Jan 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.0.8-alt1
- New version 0.0.8
- Separated lib%name{,-devel} subpackages

* Mon Feb 22 2010 Vladimir Lettiev <crux@altlinux.ru> 0.0.6-alt1
- New version 0.0.6

* Wed Sep 30 2009 Vladimir Lettiev <crux@altlinux.ru> 0.0.5-alt1
- 0.0.5
- patch from ktirf@ (closes: #21305)

* Sun Apr 26 2009 Vladimir Lettiev <crux@altlinux.ru> 0.0.3-alt1
- initial build


%def_disable snapshot
%define _name metacity
%define ver_major 3.46
%define api_ver 3.0
%def_disable static
%def_enable vulkan

Name: %_name%api_ver
Version: %ver_major.1
Release: alt1

Summary: Metacity window manager
License: GPL-2.0-or-later
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Projects/Metacity

%if_disabled snapshot
Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

# From configure.ac
%define gtk_ver 3.22.0
%define glib_ver 2.44.0
%define startup_notification_ver 0.7
%define xcomposite_ver 0.3
%define gsds_ver 3.3.0

Conflicts: %_name
Obsoletes: %name-themes-default < %version-%release
Obsoletes: %name-theme-atlanta < %version-%release	%name-theme-bright < %version-%release
Obsoletes: %name-theme-crux < %version-%release		%name-theme-esco < %version-%release
Obsoletes: %name-theme-gorilla < %version-%release	%name-theme-metabox < %version-%release
Obsoletes: %name-theme-simple < %version-%release

Requires: lib%name = %version-%release
Requires: zenity

# From configure.ac
BuildRequires(pre): rpm-build-gnome
BuildRequires: autoconf-archive
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libstartup-notification-devel >= %startup_notification_ver
BuildRequires: gsettings-desktop-schemas-devel >= %gsds_ver
BuildRequires: libXcomposite-devel >= %xcomposite_ver
BuildRequires: libXfixes-devel libXrender-devel libXdamage-devel libXtst-devel
BuildRequires: libXrender-devel
BuildRequires: libXcursor-devel libXt-devel libXinerama-devel libXext-devel
BuildRequires: yelp-tools itstool zenity libcanberra-gtk3-devel
BuildRequires: libXrandr-devel libX11-devel libXres-devel libSM-devel
BuildRequires: libICE-devel libXpresent-devel perl-XML-Parser libgtop-devel
%{?_enable_vulkan:BuildRequires: libvulkan-devel}

%description
A window manager for GNOME, with a focus on simplicity and usability
rather than novelties or gimmicks.  It uses GTK+ 3 for drawing window frames,
so that it inherits colors, fonts, and so on from the GTK+ theme.  Its author
has characterized it as a boring window manager for the adult in you.
Many window managers are like Marshmallow Froot Loops; Metacity is like Cheerios.

%package -n lib%name
Summary: Shared library for Metacity
Group: System/Libraries

%description -n lib%name
This package contains shared library needed to run Metacity.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Conflicts: lib%_name-devel
Requires: lib%name = %version-%release
Requires: libgtk+3-devel >= %gtk_ver

%description -n lib%name-devel
This package contains headers and development libraries for lib%name

%package -n lib%name-devel-static
Summary: Static version of lib%name
Group: Development/C
Conflicts: lib%_name-devel-static
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains the lib%name static library.

%prep
%setup -n %_name-%version

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure \
    %{subst_enable static} \
    --enable-sm \
    --enable-startup-notification \
    --enable-xinerama \
    --disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %_name --output=%name.lang

%files -f %name.lang
%_bindir/%_name
%_bindir/%_name-message
%_bindir/%_name-theme-viewer
%_desktopdir/%_name.desktop
%_datadir/gnome-control-center/keybindings/50-%{_name}*.xml
%_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.%_name.keybindings.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.%_name.theme.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.%_name.enums.xml
%_man1dir/%_name.1.*
%_man1dir/%_name-message.1.*
%_man1dir/%_name-theme-viewer.1.*
%doc README AUTHORS NEWS

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%doc doc/*.txt HACKING

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Sat Dec 24 2022 Yuri N. Sedunov <aris@altlinux.org> 3.46.1-alt1
- 3.46.1

* Tue Oct 04 2022 Yuri N. Sedunov <aris@altlinux.org> 3.46.0-alt1
- 3.46.0

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 3.44.0-alt1
- 3.44.0

* Sat Oct 23 2021 Yuri N. Sedunov <aris@altlinux.org> 3.42.0-alt1
- 3.42.0

* Thu Mar 25 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.0-alt1
- 3.40.0

* Fri Dec 25 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt2
- updated to 3.38.0-3-g7e3f13a4

* Sat Oct 24 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Sun Jun 28 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt2
- fixed build against newest Vulkan

* Fri Mar 27 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Thu Mar 05 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Sun May 05 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Sun Sep 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Sun Sep 02 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Sun Mar 11 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.25.2-alt1
- 3.25.2

* Tue Apr 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Sun Mar 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Nov 01 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Wed Sep 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Fri Aug 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Fri Jul 15 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Sat Jun 25 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1.1-alt1
- 3.20.1.1

* Fri Jun 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Sun Apr 24 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.4-alt1
- 3.18.4

* Wed Mar 30 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Tue Feb 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Wed Sep 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed Apr 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Tue Apr 07 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Mar 30 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.2-alt1
- after 3.15.2 snapshot

* Mon Nov 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Mon Oct 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Thu Oct 09 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon Sep 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- first build for Sisyphus


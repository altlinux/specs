%define _name metacity
%define ver_major 3.18
%define api_ver 3.0
%def_disable static
%def_enable compositor
%def_enable render
%def_enable shape

Name: %_name%api_ver
Version: %ver_major.2
Release: alt1

Summary: Metacity window manager
License: %gpl2plus
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Projects/Metacity

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
#Source: %_name-%version.tar

%define theme_prefix theme

# From configure.ac
%define gtk_ver 3.15.2
%define glib_ver 2.32.0
%define startup_notification_ver 0.7
%define xcomposite_ver 0.2
%define gsds_ver 3.3.0

Conflicts: %_name
Requires: %name-theme = %version-%release
Requires: lib%name = %version-%release
Requires: zenity

# From configure.in
BuildPreReq: rpm-build-gnome rpm-build-licenses
BuildPreReq: intltool >= 0.34.90
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libstartup-notification-devel >= %startup_notification_ver
BuildPreReq: gsettings-desktop-schemas-devel >= %gsds_ver
%if_enabled compositor
BuildPreReq: libXcomposite-devel >= %xcomposite_ver
BuildRequires: libXfixes-devel libXrender-devel libXdamage-devel libXtst-devel
%endif
%{?_enable_render:BuildRequires: libXrender-devel}
BuildRequires: libXcursor-devel libXt-devel libXinerama-devel
%{?_enable_shape:BuildRequires: libXext-devel}
BuildRequires: yelp-tools itstool zenity libcanberra-gtk3-devel
BuildRequires: libXrandr-devel libX11-devel libSM-devel libICE-devel perl-XML-Parser libgtop-devel

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

%package %{theme_prefix}s-default
Summary: Metacity default themes
Group: Graphical desktop/GNOME
BuildArch: noarch
Conflicts: %_name-themes-default
Provides: %name-themes = %version-%release
Requires: %name-%theme_prefix-atlanta = %version-%release	%name-%theme_prefix-bright = %version-%release
Requires: %name-%theme_prefix-crux = %version-%release		%name-%theme_prefix-esco = %version-%release
Requires: %name-%theme_prefix-gorilla = %version-%release	%name-%theme_prefix-metabox = %version-%release
Requires: %name-%theme_prefix-simple = %version-%release

%description %{theme_prefix}s-default
This is virtual package that provides default themes for Metacity.

%package %theme_prefix-atlanta
Summary: Metacity theme - Atlanta
Group: Graphical desktop/GNOME
BuildArch: noarch
Conflicts: %_name-theme-atlanta
Provides: %name-theme = %version-%release
Requires: %name = %version-%release

%description %theme_prefix-atlanta
This package contains a simple low-overhead default theme for Metacity.

%package %theme_prefix-bright
Summary: Metacity theme - Bright
Group: Graphical desktop/GNOME
BuildArch: noarch
Conflicts: %_name-theme-bright
Provides: %name-theme = %version-%release
Requires: %name = %version-%release

%description %theme_prefix-bright
This package contains a simple theme based on Havoc Pennington's Atlanta.

%package %theme_prefix-crux
Summary: Metacity theme - Crux
Group: Graphical desktop/GNOME
BuildArch: noarch
Conflicts: %_name-theme-crux
Provides: %name-theme = %version-%release
Requires: %name = %version-%release

%description %theme_prefix-crux
This package contains a port of the Crux theme by Arlo Rose and John
Harper.

%package %theme_prefix-esco
Summary: Metacity theme - Esco
Group: Graphical desktop/GNOME
BuildArch: noarch
Conflicts: %_name-theme-esco
Provides: %name-theme = %version-%release
Requires: %name = %version-%release

%description %theme_prefix-esco
This package contains a simple theme designed to look really good match
GTK+ well.

%package %theme_prefix-gorilla
Summary: Metacity theme - AgingGorilla
Group: Graphical desktop/GNOME
BuildArch: noarch
Conflicts: %_name-theme-gorilla
Provides: %name-theme = %version-%release
Requires: %name = %version-%release

%description %theme_prefix-gorilla
This package contains a port of the Gorilla theme by Jacub Steiner

%package %theme_prefix-metabox
Summary: Metacity theme - Metabox
Group: Graphical desktop/GNOME
BuildArch: noarch
Conflicts: %_name-theme-metabox
Provides: %name-theme = %version-%release
Requires: %name = %version-%release

%description %theme_prefix-metabox
This package contains a theme that looks a little like BlackBox.

%package %theme_prefix-simple
Summary: Metacity theme - Simple
Group: Graphical desktop/GNOME
BuildArch: noarch
Conflicts: %_name-theme-simple
Provides: %name-theme = %version-%release
Requires: %name = %version-%release

%description %theme_prefix-simple
This package contains default GNOME window theme. It based on Atlanta
theme.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
    %{subst_enable compositor} \
    %{subst_enable render} \
    %{subst_enable shape} \
    %{subst_enable static} \
    --enable-sm \
    --enable-startup-notification \
    --enable-xsync \
    --enable-xinerama \
    --disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang  --with-gnome %_name creating-%_name-themes --output=%name.lang

%files -f %name.lang
%_bindir/*
%_datadir/%_name
%_desktopdir/*
%_datadir/gnome/wm-properties/*.desktop
%_datadir/gnome-control-center/keybindings/50-metacity*.xml
%_datadir/glib-2.0/schemas/org.gnome.metacity.gschema.xml
%_datadir/GConf/gsettings/metacity-schemas.convert
%_datadir/themes/Adwaita/metacity-1/metacity-theme-3.xml
%_datadir/themes/HighContrast/metacity-1/metacity-theme-3.xml
%_man1dir/*
%doc README AUTHORS NEWS

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%doc doc/*.txt doc/*.dtd HACKING

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files %{theme_prefix}s-default

%files %theme_prefix-gorilla
%_datadir/themes/AgingGorilla/*

%files %theme_prefix-atlanta
%_datadir/themes/Atlanta/*

%files %theme_prefix-bright
%_datadir/themes/Bright/*

%files %theme_prefix-crux
%_datadir/themes/Crux/*

%files %theme_prefix-esco
%_datadir/themes/Esco/*

%files %theme_prefix-metabox
%_datadir/themes/Metabox/*

%files %theme_prefix-simple
%_datadir/themes/Simple/*

%changelog
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


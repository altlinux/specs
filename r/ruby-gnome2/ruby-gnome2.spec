%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel

Name:          ruby-gnome2
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
License:       LGPL-2.1-or-later
Group:         Development/Ruby
Url:           https://ruby-gnome2.osdn.jp/
Vcs:           https://github.com/ruby-gnome2/ruby-gnome2.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
BuildRequires: gcc-c++
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(vte)
BuildRequires: pkgconfig(libvlc)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(mount)
BuildRequires: pkgconfig(blkid)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(xcb-xinerama)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xcb-randr)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(libselinux)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(libthai)
BuildRequires: pkgconfig(datrie-0.2)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libbrotlicommon)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(glproto)
BuildRequires: pkgconfig(dri2proto)
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(ossp-uuid)
BuildRequires: pkgconfig(gegl-0.4)
BuildRequires: pkgconfig(atk-bridge-2.0)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xres)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(xshmfence)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libdeflate)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(libcap)
BuildRequires: shared-mime-info-devel
BuildRequires: gem(pkg-config) >= 1.3.5
BuildRequires: gem(native-package-installer) >= 1.0.3
BuildRequires: gem-cairo-headers-devel
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(cairo) >= 1.16.2
BuildRequires: gem(erb) >= 0
BuildRequires: gem(fiddle) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(webrick) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names ruby-gnome2
Requires:      gem(adwaita) = 4.3.6
Requires:      gem(atk) = 4.3.6
Requires:      gem(cairo-gobject) = 4.3.6
Requires:      gem(clutter) = 4.3.6
Requires:      gem(clutter-gdk) = 4.3.6
Requires:      gem(clutter-gstreamer) = 4.3.6
Requires:      gem(clutter-gtk) = 4.3.6
Requires:      gem(gdk3) = 4.3.6
Requires:      gem(gdk4) = 4.3.6
Requires:      gem(gdk_pixbuf2) = 4.3.6
Requires:      gem(gegl) = 4.3.6
Requires:      gem(gio2) = 4.3.6
Requires:      gem(glib2) = 4.3.6
Requires:      gem(gnumeric) = 4.3.6
Requires:      gem(gobject-introspection) = 4.3.6
Requires:      gem(goffice) = 4.3.6
Requires:      gem(graphene1) = 4.3.6
Requires:      gem(gsf) = 4.3.6
Requires:      gem(gsk4) = 4.3.6
Requires:      gem(gstreamer) = 4.3.6
Requires:      gem(gtk3) = 4.3.6
Requires:      gem(gtk4) = 4.3.6
Requires:      gem(gtksourceview3) = 4.3.6
Requires:      gem(gtksourceview4) = 4.3.6
Requires:      gem(gtksourceview5) = 4.3.6
Requires:      gem(gvlc) = 4.3.6
Requires:      gem(libhandy) = 4.3.6
Requires:      gem(libsecret) = 4.3.6
Requires:      gem(pango) = 4.3.6
Requires:      gem(poppler) = 4.3.6
Requires:      gem(rsvg2) = 4.3.6
Requires:      gem(vte3) = 4.3.6
Requires:      gem(vte4) = 4.3.6
Requires:      gem(webkit-gtk) = 4.3.6
Requires:      gem(webkit2-gtk) = 4.3.6
Requires:      gem(wnck3) = 4.3.6

%description
This is a set of bindings for the GNOME 2.x and 3.x libraries to use from Ruby
2.1, 2.2, 2.3 and 2.4.


%package       -n gem-gsf
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gio2) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(gsf) = 4.3.6

%description   -n gem-gsf
Ruby/GSF is a Ruby binding of GSF which is needed by GOffice.


%if_enabled    doc
%package       -n gem-gsf-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gsf
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gsf) = 4.3.6

%description   -n gem-gsf-doc
Ruby bindings for GNOME documentation files.

Ruby/GSF is a Ruby binding of GSF which is needed by GOffice.

%description   -n gem-gsf-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gsf.
%endif


%if_enabled    devel
%package       -n gem-gsf-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gsf
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(gsf) = 4.3.6

%description   -n gem-gsf-devel
Ruby bindings for GNOME development package.

Ruby/GSF is a Ruby binding of GSF which is needed by GOffice.

%description   -n gem-gsf-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gsf.
%endif


%package       -n gem-atk
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(glib2) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(atk) = 4.3.6

%description   -n gem-atk
Ruby/ATK is a Ruby binding of ATK-1.12.x or later based on
GObject-Introspection.


%if_enabled    doc
%package       -n gem-atk-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета atk
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(atk) = 4.3.6

%description   -n gem-atk-doc
Ruby bindings for GNOME documentation files.

Ruby/ATK is a Ruby binding of ATK-1.12.x or later based on
GObject-Introspection.

%description   -n gem-atk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета atk.
%endif


%if_enabled    devel
%package       -n gem-atk-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета atk
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(atk) = 4.3.6

%description   -n gem-atk-devel
Ruby bindings for GNOME development package.

Ruby/ATK is a Ruby binding of ATK-1.12.x or later based on
GObject-Introspection.

%description   -n gem-atk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета atk.
%endif


%package       -n gem-gtk4
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(atk) = 4.3.6
Requires:      gem(gdk4) = 4.3.6
Requires:      gem(gsk4) = 4.3.6
Provides:      gem(gtk4) = 4.3.6

%description   -n gem-gtk4
Ruby/GTK4 is a Ruby binding of GTK+ 4.


%if_enabled    doc
%package       -n gem-gtk4-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gtk4
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtk4) = 4.3.6

%description   -n gem-gtk4-doc
Ruby bindings for GNOME documentation files.

Ruby/GTK4 is a Ruby binding of GTK+ 4.

%description   -n gem-gtk4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gtk4.
%endif


%if_enabled    devel
%package       -n gem-gtk4-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gtk4
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(gtk4) = 4.3.6

%description   -n gem-gtk4-devel
Ruby bindings for GNOME development package.

Ruby/GTK4 is a Ruby binding of GTK+ 4.

%description   -n gem-gtk4-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gtk4.
%endif


%package       -n gem-gtk3
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(atk) = 4.3.6
Requires:      gem(gdk3) = 4.3.6
Provides:      gem(gtk3) = 4.3.6

%description   -n gem-gtk3
Ruby/GTK3 is a Ruby binding of GTK+ 3.


%if_enabled    doc
%package       -n gem-gtk3-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gtk3
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtk3) = 4.3.6

%description   -n gem-gtk3-doc
Ruby bindings for GNOME documentation files.

Ruby/GTK3 is a Ruby binding of GTK+ 3.

%description   -n gem-gtk3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gtk3.
%endif


%if_enabled    devel
%package       -n gem-gtk3-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gtk3
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(gtk3) = 4.3.6

%description   -n gem-gtk3-devel
Ruby bindings for GNOME development package.

Ruby/GTK3 is a Ruby binding of GTK+ 3.

%description   -n gem-gtk3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gtk3.
%endif


%package       -n gem-gsk4
Version:       4.3.6
Release:       alt1
Summary:       Ruby/GSK4 is a Ruby binding of GSK 4.x
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gdk4) = 4.3.6
Requires:      gem(graphene1) = 4.3.6
Provides:      gem(gsk4) = 4.3.6

%description   -n gem-gsk4
Ruby/GSK4 is a Ruby binding of GSK 4.x.


%if_enabled    doc
%package       -n gem-gsk4-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby/GSK4 is a Ruby binding of GSK 4.x documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gsk4
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gsk4) = 4.3.6

%description   -n gem-gsk4-doc
Ruby/GSK4 is a Ruby binding of GSK 4.x documentation files.

%description   -n gem-gsk4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gsk4.
%endif


%if_enabled    devel
%package       -n gem-gsk4-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby/GSK4 is a Ruby binding of GSK 4.x development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gsk4
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gsk4) = 4.3.6

%description   -n gem-gsk4-devel
Ruby/GSK4 is a Ruby binding of GSK 4.x development package.

%description   -n gem-gsk4-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gsk4.
%endif


%package       -n gem-vte3
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtk3) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(vte3) = 4.3.6

%description   -n gem-vte3
Ruby/VTE3 is a Ruby binding of VTE for use with GTK3.


%if_enabled    doc
%package       -n gem-vte3-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vte3
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(vte3) = 4.3.6

%description   -n gem-vte3-doc
Ruby bindings for GNOME documentation files.

Ruby/VTE3 is a Ruby binding of VTE for use with GTK3.

%description   -n gem-vte3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vte3.
%endif


%if_enabled    devel
%package       -n gem-vte3-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vte3
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(vte3) = 4.3.6

%description   -n gem-vte3-devel
Ruby bindings for GNOME development package.

Ruby/VTE3 is a Ruby binding of VTE for use with GTK3.

%description   -n gem-vte3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vte3.
%endif


%package       -n gem-gio2
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(fiddle) >= 0
Requires:      gem(gobject-introspection) = 4.3.6
Provides:      gem(gio2) = 4.3.6

%description   -n gem-gio2
Ruby/Graphic InterfaceO2 is a Ruby binding of gio-2.0.x.


%if_enabled    doc
%package       -n gem-gio2-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gio2
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gio2) = 4.3.6

%description   -n gem-gio2-doc
Ruby bindings for GNOME documentation files.

Ruby/Graphic InterfaceO2 is a Ruby binding of gio-2.0.x.

%description   -n gem-gio2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gio2.
%endif


%if_enabled    devel
%package       -n gem-gio2-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gio2
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(gio2) = 4.3.6

%description   -n gem-gio2-devel
Ruby bindings for GNOME development package.

Ruby/Graphic InterfaceO2 is a Ruby binding of gio-2.0.x.

%description   -n gem-gio2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gio2.
%endif


%package       -n gem-gegl
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gio2) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(gegl) = 4.3.6

%description   -n gem-gegl
Ruby/GEGL is a Ruby binding of GEGL.


%if_enabled    doc
%package       -n gem-gegl-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gegl
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gegl) = 4.3.6

%description   -n gem-gegl-doc
Ruby bindings for GNOME documentation files.

Ruby/GEGL is a Ruby binding of GEGL.

%description   -n gem-gegl-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gegl.
%endif


%if_enabled    devel
%package       -n gem-gegl-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gegl
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(gegl) = 4.3.6

%description   -n gem-gegl-devel
Ruby bindings for GNOME development package.

Ruby/GEGL is a Ruby binding of GEGL.

%description   -n gem-gegl-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gegl.
%endif


%package       -n gem-vte4
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtk4) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(vte4) = 4.3.6

%description   -n gem-vte4
Ruby/VTE4 is a Ruby binding of VTE for GTK 4


%if_enabled    doc
%package       -n gem-vte4-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vte4
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(vte4) = 4.3.6

%description   -n gem-vte4-doc
Ruby bindings for GNOME documentation files.

Ruby/VTE4 is a Ruby binding of VTE for GTK 4

%description   -n gem-vte4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vte4.
%endif


%if_enabled    devel
%package       -n gem-vte4-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vte4
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(vte4) = 4.3.6

%description   -n gem-vte4-devel
Ruby bindings for GNOME development package.

Ruby/VTE4 is a Ruby binding of VTE for GTK 4

%description   -n gem-vte4-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vte4.
%endif


%package       -n gem-gdk4
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cairo-gobject) = 4.3.6
Requires:      gem(gdk_pixbuf2) = 4.3.6
Requires:      gem(pango) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(gdk4) = 4.3.6

%description   -n gem-gdk4
Ruby/GDK4 is a Ruby binding of GDK 4.


%if_enabled    doc
%package       -n gem-gdk4-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gdk4
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gdk4) = 4.3.6

%description   -n gem-gdk4-doc
Ruby bindings for GNOME documentation files.

Ruby/GDK4 is a Ruby binding of GDK 4.

%description   -n gem-gdk4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gdk4.
%endif


%if_enabled    devel
%package       -n gem-gdk4-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gdk4
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(gdk4) = 4.3.6

%description   -n gem-gdk4-devel
Ruby bindings for GNOME development package.

Ruby/GDK4 is a Ruby binding of GDK 4.

%description   -n gem-gdk4-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gdk4.
%endif


%package       -n gem-gdk3
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cairo-gobject) = 4.3.6
Requires:      gem(gdk_pixbuf2) = 4.3.6
Requires:      gem(pango) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(gdk3) = 4.3.6

%description   -n gem-gdk3
Ruby/GDK3 is a Ruby binding of GDK 3.


%if_enabled    doc
%package       -n gem-gdk3-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gdk3
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gdk3) = 4.3.6

%description   -n gem-gdk3-doc
Ruby bindings for GNOME documentation files.

Ruby/GDK3 is a Ruby binding of GDK 3.

%description   -n gem-gdk3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gdk3.
%endif


%if_enabled    devel
%package       -n gem-gdk3-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gdk3
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(gdk3) = 4.3.6

%description   -n gem-gdk3-devel
Ruby bindings for GNOME development package.

Ruby/GDK3 is a Ruby binding of GDK 3.

%description   -n gem-gdk3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gdk3.
%endif


%package       -n gem-gvlc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(glib2) = 4.3.6
Provides:      gem(gvlc) = 4.3.6

%description   -n gem-gvlc
Ruby/VLC is a Ruby binding of libVLC for Ruby/GTK.


%if_enabled    doc
%package       -n gem-gvlc-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gvlc
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gvlc) = 4.3.6

%description   -n gem-gvlc-doc
Ruby bindings for GNOME documentation files.

Ruby/VLC is a Ruby binding of libVLC for Ruby/GTK.

%description   -n gem-gvlc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gvlc.
%endif


%if_enabled    devel
%package       -n gem-gvlc-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gvlc
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(gvlc) = 4.3.6

%description   -n gem-gvlc-devel
Ruby bindings for GNOME development package.

Ruby/VLC is a Ruby binding of libVLC for Ruby/GTK.

%description   -n gem-gvlc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gvlc.
%endif


%package       -n gem-pango
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cairo-gobject) = 4.3.6
Requires:      gem(gobject-introspection) = 4.3.6
Provides:      gem(pango) = 4.3.6

%description   -n gem-pango
Ruby/Pango is a Ruby binding of pango based on GObject-Introspection.


%if_enabled    doc
%package       -n gem-pango-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pango
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(pango) = 4.3.6

%description   -n gem-pango-doc
Ruby bindings for GNOME documentation files.

Ruby/Pango is a Ruby binding of pango based on GObject-Introspection.

%description   -n gem-pango-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pango.
%endif


%if_enabled    devel
%package       -n gem-pango-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pango
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(pango) = 4.3.6

%description   -n gem-pango-devel
Ruby bindings for GNOME development package.

Ruby/Pango is a Ruby binding of pango based on GObject-Introspection.

%description   -n gem-pango-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pango.
%endif


%package       -n gem-wnck3
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtk3) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(wnck3) = 4.3.6

%description   -n gem-wnck3
Executable file for wnck3 gem.


%if_enabled    doc
%package       -n gem-wnck3-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета wnck3
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(wnck3) = 4.3.6

%description   -n gem-wnck3-doc
Ruby bindings for GNOME documentation files.

Executable file for wnck3 gem.

%description   -n gem-wnck3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета wnck3.
%endif


%if_enabled    devel
%package       -n gem-wnck3-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета wnck3
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(wnck3) = 4.3.6

%description   -n gem-wnck3-devel
Ruby bindings for GNOME development package.

Executable file for wnck3 gem.

%description   -n gem-wnck3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета wnck3.
%endif


%package       -n gem-glib2
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(native-package-installer) >= 1.0.3
Requires:      gem(pkg-config) >= 1.3.5
Obsoletes:     ruby-glib2 < %EVR
Provides:      ruby-glib2 = %EVR
Provides:      gem(glib2) = 4.3.6

%description   -n gem-glib2
GLib is a useful general-purpose C library, notably used by GTK+ and GNOME. This
package contains libraries for using GLib 2 with the Ruby programming language.
It is most likely useful in conjunction with Ruby bindings for other libraries
such as GTK+.


%if_enabled    doc
%package       -n gem-glib2-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета glib2
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(glib2) = 4.3.6
Obsoletes:     ruby-glib2-doc < %EVR
Provides:      ruby-glib2-doc = %EVR

%description   -n gem-glib2-doc
Ruby bindings for GNOME documentation files.

GLib is a useful general-purpose C library, notably used by GTK+ and GNOME. This
package contains libraries for using GLib 2 with the Ruby programming language.
It is most likely useful in conjunction with Ruby bindings for other libraries
such as GTK+.

%description   -n gem-glib2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета glib2.
%endif


%if_enabled    devel
%package       -n gem-glib2-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета glib2
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(glib2) = 4.3.6

%description   -n gem-glib2-devel
Ruby bindings for GNOME development package.

GLib is a useful general-purpose C library, notably used by GTK+ and GNOME. This
package contains libraries for using GLib 2 with the Ruby programming language.
It is most likely useful in conjunction with Ruby bindings for other libraries
such as GTK+.

%description   -n gem-glib2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета glib2.
%endif


%package       -n gem-rsvg2
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cairo-gobject) = 4.3.6
Requires:      gem(gdk_pixbuf2) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(rsvg2) = 4.3.6

%description   -n gem-rsvg2
Ruby/RSVG2 is a Ruby binding of librsvg based on GObject-Introspection.


%if_enabled    doc
%package       -n gem-rsvg2-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rsvg2
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rsvg2) = 4.3.6

%description   -n gem-rsvg2-doc
Ruby bindings for GNOME documentation files.

Ruby/RSVG2 is a Ruby binding of librsvg based on GObject-Introspection.

%description   -n gem-rsvg2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rsvg2.
%endif


%if_enabled    devel
%package       -n gem-rsvg2-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rsvg2
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(rsvg2) = 4.3.6

%description   -n gem-rsvg2-devel
Ruby bindings for GNOME development package.

Ruby/RSVG2 is a Ruby binding of librsvg based on GObject-Introspection.

%description   -n gem-rsvg2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rsvg2.
%endif


%package       -n gem-clutter
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cairo-gobject) = 4.3.6
Requires:      gem(gobject-introspection) = 4.3.6
Requires:      gem(pango) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(clutter) = 4.3.6

%description   -n gem-clutter
Ruby/Clutter is a Ruby binding of Clutter.


%if_enabled    doc
%package       -n gem-clutter-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета clutter
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(clutter) = 4.3.6

%description   -n gem-clutter-doc
Ruby bindings for GNOME documentation files.

Ruby/Clutter is a Ruby binding of Clutter.

%description   -n gem-clutter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета clutter.
%endif


%if_enabled    devel
%package       -n gem-clutter-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета clutter
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(clutter) = 4.3.6

%description   -n gem-clutter-devel
Ruby bindings for GNOME development package.

Ruby/Clutter is a Ruby binding of Clutter.

%description   -n gem-clutter-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета clutter.
%endif


%package       -n gem-goffice
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gsf) = 4.3.6
Requires:      gem(gtk3) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(goffice) = 4.3.6

%description   -n gem-goffice
Ruby/GOffice is a Ruby binding of GOffice.


%if_enabled    doc
%package       -n gem-goffice-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета goffice
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(goffice) = 4.3.6

%description   -n gem-goffice-doc
Ruby bindings for GNOME documentation files.

Ruby/GOffice is a Ruby binding of GOffice.

%description   -n gem-goffice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета goffice.
%endif


%if_enabled    devel
%package       -n gem-goffice-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета goffice
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(goffice) = 4.3.6

%description   -n gem-goffice-devel
Ruby bindings for GNOME development package.

Ruby/GOffice is a Ruby binding of GOffice.

%description   -n gem-goffice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета goffice.
%endif


%package       -n gem-poppler
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cairo-gobject) = 4.3.6
Requires:      gem(gio2) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(poppler) = 4.3.6

%description   -n gem-poppler
Ruby/Poppler is a Ruby binding of poppler-glib.


%if_enabled    doc
%package       -n gem-poppler-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета poppler
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(poppler) = 4.3.6

%description   -n gem-poppler-doc
Ruby bindings for GNOME documentation files.

Ruby/Poppler is a Ruby binding of poppler-glib.

%description   -n gem-poppler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета poppler.
%endif


%if_enabled    devel
%package       -n gem-poppler-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета poppler
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(poppler) = 4.3.6

%description   -n gem-poppler-devel
Ruby bindings for GNOME development package.

Ruby/Poppler is a Ruby binding of poppler-glib.

%description   -n gem-poppler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета poppler.
%endif


%package       -n gem-adwaita
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtk4) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(adwaita) = 4.3.6

%description   -n gem-adwaita
Ruby/Adwaita is a Ruby binding of Adwaita.


%if_enabled    doc
%package       -n gem-adwaita-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета adwaita
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(adwaita) = 4.3.6

%description   -n gem-adwaita-doc
Ruby bindings for GNOME documentation files.

Ruby/Adwaita is a Ruby binding of Adwaita.

%description   -n gem-adwaita-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета adwaita.
%endif


%if_enabled    devel
%package       -n gem-adwaita-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета adwaita
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(adwaita) = 4.3.6

%description   -n gem-adwaita-devel
Ruby bindings for GNOME development package.

Ruby/Adwaita is a Ruby binding of Adwaita.

%description   -n gem-adwaita-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета adwaita.
%endif


%package       -n gem-libhandy
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtk3) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(libhandy) = 4.3.6

%description   -n gem-libhandy
Ruby/Handy is a Ruby binding of Handy.


%if_enabled    doc
%package       -n gem-libhandy-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета libhandy
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(libhandy) = 4.3.6

%description   -n gem-libhandy-doc
Ruby bindings for GNOME documentation files.

Ruby/Handy is a Ruby binding of Handy.

%description   -n gem-libhandy-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета libhandy.
%endif


%if_enabled    devel
%package       -n gem-libhandy-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета libhandy
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(libhandy) = 4.3.6

%description   -n gem-libhandy-devel
Ruby bindings for GNOME development package.

Ruby/Handy is a Ruby binding of Handy.

%description   -n gem-libhandy-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета libhandy.
%endif


%package       -n gem-gnumeric
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(goffice) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(gnumeric) = 4.3.6

%description   -n gem-gnumeric
Ruby/Gnumeric is a Ruby binding of Gnumeric.


%if_enabled    doc
%package       -n gem-gnumeric-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gnumeric
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gnumeric) = 4.3.6

%description   -n gem-gnumeric-doc
Ruby bindings for GNOME documentation files.

Ruby/Gnumeric is a Ruby binding of Gnumeric.

%description   -n gem-gnumeric-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gnumeric.
%endif


%if_enabled    devel
%package       -n gem-gnumeric-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gnumeric
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(gnumeric) = 4.3.6

%description   -n gem-gnumeric-devel
Ruby bindings for GNOME development package.

Ruby/Gnumeric is a Ruby binding of Gnumeric.

%description   -n gem-gnumeric-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gnumeric.
%endif


%package       -n gem-gstreamer
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gobject-introspection) = 4.3.6
Provides:      gem(gstreamer) = 4.3.6

%description   -n gem-gstreamer
Ruby/GStreamer is a Ruby binding for GStreamer.


%if_enabled    doc
%package       -n gem-gstreamer-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gstreamer
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gstreamer) = 4.3.6

%description   -n gem-gstreamer-doc
Ruby bindings for GNOME documentation files.

Ruby/GStreamer is a Ruby binding for GStreamer.

%description   -n gem-gstreamer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gstreamer.
%endif


%if_enabled    devel
%package       -n gem-gstreamer-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gstreamer
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(gstreamer) = 4.3.6

%description   -n gem-gstreamer-devel
Ruby bindings for GNOME development package.

Ruby/GStreamer is a Ruby binding for GStreamer.

%description   -n gem-gstreamer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gstreamer.
%endif


%package       -n gem-graphene1
Version:       4.3.6
Release:       alt1
Summary:       Ruby/Graphene1 is a Ruby binding of Graphene
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gobject-introspection) = 4.3.6
Provides:      gem(graphene1) = 4.3.6

%description   -n gem-graphene1
Ruby/Graphene1 is a Ruby binding of Graphene.


%if_enabled    doc
%package       -n gem-graphene1-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby/Graphene1 is a Ruby binding of Graphene documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета graphene1
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(graphene1) = 4.3.6

%description   -n gem-graphene1-doc
Ruby/Graphene1 is a Ruby binding of Graphene documentation files.

%description   -n gem-graphene1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета graphene1.
%endif


%if_enabled    devel
%package       -n gem-graphene1-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby/Graphene1 is a Ruby binding of Graphene development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета graphene1
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(graphene1) = 4.3.6

%description   -n gem-graphene1-devel
Ruby/Graphene1 is a Ruby binding of Graphene development package.

%description   -n gem-graphene1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета graphene1.
%endif


%package       -n gem-libsecret
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gobject-introspection) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(libsecret) = 4.3.6

%description   -n gem-libsecret
Executable file for libsecret gem.


%if_enabled    doc
%package       -n gem-libsecret-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета libsecret
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(libsecret) = 4.3.6

%description   -n gem-libsecret-doc
Ruby bindings for GNOME documentation files.

Executable file for libsecret gem.

%description   -n gem-libsecret-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета libsecret.
%endif


%if_enabled    devel
%package       -n gem-libsecret-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета libsecret
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(libsecret) = 4.3.6

%description   -n gem-libsecret-devel
Ruby bindings for GNOME development package.

Executable file for libsecret gem.

%description   -n gem-libsecret-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета libsecret.
%endif


%package       -n gem-webkit-gtk
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtk4) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(webkit-gtk) = 4.3.6

%description   -n gem-webkit-gtk
Ruby/WebKitGTK is a Ruby binding of WebKitGTK+.


%if_enabled    doc
%package       -n gem-webkit-gtk-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета webkit-gtk
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(webkit-gtk) = 4.3.6

%description   -n gem-webkit-gtk-doc
Ruby bindings for GNOME documentation files.

Ruby/WebKitGTK is a Ruby binding of WebKitGTK+.

%description   -n gem-webkit-gtk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета webkit-gtk.
%endif


%if_enabled    devel
%package       -n gem-webkit-gtk-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета webkit-gtk
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(webkit-gtk) = 4.3.6

%description   -n gem-webkit-gtk-devel
Ruby bindings for GNOME development package.

Ruby/WebKitGTK is a Ruby binding of WebKitGTK+.

%description   -n gem-webkit-gtk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета webkit-gtk.
%endif


%package       -n gem-webkit2-gtk
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtk3) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(webkit2-gtk) = 4.3.6

%description   -n gem-webkit2-gtk
Ruby/WebKit2GTK is a Ruby binding of WebKit2GTK+.


%if_enabled    doc
%package       -n gem-webkit2-gtk-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета webkit2-gtk
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(webkit2-gtk) = 4.3.6

%description   -n gem-webkit2-gtk-doc
Ruby bindings for GNOME documentation files.

Ruby/WebKit2GTK is a Ruby binding of WebKit2GTK+.

%description   -n gem-webkit2-gtk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета webkit2-gtk.
%endif


%if_enabled    devel
%package       -n gem-webkit2-gtk-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета webkit2-gtk
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(webkit2-gtk) = 4.3.6

%description   -n gem-webkit2-gtk-devel
Ruby bindings for GNOME development package.

Ruby/WebKit2GTK is a Ruby binding of WebKit2GTK+.

%description   -n gem-webkit2-gtk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета webkit2-gtk.
%endif


%package       -n gem-gdk-pixbuf2
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gio2) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(gdk_pixbuf2) = 4.3.6

%description   -n gem-gdk-pixbuf2
Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x.


%if_enabled    doc
%package       -n gem-gdk-pixbuf2-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gdk_pixbuf2
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gdk_pixbuf2) = 4.3.6

%description   -n gem-gdk-pixbuf2-doc
Ruby bindings for GNOME documentation files.

Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x.

%description   -n gem-gdk-pixbuf2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gdk_pixbuf2.
%endif


%if_enabled    devel
%package       -n gem-gdk-pixbuf2-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gdk_pixbuf2
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(gdk_pixbuf2) = 4.3.6

%description   -n gem-gdk-pixbuf2-devel
Ruby bindings for GNOME development package.

Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x.

%description   -n gem-gdk-pixbuf2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gdk_pixbuf2.
%endif


%package       -n gem-clutter-gtk
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(clutter) = 4.3.6
Requires:      gem(clutter-gdk) = 4.3.6
Requires:      gem(gtk3) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(clutter-gtk) = 4.3.6

%description   -n gem-clutter-gtk
Ruby/ClutterGTK is a Ruby binding of Clutter-GTK.


%if_enabled    doc
%package       -n gem-clutter-gtk-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета clutter-gtk
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(clutter-gtk) = 4.3.6

%description   -n gem-clutter-gtk-doc
Ruby bindings for GNOME documentation files.

Ruby/ClutterGTK is a Ruby binding of Clutter-GTK.

%description   -n gem-clutter-gtk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета clutter-gtk.
%endif


%if_enabled    devel
%package       -n gem-clutter-gtk-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета clutter-gtk
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(clutter-gtk) = 4.3.6

%description   -n gem-clutter-gtk-devel
Ruby bindings for GNOME development package.

Ruby/ClutterGTK is a Ruby binding of Clutter-GTK.

%description   -n gem-clutter-gtk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета clutter-gtk.
%endif


%package       -n gem-clutter-gdk
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(clutter) = 4.3.6
Requires:      gem(gdk3) = 4.3.6
Provides:      gem(clutter-gdk) = 4.3.6

%description   -n gem-clutter-gdk
Ruby/ClutterGDK is a Ruby binding of GDK specific API of Clutter.


%if_enabled    doc
%package       -n gem-clutter-gdk-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета clutter-gdk
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(clutter-gdk) = 4.3.6

%description   -n gem-clutter-gdk-doc
Ruby bindings for GNOME documentation files.

Ruby/ClutterGDK is a Ruby binding of GDK specific API of Clutter.

%description   -n gem-clutter-gdk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета clutter-gdk.
%endif


%if_enabled    devel
%package       -n gem-clutter-gdk-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета clutter-gdk
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(clutter-gdk) = 4.3.6

%description   -n gem-clutter-gdk-devel
Ruby bindings for GNOME development package.

Ruby/ClutterGDK is a Ruby binding of GDK specific API of Clutter.

%description   -n gem-clutter-gdk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета clutter-gdk.
%endif


%package       -n gem-cairo-gobject
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cairo) >= 1.16.2
Requires:      gem(glib2) = 4.3.6
Provides:      gem(cairo-gobject) = 4.3.6

%description   -n gem-cairo-gobject
Ruby/CairoGObject is a Ruby binding of cairo-gobject.


%if_enabled    doc
%package       -n gem-cairo-gobject-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cairo-gobject
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cairo-gobject) = 4.3.6

%description   -n gem-cairo-gobject-doc
Ruby bindings for GNOME documentation files.

Ruby/CairoGObject is a Ruby binding of cairo-gobject.

%description   -n gem-cairo-gobject-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cairo-gobject.
%endif


%if_enabled    devel
%package       -n gem-cairo-gobject-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cairo-gobject
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(cairo-gobject) = 4.3.6

%description   -n gem-cairo-gobject-devel
Ruby bindings for GNOME development package.

Ruby/CairoGObject is a Ruby binding of cairo-gobject.

%description   -n gem-cairo-gobject-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cairo-gobject.
%endif


%package       -n gem-gtksourceview5
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtk4) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(gtksourceview5) = 4.3.6

%description   -n gem-gtksourceview5
Ruby/GtkSourceView5 is a Ruby binding of gtksourceview-5.x.


%if_enabled    doc
%package       -n gem-gtksourceview5-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gtksourceview5
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtksourceview5) = 4.3.6

%description   -n gem-gtksourceview5-doc
Ruby bindings for GNOME documentation files.

Ruby/GtkSourceView5 is a Ruby binding of gtksourceview-5.x.

%description   -n gem-gtksourceview5-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gtksourceview5.
%endif


%if_enabled    devel
%package       -n gem-gtksourceview5-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gtksourceview5
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtksourceview5) = 4.3.6

%description   -n gem-gtksourceview5-devel
Ruby bindings for GNOME development package.

Ruby/GtkSourceView5 is a Ruby binding of gtksourceview-5.x.

%description   -n gem-gtksourceview5-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gtksourceview5.
%endif


%package       -n gem-gtksourceview4
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtk3) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(gtksourceview4) = 4.3.6

%description   -n gem-gtksourceview4
Ruby/GtkSourceView4 is a Ruby binding of gtksourceview-4.x.


%if_enabled    doc
%package       -n gem-gtksourceview4-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gtksourceview4
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtksourceview4) = 4.3.6

%description   -n gem-gtksourceview4-doc
Ruby bindings for GNOME documentation files.

Ruby/GtkSourceView4 is a Ruby binding of gtksourceview-4.x.

%description   -n gem-gtksourceview4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gtksourceview4.
%endif


%if_enabled    devel
%package       -n gem-gtksourceview4-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gtksourceview4
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(gtksourceview4) = 4.3.6

%description   -n gem-gtksourceview4-devel
Ruby bindings for GNOME development package.

Ruby/GtkSourceView4 is a Ruby binding of gtksourceview-4.x.

%description   -n gem-gtksourceview4-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gtksourceview4.
%endif


%package       -n gem-gtksourceview3
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtk3) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(gtksourceview3) = 4.3.6

%description   -n gem-gtksourceview3
Ruby/GtkSourceView3 is a Ruby binding of gtksourceview-3.x.


%if_enabled    doc
%package       -n gem-gtksourceview3-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gtksourceview3
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gtksourceview3) = 4.3.6

%description   -n gem-gtksourceview3-doc
Ruby bindings for GNOME documentation files.

Ruby/GtkSourceView3 is a Ruby binding of gtksourceview-3.x.

%description   -n gem-gtksourceview3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gtksourceview3.
%endif


%if_enabled    devel
%package       -n gem-gtksourceview3-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gtksourceview3
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(gtksourceview3) = 4.3.6

%description   -n gem-gtksourceview3-devel
Ruby bindings for GNOME development package.

Ruby/GtkSourceView3 is a Ruby binding of gtksourceview-3.x.

%description   -n gem-gtksourceview3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gtksourceview3.
%endif


%package       -n gem-clutter-gstreamer
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(clutter) = 4.3.6
Requires:      gem(gdk_pixbuf2) = 4.3.6
Requires:      gem(gstreamer) = 4.3.6
Requires:      gem(rake) >= 0
Provides:      gem(clutter-gstreamer) = 4.3.6

%description   -n gem-clutter-gstreamer
Ruby/ClutterGStreamer is a Ruby binding of Clutter-GStreamer.


%if_enabled    doc
%package       -n gem-clutter-gstreamer-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета clutter-gstreamer
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(clutter-gstreamer) = 4.3.6

%description   -n gem-clutter-gstreamer-doc
Ruby bindings for GNOME documentation files.

Ruby/ClutterGStreamer is a Ruby binding of Clutter-GStreamer.

%description   -n gem-clutter-gstreamer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета clutter-gstreamer.
%endif


%if_enabled    devel
%package       -n gem-clutter-gstreamer-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета clutter-gstreamer
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(clutter-gstreamer) = 4.3.6

%description   -n gem-clutter-gstreamer-devel
Ruby bindings for GNOME development package.

Ruby/ClutterGStreamer is a Ruby binding of Clutter-GStreamer.

%description   -n gem-clutter-gstreamer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета clutter-gstreamer.
%endif


%package       -n gem-gobject-introspection
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(glib2) = 4.3.6
Provides:      gem(gobject-introspection) = 4.3.6

%description   -n gem-gobject-introspection
Ruby/GObjectIntrospection is a Ruby binding of GObject Introspect.


%if_enabled    doc
%package       -n gem-gobject-introspection-doc
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gobject-introspection
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gobject-introspection) = 4.3.6

%description   -n gem-gobject-introspection-doc
Ruby bindings for GNOME documentation files.

Ruby/GObjectIntrospection is a Ruby binding of GObject Introspect.

%description   -n gem-gobject-introspection-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gobject-introspection.
%endif


%if_enabled    devel
%package       -n gem-gobject-introspection-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gobject-introspection
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby-gnome2-devel
Requires:      gem(gobject-introspection) = 4.3.6

%description   -n gem-gobject-introspection-devel
Ruby bindings for GNOME development package.

Ruby/GObjectIntrospection is a Ruby binding of GObject Introspect.

%description   -n gem-gobject-introspection-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gobject-introspection.
%endif


%if_enabled    devel
%package       -n ruby-gnome2-devel
Version:       4.3.6
Release:       alt1
Summary:       Ruby bindings for GNOME
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-gnome2
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      pkgconfig(pixman-1)
Requires:      pkgconfig(expat)
Requires:      pkgconfig(libdrm)
Requires:      pkgconfig(libpcre)
Requires:      pkgconfig(xdmcp)
Requires:      pkgconfig(xdamage)
Requires:      pkgconfig(xxf86vm)
Requires:      pkgconfig(vte)
Requires:      pkgconfig(libvlc)
Requires:      pkgconfig(uuid)
Requires:      pkgconfig(fribidi)
Requires:      pkgconfig(libtiff-4)
Requires:      pkgconfig(mount)
Requires:      pkgconfig(blkid)
Requires:      pkgconfig(epoxy)
Requires:      pkgconfig(xcb-xinerama)
Requires:      pkgconfig(xi)
Requires:      pkgconfig(xcb-randr)
Requires:      pkgconfig(xcursor)
Requires:      pkgconfig(xcomposite)
Requires:      pkgconfig(libpng)
Requires:      pkgconfig(libxml-2.0)
Requires:      pkgconfig(wayland-cursor)
Requires:      pkgconfig(wayland-egl)
Requires:      pkgconfig(wayland-client)
Requires:      pkgconfig(xkbcommon)
Requires:      pkgconfig(gstreamer-plugins-base-1.0)
Requires:      pkgconfig(gobject-introspection-1.0)
Requires:      pkgconfig(libselinux)
Requires:      pkgconfig(xtst)
Requires:      pkgconfig(libthai)
Requires:      pkgconfig(datrie-0.2)
Requires:      pkgconfig(glib-2.0)
Requires:      pkgconfig(gio-2.0)
Requires:      pkgconfig(pango)
Requires:      pkgconfig(libjpeg)
Requires:      pkgconfig(libbrotlicommon)
Requires:      pkgconfig(cairo)
Requires:      pkgconfig(glproto)
Requires:      pkgconfig(dri2proto)
Requires:      pkgconfig(xau)
Requires:      pkgconfig(xext)
Requires:      pkgconfig(libffi)
Requires:      pkgconfig(ossp-uuid)
Requires:      pkgconfig(gegl-0.4)
Requires:      pkgconfig(atk-bridge-2.0)
Requires:      pkgconfig(xrandr)
Requires:      pkgconfig(xinerama)
Requires:      pkgconfig(gtk+-3.0)
Requires:      pkgconfig(gtk4)
Requires:      pkgconfig(harfbuzz)
Requires:      pkgconfig(xshmfence)
Requires:      pkgconfig(libpcre2-8)
Requires:      pkgconfig(libsystemd)
Requires:      pkgconfig(libwebp)
Requires:      pkgconfig(libzstd)
Requires:      pkgconfig(liblzma)
Requires:      pkgconfig(libdeflate)
Requires:      pkgconfig(bzip2)
Requires:      pkgconfig(libcap)
Requires:      shared-mime-info-devel
Requires:      ruby-gnome2 = 4.3.6-alt1
Requires:      gem(adwaita) >= 0
Requires:      gem(atk) = 4.3.6
Requires:      gem(bundler) >= 0
Requires:      gem(cairo) >= 1.16.2
Requires:      gem(cairo-gobject) = 4.3.6
Requires:      gem(clutter) = 4.3.6
Requires:      gem(clutter-gdk) = 4.3.6
Requires:      gem(clutter-gstreamer) >= 0
Requires:      gem(clutter-gtk) >= 0
Requires:      gem(erb) >= 0
Requires:      gem(fiddle) >= 0
Requires:      gem(gdk3) = 4.3.6
Requires:      gem(gdk4) = 4.3.6
Requires:      gem(gdk_pixbuf2) = 4.3.6
Requires:      gem(gegl) >= 0
Requires:      gem(gio2) = 4.3.6
Requires:      gem(glib2) = 4.3.6
Requires:      gem(gnumeric) >= 0
Requires:      gem(gobject-introspection) = 4.3.6
Requires:      gem(goffice) = 4.3.6
Requires:      gem(graphene1) = 4.3.6
Requires:      gem(gsf) = 4.3.6
Requires:      gem(gsk4) = 4.3.6
Requires:      gem(gstreamer) = 4.3.6
Requires:      gem(gtk3) = 4.3.6
Requires:      gem(gtk4) = 4.3.6
Requires:      gem(gtksourceview3) >= 0
Requires:      gem(gtksourceview4) >= 0
Requires:      gem(gtksourceview5) >= 0
Requires:      gem(gvlc) >= 0
Requires:      gem(libhandy) >= 0
Requires:      gem(libsecret) >= 0
Requires:      gem(native-package-installer) >= 1.0.3
Requires:      gem(pango) = 4.3.6
Requires:      gem(pkg-config) >= 1.3.5
Requires:      gem(poppler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rsvg2) >= 0
Requires:      gem(vte3) >= 0
Requires:      gem(vte4) >= 0
Requires:      gem(webkit-gtk) >= 0
Requires:      gem(webkit2-gtk) >= 0
Requires:      gem(wnck3) >= 0

%description   -n ruby-gnome2-devel
Ruby bindings for GNOME development package.

This is a set of bindings for the GNOME 2.x and 3.x libraries to use from Ruby
2.1, 2.2, 2.3 and 2.4.

%description   -n ruby-gnome2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-gnome2. %endif
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files

%files         -n gem-gsf
%doc COPYING.LIB README.md
%ruby_gemspecdir/gsf-4.3.6.gemspec
%ruby_gemslibdir/gsf-4.3.6
%ruby_gemsextdir/gsf-4.3.6

%if_enabled    doc
%files         -n gem-gsf-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gsf-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gsf-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-atk
%doc COPYING.LIB README.md
%ruby_gemspecdir/atk-4.3.6.gemspec
%ruby_gemslibdir/atk-4.3.6
%ruby_gemsextdir/atk-4.3.6

%if_enabled    doc
%files         -n gem-atk-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/atk-4.3.6
%endif

%if_enabled    devel
%files         -n gem-atk-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-gtk4
%doc COPYING.LIB README.md
%ruby_gemspecdir/gtk4-4.3.6.gemspec
%ruby_gemslibdir/gtk4-4.3.6
%ruby_gemsextdir/gtk4-4.3.6

%if_enabled    doc
%files         -n gem-gtk4-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gtk4-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gtk4-devel
%doc COPYING.LIB README.md
%ruby_includedir/*
%endif

%files         -n gem-gtk3
%doc COPYING.LIB README.md
%ruby_gemspecdir/gtk3-4.3.6.gemspec
%ruby_gemslibdir/gtk3-4.3.6
%ruby_gemsextdir/gtk3-4.3.6

%if_enabled    doc
%files         -n gem-gtk3-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gtk3-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gtk3-devel
%doc COPYING.LIB README.md
%ruby_includedir/*
%endif

%files         -n gem-gsk4
%doc COPYING.LIB README.md
%ruby_gemspecdir/gsk4-4.3.6.gemspec
%ruby_gemslibdir/gsk4-4.3.6

%if_enabled    doc
%files         -n gem-gsk4-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gsk4-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gsk4-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-vte3
%doc COPYING.LIB README.md
%ruby_gemspecdir/vte3-4.3.6.gemspec
%ruby_gemslibdir/vte3-4.3.6
%ruby_gemsextdir/vte3-4.3.6

%if_enabled    doc
%files         -n gem-vte3-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/vte3-4.3.6
%endif

%if_enabled    devel
%files         -n gem-vte3-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-gio2
%doc COPYING.LIB README.md
%ruby_gemspecdir/gio2-4.3.6.gemspec
%ruby_gemslibdir/gio2-4.3.6
%ruby_gemsextdir/gio2-4.3.6

%if_enabled    doc
%files         -n gem-gio2-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gio2-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gio2-devel
%doc COPYING.LIB README.md
%ruby_includedir/*
%endif

%files         -n gem-gegl
%doc COPYING.LIB README.md
%ruby_gemspecdir/gegl-4.3.6.gemspec
%ruby_gemslibdir/gegl-4.3.6
%ruby_gemsextdir/gegl-4.3.6

%if_enabled    doc
%files         -n gem-gegl-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gegl-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gegl-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-vte4
%doc COPYING.LIB README.md
%ruby_gemspecdir/vte4-4.3.6.gemspec
%ruby_gemslibdir/vte4-4.3.6
%ruby_gemsextdir/vte4-4.3.6

%if_enabled    doc
%files         -n gem-vte4-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/vte4-4.3.6
%endif

%if_enabled    devel
%files         -n gem-vte4-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-gdk4
%doc COPYING.LIB README.md
%ruby_gemspecdir/gdk4-4.3.6.gemspec
%ruby_gemslibdir/gdk4-4.3.6
%ruby_gemsextdir/gdk4-4.3.6

%if_enabled    doc
%files         -n gem-gdk4-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gdk4-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gdk4-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-gdk3
%doc COPYING.LIB README.md
%ruby_gemspecdir/gdk3-4.3.6.gemspec
%ruby_gemslibdir/gdk3-4.3.6
%ruby_gemsextdir/gdk3-4.3.6

%if_enabled    doc
%files         -n gem-gdk3-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gdk3-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gdk3-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-gvlc
%doc COPYING.LIB README.md
%ruby_gemspecdir/gvlc-4.3.6.gemspec
%ruby_gemslibdir/gvlc-4.3.6
%ruby_gemsextdir/gvlc-4.3.6

%if_enabled    doc
%files         -n gem-gvlc-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gvlc-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gvlc-devel
%doc COPYING.LIB README.md
%ruby_includedir/*
%endif

%files         -n gem-pango
%doc COPYING.LIB README.md
%ruby_gemspecdir/pango-4.3.6.gemspec
%ruby_gemslibdir/pango-4.3.6
%ruby_gemsextdir/pango-4.3.6

%if_enabled    doc
%files         -n gem-pango-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/pango-4.3.6
%endif

%if_enabled    devel
%files         -n gem-pango-devel
%doc COPYING.LIB README.md
%ruby_includedir/*
%endif

%files         -n gem-wnck3
%doc COPYING.LIB README.md
%ruby_gemspecdir/wnck3-4.3.6.gemspec
%ruby_gemslibdir/wnck3-4.3.6
%ruby_gemsextdir/wnck3-4.3.6

%if_enabled    doc
%files         -n gem-wnck3-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/wnck3-4.3.6
%endif

%if_enabled    devel
%files         -n gem-wnck3-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-glib2
%doc COPYING.LIB README.md
%ruby_gemspecdir/glib2-4.3.6.gemspec
%ruby_gemslibdir/glib2-4.3.6
%ruby_gemsextdir/glib2-4.3.6

%if_enabled    doc
%files         -n gem-glib2-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/glib2-4.3.6
%endif

%if_enabled    devel
%files         -n gem-glib2-devel
%doc COPYING.LIB README.md
%ruby_includedir/*
%endif

%files         -n gem-rsvg2
%doc COPYING.LIB README.md
%ruby_gemspecdir/rsvg2-4.3.6.gemspec
%ruby_gemslibdir/rsvg2-4.3.6
%ruby_gemsextdir/rsvg2-4.3.6

%if_enabled    doc
%files         -n gem-rsvg2-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/rsvg2-4.3.6
%endif

%if_enabled    devel
%files         -n gem-rsvg2-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-clutter
%doc COPYING.LIB README.md
%ruby_gemspecdir/clutter-4.3.6.gemspec
%ruby_gemslibdir/clutter-4.3.6
%ruby_gemsextdir/clutter-4.3.6

%if_enabled    doc
%files         -n gem-clutter-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/clutter-4.3.6
%endif

%if_enabled    devel
%files         -n gem-clutter-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-goffice
%doc COPYING.LIB README.md
%ruby_gemspecdir/goffice-4.3.6.gemspec
%ruby_gemslibdir/goffice-4.3.6
%ruby_gemsextdir/goffice-4.3.6

%if_enabled    doc
%files         -n gem-goffice-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/goffice-4.3.6
%endif

%if_enabled    devel
%files         -n gem-goffice-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-poppler
%doc COPYING.LIB README.md
%ruby_gemspecdir/poppler-4.3.6.gemspec
%ruby_gemslibdir/poppler-4.3.6
%ruby_gemsextdir/poppler-4.3.6

%if_enabled    doc
%files         -n gem-poppler-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/poppler-4.3.6
%endif

%if_enabled    devel
%files         -n gem-poppler-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-adwaita
%doc COPYING.LIB README.md
%ruby_gemspecdir/adwaita-4.3.6.gemspec
%ruby_gemslibdir/adwaita-4.3.6
%ruby_gemsextdir/adwaita-4.3.6

%if_enabled    doc
%files         -n gem-adwaita-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/adwaita-4.3.6
%endif

%if_enabled    devel
%files         -n gem-adwaita-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-libhandy
%doc COPYING.LIB README.md
%ruby_gemspecdir/libhandy-4.3.6.gemspec
%ruby_gemslibdir/libhandy-4.3.6
%ruby_gemsextdir/libhandy-4.3.6

%if_enabled    doc
%files         -n gem-libhandy-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/libhandy-4.3.6
%endif

%if_enabled    devel
%files         -n gem-libhandy-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-gnumeric
%doc COPYING.LIB README.md
%ruby_gemspecdir/gnumeric-4.3.6.gemspec
%ruby_gemslibdir/gnumeric-4.3.6
%ruby_gemsextdir/gnumeric-4.3.6

%if_enabled    doc
%files         -n gem-gnumeric-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gnumeric-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gnumeric-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-gstreamer
%doc COPYING.LIB README.md
%ruby_gemspecdir/gstreamer-4.3.6.gemspec
%ruby_gemslibdir/gstreamer-4.3.6
%ruby_gemsextdir/gstreamer-4.3.6

%if_enabled    doc
%files         -n gem-gstreamer-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gstreamer-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gstreamer-devel
%doc COPYING.LIB README.md
%ruby_includedir/*
%endif

%files         -n gem-graphene1
%doc COPYING.LIB README.md
%ruby_gemspecdir/graphene1-4.3.6.gemspec
%ruby_gemslibdir/graphene1-4.3.6

%if_enabled    doc
%files         -n gem-graphene1-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/graphene1-4.3.6
%endif

%if_enabled    devel
%files         -n gem-graphene1-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-libsecret
%doc COPYING.LIB README.md
%ruby_gemspecdir/libsecret-4.3.6.gemspec
%ruby_gemslibdir/libsecret-4.3.6
%ruby_gemsextdir/libsecret-4.3.6

%if_enabled    doc
%files         -n gem-libsecret-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/libsecret-4.3.6
%endif

%if_enabled    devel
%files         -n gem-libsecret-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-webkit-gtk
%doc COPYING.LIB README.md
%ruby_gemspecdir/webkit-gtk-4.3.6.gemspec
%ruby_gemslibdir/webkit-gtk-4.3.6
%ruby_gemsextdir/webkit-gtk-4.3.6

%if_enabled    doc
%files         -n gem-webkit-gtk-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/webkit-gtk-4.3.6
%endif

%if_enabled    devel
%files         -n gem-webkit-gtk-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-webkit2-gtk
%doc COPYING.LIB README.md
%ruby_gemspecdir/webkit2-gtk-4.3.6.gemspec
%ruby_gemslibdir/webkit2-gtk-4.3.6
%ruby_gemsextdir/webkit2-gtk-4.3.6

%if_enabled    doc
%files         -n gem-webkit2-gtk-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/webkit2-gtk-4.3.6
%endif

%if_enabled    devel
%files         -n gem-webkit2-gtk-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-gdk-pixbuf2
%doc COPYING.LIB README.md
%ruby_gemspecdir/gdk_pixbuf2-4.3.6.gemspec
%ruby_gemslibdir/gdk_pixbuf2-4.3.6
%ruby_gemsextdir/gdk_pixbuf2-4.3.6

%if_enabled    doc
%files         -n gem-gdk-pixbuf2-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gdk_pixbuf2-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gdk-pixbuf2-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-clutter-gtk
%doc COPYING.LIB README.md
%ruby_gemspecdir/clutter-gtk-4.3.6.gemspec
%ruby_gemslibdir/clutter-gtk-4.3.6
%ruby_gemsextdir/clutter-gtk-4.3.6

%if_enabled    doc
%files         -n gem-clutter-gtk-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/clutter-gtk-4.3.6
%endif

%if_enabled    devel
%files         -n gem-clutter-gtk-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-clutter-gdk
%doc COPYING.LIB README.md
%ruby_gemspecdir/clutter-gdk-4.3.6.gemspec
%ruby_gemslibdir/clutter-gdk-4.3.6

%if_enabled    doc
%files         -n gem-clutter-gdk-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/clutter-gdk-4.3.6
%endif

%if_enabled    devel
%files         -n gem-clutter-gdk-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-cairo-gobject
%doc COPYING.LIB README.md
%ruby_gemspecdir/cairo-gobject-4.3.6.gemspec
%ruby_gemslibdir/cairo-gobject-4.3.6
%ruby_gemsextdir/cairo-gobject-4.3.6

%if_enabled    doc
%files         -n gem-cairo-gobject-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/cairo-gobject-4.3.6
%endif

%if_enabled    devel
%files         -n gem-cairo-gobject-devel
%doc COPYING.LIB README.md
%ruby_includedir/*
%endif

%files         -n gem-gtksourceview5
%doc COPYING.LIB README.md
%ruby_gemspecdir/gtksourceview5-4.3.6.gemspec
%ruby_gemslibdir/gtksourceview5-4.3.6
%ruby_gemsextdir/gtksourceview5-4.3.6

%if_enabled    doc
%files         -n gem-gtksourceview5-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gtksourceview5-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gtksourceview5-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-gtksourceview4
%doc COPYING.LIB README.md
%ruby_gemspecdir/gtksourceview4-4.3.6.gemspec
%ruby_gemslibdir/gtksourceview4-4.3.6
%ruby_gemsextdir/gtksourceview4-4.3.6

%if_enabled    doc
%files         -n gem-gtksourceview4-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gtksourceview4-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gtksourceview4-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-gtksourceview3
%doc COPYING.LIB README.md
%ruby_gemspecdir/gtksourceview3-4.3.6.gemspec
%ruby_gemslibdir/gtksourceview3-4.3.6
%ruby_gemsextdir/gtksourceview3-4.3.6

%if_enabled    doc
%files         -n gem-gtksourceview3-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gtksourceview3-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gtksourceview3-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-clutter-gstreamer
%doc COPYING.LIB README.md
%ruby_gemspecdir/clutter-gstreamer-4.3.6.gemspec
%ruby_gemslibdir/clutter-gstreamer-4.3.6
%ruby_gemsextdir/clutter-gstreamer-4.3.6

%if_enabled    doc
%files         -n gem-clutter-gstreamer-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/clutter-gstreamer-4.3.6
%endif

%if_enabled    devel
%files         -n gem-clutter-gstreamer-devel
%doc COPYING.LIB README.md
%endif

%files         -n gem-gobject-introspection
%doc COPYING.LIB README.md
%ruby_gemspecdir/gobject-introspection-4.3.6.gemspec
%ruby_gemslibdir/gobject-introspection-4.3.6
%ruby_gemsextdir/gobject-introspection-4.3.6

%if_enabled    doc
%files         -n gem-gobject-introspection-doc
%doc COPYING.LIB README.md
%ruby_gemsdocdir/gobject-introspection-4.3.6
%endif

%if_enabled    devel
%files         -n gem-gobject-introspection-devel
%doc COPYING.LIB README.md
%ruby_includedir/*
%endif

%if_enabled    devel
%files         -n ruby-gnome2-devel
%endif


%changelog
* Sat May 16 2026 Pavel Skrylev <majioa@altlinux.org> 4.3.6-alt1
- ^ 4.3.5 -> 4.3.6
- ! croppen out dep to libgtksourceview, closing ALT #59088

* Wed Mar 25 2026 Pavel Skrylev <majioa@altlinux.org> 4.3.5-alt1
- ^ 4.2.5 -> 4.3.5

* Tue Oct 21 2025 Pavel Skrylev <majioa@altlinux.org> 4.2.5-alt0.5
- ! fixed lost deps to some pkgconfig modules

* Mon Aug 11 2025 Pavel Skrylev <majioa@altlinux.org> 4.2.5-alt0.4
- * used cairo headers devel instead of just gem cairo devel

* Mon May 12 2025 Pavel Skrylev <majioa@altlinux.org> 4.2.5-alt0.3
- ![NBTFS] fixed devel packages for build and devel functions to pkgconfig

* Tue Mar 04 2025 Pavel Skrylev <majioa@altlinux.org> 4.2.5-alt0.2
- ! fixed disappeared dep to libsystemd.pc on build

* Wed Nov 06 2024 Pavel Skrylev <majioa@altlinux.org> 4.2.5-alt0.1
- ^ 4.2.0 -> 4.2.5

* Wed May 15 2024 Pavel Skrylev <majioa@altlinux.org> 4.2.0-alt1.2
- ! fixed build deps to properly build so extensions (closes #50358)

* Sun Dec 24 2023 Pavel Skrylev <majioa@altlinux.org> 4.2.0-alt1.1
- ! fixed dep to gem-pkg-devel moving under check cond

* Sun Dec 24 2023 Pavel Skrylev <majioa@altlinux.org> 4.2.0-alt1
- ^ 4.1.7 -> 4.2.0

* Fri Jun 23 2023 Pavel Skrylev <majioa@altlinux.org> 4.1.7-alt1
- ^ 3.5.1 -> 4.1.7

* Mon Sep 26 2022 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt1.3
- + lost dep to pkgconfig(libpcre2-8)
- + ruby-gnome2-devel package with uplinks form devel subpackage

* Mon Jun 27 2022 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt1.2
- comment out dep to gem cairo

* Fri Apr 15 2022 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt1.1
- ! spec to avoid compilation errors

* Wed Mar 09 2022 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt1
- ^ 3.4.3 -> 3.5.1

* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 3.4.3-alt1.1
- ! spec with settigns proper aliases

* Tue Jun 30 2020 Pavel Skrylev <majioa@altlinux.org> 3.4.3-alt1
- ^ 3.4.1 -> 3.4.3
- + a few package task build depended gem

* Thu Jun 04 2020 Pavel Skrylev <majioa@altlinux.org> 3.4.1-alt1.4
- Fix

* Mon May 25 2020 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1.3
- Fix build by adding libbrotli-devel.

* Sat May 09 2020 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1.2
- Do not require deprecated libwlc0-devel for wayland-protocols.pc.

* Thu Apr 02 2020 Pavel Skrylev <majioa@altlinux.org> 3.4.1-alt1.1
- ! build required package names

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 3.4.1-alt1
- updated (^) 3.3.8 -> 3.4.1

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.8-alt1
- updated (^) 3.3.7 -> 3.3.8
- fixed (!) spec according to changelog rules

* Tue Aug 20 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.7-alt1
- updated (^) 3.3.6 -> 3.3.7
- added (+) libthai-devel, and libdatrie-devel build reqs
- added (+) wnck3, and libsecret gems

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.6-alt2
- ignore ruby-gnome2 gemfile

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.6-alt1
- Bump to 3.3.6

* Tue Mar 19 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.2-alt2
- Fix build for new gnome

* Tue Feb 05 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.2-alt1
- Bump to 3.3.2 gem;
- Use Ruby Policy 2.0;
- All the subpackages now included.

* Sun Jan 20 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.1-alt1
- Bump to 3.3.1 gem.

* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.9-alt2
- Fix build (add libpcre-devel).

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.9-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.7-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 07 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.7-alt1
- New version.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.6-alt1
- New version.

* Wed May 02 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.5-alt1
- New version.

* Mon Apr 09 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.4-alt1
- New version.

* Tue Apr 03 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt2
- Build with libvte3.

* Tue Apr 03 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- New version.

* Mon Apr 02 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.2-alt1
- New version.

* Sat Mar 31 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- New version.
- Build with gstreamer1.0-devel.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Apr 21 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- Initial build in Sisyphus

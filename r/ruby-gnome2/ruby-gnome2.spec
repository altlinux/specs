Name:          ruby-gnome2
Version:       3.5.1
Release:       alt1
Summary:       Ruby bindings for GNOME
License:       LGPL-2.1+
Group:         Development/Ruby
Url:           https://ruby-gnome2.osdn.jp/
Vcs:           https://github.com/ruby-gnome2/ruby-gnome2.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libgtk+2-devel
BuildRequires: libgtk+3-devel
BuildRequires: libpixman-devel
BuildRequires: libexpat-devel
BuildRequires: libharfbuzz-devel
BuildRequires: libdrm-devel
BuildRequires: libpcre-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXdamage-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libvte3-devel
BuildRequires: libvte-devel
BuildRequires: libvlc-devel
BuildRequires: libuuid-devel
BuildRequires: libgtksourceview-devel
BuildRequires: libfribidi-devel
BuildRequires: libtiff-devel
BuildRequires: libmount-devel
BuildRequires: libblkid-devel
BuildRequires: libat-spi2-core-devel
BuildRequires: libepoxy-devel
BuildRequires: libXinerama-devel
BuildRequires: libXi-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: libXcomposite-devel
BuildRequires: libpng-devel
BuildRequires: libxml2-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: wayland-protocols
BuildRequires: libxkbcommon-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: gobject-introspection-devel
BuildRequires: at-spi2-atk-devel
BuildRequires: libselinux-devel
BuildRequires: libXtst-devel
BuildRequires: libthai-devel
BuildRequires: libdatrie-devel
BuildRequires: bzlib-devel
BuildRequires: glib2-devel
BuildRequires: libgio-devel
BuildRequires: libpango-devel
BuildRequires: gst-plugins-devel
BuildRequires: gcc-c++
BuildRequires: libbrotli-devel
BuildRequires: gem-cairo-devel
BuildRequires: gem(cairo) >= 1.16.2
BuildRequires: gem(fiddle) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(pkg-config) >= 1.3.5
BuildRequires: gem(native-package-installer) >= 1.0.3
BuildRequires: gem(test-unit) >= 2
BuildRequires: gem(cairo) >= 0
BuildRequires: gem(native-package-installer) >= 0
BuildRequires: gem(pkg-config) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(cairo) >= 0
Requires:      gem(native-package-installer) >= 0
Requires:      gem(pkg-config) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(webrick) >= 0


%description
This is a set of bindings for the GNOME 2.x and 3.x libraries to use from Ruby
2.1, 2.2, 2.3 and 2.4.


%package       -n gem-gegl
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GEGL is a Ruby binding of GEGL
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gio2) = 3.5.1
Provides:      gem(gegl) = 3.5.1

%description   -n gem-gegl
Ruby/GEGL is a Ruby binding of GEGL.


%package       -n gem-gegl-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GEGL is a Ruby binding of GEGL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gegl
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gegl) = 3.5.1

%description   -n gem-gegl-doc
Ruby/GEGL is a Ruby binding of GEGL documentation files.

%description   -n gem-gegl-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gegl.


%package       -n gem-gegl-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GEGL is a Ruby binding of GEGL development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gegl
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gegl) = 3.5.1

%description   -n gem-gegl-devel
Ruby/GEGL is a Ruby binding of GEGL development package.

%description   -n gem-gegl-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gegl.


%package       -n gem-gobject-introspection
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GObjectIntrospection is a Ruby binding of GObject Introspect
Group:         Development/Ruby

Requires:      gem(glib2) = 3.5.1
Provides:      gem(gobject-introspection) = 3.5.1

%description   -n gem-gobject-introspection
Ruby/GObjectIntrospection is a Ruby binding of GObject Introspect.


%package       -n gem-gobject-introspection-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GObjectIntrospection is a Ruby binding of GObject Introspect documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gobject-introspection
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gobject-introspection) = 3.5.1

%description   -n gem-gobject-introspection-doc
Ruby/GObjectIntrospection is a Ruby binding of GObject Introspect documentation
files.

%description   -n gem-gobject-introspection-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gobject-introspection.


%package       -n gem-gobject-introspection-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GObjectIntrospection is a Ruby binding of GObject Introspect development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gobject-introspection
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gobject-introspection) = 3.5.1

%description   -n gem-gobject-introspection-devel
Ruby/GObjectIntrospection is a Ruby binding of GObject Introspect development
package.

%description   -n gem-gobject-introspection-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gobject-introspection.


%package       -n gem-gdk4
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GDK4 is a Ruby binding of GDK 4
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pango) = 3.5.1
Requires:      gem(gdk_pixbuf2) = 3.5.1
Requires:      gem(cairo-gobject) = 3.5.1
Provides:      gem(gdk4) = 3.5.1

%description   -n gem-gdk4
Ruby/GDK4 is a Ruby binding of GDK 4.


%package       -n gem-gdk4-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GDK4 is a Ruby binding of GDK 4 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gdk4
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gdk4) = 3.5.1

%description   -n gem-gdk4-doc
Ruby/GDK4 is a Ruby binding of GDK 4 documentation files.

%description   -n gem-gdk4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gdk4.


%package       -n gem-gdk4-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GDK4 is a Ruby binding of GDK 4 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gdk4
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gdk4) = 3.5.1

%description   -n gem-gdk4-devel
Ruby/GDK4 is a Ruby binding of GDK 4 development package.

%description   -n gem-gdk4-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gdk4.


%package       -n gem-cairo-gobject
Version:       3.5.1
Release:       alt1
Summary:       Ruby/CairoGObject is a Ruby binding of cairo-gobject
Group:         Development/Ruby

Requires:      gem(cairo) >= 1.16.2
Requires:      gem(glib2) = 3.5.1
Provides:      gem(cairo-gobject) = 3.5.1

%description   -n gem-cairo-gobject
Ruby/CairoGObject is a Ruby binding of cairo-gobject.


%package       -n gem-cairo-gobject-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/CairoGObject is a Ruby binding of cairo-gobject documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cairo-gobject
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(cairo-gobject) = 3.5.1

%description   -n gem-cairo-gobject-doc
Ruby/CairoGObject is a Ruby binding of cairo-gobject documentation
files.

%description   -n gem-cairo-gobject-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cairo-gobject.


%package       -n gem-cairo-gobject-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/CairoGObject is a Ruby binding of cairo-gobject development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cairo-gobject
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cairo-gobject) = 3.5.1

%description   -n gem-cairo-gobject-devel
Ruby/CairoGObject is a Ruby binding of cairo-gobject development
package.

%description   -n gem-cairo-gobject-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cairo-gobject.


%package       -n gem-rsvg2
Version:       3.5.1
Release:       alt1
Summary:       Ruby/RSVG2 is a Ruby binding of librsvg based on GObject-Introspection
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gdk_pixbuf2) = 3.5.1
Requires:      gem(cairo-gobject) = 3.5.1
Provides:      gem(rsvg2) = 3.5.1

%description   -n gem-rsvg2
Ruby/RSVG2 is a Ruby binding of librsvg based on GObject-Introspection.


%package       -n gem-rsvg2-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/RSVG2 is a Ruby binding of librsvg based on GObject-Introspection documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rsvg2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rsvg2) = 3.5.1

%description   -n gem-rsvg2-doc
Ruby/RSVG2 is a Ruby binding of librsvg based on GObject-Introspection
documentation files.

%description   -n gem-rsvg2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rsvg2.


%package       -n gem-rsvg2-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/RSVG2 is a Ruby binding of librsvg based on GObject-Introspection development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rsvg2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rsvg2) = 3.5.1

%description   -n gem-rsvg2-devel
Ruby/RSVG2 is a Ruby binding of librsvg based on GObject-Introspection
development package.

%description   -n gem-rsvg2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rsvg2.


%package       -n gem-gio2
Version:       3.5.1
Release:       alt1
Summary:       Ruby/Graphic InterfaceO2 is a Ruby binding of gio-2.0.x
Group:         Development/Ruby

Requires:      gem(fiddle) >= 0
Requires:      gem(gobject-introspection) = 3.5.1
Provides:      gem(gio2) = 3.5.1

%description   -n gem-gio2
Ruby/Graphic InterfaceO2 is a Ruby binding of gio-2.0.x.


%package       -n gem-gio2-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/Graphic InterfaceO2 is a Ruby binding of gio-2.0.x documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gio2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gio2) = 3.5.1

%description   -n gem-gio2-doc
Ruby/Graphic InterfaceO2 is a Ruby binding of gio-2.0.x documentation
files.

%description   -n gem-gio2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gio2.


%package       -n gem-gio2-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/Graphic InterfaceO2 is a Ruby binding of gio-2.0.x development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gio2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gio2) = 3.5.1

%description   -n gem-gio2-devel
Ruby/Graphic InterfaceO2 is a Ruby binding of gio-2.0.x development
package.

%description   -n gem-gio2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gio2.


%package       -n gem-wnck3
Version:       3.5.1
Release:       alt1
Summary:       Executable file for wnck3 gem
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gtk3) = 3.5.1
Provides:      gem(wnck3) = 3.5.1

%description   -n gem-wnck3
Executable file for wnck3 gem.


%package       -n gem-wnck3-doc
Version:       3.5.1
Release:       alt1
Summary:       Executable file for wnck3 gem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета wnck3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(wnck3) = 3.5.1

%description   -n gem-wnck3-doc
Executable file for wnck3 gem documentation files.

%description   -n gem-wnck3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета wnck3.


%package       -n gem-wnck3-devel
Version:       3.5.1
Release:       alt1
Summary:       Executable file for wnck3 gem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета wnck3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(wnck3) = 3.5.1

%description   -n gem-wnck3-devel
Executable file for wnck3 gem development package.

%description   -n gem-wnck3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета wnck3.


%package       -n gem-gnumeric
Version:       3.5.1
Release:       alt1
Summary:       Ruby/Gnumeric is a Ruby binding of Gnumeric
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(goffice) = 3.5.1
Provides:      gem(gnumeric) = 3.5.1

%description   -n gem-gnumeric
Ruby/Gnumeric is a Ruby binding of Gnumeric.


%package       -n gem-gnumeric-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/Gnumeric is a Ruby binding of Gnumeric documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gnumeric
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gnumeric) = 3.5.1

%description   -n gem-gnumeric-doc
Ruby/Gnumeric is a Ruby binding of Gnumeric documentation files.

%description   -n gem-gnumeric-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gnumeric.


%package       -n gem-gnumeric-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/Gnumeric is a Ruby binding of Gnumeric development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gnumeric
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gnumeric) = 3.5.1

%description   -n gem-gnumeric-devel
Ruby/Gnumeric is a Ruby binding of Gnumeric development package.

%description   -n gem-gnumeric-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gnumeric.


%package       -n gem-gtk3
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GTK3 is a Ruby binding of GTK+ 3
Group:         Development/Ruby

Requires:      gem(gio2) = 3.5.1
Requires:      gem(atk) = 3.5.1
Requires:      gem(pango) = 3.5.1
Requires:      gem(gdk_pixbuf2) = 3.5.1
Requires:      gem(gdk3) = 3.5.1
Provides:      gem(gtk3) = 3.5.1

%description   -n gem-gtk3
Ruby/GTK3 is a Ruby binding of GTK+ 3.


%package       -n gem-gtk3-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GTK3 is a Ruby binding of GTK+ 3 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gtk3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gtk3) = 3.5.1

%description   -n gem-gtk3-doc
Ruby/GTK3 is a Ruby binding of GTK+ 3 documentation files.

%description   -n gem-gtk3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gtk3.


%package       -n gem-gtk3-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GTK3 is a Ruby binding of GTK+ 3 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gtk3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gtk3) = 3.5.1

%description   -n gem-gtk3-devel
Ruby/GTK3 is a Ruby binding of GTK+ 3 development package.

%description   -n gem-gtk3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gtk3.


%package       -n gem-goffice
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GOffice is a Ruby binding of GOffice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gsf) = 3.5.1
Requires:      gem(gtk3) = 3.5.1
Provides:      gem(goffice) = 3.5.1

%description   -n gem-goffice
Ruby/GOffice is a Ruby binding of GOffice.


%package       -n gem-goffice-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GOffice is a Ruby binding of GOffice documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета goffice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(goffice) = 3.5.1

%description   -n gem-goffice-doc
Ruby/GOffice is a Ruby binding of GOffice documentation files.

%description   -n gem-goffice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета goffice.


%package       -n gem-goffice-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GOffice is a Ruby binding of GOffice development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета goffice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(goffice) = 3.5.1

%description   -n gem-goffice-devel
Ruby/GOffice is a Ruby binding of GOffice development package.

%description   -n gem-goffice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета goffice.


%package       -n gem-vte3
Version:       3.5.1
Release:       alt1
Summary:       Ruby/VTE3 is a Ruby binding of VTE for use with GTK3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gtk3) = 3.5.1
Provides:      gem(vte3) = 3.5.1

%description   -n gem-vte3
Ruby/VTE3 is a Ruby binding of VTE for use with GTK3.


%package       -n gem-vte3-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/VTE3 is a Ruby binding of VTE for use with GTK3 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vte3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vte3) = 3.5.1

%description   -n gem-vte3-doc
Ruby/VTE3 is a Ruby binding of VTE for use with GTK3 documentation
files.

%description   -n gem-vte3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vte3.


%package       -n gem-vte3-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/VTE3 is a Ruby binding of VTE for use with GTK3 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vte3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vte3) = 3.5.1

%description   -n gem-vte3-devel
Ruby/VTE3 is a Ruby binding of VTE for use with GTK3 development
package.

%description   -n gem-vte3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vte3.


%package       -n gem-clutter-gdk
Version:       3.5.1
Release:       alt1
Summary:       Ruby/ClutterGDK is a Ruby binding of GDK specific API of Clutter
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(clutter) = 3.5.1
Requires:      gem(gdk3) = 3.5.1
Provides:      gem(clutter-gdk) = 3.5.1

%description   -n gem-clutter-gdk
Ruby/ClutterGDK is a Ruby binding of GDK specific API of Clutter.


%package       -n gem-clutter-gdk-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/ClutterGDK is a Ruby binding of GDK specific API of Clutter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета clutter-gdk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(clutter-gdk) = 3.5.1

%description   -n gem-clutter-gdk-doc
Ruby/ClutterGDK is a Ruby binding of GDK specific API of Clutter documentation
files.

%description   -n gem-clutter-gdk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета clutter-gdk.


%package       -n gem-clutter-gdk-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/ClutterGDK is a Ruby binding of GDK specific API of Clutter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета clutter-gdk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(clutter-gdk) = 3.5.1

%description   -n gem-clutter-gdk-devel
Ruby/ClutterGDK is a Ruby binding of GDK specific API of Clutter development
package.

%description   -n gem-clutter-gdk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета clutter-gdk.


%package       -n gem-gtksourceview4
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GtkSourceView4 is a Ruby binding of gtksourceview-4.x
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gtk3) = 3.5.1
Provides:      gem(gtksourceview4) = 3.5.1

%description   -n gem-gtksourceview4
Ruby/GtkSourceView4 is a Ruby binding of gtksourceview-4.x.


%package       -n gem-gtksourceview4-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GtkSourceView4 is a Ruby binding of gtksourceview-4.x documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gtksourceview4
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gtksourceview4) = 3.5.1

%description   -n gem-gtksourceview4-doc
Ruby/GtkSourceView4 is a Ruby binding of gtksourceview-4.x documentation
files.

%description   -n gem-gtksourceview4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gtksourceview4.


%package       -n gem-gtksourceview4-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GtkSourceView4 is a Ruby binding of gtksourceview-4.x development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gtksourceview4
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gtksourceview4) = 3.5.1

%description   -n gem-gtksourceview4-devel
Ruby/GtkSourceView4 is a Ruby binding of gtksourceview-4.x development
package.

%description   -n gem-gtksourceview4-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gtksourceview4.


%package       -n gem-poppler
Version:       3.5.1
Release:       alt1
Summary:       Ruby/Poppler is a Ruby binding of poppler-glib
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cairo-gobject) = 3.5.1
Requires:      gem(gio2) = 3.5.1
Provides:      gem(poppler) = 3.5.1

%description   -n gem-poppler
Ruby/Poppler is a Ruby binding of poppler-glib.


%package       -n gem-poppler-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/Poppler is a Ruby binding of poppler-glib documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета poppler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(poppler) = 3.5.1

%description   -n gem-poppler-doc
Ruby/Poppler is a Ruby binding of poppler-glib documentation files.

%description   -n gem-poppler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета poppler.


%package       -n gem-poppler-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/Poppler is a Ruby binding of poppler-glib development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета poppler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(poppler) = 3.5.1

%description   -n gem-poppler-devel
Ruby/Poppler is a Ruby binding of poppler-glib development package.

%description   -n gem-poppler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета poppler.


%package       -n gem-gdk-pixbuf2
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gio2) = 3.5.1
Provides:      gem(gdk_pixbuf2) = 3.5.1

%description   -n gem-gdk-pixbuf2
Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x.


%package       -n gem-gdk-pixbuf2-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gdk_pixbuf2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gdk_pixbuf2) = 3.5.1

%description   -n gem-gdk-pixbuf2-doc
Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x documentation
files.

%description   -n gem-gdk-pixbuf2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gdk_pixbuf2.


%package       -n gem-gdk-pixbuf2-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gdk_pixbuf2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gdk_pixbuf2) = 3.5.1

%description   -n gem-gdk-pixbuf2-devel
Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x development
package.

%description   -n gem-gdk-pixbuf2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gdk_pixbuf2.


%package       -n gem-gstreamer
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GStreamer is a Ruby binding for GStreamer
Group:         Development/Ruby

Requires:      gem(gobject-introspection) = 3.5.1
Provides:      gem(gstreamer) = 3.5.1

%description   -n gem-gstreamer
Ruby/GStreamer is a Ruby binding for GStreamer.


%package       -n gem-gstreamer-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GStreamer is a Ruby binding for GStreamer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gstreamer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gstreamer) = 3.5.1

%description   -n gem-gstreamer-doc
Ruby/GStreamer is a Ruby binding for GStreamer documentation files.

%description   -n gem-gstreamer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gstreamer.


%package       -n gem-gstreamer-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GStreamer is a Ruby binding for GStreamer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gstreamer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gstreamer) = 3.5.1

%description   -n gem-gstreamer-devel
Ruby/GStreamer is a Ruby binding for GStreamer development package.

%description   -n gem-gstreamer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gstreamer.


%package       -n gem-webkit-gtk
Version:       3.5.1
Release:       alt1
Summary:       Ruby/WebKitGTK is a Ruby binding of WebKitGTK+
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gtk3) = 3.5.1
Provides:      gem(webkit-gtk) = 3.5.1

%description   -n gem-webkit-gtk
Ruby/WebKitGTK is a Ruby binding of WebKitGTK+.


%package       -n gem-webkit-gtk-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/WebKitGTK is a Ruby binding of WebKitGTK+ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета webkit-gtk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(webkit-gtk) = 3.5.1

%description   -n gem-webkit-gtk-doc
Ruby/WebKitGTK is a Ruby binding of WebKitGTK+ documentation files.

%description   -n gem-webkit-gtk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета webkit-gtk.


%package       -n gem-webkit-gtk-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/WebKitGTK is a Ruby binding of WebKitGTK+ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета webkit-gtk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(webkit-gtk) = 3.5.1

%description   -n gem-webkit-gtk-devel
Ruby/WebKitGTK is a Ruby binding of WebKitGTK+ development package.

%description   -n gem-webkit-gtk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета webkit-gtk.


%package       -n gem-webkit2-gtk
Version:       3.5.1
Release:       alt1
Summary:       Ruby/WebKit2GTK is a Ruby binding of WebKit2GTK+
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gtk3) = 3.5.1
Provides:      gem(webkit2-gtk) = 3.5.1

%description   -n gem-webkit2-gtk
Ruby/WebKit2GTK is a Ruby binding of WebKit2GTK+.


%package       -n gem-webkit2-gtk-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/WebKit2GTK is a Ruby binding of WebKit2GTK+ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета webkit2-gtk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(webkit2-gtk) = 3.5.1

%description   -n gem-webkit2-gtk-doc
Ruby/WebKit2GTK is a Ruby binding of WebKit2GTK+ documentation files.

%description   -n gem-webkit2-gtk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета webkit2-gtk.


%package       -n gem-webkit2-gtk-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/WebKit2GTK is a Ruby binding of WebKit2GTK+ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета webkit2-gtk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(webkit2-gtk) = 3.5.1
Requires:      gem(webrick) >= 0

%description   -n gem-webkit2-gtk-devel
Ruby/WebKit2GTK is a Ruby binding of WebKit2GTK+ development package.

%description   -n gem-webkit2-gtk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета webkit2-gtk.


%package       -n gem-libsecret
Version:       3.5.1
Release:       alt1
Summary:       Executable file for libsecret gem
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gobject-introspection) = 3.5.1
Provides:      gem(libsecret) = 3.5.1

%description   -n gem-libsecret
Executable file for libsecret gem.


%package       -n gem-libsecret-doc
Version:       3.5.1
Release:       alt1
Summary:       Executable file for libsecret gem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета libsecret
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(libsecret) = 3.5.1

%description   -n gem-libsecret-doc
Executable file for libsecret gem documentation files.

%description   -n gem-libsecret-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета libsecret.


%package       -n gem-libsecret-devel
Version:       3.5.1
Release:       alt1
Summary:       Executable file for libsecret gem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета libsecret
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(libsecret) = 3.5.1

%description   -n gem-libsecret-devel
Executable file for libsecret gem development package.

%description   -n gem-libsecret-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета libsecret.


%package       -n gem-atk
Version:       3.5.1
Release:       alt1
Summary:       Ruby/ATK is a Ruby binding of ATK-1.12.x or later based on GObject-Introspection
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(glib2) = 3.5.1
Provides:      gem(atk) = 3.5.1

%description   -n gem-atk
Ruby/ATK is a Ruby binding of ATK-1.12.x or later based on GObject-Introspection.


%package       -n gem-atk-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/ATK is a Ruby binding of ATK-1.12.x or later based on GObject-Introspection documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета atk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(atk) = 3.5.1

%description   -n gem-atk-doc
Ruby/ATK is a Ruby binding of ATK-1.12.x or later based on GObject-Introspection
documentation files.

%description   -n gem-atk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета atk.


%package       -n gem-atk-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/ATK is a Ruby binding of ATK-1.12.x or later based on GObject-Introspection development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета atk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(atk) = 3.5.1

%description   -n gem-atk-devel
Ruby/ATK is a Ruby binding of ATK-1.12.x or later based on GObject-Introspection
development package.

%description   -n gem-atk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета atk.


%package       -n gem-gtk4
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GTK4 is a Ruby binding of GTK+ 4
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gio2) = 3.5.1
Requires:      gem(atk) = 3.5.1
Requires:      gem(pango) = 3.5.1
Requires:      gem(gdk_pixbuf2) = 3.5.1
Requires:      gem(gdk4) = 3.5.1
Provides:      gem(gtk4) = 3.5.1

%description   -n gem-gtk4
Ruby/GTK4 is a Ruby binding of GTK+ 4.


%package       -n gem-gtk4-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GTK4 is a Ruby binding of GTK+ 4 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gtk4
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gtk4) = 3.5.1

%description   -n gem-gtk4-doc
Ruby/GTK4 is a Ruby binding of GTK+ 4 documentation files.

%description   -n gem-gtk4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gtk4.


%package       -n gem-gtk4-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GTK4 is a Ruby binding of GTK+ 4 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gtk4
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gtk4) = 3.5.1

%description   -n gem-gtk4-devel
Ruby/GTK4 is a Ruby binding of GTK+ 4 development package.

%description   -n gem-gtk4-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gtk4.


%package       -n gem-pango
Version:       3.5.1
Release:       alt1
Summary:       Ruby/Pango is a Ruby binding of pango based on GObject-Introspection
Group:         Development/Ruby

Requires:      gem(cairo-gobject) = 3.5.1
Requires:      gem(gobject-introspection) = 3.5.1
Provides:      gem(pango) = 3.5.1

%description   -n gem-pango
Ruby/Pango is a Ruby binding of pango based on GObject-Introspection.


%package       -n gem-pango-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/Pango is a Ruby binding of pango based on GObject-Introspection documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pango
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pango) = 3.5.1

%description   -n gem-pango-doc
Ruby/Pango is a Ruby binding of pango based on GObject-Introspection
documentation files.

%description   -n gem-pango-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pango.


%package       -n gem-pango-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/Pango is a Ruby binding of pango based on GObject-Introspection development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pango
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pango) = 3.5.1

%description   -n gem-pango-devel
Ruby/Pango is a Ruby binding of pango based on GObject-Introspection development
package.

%description   -n gem-pango-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pango.


%package       -n gem-clutter-gtk
Version:       3.5.1
Release:       alt1
Summary:       Ruby/ClutterGTK is a Ruby binding of Clutter-GTK
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(clutter) = 3.5.1
Requires:      gem(clutter-gdk) = 3.5.1
Requires:      gem(gtk3) = 3.5.1
Provides:      gem(clutter-gtk) = 3.5.1

%description   -n gem-clutter-gtk
Ruby/ClutterGTK is a Ruby binding of Clutter-GTK.


%package       -n gem-clutter-gtk-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/ClutterGTK is a Ruby binding of Clutter-GTK documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета clutter-gtk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(clutter-gtk) = 3.5.1

%description   -n gem-clutter-gtk-doc
Ruby/ClutterGTK is a Ruby binding of Clutter-GTK documentation files.

%description   -n gem-clutter-gtk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета clutter-gtk.


%package       -n gem-clutter-gtk-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/ClutterGTK is a Ruby binding of Clutter-GTK development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета clutter-gtk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(clutter-gtk) = 3.5.1

%description   -n gem-clutter-gtk-devel
Ruby/ClutterGTK is a Ruby binding of Clutter-GTK development package.

%description   -n gem-clutter-gtk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета clutter-gtk.


%package       -n gem-clutter-gstreamer
Version:       3.5.1
Release:       alt1
Summary:       Ruby/ClutterGStreamer is a Ruby binding of Clutter-GStreamer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gdk_pixbuf2) = 3.5.1
Requires:      gem(clutter) = 3.5.1
Requires:      gem(gstreamer) = 3.5.1
Provides:      gem(clutter-gstreamer) = 3.5.1

%description   -n gem-clutter-gstreamer
Ruby/ClutterGStreamer is a Ruby binding of Clutter-GStreamer.


%package       -n gem-clutter-gstreamer-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/ClutterGStreamer is a Ruby binding of Clutter-GStreamer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета clutter-gstreamer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(clutter-gstreamer) = 3.5.1

%description   -n gem-clutter-gstreamer-doc
Ruby/ClutterGStreamer is a Ruby binding of Clutter-GStreamer documentation
files.

%description   -n gem-clutter-gstreamer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета clutter-gstreamer.


%package       -n gem-clutter-gstreamer-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/ClutterGStreamer is a Ruby binding of Clutter-GStreamer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета clutter-gstreamer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(clutter-gstreamer) = 3.5.1

%description   -n gem-clutter-gstreamer-devel
Ruby/ClutterGStreamer is a Ruby binding of Clutter-GStreamer development
package.

%description   -n gem-clutter-gstreamer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета clutter-gstreamer.


%package       -n gem-gsf
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GSF is a Ruby binding of GSF which is needed by GOffice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gio2) = 3.5.1
Provides:      gem(gsf) = 3.5.1

%description   -n gem-gsf
Ruby/GSF is a Ruby binding of GSF which is needed by GOffice.


%package       -n gem-gsf-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GSF is a Ruby binding of GSF which is needed by GOffice documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gsf
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gsf) = 3.5.1

%description   -n gem-gsf-doc
Ruby/GSF is a Ruby binding of GSF which is needed by GOffice documentation
files.

%description   -n gem-gsf-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gsf.


%package       -n gem-gsf-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GSF is a Ruby binding of GSF which is needed by GOffice development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gsf
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gsf) = 3.5.1

%description   -n gem-gsf-devel
Ruby/GSF is a Ruby binding of GSF which is needed by GOffice development
package.

%description   -n gem-gsf-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gsf.


%package       -n gem-gdk3
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GDK3 is a Ruby binding of GDK 3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pango) = 3.5.1
Requires:      gem(gdk_pixbuf2) = 3.5.1
Requires:      gem(cairo-gobject) = 3.5.1
Provides:      gem(gdk3) = 3.5.1

%description   -n gem-gdk3
Ruby/GDK3 is a Ruby binding of GDK 3.


%package       -n gem-gdk3-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GDK3 is a Ruby binding of GDK 3 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gdk3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gdk3) = 3.5.1

%description   -n gem-gdk3-doc
Ruby/GDK3 is a Ruby binding of GDK 3 documentation files.

%description   -n gem-gdk3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gdk3.


%package       -n gem-gdk3-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GDK3 is a Ruby binding of GDK 3 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gdk3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gdk3) = 3.5.1

%description   -n gem-gdk3-devel
Ruby/GDK3 is a Ruby binding of GDK 3 development package.

%description   -n gem-gdk3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gdk3.


%package       -n gem-gvlc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/VLC is a Ruby binding of libVLC for Ruby/GTK
Group:         Development/Ruby

Requires:      gem(glib2) = 3.5.1
Provides:      gem(gvlc) = 3.5.1

%description   -n gem-gvlc
Ruby/VLC is a Ruby binding of libVLC for Ruby/GTK.


%package       -n gem-gvlc-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/VLC is a Ruby binding of libVLC for Ruby/GTK documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gvlc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gvlc) = 3.5.1

%description   -n gem-gvlc-doc
Ruby/VLC is a Ruby binding of libVLC for Ruby/GTK documentation
files.

%description   -n gem-gvlc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gvlc.


%package       -n gem-gvlc-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/VLC is a Ruby binding of libVLC for Ruby/GTK development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gvlc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gvlc) = 3.5.1

%description   -n gem-gvlc-devel
Ruby/VLC is a Ruby binding of libVLC for Ruby/GTK development
package.

%description   -n gem-gvlc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gvlc.


%package       -n gem-glib2
Version:       3.5.1
Release:       alt1
Summary:       GLib 2 bindings for the Ruby language
Group:         Development/Ruby

Requires:      gem(pkg-config) >= 1.3.5
Requires:      gem(native-package-installer) >= 1.0.3
Obsoletes:     ruby-glib2
Provides:      ruby-glib2
Provides:      gem(glib2) = 3.5.1

%description   -n gem-glib2
GLib is a useful general-purpose C library, notably used by GTK+ and GNOME. This
package contains libraries for using GLib 2 with the Ruby programming language.
It is most likely useful in conjunction with Ruby bindings for other libraries
such as GTK+.


%package       -n gem-glib2-doc
Version:       3.5.1
Release:       alt1
Summary:       GLib 2 bindings for the Ruby language documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета glib2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(glib2) = 3.5.1
Obsoletes:     ruby-glib2-doc
Provides:      ruby-glib2-doc

%description   -n gem-glib2-doc
GLib 2 bindings for the Ruby language documentation files.

GLib is a useful general-purpose C library, notably used by GTK+ and GNOME. This
package contains libraries for using GLib 2 with the Ruby programming language.
It is most likely useful in conjunction with Ruby bindings for other libraries
such as GTK+.

%description   -n gem-glib2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета glib2.


%package       -n gem-glib2-devel
Version:       3.5.1
Release:       alt1
Summary:       GLib 2 bindings for the Ruby language development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета glib2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(glib2) = 3.5.1
Requires:      gem(test-unit) >= 2
Obsoletes:     ruby-gnome2-devel
Provides:      ruby-gnome2-devel

%description   -n gem-glib2-devel
GLib 2 bindings for the Ruby language development package.

GLib is a useful general-purpose C library, notably used by GTK+ and GNOME. This
package contains libraries for using GLib 2 with the Ruby programming language.
It is most likely useful in conjunction with Ruby bindings for other libraries
such as GTK+.

%description   -n gem-glib2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета glib2.


%package       -n gem-gtksourceview3
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GtkSourceView3 is a Ruby binding of gtksourceview-3.x
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gtk3) = 3.5.1
Provides:      gem(gtksourceview3) = 3.5.1

%description   -n gem-gtksourceview3
Ruby/GtkSourceView3 is a Ruby binding of gtksourceview-3.x.


%package       -n gem-gtksourceview3-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GtkSourceView3 is a Ruby binding of gtksourceview-3.x documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gtksourceview3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gtksourceview3) = 3.5.1

%description   -n gem-gtksourceview3-doc
Ruby/GtkSourceView3 is a Ruby binding of gtksourceview-3.x documentation
files.

%description   -n gem-gtksourceview3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gtksourceview3.


%package       -n gem-gtksourceview3-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/GtkSourceView3 is a Ruby binding of gtksourceview-3.x development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gtksourceview3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gtksourceview3) = 3.5.1

%description   -n gem-gtksourceview3-devel
Ruby/GtkSourceView3 is a Ruby binding of gtksourceview-3.x development
package.

%description   -n gem-gtksourceview3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gtksourceview3.


%package       -n gem-clutter
Version:       3.5.1
Release:       alt1
Summary:       Ruby/Clutter is a Ruby binding of Clutter
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cairo-gobject) = 3.5.1
Requires:      gem(gobject-introspection) = 3.5.1
Requires:      gem(pango) = 3.5.1
Provides:      gem(clutter) = 3.5.1

%description   -n gem-clutter
Ruby/Clutter is a Ruby binding of Clutter.


%package       -n gem-clutter-doc
Version:       3.5.1
Release:       alt1
Summary:       Ruby/Clutter is a Ruby binding of Clutter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета clutter
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(clutter) = 3.5.1

%description   -n gem-clutter-doc
Ruby/Clutter is a Ruby binding of Clutter documentation files.

%description   -n gem-clutter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета clutter.


%package       -n gem-clutter-devel
Version:       3.5.1
Release:       alt1
Summary:       Ruby/Clutter is a Ruby binding of Clutter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета clutter
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(clutter) = 3.5.1

%description   -n gem-clutter-devel
Ruby/Clutter is a Ruby binding of Clutter development package.

%description   -n gem-clutter-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета clutter.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files

%files         -n gem-gegl
%doc README.md
%ruby_gemspecdir/gegl-3.5.1.gemspec
%ruby_gemslibdir/gegl-3.5.1

%files         -n gem-gegl-doc
%doc README.md
%ruby_gemsdocdir/gegl-3.5.1

%files         -n gem-gegl-devel
%doc README.md

%files         -n gem-gobject-introspection
%doc README.md
%ruby_gemspecdir/gobject-introspection-3.5.1.gemspec
%ruby_gemslibdir/gobject-introspection-3.5.1
%ruby_gemsextdir/gobject-introspection-3.5.1

%files         -n gem-gobject-introspection-doc
%doc README.md
%ruby_gemsdocdir/gobject-introspection-3.5.1

%files         -n gem-gobject-introspection-devel
%doc README.md
%ruby_includedir/gobject-introspection/*

%files         -n gem-gdk4
%doc README.md
%ruby_gemspecdir/gdk4-3.5.1.gemspec
%ruby_gemslibdir/gdk4-3.5.1

%files         -n gem-gdk4-doc
%doc README.md
%ruby_gemsdocdir/gdk4-3.5.1

%files         -n gem-gdk4-devel
%doc README.md

%files         -n gem-cairo-gobject
%doc README.md
%ruby_gemspecdir/cairo-gobject-3.5.1.gemspec
%ruby_gemslibdir/cairo-gobject-3.5.1
%ruby_gemsextdir/cairo-gobject-3.5.1

%files         -n gem-cairo-gobject-doc
%doc README.md
%ruby_gemsdocdir/cairo-gobject-3.5.1

%files         -n gem-cairo-gobject-devel
%doc README.md
%ruby_includedir/cairo-gobject/*

%files         -n gem-rsvg2
%doc README.md
%ruby_gemspecdir/rsvg2-3.5.1.gemspec
%ruby_gemslibdir/rsvg2-3.5.1

%files         -n gem-rsvg2-doc
%doc README.md
%ruby_gemsdocdir/rsvg2-3.5.1

%files         -n gem-rsvg2-devel
%doc README.md

%files         -n gem-gio2
%doc README.md
%ruby_gemspecdir/gio2-3.5.1.gemspec
%ruby_gemslibdir/gio2-3.5.1
%ruby_gemsextdir/gio2-3.5.1

%files         -n gem-gio2-doc
%doc README.md
%ruby_gemsdocdir/gio2-3.5.1

%files         -n gem-gio2-devel
%doc README.md
%ruby_includedir/gio2/*

%files         -n gem-wnck3
%doc README.md
%ruby_gemspecdir/wnck3-3.5.1.gemspec
%ruby_gemslibdir/wnck3-3.5.1

%files         -n gem-wnck3-doc
%doc README.md
%ruby_gemsdocdir/wnck3-3.5.1

%files         -n gem-wnck3-devel
%doc README.md

%files         -n gem-gnumeric
%doc README.md
%ruby_gemspecdir/gnumeric-3.5.1.gemspec
%ruby_gemslibdir/gnumeric-3.5.1

%files         -n gem-gnumeric-doc
%doc README.md
%ruby_gemsdocdir/gnumeric-3.5.1

%files         -n gem-gnumeric-devel
%doc README.md

%files         -n gem-gtk3
%doc README.md
%ruby_gemspecdir/gtk3-3.5.1.gemspec
%ruby_gemslibdir/gtk3-3.5.1
%ruby_gemsextdir/gtk3-3.5.1

%files         -n gem-gtk3-doc
%doc README.md
%ruby_gemsdocdir/gtk3-3.5.1

%files         -n gem-gtk3-devel
%doc README.md
%ruby_includedir/gtk3/*

%files         -n gem-goffice
%doc README.md
%ruby_gemspecdir/goffice-3.5.1.gemspec
%ruby_gemslibdir/goffice-3.5.1

%files         -n gem-goffice-doc
%doc README.md
%ruby_gemsdocdir/goffice-3.5.1

%files         -n gem-goffice-devel
%doc README.md

%files         -n gem-vte3
%doc README.md
%ruby_gemspecdir/vte3-3.5.1.gemspec
%ruby_gemslibdir/vte3-3.5.1

%files         -n gem-vte3-doc
%doc README.md
%ruby_gemsdocdir/vte3-3.5.1

%files         -n gem-vte3-devel
%doc README.md

%files         -n gem-clutter-gdk
%doc README.md
%ruby_gemspecdir/clutter-gdk-3.5.1.gemspec
%ruby_gemslibdir/clutter-gdk-3.5.1

%files         -n gem-clutter-gdk-doc
%doc README.md
%ruby_gemsdocdir/clutter-gdk-3.5.1

%files         -n gem-clutter-gdk-devel
%doc README.md

%files         -n gem-gtksourceview4
%doc README.md
%ruby_gemspecdir/gtksourceview4-3.5.1.gemspec
%ruby_gemslibdir/gtksourceview4-3.5.1

%files         -n gem-gtksourceview4-doc
%doc README.md
%ruby_gemsdocdir/gtksourceview4-3.5.1

%files         -n gem-gtksourceview4-devel
%doc README.md

%files         -n gem-poppler
%doc README.md
%ruby_gemspecdir/poppler-3.5.1.gemspec
%ruby_gemslibdir/poppler-3.5.1

%files         -n gem-poppler-doc
%doc README.md
%ruby_gemsdocdir/poppler-3.5.1

%files         -n gem-poppler-devel
%doc README.md

%files         -n gem-gdk-pixbuf2
%doc README.md
%ruby_gemspecdir/gdk_pixbuf2-3.5.1.gemspec
%ruby_gemslibdir/gdk_pixbuf2-3.5.1

%files         -n gem-gdk-pixbuf2-doc
%doc README.md
%ruby_gemsdocdir/gdk_pixbuf2-3.5.1

%files         -n gem-gdk-pixbuf2-devel
%doc README.md

%files         -n gem-gstreamer
%doc README.md
%ruby_gemspecdir/gstreamer-3.5.1.gemspec
%ruby_gemslibdir/gstreamer-3.5.1
%ruby_gemsextdir/gstreamer-3.5.1

%files         -n gem-gstreamer-doc
%doc README.md
%ruby_gemsdocdir/gstreamer-3.5.1

%files         -n gem-gstreamer-devel
%doc README.md
%ruby_includedir/gstreamer/*

%files         -n gem-webkit-gtk
%doc README.md
%ruby_gemspecdir/webkit-gtk-3.5.1.gemspec
%ruby_gemslibdir/webkit-gtk-3.5.1

%files         -n gem-webkit-gtk-doc
%doc README.md
%ruby_gemsdocdir/webkit-gtk-3.5.1

%files         -n gem-webkit-gtk-devel
%doc README.md

%files         -n gem-webkit2-gtk
%doc README.md
%ruby_gemspecdir/webkit2-gtk-3.5.1.gemspec
%ruby_gemslibdir/webkit2-gtk-3.5.1

%files         -n gem-webkit2-gtk-doc
%doc README.md
%ruby_gemsdocdir/webkit2-gtk-3.5.1

%files         -n gem-webkit2-gtk-devel
%doc README.md

%files         -n gem-libsecret
%doc README.md
%ruby_gemspecdir/libsecret-3.5.1.gemspec
%ruby_gemslibdir/libsecret-3.5.1

%files         -n gem-libsecret-doc
%doc README.md
%ruby_gemsdocdir/libsecret-3.5.1

%files         -n gem-libsecret-devel
%doc README.md

%files         -n gem-atk
%doc README.md
%ruby_gemspecdir/atk-3.5.1.gemspec
%ruby_gemslibdir/atk-3.5.1

%files         -n gem-atk-doc
%doc README.md
%ruby_gemsdocdir/atk-3.5.1

%files         -n gem-atk-devel
%ruby_includedir/atk/*
%doc README.md

%files         -n gem-gtk4
%doc README.md
%ruby_gemspecdir/gtk4-3.5.1.gemspec
%ruby_gemslibdir/gtk4-3.5.1

%files         -n gem-gtk4-doc
%doc README.md
%ruby_gemsdocdir/gtk4-3.5.1

%files         -n gem-gtk4-devel
%doc README.md

%files         -n gem-pango
%doc README.md
%ruby_gemspecdir/pango-3.5.1.gemspec
%ruby_gemslibdir/pango-3.5.1
%ruby_gemsextdir/pango-3.5.1

%files         -n gem-pango-doc
%doc README.md
%ruby_gemsdocdir/pango-3.5.1

%files         -n gem-pango-devel
%doc README.md
%ruby_includedir/pango/*

%files         -n gem-clutter-gtk
%doc README.md
%ruby_gemspecdir/clutter-gtk-3.5.1.gemspec
%ruby_gemslibdir/clutter-gtk-3.5.1

%files         -n gem-clutter-gtk-doc
%doc README.md
%ruby_gemsdocdir/clutter-gtk-3.5.1

%files         -n gem-clutter-gtk-devel
%doc README.md

%files         -n gem-clutter-gstreamer
%doc README.md
%ruby_gemspecdir/clutter-gstreamer-3.5.1.gemspec
%ruby_gemslibdir/clutter-gstreamer-3.5.1

%files         -n gem-clutter-gstreamer-doc
%doc README.md
%ruby_gemsdocdir/clutter-gstreamer-3.5.1

%files         -n gem-clutter-gstreamer-devel
%doc README.md

%files         -n gem-gsf
%doc README.md
%ruby_gemspecdir/gsf-3.5.1.gemspec
%ruby_gemslibdir/gsf-3.5.1

%files         -n gem-gsf-doc
%doc README.md
%ruby_gemsdocdir/gsf-3.5.1

%files         -n gem-gsf-devel
%doc README.md

%files         -n gem-gdk3
%doc README.md
%ruby_gemspecdir/gdk3-3.5.1.gemspec
%ruby_gemslibdir/gdk3-3.5.1

%files         -n gem-gdk3-doc
%doc README.md
%ruby_gemsdocdir/gdk3-3.5.1

%files         -n gem-gdk3-devel
%doc README.md

%files         -n gem-gvlc
%doc README.md
%ruby_gemspecdir/gvlc-3.5.1.gemspec
%ruby_gemslibdir/gvlc-3.5.1
%ruby_gemsextdir/gvlc-3.5.1

%files         -n gem-gvlc-doc
%doc README.md
%ruby_gemsdocdir/gvlc-3.5.1

%files         -n gem-gvlc-devel
%doc README.md
%ruby_includedir/gvlc/*

%files         -n gem-glib2
%doc README.md
%ruby_gemspecdir/glib2-3.5.1.gemspec
%ruby_gemslibdir/glib2-3.5.1
%ruby_gemsextdir/glib2-3.5.1

%files         -n gem-glib2-doc
%doc README.md
%ruby_gemsdocdir/glib2-3.5.1

%files         -n gem-glib2-devel
%doc README.md
%ruby_includedir/glib2/*

%files         -n gem-gtksourceview3
%doc README.md
%ruby_gemspecdir/gtksourceview3-3.5.1.gemspec
%ruby_gemslibdir/gtksourceview3-3.5.1

%files         -n gem-gtksourceview3-doc
%doc README.md
%ruby_gemsdocdir/gtksourceview3-3.5.1

%files         -n gem-gtksourceview3-devel
%doc README.md

%files         -n gem-clutter
%doc README.md
%ruby_gemspecdir/clutter-3.5.1.gemspec
%ruby_gemslibdir/clutter-3.5.1

%files         -n gem-clutter-doc
%doc README.md
%ruby_gemsdocdir/clutter-3.5.1

%files         -n gem-clutter-devel
%doc README.md


%changelog
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

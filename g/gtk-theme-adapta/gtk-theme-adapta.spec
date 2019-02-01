Name: gtk-theme-adapta
Summary: An adaptive Gtk+ theme based on Material Design Guidelines
Version: 3.95.0.11
Release: alt1
License: GPLv2 and CC-BY-SA

Group: Graphical desktop/GNOME
Url: https://github.com/adapta-project/adapta-gtk-theme
Packager: Leontiy Volodin <lvol@altlinux.org>

# Source-url:   https://github.com/adapta-project/adapta-gtk-theme/archive/%version.tar.gz
Source: %name-%version.tar.gz

BuildArch: noarch

BuildRequires: fdupes
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: inkscape >= 0.91
BuildRequires: parallel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: procps
BuildRequires: sassc    >= 3.3
BuildRequires: /proc

Requires: gnome-themes-extra
Requires: fonts-ttf-google-noto-sans
Requires: fonts-ttf-roboto
Requires: libgtk-engines-default

%description
%summary.

%package gedit
Summary: Gedit style addon for %name
Group: Graphical desktop/GNOME
Requires: %name == %version-%release
Requires: libgtksourceview3

%description gedit
Gedit style addon for %name.

%package plank
Summary: Plank dock theme addon for %name
Group: Graphical desktop/Other
Requires: %name == %version-%release
Requires: plank

%description plank
Plank dock theme addon for %name.

%prep
%setup

%build
NOCONFIGURE=yes ./autogen.sh --prefix=%buildroot/usr
%configure \
  --enable-gtk_next      \
  --enable-plank         \
  --enable-telegram
%make_build

%install
make install DESTDIR=%buildroot
for f in COPYING LICENSE_CC_BY_SA4 README.md; do
  %_bindir/find %buildroot -type f -name "$f" -print -delete
done

# Add the gedit styles addon to the right location.
mkdir -p %buildroot%_datadir/gtksourceview-3.0/styles
ln -s %_datadir/themes/Adapta/gedit/adapta.xml \
  %buildroot%_datadir/gtksourceview-3.0/styles/adapta.xml

# Add the plank addon to the right location.
mkdir -p %buildroot%_datadir/plank/themes/Adapta
ln -s %_datadir/themes/Adapta/plank/dock.theme \
  %buildroot%_datadir/plank/themes/Adapta/dock.theme

fdupes -s %buildroot%_datadir/themes

%files
%doc COPYING LICENSE_CC_BY_SA4
%doc README.md
%_datadir/themes/Adapta*

%files gedit
%doc extra/gedit/README.md
%_datadir/gtksourceview-3.0/styles/adapta.xml

%files plank
%_datadir/plank/themes/Adapta

%changelog
* Fri Feb 01 2019 Leontiy Volodin <lvol@altlinux.org> 3.95.0.11-alt1
- Initial build for ALT Sisyphus

Name: gtk+3-themes-incompatible
Version: 3.20
Release: alt1

Summary: metapackage to kick GTK3 themes that are known broken
License: public domain
Group: Graphical desktop/GNOME

Url: https://blogs.gnome.org/mclasen/2015/11/20/a-gtk-update/
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

# https://github.com/jpfleury/clearlooks-phenix
Conflicts: gtk3-theme-clearlooks-phenix <= 6.0.3-alt3

%description
This package should facilitate upgrades between branches
like p7 to p8 (or major distribution versions like 7.0 to 8.0)
as GTK3 theme support changes quite often and 3rd party themes
might lag behind causing all kinds of havoc onto unsuspecting
users; getting rid of those is less evil than allowing that
unfortunately.

%files

%changelog
* Wed Apr 27 2016 Michael Shigorin <mike@altlinux.org> 3.20-alt1
- initial release (see also #32028)


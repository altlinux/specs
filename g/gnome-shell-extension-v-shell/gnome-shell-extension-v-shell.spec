%global _unpackaged_files_terminate_build 1
%global uuid vertical-workspaces@G-dH.github.com
%global schema org.gnome.shell.extensions.vertical-workspaces
%global gettext_domain vertical-workspaces

Name: gnome-shell-extension-v-shell
Version: 50.8
Release: alt3
Summary: Customize the GNOME Shell overview and workspaces
License: GPL-3.0
Group: Graphical desktop/GNOME
URL: https://extensions.gnome.org/extension/5177/vertical-workspaces
VCS: https://github.com/G-dH/vertical-workspaces

Source: %name-%version.tar
Source1: ru.po

Patch: alt-fix-prefs-layout.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: libgio

%description
V-Shell is a GNOME Shell extension that customizes the overview and workspace
layout, supporting both horizontal and vertical workspaces.

%prep
%setup
%patch -p1
cp -p %SOURCE1 po/ru.po
echo ru >> po/LINGUAS

%build
%meson
%meson_build

%install
%meson_install
rm -f %buildroot%_datadir/glib-2.0/schemas/gschemas.compiled
%find_lang %gettext_domain

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid
%_datadir/glib-2.0/schemas/%schema.gschema.xml

%changelog
* Sat Aug 29 2026 Alexander Makeenkov <amakeenk@altlinux.org> 50.8-alt3
- Fixed preferences layout with long Russian labels (closes: #60307).
- Completed Russian translation (closes: #60308).

* Thu Aug 27 2026 Alexander Makeenkov <amakeenk@altlinux.org> 50.8-alt2
- Added Russian translation.

* Tue Aug 25 2026 Alexander Makeenkov <amakeenk@altlinux.org> 50.8-alt1
- Updated to version 50.8.

* Thu Aug 13 2026 Alexander Makeenkov <amakeenk@altlinux.org> 50.7-alt1
- Initial build for ALT.

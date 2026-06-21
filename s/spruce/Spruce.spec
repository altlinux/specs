%define _unpackaged_files_terminate_build 1
%define oname io.github.shonubot.Spruce

Name: spruce
Version: 0.2.1
Release: alt1

Summary: Lightweight cache cleaner and system maintenance tool
License: GPL-3.0-or-later
Group: Other

Url: https://github.com/shonubot/Spruce
Vcs: https://github.com/shonubot/Spruce

BuildArch: noarch
AutoProv: nopython3
Obsoletes: python3-module-spruce <= 0.1.6-alt1

Source: %name-%version.tar
#seted GSK_RENDERER=gl for fixed segmentation fault on XFCE
Patch: set_GSK_RENDERER.patch

Requires: python3-module-pycairo
Requires: python3-module-pygobject3
%add_python3_path %_datadir/%name

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson
BuildRequires: pkgconfig(pygobject-3.0) pkgconfig(python3)
BuildRequires: pkgconfig(gtk4) pkgconfig(pango) pkgconfig(pangocairo)
BuildRequires: pkgconfig(libadwaita-1) typelib(Adw)

%description
Spruce is a lightweight cache cleaner and system maintenance tool designed for GNU/Linux.
It helps keep your system fresh by clearing unneeded caches, logs, temporary files and
unused Flatpak runtimes in a clean, Adwaita-based GTK interface.

%prep
%setup
%patch -p0

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/%name
%_datadir/applications/%oname.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/%name
%_datadir/metainfo/%oname.metainfo.xml
%_datadir/glib-2.0/schemas/%oname.gschema.xml
%doc *.md

%changelog
* Sun Jun 21 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.2.1-alt1
- 0.2.0 -> 0.2.1

* Sun Mar 29 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.2.0-alt2
- seted GSK_RENDERER=gl for fixed segmentation fault on XFCE (ALT #58349)

* Sun Mar 22 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.2.0-alt1
- 0.1.8 -> 0.2.0

* Sat Mar 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.1.8-alt2
- added pygobject3 dependency

* Tue Feb 03 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.1.8-alt1
- 0.1.7 -> 0.1.8

* Sun Feb 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.1.7-alt1
- 0.1.6 -> 0.1.7

* Thu Jan 29 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.1.6-alt2
- updated to git.e8a4f030
- changed license tag

* Wed Dec 31 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.6-alt1
- 0.1.5 -> 0.1.6
- changed license tag

* Sun Dec 21 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.5-alt1
- 0.1.4 -> 0.1.5

* Mon Dec 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.4-alt2
- Add pycairo dependency

* Sun Dec 14 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.4-alt1
- 0.1.3 -> 0.1.4

* Wed Dec 10 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.3-alt1
- Initial build for ALT Linux.

%define oname io.github.shonubot.Spruce

Name: spruce
Version: 0.1.4
Release: alt2

Summary: Lightweight cache cleaner and system maintenance tool
License: GPL-3.0-or-later
Group: Other

Url: https://github.com/shonubot/Spruce
Vcs: https://github.com/shonubot/Spruce

BuildArch: noarch

Source: %name-%version.tar

Requires: python3-module-pycairo

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson
BuildRequires: pkgconfig(pygobject-3.0) pkgconfig(python3)
BuildRequires: pkgconfig(gtk4) pkgconfig(pango) pkgconfig(pangocairo)
BuildRequires: pkgconfig(libadwaita-1) typelib(Adw)

%description
Spruce is a lightweight cache cleaner and system maintenance tool designed for GNU/Linux.
It helps keep your system fresh by clearing unneeded caches, logs, temporary files and
unused Flatpak runtimes in a clean, Adwaita-based GTK interface.


%package -n python3-module-%name
Group:   Development/Python3
Summary: Python3 module for %name
%description -n python3-module-%name
%summary.

%prep
%setup

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
%doc *.md

%files -n python3-module-%name
%python3_sitelibdir/%name/

%changelog
* Mon Dec 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.4-alt2
- Add pycairo dependency

* Sun Dec 14 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.4-alt1
- 0.1.3 -> 0.1.4

* Wed Dec 10 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.3-alt1
- Initial build for ALT Linux.

Name: menulibre
Version: 2.2.3
Release: alt1

Summary: Advanced FreeDesktop.org compliant menu editor
License: GPL-3.0-only
Group: Graphical desktop/Other
BuildArch: noarch
Epoch: 1

URL: https://github.com/bluesabre/menulibre
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): intltool
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-distutils-extra
BuildRequires: python3-module-pyxdg python3-module-pygobject3 libgtk+3-gir-devel libgtksourceview3-gir-devel libgnome-menus-gir-devel

Requires: libgtk+3-gir libgtksourceview3-gir libgnome-menus-gir

%define _unpackaged_files_terminate_build 1

%description
MenuLibre is an advanced menu editor that provides modern features in a clean,
easy-to-use interface.
All fields specified in the FreeDesktop.org Desktop Entry and Menu
specifications are available to quickly update. Additionally, MenuLibre provides
an editor for the launcher actions used by applications such as Unity and Plank.

Features:
  * A beautiful interface powered by the latest version of GTK+;
  * Create new launchers, or modify existing ones with complete control over
    common settings and access to advanced settings;
  * Add, remove, and adjust desktop actions: powerful shortcuts available used
    by Unity, Xfce, and Pantheon;
  * Easily rearrange menu items to suit your needs.

%prep
%setup
%patch0 -p1

%build
export XDG_RUNTIME_DIR="$TMPDIR"
%python3_build

%install
install -Dm0644 build/share/applications/menulibre.desktop %buildroot%_desktopdir/%name.desktop
export LANG=C.UTF-8
export XDG_RUNTIME_DIR="$TMPDIR"
%python3_install

# Install localizations
mkdir -p %buildroot%_datadir/locale
cp -a build/mo/* %buildroot%_datadir/locale/

%find_lang %name

%files -f %name.lang
%doc %_defaultdocdir/%name
%_bindir/%{name}*
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/*.*
%_pixmapsdir/*.*
%_man1dir/%{name}*.*
%_datadir/metainfo/*.xml
%python3_sitelibdir_noarch/%{name}*

# Glibc doesn't support ms@Arab locale
%exclude %_datadir/locale/ms@Arab/LC_MESSAGES/menulibre.mo

%changelog
* Tue Jan 11 2022 Mikhail Efremov <sem@altlinux.org> 1:2.2.3-alt1
- Don't package ms@Arab translation.
- Updated summary and description.
- Don't use rpm-build-licenses.
- Minor spec cleanup.
- Updated Url tag.
- Updated to 2.2.3.

* Wed Sep 30 2020 Mikhail Efremov <sem@altlinux.org> 1:2.2.1-alt2
- Use gi.require_version for Gdk.

* Wed Oct 02 2019 Mikhail Efremov <sem@altlinux.org> 1:2.2.1-alt1
- Updated to 2.2.1.

* Wed Jun 18 2014 Mikhail Efremov <sem@altlinux.org> 1:2.0.4-alt1
- Updated to 2.0.4.

* Tue Mar 11 2014 Mikhail Efremov <sem@altlinux.org> 1:2.0.3-alt1
- Fix Xfce name (XFCE -> Xfce).
- Updated to 2.0.3.

* Mon Jul 08 2013 Mikhail Efremov <sem@altlinux.org> 13.04.17-alt1
- Updated to 13.04.17.

* Wed Apr 24 2013 Mikhail Efremov <sem@altlinux.org> 13.04.12-alt1
- Fix directory creation.
- Initial build.


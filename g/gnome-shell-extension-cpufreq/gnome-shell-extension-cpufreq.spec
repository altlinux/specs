%define ver_major 43
%define ver_minor 0
%define git 59cebf0
%define domain konkor
%define _libexecdir %_prefix/libexec
%define _name cpufreq
%define xdg_name org.gnome.shell.extensions.%_name

Name: gnome-shell-extension-cpufreq
Version: 52.0
Release: alt2.g%{git}

Summary: System Monitor and Power Manager for Gnome Shell
Group: Graphical desktop/GNOME
License: GPLv3+
Url: https://github.com/konkor/cpufreq

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: gnome-shell >= %ver_major.%ver_minor

BuildRequires(pre): gnome-common
BuildRequires: libgjs-devel libmozjs78-tools

%description
CPU Monitor and Power Manager for GNOME Shell.

%prep
%setup -n %name-%version
%patch -p1

%build
%autoreconf
%configure
%make

%install
%make DESTDIR=%buildroot install
%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/%_name-manager.desktop
%dir %_datadir/gnome-shell/extensions/cpufreq@%domain
%_datadir/gnome-shell/extensions/cpufreq@%domain/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/*/*.svg
%_pixmapsdir/%_name.svg
%dir %_datadir/fonts/truetype/%_name
%_datadir/fonts/truetype/%_name/%_name.ttf
%_datadir/polkit-1/actions/%domain.%_name.policy

%doc LICENSE README.md

%changelog
* Thu Mar 09 2023 Anton Midyukov <antohami@altlinux.org> 52.0-alt2.g59cebf0
- NMU: switch to use AyatanaAppindicator3

* Wed Sep 28 2022 L.A. Kostis <lakostis@altlinux.ru> 52.0-alt1.g59cebf0
- GIT 59cebf0 with gnome 43 support.

* Tue May 10 2022 L.A. Kostis <lakostis@altlinux.ru> 50.0-alt1.gb0924df
- GIT b0924df with gnome 42 compatibility fixes.

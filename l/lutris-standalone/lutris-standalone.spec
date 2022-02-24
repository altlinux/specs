%def_enable meson

%define appid net.lutris.Lutris
%define repo lutris

Name: lutris-standalone
Version: 0.5.7.1
Release: alt1
Summary: Manager for game installation and execution
License: GPL-2.0 and GPL-2.0+ and GPL-3.0+ and CC0-1.0 and LGPL-2.1+ and CC-BY-NC-SA-2.0 and CC-BY-SA-3.0
Group: Games/Other
Url: https://lutris.net

Source: http://lutris.net/releases/lutris_%version.tar.xz
Patch: lutris_0.5.7_alt_python3_pixbuf_path.patch

AutoProv: no, nopython
# %brp_strip_none %_alterator_libdir/*
# %add_verify_elf_skiplist %_alterator_libdir/*
# %add_findreq_skiplist %_alterator_libdir/*

%if_enabled meson
BuildPreReq: meson
%endif
BuildRequires: rpm-build-python3
# Automatically added by buildreq on Fri Aug 30 2019 (-bi)
# optimized out: bash4 bashrc kmod perl python-base python-modules python3 python3-base python3-dev python3-module-pkg_resources rpm-build-python3 sh4 tzdata xz
#BuildRequires: eject fuse python3-module-setuptools rpm-build-gir unzip xlsfonts
Requires: python3-module-pygobject3 python3-module-yaml python3-module-requests python3-module-pylint python3-module-distro python3-module-setproctitle python3-module-Pillow libgdk-pixbuf-gir libgnome-desktop3-gir libwebkit2gtk-gir libnotify-gir libgtk+3-gir
Requires: python3-module-evdev
# Recommends: psmisc p7zip curl cabextract xrandr glibc-gconv-modules winetricks

Conflicts: lutris

BuildArch: noarch

%description
Lutris allows to gather and manage (install, configure and launch)
all games acquired from any source, in a single interface.
This includes, for example, Steam or Desura games, Windows games (WINE),
or emulated console games and browser games.

Recommends for install: psmisc p7zip curl cabextract xrandr glibc-gconv-modules winetricks

%prep
%setup -n %name
%patch -p2

%build
%if_enabled meson
%meson
%meson_build
%else
%python3_build
%endif

%install
%if_enabled meson
%meson_install
%else
%python3_install
%endif
%find_lang %repo

%files -f %repo.lang
%doc README.rst CONTRIBUTING.md AUTHORS
%doc LICENSE
%_bindir/%repo
%_datadir/%repo/
%_desktopdir/%appid.desktop
%_iconsdir/hicolor/scalable/apps/%repo.svg
%_iconsdir/hicolor/??x??/apps/%repo.png
%_iconsdir/hicolor/???x???/apps/%repo.png
%python3_sitelibdir/%{repo}*
%_datadir/metainfo/%appid.metainfo.xml
%_man1dir/%repo.1.xz

%changelog
* Mon Feb 21 2022 Leontiy Volodin <lvol@altlinux.org> 0.5.7.1-alt1
- Built as standalone stable version.

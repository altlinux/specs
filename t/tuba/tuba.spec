%global xdg_name dev.geopjr.Tuba
%global alt_name fedi

Name: tuba
Version: 0.8.4
Release: alt1
License: GPL-3.0-only
Group: Networking/Other

Summary: Browse the Fediverse
Summary(ru): Обзор сети Fediverse
Summary(pt): Navegue pelo Fediverse
Summary(zh): 浏览 Fediverse

Url: https://github.com/GeopJr/Tuba

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libspelling-1)
BuildRequires: pkgconfig(libwebp)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

# for ownership of icon parent directories
Requires: hicolor-icon-theme

%description
Explore the federated social web with Tuba for GNOME. Stay connected to your
favorite communities, family and friends with support for popular Fediverse
platforms like Mastodon, GoToSocial, Akkoma & more!

%description -l ru
Исследуйте федеративную социальную сеть с помощью Tuba для GNOME. Оставайтесь
на связи со своими любимыми сообществами, семьей и друзьями благодаря поддержке
популярных платформ Fediverse, таких как Mastodon, GoToSocial, Akkoma и других!

%description -l pt
Explore a rede social federada com o Tuba para o GNOME. Mantenha-se conectado
às suas comunidades favoritas, familiares e amigos com suporte para plataformas
populares do Fediverse, como Mastodon, GoToSocial, Akkoma &amp; mais!

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %xdg_name

%check
# The .desktop and .metainfo.xml files are validated during the test suite, so
# we don't need to run those validate commands separately.
%meson_test

%files -f %xdg_name.lang
%doc LICENSE
%doc README.md
%_mandir/man1/%xdg_name.1*
%_bindir/%xdg_name
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%_datadir/gtksourceview-5/language-specs/%alt_name-*.lang
%_datadir/gtksourceview-5/styles/%alt_name-*.xml
%_datadir/gtksourceview-5/styles/%alt_name.xml
%exclude %_datadir/locale/zh_Hans/LC_MESSAGES/dev.geopjr.Tuba.mo

%changelog
* Tue Sep 10 2024 Anton Palgunov <toxblh@altlinux.org> 0.8.4-alt1
- new version 0.8.4 (with rpmrb script)

* Sun Sep 01 2024 Anton Palgunov <toxblh@altlinux.org> 0.8.3-alt1
- new version 0.8.3 (with rpmrb script)

* Sun Apr 07 2024 Anton Palgunov <toxblh@altlinux.org> 0.7.2-alt1
- new version 0.7.2 (with rpmrb script)

* Thu Mar 28 2024 Anton Palgunov <toxblh@altlinux.org> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script)

* Wed Mar 20 2024 Anton Palgunov <toxblh@altlinux.org> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Sun Feb 11 2024 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.3-alt1.1
- Push to Sisyphus

* Sat Feb 10 2024 Anton Palgunov <toxblh@altlinux.org> 0.6.3-alt1
- initial build for ALT Sisyphus


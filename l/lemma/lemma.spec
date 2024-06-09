%define _name Lemma
%define pypi_name lemma
%define ver_major 13
%define rdn_name org.cvfosammmm.%_name

%def_enable check

Name: %pypi_name
Version: %ver_major
Release: alt1

Summary: Note-Taking App
License: GPL-3.0-or-later
Group: Text tools
Url: https://www.cvfosammmm.org/lemma/

BuildArch: noarch

Vcs: https://github.com/cvfosammmm/Lemma.git
Source: %name-%version.tar

%add_python3_path %_datadir/%_name

Requires: dconf
Requires: typelib(Adw) = 1

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson /usr/bin/glib-compile-resources
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli /usr/bin/glib-compile-schemas}

%description
Take notes with beautiful typography.

Warning: Lemma is currently in alpha stage, data loss is likely at this
point. Please be careful and make regular backups.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%python3_sitelibdir_noarch/%name/
%dir %python3_sitelibdir_noarch/lib
%python3_sitelibdir_noarch/lib/fontconfig/
%python3_sitelibdir_noarch/lib/freetype2/
%python3_sitelibdir_noarch/lib/harfpy/
%_datadir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
#%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README.*

%changelog
* Sun Jun 09 2024 Yuri N. Sedunov <aris@altlinux.org> 13-alt1
- first build for Sisyphus




%define _unpackaged_files_terminate_build 1
%define app_id page.codeberg.censor.Censor

Name: censor
Version: 0.7.2
Release: alt1

Summary: Censor is a PDF document redaction tool.
License: License: GPL-3.0-or-later AND CC-BY-SA-4.0
Group: File tools
Url: https://codeberg.org/censor/Censor
Vcs: https://codeberg.org/censor/Censor

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-macros-meson
BuildRequires: meson
BuildRequires: blueprint-compiler
Requires: python3-module-pymupdf
Requires: python3-module-pytest

%description
Censor is a PDF document redaction tool. It permanently removes text and images
in redacted areas and can draw rectangles over them. It uses the MuPDF library
with its python bindings from the PyMuPDF module.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name
#Manually removed zh_Hans due to Bug 48467.
rm -rf %buildroot%_datadir/locale/zh_Hans

%files -f %name.lang
%_bindir/censor
%_desktopdir/%app_id.desktop
%_datadir/%name/*
%_datadir/dbus-1/services/%app_id.service
%_datadir/licenses/%app_id/*
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_iconsdir/hicolor/scalable/apps/%app_id.svg
%_iconsdir/hicolor/symbolic/apps/%app_id-symbolic.svg

%changelog
* Mon Jun 29 2026 Pavel Mitrofanov <cobalt@altlinux.org> 0.7.2-alt1
- Initial commit.

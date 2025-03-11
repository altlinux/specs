Name: lv2-blop-plugins
Version: 1.0.4
Release: alt1

Summary: LV2 port of the BLOP LADSPA plugins
License: GPLv3
Group: Sound
Url: https://gitlab.com/drobilla/blop-lv2

Source: %name-%version-%release.tar

BuildRequires: meson
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(lv2)

%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc AUTHORS COPYING README*
%_libdir/lv2/*

%changelog
* Tue Mar 11 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.4-alt1
- initial

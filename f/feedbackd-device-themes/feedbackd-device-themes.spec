%def_disable snapshot
%define _name feedbackd
%define ver_major 0.1

%def_enable check

Name: %_name-device-themes
Version: %ver_major.0
Release: alt1

Summary: Device specific feedback themes for Feedbackd
License: GPL-3.0-or-later
Group: System/Configuration/Hardware
Url: https://source.puri.sm/Librem5/feedbackd-device-themes

BuildArch: noarch

Vcs: https://source.puri.sm/Librem5/feedbackd-device-themes.git
%if_disabled snapshot
Source: https://storage.puri.sm/releases/%name/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
%{?_enable_check:BuildRequires: /usr/bin/fbd-theme-validate /usr/bin/json-glib-validate}

%description
feedbackd provides a DBus daemon (feedbackd) to act on events to provide
haptic, visual and audio feedback. This package contains the device
specific feedback theme files.

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
%_datadir/%_name/themes/*.json
%doc README.* NEWS

%changelog
* Sun May 19 2024 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus

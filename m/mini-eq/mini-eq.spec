%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 0.8
%define beta %nil
%define _name mini-eq
%define pypi_name mini_eq
%define domain bhack.github.io
%define uuid %{_name}@%domain
%define rdn_name io.github.bhack.%_name

%def_enable check

Name: %_name
Version: %ver_major.7
Release: alt1%beta

Summary: Mini EQ is a small parametric equalizer for PipeWire desktops
Group: Sound
License: GPL-3.0-only
Url: https://github.com/bhack/mini-eq

Vcs: https://github.com/bhack/mini-eq.git

%if_disabled snapshot
Source: %url/archive/v%version%beta/%_name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif

BuildArch: noarch

%define shell_ver 50
%define pwg_ver 0.3.9

Requires: pipewire wireplumber libebur128
Requires: python3-module-pygobject3 python3(numpy)
Requires: pipewire-gobject-gir >= %pwg_ver

BuildRequires(pre):rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: python3(wheel) python3(setuptools)
BuildRequires: /usr/bin/appstreamcli desktop-file-utils
%{?_enable_check:BuildRequires: python3(pytest)  python3(pytest-cov)
BuildRequires: git python3(numpy) python3(cairo) python3-module-pygobject3
BuildRequires: typelib(Pwg) typelib(Adw) = 1}

%description
Mini EQ is a small system-wide parametric equalizer for PipeWire desktops.
It uses GTK/Libadwaita for the UI, pipewire-gobject for app-facing PipeWire
routing, metadata, and monitor streams, and PipeWire filter-chain with builtin
biquad filters for the equalizer. When libebur128 is available, the monitor can
also show live LUFS loudness.

%package -n gnome-shell-extension-%name
Summary: GNOME Shell extension for Mini EQ
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: gnome-shell >= %shell_ver
Requires: %name = %EVR

%description -n gnome-shell-extension-%name
This package provides GNOME Shell extension for Mini EQ.

%prep
%setup -n %_name-%version%beta

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot%_datadir/{applications,metainfo,gnome-shell/extensions/%uuid}
cp -a data/%rdn_name.desktop %buildroot%_datadir/applications/
cp -ar src/%pypi_name/assets/icons/ %buildroot%_datadir/
cp -a data/%rdn_name.metainfo.xml %buildroot%_datadir/metainfo/
cp -a extensions/gnome-shell/%uuid/* \
    %buildroot%_datadir/gnome-shell/extensions/%uuid/
%find_lang %_name

%check
%pyproject_run_pytest

%files -f %_name.lang
%_bindir/%_name
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/
%_datadir/applications/%rdn_name.desktop
%_datadir/icons/hicolor/*/*/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%files -n gnome-shell-extension-%name
%_datadir/gnome-shell/extensions/%uuid/
%doc extensions/gnome-shell/README*

%changelog
* Sat Jun 13 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.7-alt1
- 0.8.7

* Thu Jun 04 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.6-alt1
- 0.8.6

* Mon Jun 01 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.5-alt1
- 0.8.5

* Sun May 24 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.4-alt1
- 0.8.4

* Wed May 20 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- 0.8.3

* Sun May 17 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Fri May 15 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Wed May 13 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Mon May 11 2026 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- first build for Sisyphus


%define _unpackaged_files_terminate_build 1

Name: gnome-software-plugin-stplr
Version: 0.3.0
Release: alt1

Summary: Stapler Support for GNOME Software
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://altlinux.space/stapler/gnome-software-plugin-stplr
Vcs: https://altlinux.space/stapler/gnome-software-plugin-stplr.git

Source: %name-%version.tar

Requires: stplr >= 0.1.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala
BuildRequires: pkgconfig(gnome-software)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: libpolkit-devel

# Needed by scripts/detect-gs-plugin-api-version.sh to detect unstable API.
BuildRequires: gnome-software

%description
This package provides support for install packages from Stapler via GNOME Software.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%_libdir/gnome-software/plugins-*/libgs_plugin_stplr.so
%_prefix/libexec/%name
%_datadir/polkit-1/actions/dev.stplr.%name.policy

%doc README.md

%changelog
* Mon Apr 06 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

* Tue Feb 24 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.2.0-alt2
- Add Url and Vcs tags.

* Sat Feb 21 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.2.0-alt1
- New version 0.2.0.

* Tue Feb 17 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.1.1-alt1
- New version 0.1.1.

* Tue Jan 27 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.1.0-alt1
- Initial build.


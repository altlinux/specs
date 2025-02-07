%define _unpackaged_files_terminate_build 1

Name:    caja-admin
Version: 0.0.5
Release: alt1

Summary: Add administrative actions to Caja's right-click menu
License: GPLv3
Group: Graphical desktop/MATE
Url:     https://github.com/infirit/caja-admin

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

Requires: python3-module-caja
Requires: /usr/bin/caja

%description
Add administrative actions to Caja's right-click menu
Caja Admin is a simple Python extension for the Caja file manager that
adds some administrative actions to the right-click menu:
- Open as Administrator: opens a folder in a new Caja window running
 with administrator (root) privileges.
- Edit as Administrator: opens a file in a Pluma window running with
 administrator (root) privileges.
- Run as Administrator: runs an executable file with administrator
 (root) privileges inside a MATE Terminal.

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%doc NEWS NEWS.GNOME AUTHORS LICENSE *.md
%_datadir/caja-python/extensions
%_datadir/polkit-1/actions/org.freedesktop.caja-admin.policy


%changelog
* Fri Feb 07 2025 Nikolay Strelkov <snk@altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus

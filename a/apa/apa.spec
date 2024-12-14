%define _unpackaged_files_terminate_build 1

Name: apa
Version: 0.1.0.alpha
Release: alt1

Summary: An assistant for working with packages in your ALT distros
License: GPL-3.0-or-later
Group: System/Configuration/Packaging
Url: https://github.com/alt-gnome/apa
VCS: https://github.com/alt-gnome/apa

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: apt
BuildRequires: apt-repo
BuildRequires: update-kernel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(packagekit-glib2)
BuildRequires: pkgconfig(libalt-repo-1)
BuildRequires: pkgconfig(libvazzy-1)

%description
An assistant for working with packages in your ALT distros.

Use `apa help` for more information.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_sysconfdir/%name/

%changelog
* Sat Dec 14 2024 Alexey Volkov <qualimock@altlinux.org> 0.1.0.alpha-alt1
- Initial build for ALT

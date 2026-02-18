%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name appimage-thumbnailer
%define ver_major 4.0

# DwarFS tools: dwarfsextract, dwarfsck required
%def_disable bundle_dwarfs
%define dwarfs_ver = 0.14.1
%def_disable bundle_squashfs
%define squashfs_ver 4.6.1
%def_enable check

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: AppImage Thumbnailer
Group: Graphical desktop/GNOME
License: MIT
Url: https://github.com/kem-a/appimage-thumbnailer

Vcs: https://github.com/kem-a/appimage-thumbnailer.git

%if_enabled snapshot
Source: %_name-%version.tar
%else
Source: %url/archive/v%version/%_name-%version.tar.gz
%endif

ExclusiveArch: x86_64 aarch64

%define pixbuf_ver 2.42
%define rsvg_ver 2.54
%define dwarfs_ver 0.14.1

Requires: dwarfs-tools >= %dwarfs_ver
# if kernel < 3.18
Requires: fuse-dwarfs
Requires: squashfs-tools >= %squashfs_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(gdk-pixbuf-2.0) >= %pixbuf_ver
BuildRequires: pkgconfig(librsvg-2.0) >= %rsvg_ver

%description
An in-process thumbnailer that extracts AppImage icons and writes
ready-to-use PNG thumbnails for desktop environments implementing the
freedesktop.org spec.

%prep
%setup

%build
%meson \
    %{subst_enable_meson_bool bundle_dwarfs bundle_dwarfs} \
    %{subst_enable_meson_bool bundle_squashfs bundle_squashfs} \
%nil
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %_name

%check
%__meson_test -v

%files -f %name.lang
%_bindir/%_name
%_datadir/thumbnailers/%_name.thumbnailer
%doc README*

%changelog
* Wed Feb 18 2026 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Tue Jan 06 2026 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Wed Dec 24 2025 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Dec 15 2025 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- first build for Sisyphus



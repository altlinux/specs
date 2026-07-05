%define _unpackaged_files_terminate_build 1

Name: gdmap
Version: 1.4.0
Release: alt1

Summary: Tool to visualize disk space
License: GPL-2.0-or-later
Group: File tools
Url: https://gitlab.com/sjohannes/gdmap

Source: %name-%version.tar

# sync with version 1.4.0-1 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libxml-2.0)

%description
GdMap is a tool which allows you to visualize disk space. Ever
wondered why your hard disk is full or what directory and files take
up most of the space? With GdMap these questions can be answered
quickly. To display directory structures cushion treemaps are used
which visualize a complete folder or even the whole hard drive with
one picture.

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%files -f %{name}.lang
%_bindir/gdmap
%_desktopdir/gdmap.desktop
%_man1dir/gdmap.1.*
%_datadir/gdmap/pixmaps/gdmap_icon.png
%_pixmapsdir/gdmap_icon.png

%changelog
* Sun Jul 05 2026 Nikolay Strelkov <snk@altlinux.org> 1.4.0-alt1
- Initial build of gtk3-based version for Sisyphus.

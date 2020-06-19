
Name: libgnt
Version: 2.14.0
Release: alt1
Summary: TUI toolkit based on GLib and ncurses
License: GPL-2.0-or-later
Group: System/Libraries
Url: https://pidgin.im/
# http://downloads.sf.net/pidgin/%name-%version.tar.xz
Source: %name-%version.tar

Conflicts: finch < 2.14.0
BuildRequires(pre): meson
BuildRequires: gtk-doc
BuildRequires: libncurses-devel libncursesw-devel
BuildRequires: pkgconfig(glib-2.0) >= 2.16.0 pkgconfig(gobject-2.0) pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(libxml-2.0) >= 2.6.0

%description
GNT is an ncurses toolkit for creating text-mode graphical user
interfaces in a fast and easy way.

%package devel
Summary: Development files of GNT
Group: Development/Other
Requires: %name = %EVR
Conflicts: finch-devel < 2.14.0

%description devel
GNT is an ncurses toolkit for creating text-mode graphical user
interfaces in a fast and easy way.

The GNT development package includes the header files, libraries,
and development tools necessary for compiling and linking
applications which will use GNT.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files
%doc ChangeLog README.md
%_libdir/%name.so.*

%files devel
%_includedir/gnt
%_libdir/%name.so
%_libdir/gnt
%_pkgconfigdir/gnt.pc
%_datadir/gtk-doc/*/%name/

%changelog
* Fri Jun 19 2020 Alexey Shabalin <shaba@altlinux.org> 2.14.0-alt1
- Initial build


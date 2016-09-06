Name: image-analyzer
Version: 3.0.0
Release: alt1
Summary: Simple Gtk+ application that displays tree structure of disc image
Summary(ru_RU.UTF-8): Простое GTK+ приложение для просмотра структуры образа диска
License: GPLv2+
Group: Emulators
Url: http://cdemu.sourceforge.net/
Packager: Anton Midyukov <antohami@altlinux.org>
Source: http://downloads.sourceforge.net/cdemu/%name-%version.tar.bz2
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake intltool gcc-c++ libmirage-devel >= 3.0.0 libxml2-devel pkgconfig(glib-2.0) pkgconfig(gobject-2.0) pkgconfig(gtk+-3.0) desktop-file-utils

%description
Image Analyzer is a simple Gtk+ application that displays tree structure of disc
image created by libMirage.

It is mostly intended as a demonstration of libMirage API use, although it can
be also used to verify that an image is correctly handled by libMirage.

%description -l ru_RU.UTF-8
Image Analyzer представляет собой простое Gtk+ приложениеn для просмотра структуры
образов созданных с помощью libMirage.

Он в основном предназначен для демонстрации того, как использовать API
libMirage, тем не менее он может также использоваться для того, чтобы проверить, 
корректно ли обрабатывается образ libMirage.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS COPYING
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/*.svg

%changelog
* Tue Sep 06 2016 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt1
- Initial build for ALT Linux Sisyphus.

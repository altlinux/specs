Name: libwebp-pixbuf-loader
Version: 0.2.1
Release: alt1
Summary: WebP image loader for GTK+ applications
Group: System/Libraries
License: LGPLv2+
URL: https://github.com/aruiz/webp-pixbuf-loader

Source0: %name-%version.tar

BuildRequires: libgdk-pixbuf-devel libwebp-devel meson

%description
webp-pixbuf-loader contains a plugin to load WebP images in GTK+ applications

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_libdir/gdk-pixbuf-2.0/*/loaders/libpixbufloader-webp.so
%_datadir/thumbnailers/webp-pixbuf.thumbnailer

%changelog
* Mon Mar 06 2023 Valery Inozemtsev <shrek@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Fri Nov 18 2022 Valery Inozemtsev <shrek@altlinux.ru> 0.0.7-alt1
- initial release


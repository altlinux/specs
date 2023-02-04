Name:    libg15render
Version: 3.0.4
Release: alt1

Summary: Library to render text and shapes into a buffer usable by the Logitech G15 Gaming Keyboard.
License: GPL-2.0
Group:   System/Libraries
Url:     https://gitlab.com/menelkir/libg15render

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires: libg15-devel
BuildRequires: libfreetype-devel

%description
This is a library to render text and shapes into a buffer usable by the.
Logitech G15 Gaming Keyboard. This library probably isn't very useful without
libg15 and/or g15daemon.

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
%summary

%prep
%setup

%build
%configure --enable-ttf --disable-static
%make_build

%install
%makeinstall_std
rm -f %buildroot%_defaultdocdir/%name-3.0/*

%files
%doc AUTHORS README.rst
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_man3dir/*.3*

%changelog
* Mon Jan 30 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.4-alt1
- Initial build for Sisyphus.

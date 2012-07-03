Name: gsimplecal
Version: 0.8
Release: alt1

Summary: Simple and lightweight GTK calendar
License: BSD-Style
Group: Office
Url: https://github.com/dmedvinsky/gsimplecal/

Packager: Egor Glukhov <kaman@altlinux.org>
Source: %name-%version.tar

BuildRequires: gcc-c++ libgtk+2-devel

%description
%name is a lightweight calendar application written in C++ using GTK2.

It was intentionally made for use with tint2 panel in the openbox environment
to be launched upon clock click, but of course it will work without it.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/*

%changelog
* Mon May 9 2011 Egor Glukhov <kaman@altlinux.org> 0.8-alt1
- Initial build

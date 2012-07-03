%define base gtk-engines
%define gtk2_ver 2.1.2

Name: %base-wonderland
Version: 1.0
Release: alt1

Summary: A GTK+2 theme engine - Wonderland (Bluecurve)
Summary(ru_RU.UTF-8): Модуль прорисовки "Страна чудес" (Bluecurve) для GTK+2
License: GPL
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org/pub/gnome/teams/art.gnome.org/themes/gtk2/
Source: GTK2-Wonderland-Engine-%version.tar.bz2
Requires: libgtk+2 >= %gtk2_ver
BuildPreReq: libgtk+2-devel >= %gtk2_ver
BuildRequires: gcc-c++ glib2-devel glibc-devel-static libatk-devel libgtk+2-devel libpango-devel libstdc++-devel pkgconfig

%description
Wonderland (also known as RedHat Bluecurve) theme engine.

%description -l ru_RU.UTF-8
Модуль прорисовки "Страна чудес" (также известный как Bluecurve).

%prep
%setup -q -n Bluecurve

%build
%configure
%make_build

%install
%makeinstall

%files
%_libdir/gtk-*/*/engines/*.so
%_datadir/themes/*
%doc AUTHORS README ChangeLog NEWS

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build


%define _name rezlooks
%define engine_prefix libgtk-engine

Name: %engine_prefix-%_name
Version: 0.6
Release: alt1

Summary: Rezlooks GTK2 engine
Summary(ru_RU.UTF-8):Модуль прорисовки Rezlooks для GTK2
License: GPL
Group: Graphical desktop/GNOME
Url: http://rezza.driftingmind.net/
Source0: %_name-%version.tar.gz

%define gtk_ver 2.10.0
%define gtk_binary_ver 2.10.0
%define engines_dir %_libdir/gtk-2.0/%gtk_binary_ver/engines

BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildRequires: gcc-c++ gcc-g77 libgtk+2-devel

%description
This is Doug Whiteley's rezlooks GTK+ engine, based on clearlooks.

%description -l ru_RU.UTF-8
Это модуль прорисовки Rezlooks для GTK2 от Doug Whiteley, основанный на clearlooks.

%prep
%setup -q -n %_name-%version

%build
%configure --enable-animation
%make

%install
%makeinstall

%files
%doc AUTHORS README Changelog
%engines_dir/*.so
%exclude %engines_dir/*.la

%changelog
* Wed Dec 06 2006 Vyacheslav Dikonov <slava@altlinux.ru> 0.6-alt1
- ALTLinux build

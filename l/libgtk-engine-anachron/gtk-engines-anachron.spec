%define _name anachron
%define engine_prefix libgtk-engine

Name: %engine_prefix-%_name
Version: 0.1
Release: alt1

Summary: Anachron GTK2 engine
Summary(ru_RU.UTF-8):Модуль прорисовки Anachron для GTK2
License: GPL
Group: Graphical desktop/GNOME
Url: http://www.gnome-look.org
Source0: %_name.tar.gz

%define gtk_ver 2.10.0
%define gtk_binary_ver 2.10.0
%define engines_dir %_libdir/gtk-2.0/%gtk_binary_ver/engines

BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildRequires: gcc-c++ gcc-g77 libgtk+2-devel

%description
A GTK+ 2.x engine implemented in by Dennis Moehlmann based on the design of the Ana SVG-theme by Witek Tarchalski.

%description -l ru_RU.UTF-8
Модуль прорисовки GTK2 сделанный Dennis Möhlmann по мотивам SVG-темы Ana от Witek Tarchalski.

%prep
%setup -q -n %_name

%build
%__autoreconf
%configure
%make

%install
%makeinstall

%files
%doc AUTHORS README ChangeLog
%engines_dir/*.so

%exclude %engines_dir/*.la

%changelog
* Wed Dec 06 2006 Vyacheslav Dikonov <slava@altlinux.ru> 0.1-alt1
- ALTLinux build

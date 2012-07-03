%define _name ubuntulooks
%define engine_prefix libgtk-engine

Name: %engine_prefix-%_name
Version: 0.9.11
Release: alt1

Summary: Ubuntulooks GTK2 engine
Summary(ru_RU.UTF-8):Модуль прорисовки Ubuntulooks для GTK2
License: GPL
Group: Graphical desktop/GNOME
Url: http://www.gnome-look.org
Source0: ubuntulooks_%version.orig.tar.gz

%define gtk_ver 2.10.0
%define gtk_binary_ver 2.10.0
%define engines_dir %_libdir/gtk-2.0/%gtk_binary_ver/engines

BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildRequires: gcc-c++ gcc-g77 libgtk+2-devel

%description
Ubuntulooks is an engine forked from Clearlooks 2.7 to bring a unique look to Ubuntu.

%description -l ru_RU.UTF-8
Ubuntulooks - самостоятельный вариант Clearlooks 2.7, созданный для придания уникального внешнего вида дистрибутиву Ubuntu.

%prep
%setup -q -n %_name-%version

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
* Wed Dec 06 2006 Vyacheslav Dikonov <slava@altlinux.ru> 0.9.11-alt1
- ALTLinux build

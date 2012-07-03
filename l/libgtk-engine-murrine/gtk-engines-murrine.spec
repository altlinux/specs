%define _name murrine
%define engine_prefix libgtk-engine

Name: %engine_prefix-%_name
Version: 0.98.1.1
Release: alt0.1

Summary: Murrine GTK2 engine
Summary(ru_RU.UTF-8):Модуль прорисовки Murrine для GTK2
License: GPL
Group: Graphical desktop/GNOME
Url: http://cimi.netsons.org/pages/murrine.php
Source0: %name-%version.tar
Patch0: %name-%version-cppflags-alt.patch
Packager: Denis Koryavov <dkoryavov@altlinux.org>

%define gtk_ver 2.10.0
%define gtk_binary_ver 2.10.0
%define engines_dir %_libdir/gtk-2.0/%gtk_binary_ver/engines

BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildRequires: gcc-c++ gcc-g77 libgtk+2-devel
BuildRequires:  intltool, gettext
BuildRequires: libpixman-devel

%description
Murrine is a Gtk2 engine, written in C language, using cairo vectorial 
drawing library to draw widgets. It features a modern glassy look, 
and it is elegant and clean on the eyes. It is also extremely customizable.

%description -l ru_RU.UTF-8
Murrine - использующий cairo быстрый модуль прорисовки для GTK2.

%prep
%setup -q 
%patch0 -p1

%build
%autoreconf
#undefine __libtoolize
export CPPFLAGS+="-I %_includedir/pixman-1/"
%configure --enable-animation 
#--enable-macmenu
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README ChangeLog
%engines_dir/*.so

%exclude %engines_dir/*.la

%changelog
* Tue Nov 02 2010 Alexey Morsov <swi@altlinux.ru> 0.98.1.1-alt0.1
- new git version

* Mon Mar 23 2009 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.90.2-alt1
- Version update

* Wed Nov 12 2008 Denis Koryavov <dkoryavov@altlinux.org> 0.53.1-alt1
- Version update

* Wed Dec 06 2006 Vyacheslav Dikonov <slava@altlinux.ru> 0.31-alt1
- ALTLinux build

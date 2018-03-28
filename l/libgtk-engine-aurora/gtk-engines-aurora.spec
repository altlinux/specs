%define _name aurora
%define engine_prefix libgtk-engine

Name: %engine_prefix-%_name
Version: 1.5.1
Release: alt1.2

Summary: Aurora GTK2 engine
Summary(ru_RU.UTF-8):Модуль прорисовки Aurora для GTK2
License: GPL
Group: Graphical desktop/GNOME
Url: https://www.gnome-look.org/content/show.php/Aurora+Gtk+Engine?content=56438
Packager: Denis Koryavov <dkoryavov@altlinux.org>
Source0: %_name-%version.tar.bz2
Patch0: gtk-engines-aurora-1.5.1-alt-glib2.patch

%define gtk_ver 2.10.0
%define gtk_binary_ver 2.10.0
%define engines_dir %_libdir/gtk-2.0/%gtk_binary_ver/engines

BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildRequires: gcc-c++ gcc-g77 libgtk+2-devel

%description
Aurora is a GTK2 engine. It features a modern glassy look, 
and it is elegant and clean on the eyes.

%description -l ru_RU.UTF-8
Aurora - элегантный быстрый модуль прорисовки для GTK2.

%prep
%setup -q -n %_name-%version
%patch0 -p2

%build
%autoreconf
%configure --enable-animation --enable-macmenu
%make

%install
%makeinstall

%files
%doc AUTHORS README ChangeLog
%engines_dir/*.so

%exclude %engines_dir/*.la

%changelog
* Wed Mar 28 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1.2
- NMU: added URL

* Fri Jul 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.1
- Fixed build

* Tue Apr 21 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.5.1-alt1
- Version update

* Wed Nov 26 2008 Denis Koryavov <dkoryavov@altlinux.org> 1.4-alt1
 - Initial build

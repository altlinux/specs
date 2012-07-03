%define major 2.22
%define oname gnome-python-desktop
Name: python-module-pygnome-gtksourceview
Version: %major.0
Release: alt2.1

Summary: python bindings for the version 1 of the GtkSourceView library

License: LGPL
Group: Development/Python
Url: http://www.pygtk.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://ftp.gnome.org/pub/gnome/sources/%oname/%major/%oname-%version.tar.bz2

%define python_gnome_dir %python_sitelibdir/gtk-1.0/gnome

# manually removed: bug-buddy 
# Automatically added by buildreq on Sun Jan 06 2008
BuildRequires: gcc-c++ libgtksourceview1-devel python-module-pygtk-devel

BuildRequires: python-module-pygtk-devel >= 2.10.0

%description
Contains python bindings for the version 1 of the
GtkSourceView library.

%prep
%setup -q -n %oname-%version

%build
%configure
cd gtksourceview
%make_build

%install
cd gtksourceview
%makeinstall
rm -f %buildroot%python_sitelibdir/gtk-2.0/*.la
rm -f %buildroot%_datadir/pygtk/2.0/defs/gtksourceview.defs

%files
%doc AUTHORS ChangeLog README NEWS
%python_sitelibdir/gtk-2.0/gtksourceview.so

%changelog
* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.22.0-alt2.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.22.0-alt2
- Rebuilt with python 2.6

* Wed Apr 30 2008 Vitaly Lipatov <lav@altlinux.ru> 2.22.0-alt1
- new version 2.22.0 (with rpmrb script)

* Sun Jan 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt1
- compatibility build for ALT Linux Sisyphus

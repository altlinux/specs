Name: qgtkstyle
Version: 0.0
Release: alt1.r594

Summary: Qt style rendered using GTK
License: GPLv2
Group: Graphical desktop/Other
Url: http://labs.trolltech.com/page/Projects/Styles/GtkStyle

Source0: gtkstyle.tar.bz2

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sun May 18 2008
BuildRequires: gcc-c++ libgtk+2-devel libqt4-devel

%description
This is a Qt style rendered using GTK to give a native appearence for Qt
applications running on the GNOME desktop.

%prep
%setup -q -n gtkstyle

%build
qmake-qt4
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install

%files
%_libdir/qt4/plugins/styles/libgtkstyle.so

%changelog
* Sun May 18 2008 Igor Zubkov <icesik@altlinux.org> 0.0-alt1.r594
- build for Sisyphus


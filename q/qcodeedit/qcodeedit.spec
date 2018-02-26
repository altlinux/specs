%define oname QCodeEdit
Summary: QCodeEdit is a framework designed to make edition of source code easy for both users and developers.
Name: qcodeedit
Version: 2.2.2
Release: alt2
License: GPL
Group: Development/KDE and QT
Packager: Boris Savelev <boris@altlinux.org>
Url: http://qcodeedit.edyuk.org
Source: http://dl.sourceforge.net/sourceforge/edyuk/%name-%version.tar.bz2

# Automatically added by buildreq on Sat Mar 14 2009
BuildRequires: gcc-c++ libqt4-devel

%description
QCodeEdit is a project aiming at the creation of a flexible and powerful text
editing framework for Qt4. It has started as a sub-project of Edyuk, copyright (c)
Luc Bruant, a free and open source IDE. As it proved successful it is also
released as a standalone library to make it easy for everyone to use such
a framework within other apps without having to reinvent the wheel.

%package -n lib%name
Summary: Shared library of %oname
Group: Development/KDE and QT

%package -n lib%name-devel
Requires: lib%name = %version-%release
Summary: Devel files and examples for %oname
Group: Development/KDE and QT

%package -n lib%name-designer
Requires: lib%name = %version-%release
Summary: %oname designer plugin
Group: Development/KDE and QT

%description -n lib%name
%oname shared library.

%description -n lib%name-devel
%oname development files and examples.

%description -n lib%name-designer
%oname designer plugin.

%prep
%setup
# dont build examples
sed -i 's:example::g' %name.pro
qmake-qt4

%build
%make

%install
%makeinstall_std INSTALL_ROOT=%buildroot
mkdir -p %buildroot%_datadir/%name
cp -ap lib%name.* %buildroot%_libdir/
cp -ap example %buildroot%_datadir/%name/

%files -n lib%name
%doc README.txt
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/qt4/%oname
%_includedir/qt4/%oname/*.h
%_qt4dir/mkspecs/features/%name.prf
%dir %_datadir/%name
%_datadir/%name/*

%files -n lib%name-designer
%_qt4dir/plugins/designer/libqcodeedit-plugin.so

%changelog
* Sat Mar 14 2009 Boris Savelev <boris@altlinux.org> 2.2.2-alt2
- fix summary in lib%name-designer

* Sat Mar 14 2009 Boris Savelev <boris@altlinux.org> 2.2.2-alt1
- initial build


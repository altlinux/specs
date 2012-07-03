%define projectname bakery
Summary: 	A C++ Framework for Document-based GNOME applications.
Name: 		lib%projectname
Version: 	2.6.2
Release: 	alt1
License: 	LGPL
Group: 		System/Libraries
Source: 	ftp://download.sourceforge.net/bakery/%{projectname}-%{version}.tar.bz2
URL: 		http://bakery.sourceforge.net/
Packager: Eugene Ostapets <eostapets@altlinux.org>

# Automatically added by buildreq on Tue Jan 06 2009
BuildRequires: gcc-c++ intltool libgconfmm2-devel libglademm-devel libxml++2-devel

%description

Bakery is a C++ Framework for creating GNOME applications using
Gnome-- and Gtk--.

Bakery provides a Document/View architecture, but it doesn't force you
to use the whole architecture.  Bakery provides default functionality,
which can be easily customized.  Bakery makes it easy to start
developing GNOME applications.  Bakery gives your application
structure.  Bakery will provide easy access to GNOME technologies such
as Bonobo and GConf.

%package	devel
Summary: 	Headers for developing programs that will use bakery.
Group: 		Development/C++

%description    devel
This package contains the headers that programmers will need to develop
applications which will use bakery.

%prep
%setup -n %projectname-%version

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %projectname

%files -f %projectname.lang
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%_libdir/*.so.*

%files  devel
%doc examples/ AUTHORS COPYING ChangeLog INSTALL NEWS README
%_includedir/*
%_libdir/*.so
%_libdir/%projectname-2.6
%exclude %_libdir/*.a
%_pkgconfigdir/*.pc

%changelog
* Mon Jan 05 2009 Eugene Ostapets <eostapets@altlinux.ru> 2.6.2-alt1
- first build

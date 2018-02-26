%define ver_major 1.0
%define oname goocanvas
%def_disable static

Name: lib%oname
Version: %ver_major.0
Release: alt1
Summary: A new canvas widget for GTK+ that uses cairo for drawing

Group: System/Libraries
License: LGPLv2+
Url: http://live.gnome.org/GooCanvas
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildPreReq: rpm-build-gnome
# From configure.in
BuildPreReq: libgtk+2-devel >= 2.12.0
BuildPreReq: glib2-devel >= 2.10.0
BuildPreReq: libcairo-devel >= 1.4.0

# Automatically added by buildreq on Sun Aug 10 2008
BuildRequires: gcc-c++ gtk-doc

%description
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

%package devel
Group: Development/C
Summary: A new canvas widget for GTK+ that uses cairo for drawing
Requires: %name = %version-%release

%description devel
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

These are the files used for development.

%package devel-doc
Summary: Development package for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Contains developer documentation for %name.

%prep
%setup -q

# demo application does not compile properly 
#sed -i -e 's/ demo / /g' Makefile.am Makefile.in

%build
NOCONFIGURE=1 ./autogen.sh
%configure %{subst_enable static} --enable-gtk-doc
%make_build


%install
%make_install DESTDIR=%buildroot install

%find_lang %oname

%files -f %oname.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_libdir/*.so.*

%files devel
%_includedir/%oname-1.0
%_libdir/*.so
%_pkgconfigdir/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Thu Jun 09 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0
- move docs to devel-doc subpackage

* Tue Jul 07 2009 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt1
- 0.15

* Mon Apr 20 2009 Alexey Shabalin <shaba@altlinux.ru> 0.14-alt1
- 0.14
- remove obsolete post scripts

* Mon Oct 27 2008 Alexey Shabalin <shaba@altlinux.ru> 0.12-alt1
- 0.12
- enable back build demo

* Mon Oct 27 2008 Alexey Shabalin <shaba@altlinux.ru> 0.10-alt2
- demo application does not build; remove it

* Sun Aug 10 2008 Alexey Shabalin <shaba@altlinux.ru> 0.10-alt1
- initial build for ALTLinux


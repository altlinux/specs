# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize pkgconfig(check) pkgconfig(gdk-2.0) pkgconfig(gio-2.0) pkgconfig(x11)
# END SourceDeps(oneline)

Name: libgxim
Version: 0.5.0
Release: alt3

Summary: GObject-based XIM protocol library
License: LGPLv2+
Group: System/Libraries

Url: http://tagoh.bitbucket.org/libgxim/
Source0: http://bitbucket.org/tagoh/%name/downloads/%name-%version.tar.bz2
Source44: import.info
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildRequires: intltool gettext ruby ruby-stdlibs
BuildRequires: glib2-devel >= 2.26 gtk2-devel

%description
libgxim is a X Input Method protocol library that is implemented by GObject.
this library helps you to implement XIM servers or client applications to
communicate through XIM protocol without using Xlib API directly, particularly
if your application uses GObject-based main loop.

This package contains the shared library.

%package devel
Summary: Development files for libgxim
Group: Development/C
Requires: %name = %version-%release

%description devel
libgxim is a X Input Method protocol library that is implemented by GObject.
this library helps you to implement XIM servers or client applications to
communicate through XIM protocol without using Xlib API directly, particularly
if your application uses GObject-based main loop.

This package contains the development files to make any applications with
libgxim.

%prep
%setup

%build
%configure --disable-static --disable-rebuilds
%make_build

%install
%makeinstall_std
rm %buildroot%_libdir/*.la
%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog README
%_libdir/libgxim.so.*

%files devel
%doc AUTHORS COPYING ChangeLog README
%_libdir/libgxim.so
%_libdir/pkgconfig/*.pc
%_includedir/libgxim
%_datadir/gtk-doc/html/libgxim

%changelog
* Fri Aug 04 2017 Michael Shigorin <mike@altlinux.org> 0.5.0-alt3
- spec cleanup

* Tue Aug 26 2014 Ilya Mashkin <oddity@altlinux.ru> 0.5.0-alt2
- build for Sisyphus

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_3
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_2
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_1
- update to new release by fcimport

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_1
- initial fc import


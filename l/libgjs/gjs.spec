%def_disable snapshot
%define _libexecdir %prefix/libexec

%define ver_major 1.45
%define _name gjs
%define api_ver 1.0

%def_enable installed_tests

Name: lib%_name
Version: %ver_major.4
Release: alt1

Summary: Javascript Bindings for GNOME
Group: System/Libraries
# The following files contain code from Mozilla which
# is triple licensed under MPL1.1/LGPLv2+/GPLv2+:
# The console module (modules/console.c)
# Stack printer (gjs/stack.c)
License: MIT and (MPLv1.1 or GPLv2+ or LGPLv2+)
Url: https://live.gnome.org/Gjs/

%if_enabled snapshot
Source: %_name-%version.tar
%else
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%endif

%define glib_ver 2.42.0
%define gi_ver 1.42.0

Requires: gobject-introspection

BuildRequires: gnome-common gcc-c++ libffi-devel libmozjs24-devel libcairo-devel
BuildRequires: libgio-devel >= %glib_ver gobject-introspection-devel >= %gi_ver
BuildRequires: libreadline-devel libcairo-gobject-devel
BuildRequires: libgtk+3-devel libgtk+3-gir-devel

# for check
BuildRequires: /proc dbus-tools dbus-tools-gui

%description
Gjs allows using GNOME libraries from Javascript. It's based on the
Spidermonkey Javascript engine from Mozilla and the GObject introspection
framework.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Files for development with %name.

%package tests
Summary: Tests for the Gjs package
Group: Development/Other
Requires: %name = %version-%release
%description tests
This package provides tests programs that can be used to verify
the functionality of the installed Gjs library package.

%set_typelibdir %_libdir/%_name/girepository-1.0

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
    --disable-static \
    %{?_enable_installed_tests:--enable-installed-tests}

%make_build

%install
%makeinstall_std

%check
# check failed if installed-tests disabled
#%%make check

%files
%_bindir/%_name
%_bindir/%_name-console
%_libdir/%name.so.*
%dir %_libdir/%_name/
%dir %_typelibdir
%_typelibdir/GjsPrivate-1.0.typelib
#%_datadir/%_name-%api_ver
%doc COPYING NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name.so
%_libdir/pkgconfig/%_name-%api_ver.pc
%_libdir/pkgconfig/%_name-internals-%api_ver.pc
%doc examples/*

%if_enabled installed_tests
%add_typelib_req_skiplist typelib(GIMarshallingTests) typelib(Regress) typelib(WarnLib)
%files tests
%_libdir/%_name/libgimarshallingtests.so
%_libdir/%_name/libregress.so
%_libdir/%_name/libwarnlib.so
%_libexecdir/%_name/installed-tests/
%_datadir/installed-tests/%_name/

%exclude %_libdir/%_name/*.la
%endif


%changelog
* Wed Jul 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.45.4-alt1
- 1.45.4

* Wed Jan 27 2016 Yuri N. Sedunov <aris@altlinux.org> 1.45.3-alt1
- 1.45.3

* Wed Oct 28 2015 Yuri N. Sedunov <aris@altlinux.org> 1.44.0-alt1
- 1.44.0-10-g967d696

* Fri Jan 23 2015 Yuri N. Sedunov <aris@altlinux.org> 1.43.3-alt1
- 1.43.3

* Tue Sep 30 2014 Yuri N. Sedunov <aris@altlinux.org> 1.42.0-alt1
- 1.42.0

* Tue Sep 02 2014 Yuri N. Sedunov <aris@altlinux.org> 1.41.91-alt1
- 1.41.91

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.40.1-alt1
- 1.40.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 1.40.0-alt1
- 1.40.0

* Sun Jan 26 2014 Yuri N. Sedunov <aris@altlinux.org> 1.38.1-alt2
- new -tests subpackage

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.38.1-alt1
- 1.38.1

* Mon Apr 22 2013 Yuri N. Sedunov <aris@altlinux.org> 1.36.1-alt1
- 1.36.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 1.36.0-alt1
- 1.36.0

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.34.0-alt1
- 1.34.0

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 1.32.0-alt1
- 1.32.0

* Sat Jan 14 2012 Yuri N. Sedunov <aris@altlinux.org> 1.30.1-alt1
- 1.30.1

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 1.30.0-alt1
- 1.30.0

* Mon Sep 05 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.14-alt5
- rebuilt against libmozjs-1.8.5 not xulrunner.

* Thu Aug 25 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.14-alt4
- Rebuild against new xulrunner 6.0.
- disabled tests temporarily.

* Tue Aug 02 2011 Paul Wolneykien <manowar@altlinux.ru> 0.7.14-alt3
- Rebuild against new xulrunner 5.0.
- Use patches related to GNOME bug #646471.

* Sun Apr 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.14-alt2
- rebuilt against new xulrunner-2.0

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.14-alt1
- 0.7.14

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.13-alt1
- 0.7.13

* Wed Feb 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.11-alt1
- 0.7.11

* Wed Jan 26 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.10-alt1
- 0.7.10

* Wed Oct 06 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.4-alt1
- 0.7.4

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- 0.7.3

* Sun Aug 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Fri Mar 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- 0.6

* Sat Mar 13 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt2
- build current snapshot
- updated buildreqs

* Tue Feb 16 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- 0.4

* Thu Aug 13 2009 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- adapted for Sisyphus

* Fri Aug  7 2009 Peter Robinson <pbrobinson@gmail.com> 0.3-2
- Updates from the review request

* Wed Jul  8 2009 Peter Robinson <pbrobinson@gmail.com> 0.3-1
- New upstream release. Clarify licensing for review

* Sat Jun 27 2009 Peter Robinson <pbrobinson@gmail.com> 0.2-1
- Initial packaging

%define ver_major 0.8
%define real_name gtkmathview

Name: lib%real_name
Version: %ver_major.0
Release: alt4.1

Summary: A MathML rendering library
License: LGPL
Group: System/Libraries
Url: http://www.gnome.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%real_name-%version.tar.gz

Packager: Damir Shayhutdinov <damir@altlinux.ru>

Patch1: gtkmathview-0.7.7-without-binreloc.patch
Patch2: gtkmathview-0.7.7-stdcpp-link-fix.patch
Patch3: gtkmathview-0.7.7-link-backends-fix.patch
Patch4: gtkmathview-0.8.0-alt-fix-linking.patch
Patch5: gtkmathview-0.8.0-alt-fix-pkgconfig.patch
Patch6: libgtkmathview-0.8.0-debian-gcc43-fix.patch
Patch7: gtkmathview-0.8.0-alt-DSO.patch

%define gtk_ver 2.2.4
%define libxml2_ver 2.5.6

BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildPreReq: libxml2-devel >= %libxml2_ver


BuildRequires: gcc-c++ libpopt-devel t1lib-devel xsltproc

%description
GtkMathView is a C++ rendering engine for MathML documents. 
It provides an interactive view that can be used for browsing 
and editing MathML markup.

%package -n %name-devel
Summary: Libraries, headers, and support files needed for using gtkmathview.
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Requires: libgtk+2-devel >= %gtk_ver
Requires: libxml2-devel >= %libxml2_ver

%description -n %name-devel
Libraries, headers, and support files needed for using gtkmathview.

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup -q -n %real_name-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p2

%build
autoreconf -fisv
%configure --with-t1lib=yes
	
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name-1.0

%files -f %name-1.0.lang
%_bindir/mathmlsvg
%_bindir/mathmlps
%_libdir/*.so.*
%_datadir/%real_name
%_man1dir/mathml*
%dir %_sysconfdir/%real_name
%config(noreplace) %_sysconfdir/%real_name/*.xml
%doc AUTHORS ChangeLog NEWS README

%files -n %name-devel
%_includedir/%real_name/*
%_libdir/*.so
%exclude %_libdir/*.a
%_libdir/pkgconfig/*.pc
%doc AUTHORS README BUGS CONTRIBUTORS NEWS ANNOUNCEMENT TODO


%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt4.1
- Fixed build

* Wed Nov 10 2010 Damir Shayhutdinov <damir@altlinux.ru> 0.8.0-alt4
- Rebuilt to generate symbol provides
- Cleaned up spec a bit
- Updated buildreq

* Tue Jun 09 2009 Damir Shayhutdinov <damir@altlinux.ru> 0.8.0-alt3
- fixed build on gcc4.4 

* Tue Nov 25 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.8.0-alt2
- Fixed build on gcc4.3
- Removed obsolete ldconfig calls

* Sun Oct 21 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.8.0-alt1
- New version.

* Fri Oct 06 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.7.7-alt1
- New version.

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.7.6-alt1.1
- Rebuilt for new pkg-config dependencies.

* Wed Dec 14 2005 Vital Khilko <vk@altlinux.ru> 0.7.6-alt1
- initial build


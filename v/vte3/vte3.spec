%def_disable snapshot

%define _name vte
%define ver_major 0.46
%define api_ver 2.91

Name: %{_name}3
Version: %ver_major.1
Release: alt1

%def_disable static
%def_enable introspection
%def_enable gtk_doc
%def_disable glade
%def_enable pcre2

Summary: Terminal emulator widget for use with GTK+
License: LGPL
Group: Terminals

Requires: lib%name = %version-%release

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

%define gtk3_ver 3.8.0
%define glib_ver 2.40.0
%define pango_ver 1.22
%define gir_ver 0.10.2
%define tls_ver 3.2.7

BuildPreReq: rpm-build-python

BuildRequires: gcc-c++ gperf
BuildRequires: libncurses-devel libcairo-devel
BuildRequires: intltool >= 0.35.0
BuildRequires: gtk-doc >= 1.1.0
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk3_ver
BuildRequires: libpango-devel >= %pango_ver
BuildRequires: libgnutls-devel >= %tls_ver
BuildRequires: vala-tools libvala-devel
%{?_enable_pcre2:BuildRequires: libpcre2-devel}
%{?_enable_glade:BuildRequires: libgladeui2.0-devel}
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= %gir_ver libgtk+3-gir-devel}

%description
VTE is a terminal emulator widget for use with GTK+

%package utils
Summary: VTE utilities and test programs
Group: Terminals
Requires: lib%name = %version-%release

%description utils
Utilities, samples and test programs distributed with VTE, a terminal
emulator widget for use with GTK+3.

%package -n lib%name
Summary: Terminal emulator widget library for use with GTK+3
Group: System/Libraries

%description -n lib%name
VTE is a terminal emulator widget for use with GTK+3.
This package contains the VTE shared libraries.

%package -n lib%name-devel
Summary: Development files for VTE
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
VTE is a terminal emulator widget for use with GTK+3. This package
contains the files needed for building applications using VTE.

%package -n lib%name-devel-doc
Summary: Development documentation for VTE
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
API documentation for the VTE library.
VTE is a terminal emulator widget for use with GTK+3.

%if_enabled static
%package -n lib%name-devel-static
Summary: Static libraries for VTE
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
VTE is a terminal emulator widget for use with GTK+3. This package
contains the libraries needed for building applications statically
linked with VTE.
%endif	# enabled static

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library


%define pkgdocdir %_docdir/%name-%version

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
	--enable-shared \
	%{subst_enable static} \
	%{subst_enable introspection} \
	%{?_enable_gtk_doc:--enable-gtk-doc}
#	%{subst_enable glade}
%make_build

%install
%makeinstall_std
# fix permissions
chmod 755 %buildroot%_sysconfdir/profile.d/vte.sh

install -d -m755 %buildroot%pkgdocdir
install -p -m644 AUTHORS NEWS README %buildroot%pkgdocdir/
ln -s %_licensedir/LGPL-2 %buildroot%pkgdocdir/COPYING

install -p -m644 doc/*.txt %buildroot%pkgdocdir/
install -p -m644 src/iso2022.txt %buildroot%pkgdocdir/
install -p -m644 doc/openi18n/*.txt %buildroot%pkgdocdir/

# Remove unpackaged files
find %buildroot -type f -name '*.la' -delete

%find_lang %_name-%api_ver --output=%name.lang

%files
%_bindir/*

%files -n lib%name -f %name.lang
%dir %pkgdocdir
%pkgdocdir/AUTHORS
%pkgdocdir/COPYING
%pkgdocdir/NEWS
%pkgdocdir/README
%_libdir/*.so.*
%_sysconfdir/profile.d/vte.sh

%files -n lib%name-devel
%pkgdocdir/*.txt
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/%_name-%api_ver.pc
%_vapidir/vte-%api_ver.vapi
#%{?_enable_glade:}

%files -n lib%name-devel-doc
%doc %_datadir/gtk-doc/html/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif	# enabled static

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/Vte-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Vte-%api_ver.gir
%endif

%changelog
* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 0.46.1-alt1
- 0.46.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 0.46.0-alt1
- 0.46.0

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.44.2-alt1
- 0.44.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 0.44.1-alt1
- 0.44.1

* Sat Mar 19 2016 Yuri N. Sedunov <aris@altlinux.org> 0.44.0-alt1
- 0.44.0

* Tue Mar 15 2016 Yuri N. Sedunov <aris@altlinux.org> 0.42.5-alt1
- 0.42.5

* Thu Feb 11 2016 Yuri N. Sedunov <aris@altlinux.org> 0.42.4-alt1
- 0.42.4

* Thu Jan 28 2016 Yuri N. Sedunov <aris@altlinux.org> 0.42.3-alt1
- 0.42.3

* Thu Jan 28 2016 Yuri N. Sedunov <aris@altlinux.org> 0.42.1-alt3
- fised permissions for %%_sysconfdir/profile.d/vte.sh

* Wed Dec 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.42.1-alt2
- rebuilt against libgnutls.so.30

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 0.42.1-alt1
- 0.42.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 0.42.0-alt1
- 0.42.0

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 0.40.2-alt1
- 0.40.2

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 0.40.0-alt1
- 0.40.0

* Tue Dec 16 2014 Yuri N. Sedunov <aris@altlinux.org> 0.38.3-alt1
- 0.38.3

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.38.2-alt1
- 0.38.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 0.38.1-alt1
- 0.38.1

* Sun Sep 14 2014 Yuri N. Sedunov <aris@altlinux.org> 0.38.0-alt1
- 0.38.0

* Fri Jun 27 2014 Yuri N. Sedunov <aris@altlinux.org> 0.36.3-alt1
- 0.36.3

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 0.36.2-alt1
- 0.36.2

* Sat Apr 26 2014 Yuri N. Sedunov <aris@altlinux.org> 0.36.1-alt1
- 0.36.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 0.36.0-alt1
- 0.36.0

* Tue Mar 18 2014 Yuri N. Sedunov <aris@altlinux.org> 0.35.90-alt1
- 0.35.90

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 0.34.9-alt1
- 0.34.9

* Tue Sep 17 2013 Yuri N. Sedunov <aris@altlinux.org> 0.34.8-alt1
- 0.34.8

* Sun Jul 07 2013 Yuri N. Sedunov <aris@altlinux.org> 0.34.7-alt1
- 0.34.7

* Mon Jun 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.34.6-alt1
- 0.34.6

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 0.34.5-alt1
- 0.34.5

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 0.34.4-alt1
- 0.34.4

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 0.34.3-alt1
- 0.34.3

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 0.34.2-alt1
- 0.34.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.34.1-alt1
- 0.34.1

* Mon Sep 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.34.0-alt1
- 0.34.0

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.33.90-alt1
- 0.33.90

* Wed May 30 2012 Yuri N. Sedunov <aris@altlinux.org> 0.32.2-alt1
- 0.32.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.32.1-alt1
- 0.32.1

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.32.0-alt1
- 0.32.0

* Wed Nov 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.30.1-alt2
- applied patch proposed in
  http://bugzilla-attachments.gnome.org/attachment.cgi?id=201649
  (ALT #26611)

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0.30.1-alt1
- 0.30.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 0.30.0-alt1
- 0.30.0

* Mon Aug 29 2011 Yuri N. Sedunov <aris@altlinux.org> 0.28.2-alt1
- 0.28.2

* Wed Jun 15 2011 Yuri N. Sedunov <aris@altlinux.org> 0.28.1-alt1
- 0.28.1

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 0.28.0-alt1
- 2.28.0

* Thu Feb 24 2011 Yuri N. Sedunov <aris@altlinux.org> 0.27.90-alt1
- first build for Sisyphus.


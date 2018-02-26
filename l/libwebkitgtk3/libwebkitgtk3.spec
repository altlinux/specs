%set_verify_elf_method textrel=relaxed
%define _gtk_docdir %_datadir/gtk-doc/html
%define _libexecdir %_prefix/libexec
%define gtk_ver 3.0

%define oname webkit
# freetype/pango
%define font_backend freetype
# no/opengl/cairo/clutter
%define accelerated_compositing no
%def_enable introspection
%def_enable geolocation
%def_disable directory_upload
%def_disable file_system
%def_disable indexed_database
%def_disable input_color
%def_disable input_speech
%def_enable style_scoped
%def_enable webgl
%def_enable coverage
%def_disable web_timing
%def_disable web_audio
%def_enable blob
%def_disable media_source
%def_disable media_stream
%def_disable media_statistics
%def_enable spellcheck
%def_disable notifications
%def_enable meter_tag
%def_enable page_visibility_api
%def_enable progress_tag
%def_enable link-prefetch
%def_enable animation_api
%def_disable webkit2

Summary: Web browser engine
Name: libwebkitgtk3
Version: 1.8.1
Release: alt2
License: %bsd %lgpl2plus
Group: System/Libraries
Url: http://www.webkitgtk.org/
Source: %oname-%version.tar
# Patch1: %name-%version-fix-build.patch
# Patch2: webkit-1.6.1-alt-fix-TEXTREL.patch
Patch3: webkit-1.8.1-fix-rpath.patch
Patch100: changeset_r109329.diff

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Requires: libjavascriptcoregtk3 = %version-%release
BuildPreReq: rpm-build-licenses

BuildRequires: gcc-c++ libicu-devel bison perl-Switch zlib-devel

BuildRequires: flex >= 2.5.33
BuildRequires: gperf libjpeg-devel libpng-devel
BuildRequires: libxml2-devel >= 2.6
BuildRequires: libXt-devel
BuildRequires: libgtk+3-devel >= 3.0
BuildRequires: libgail3-devel >= 3.0
BuildRequires: libenchant-devel >= 0.22
BuildRequires: libsqlite3-devel >= 3.0
BuildRequires: libxslt-devel >= 1.1.7
BuildRequires: gstreamer-devel >= 0.10 gst-plugins-devel >= 0.10.30
BuildRequires: librsvg-devel >= 2.2.0
BuildRequires: gtk-doc >= 1.10
BuildRequires: libsoup-devel >= 2.37.92
BuildRequires: libpango-devel >= 1.21.0 libcairo-devel >= 1.10 libcairo-gobject-devel
BuildRequires: libgio-devel >= 2.25.0
BuildRequires: python-modules-json

%if %font_backend == freetype
BuildRequires: fontconfig-devel >= 2.4 libfreetype-devel
%endif
%if %accelerated_compositing == clutter
BuildRequires: libclutter-devel >= 1.8.2
BuildRequires: libclutter-gtk3-devel >= 1.0.2
%endif
%if %accelerated_compositing == opengl
BuildRequires: libGL-devel
%endif

%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 0.9.5 libgtk+3-gir-devel libsoup-gir-devel}
%{?_enable_geolocation:BuildPreReq: libgeoclue-devel}
%{?_enable_spellcheck:BuildPreReq: libenchant-devel}
%{?_enable_webgl:BuildPreReq: libGL-devel}
%{?_enable_webkit2:BuildPreReq: libat-spi2-core-devel >= 2.2.1  libgtk+2-devel libgail-devel}

%description
WebKit is an open source web browser engine.
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package devel
Summary: Development files for WebKit GTK+ port
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Requires: libjavascriptcoregtk3-devel = %version-%release

%description devel
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

This package provides development documentation for %name.

%package -n libjavascriptcoregtk3
Summary: GTK+3 version of the JavaScriptCore engine
Group: System/Libraries

%description -n libjavascriptcoregtk3
This package provides GTK+3 version of the JavaScriptCore engine from
WebKit package.

%package -n libjavascriptcoregtk3-devel
Summary: Development files for JavaScriptCore library
Group: Development/GNOME and GTK+
Requires: libjavascriptcoregtk3 = %version-%release

%description -n libjavascriptcoregtk3-devel
This package provides development files for GTK+3 version of the
JavaScriptCore engine.

%package -n libwebkit2gtk
Summary: WebKit2 is a new API layer for WebKit
Group: System/Libraries
Requires: libjavascriptcoregtk3 = %version-%release

%description -n libwebkit2gtk
WebKit2 is a new API layer for WebKit designed from the ground up to support a split process model,
where the web content (JavaScript, HTML, layout, etc) lives in a separate process from the application UI.
This model is very similar to what Google Chrome offers, with the major difference being
that we have built the process split model directly into the framework, allowing other clients of WebKit to use it.

%package -n libwebkit2gtk-devel
Summary: WebKit2 is a new API layer for WebKit
Group: Development/GNOME and GTK+
Requires: libjavascriptcoregtk3-devel = %version-%release

%description -n libwebkit2gtk-devel
WebKit2 is a new API layer for WebKit designed from the ground up to support a split process model,
where the web content (JavaScript, HTML, layout, etc) lives in a separate process from the application UI.
This model is very similar to what Google Chrome offers, with the major difference being
that we have built the process split model directly into the framework, allowing other clients of WebKit to use it.


%package jsc
Summary: JavaScriptCore shell for WebKit GTK+
Group: Development/GNOME and GTK+
Requires: libjavascriptcoregtk3 = %version-%release

%description jsc
jsc is a shell for JavaScriptCore, WebKit's JavaScript engine. It
allows you to interact with the JavaScript engine directly.

%package webinspector
Summary: Data files for WebKit GTK+'s Web Inspector
Group: Development/GNOME and GTK+

%description webinspector
WebKit GTK+ has a feature called the Web Inspector, which allows
detailed analysis of any given page's page source, live DOM hierarchy
and resources. This package contains the data files necessary for Web
Inspector to work.

%package gir
Summary: GObject introspection data for the WebkitGTK library
Group: System/Libraries
Requires: %name = %version-%release
Requires: libjavascriptcoregtk3 = %version-%release
Requires: libjavascriptcoregtk3-gir  = %version-%release

%description gir
GObject introspection data for the WebkitGTK library

%package gir-devel
Summary: GObject introspection devel data for the WebkitGTK library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: libjavascriptcoregtk3-gir = %version-%release
Requires: libjavascriptcoregtk3-devel = %version-%release
Requires: libjavascriptcoregtk3-gir-devel = %version-%release

%description gir-devel
GObject introspection devel data for the WebkitGTK library

%package -n libjavascriptcoregtk3-gir
Summary: GObject introspection data for the JavaScriptCore library
Group: System/Libraries
Requires: libjavascriptcoregtk3 = %version-%release

%description -n libjavascriptcoregtk3-gir
GObject introspection data for the JavaScriptCore library

%package -n libjavascriptcoregtk3-gir-devel
Summary: GObject introspection devel data for the JavaScriptCore library
Group: System/Libraries
BuildArch: noarch
Requires: libjavascriptcoregtk3-gir = %version-%release
Requires: libjavascriptcoregtk3-devel = %version-%release

%description -n libjavascriptcoregtk3-gir-devel
GObject introspection devel data for the JavaScriptCore library

%prep
%setup -q -n %oname-%version
#%patch1 -p1
#%patch2 -p1
# %patch3 -p1
%patch100 -p2
# fix build translations
%__subst 's|^all-local:|all-local: stamp-po|' GNUmakefile.am
rm -f Source/autotools/{compile,config.guess,config.sub,depcomp,install-sh,ltmain.sh,missing,libtool.m4,ltoptions.m4,ltsugar.m4,ltversion.m4,lt~obsolete.m4,gsettings.m4,gtk-doc.m4}

%build
gtkdocize --copy
%autoreconf -I Source/autotools

%configure \
	--enable-video \
	--with-font-backend=%font_backend \
	--with-accelerated-compositing=%accelerated_compositing \
	--with-gstreamer=0.10 \
	%{subst_enable introspection} \
	%{subst_enable geolocation} \
	%{subst_enable coverage} \
	%{subst_enable blob} \
	%{subst_enable spellcheck} \
	%{?_enable_indexed_database:--enable-indexed-database} \
	%{?_enable_input_color:--enable-input-color} \
	%{?_enable_input_speech:--enable-input-speech} \
	%{?_enable_style_scoped:--enable-style-scoped} \
	%{?_enable_directory_upload:--enable-directory-upload} \
	%{?_enable_file_system:--enable-file-system} \
	%{subst_enable webgl} \
	%{?_enable_web_timing:--enable-web-timing} \
	%{?_enable_web_audio:--enable-web-audio} \
	%{?_enable_media_source:--enable-media-source} \
	%{?_enable_media_stream:--enable-media-stream} \
	%{?_enable_media_statistics:--enable-media-statistics} \
	%{subst_enable notifications} \
	%{?_enable_page_visibility_api:--enable-page-visibility-api} \
	%{?_enable_meter_tag:--enable-meter-tag} \
	%{?_enable_progress_tag:--enable-progress-tag} \
	%{?_enable_link_prefetch:--enable-link-prefetch} \
	%{?_enable_animation_api:--enable-animation-api} \
	%{subst_enable webkit2} \
	--with-gtk=%gtk_ver

mkdir -p DerivedSources/webkit
mkdir -p DerivedSources/ANGLE
mkdir -p DerivedSources/WebKit2/webkit2gtk/webkit2
mkdir -p DerivedSources/InjectedBundle

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --output=webkitgtk.lang webkit-%gtk_ver

%files -f webkitgtk.lang
%_libdir/libwebkitgtk-3.0.so.*
%dir %_datadir/webkitgtk-3.0
%_datadir/webkitgtk-3.0/images
%_datadir/webkitgtk-3.0/resources

%files devel
%_libdir/libwebkitgtk-3.0.so
%dir %_includedir/webkitgtk-3.0
%_includedir/webkitgtk-3.0/webkit
%_pkgconfigdir/webkitgtk-3.0.pc

%files devel-doc
%_gtk_docdir/*

%files -n libjavascriptcoregtk3
%_libdir/libjavascriptcoregtk-3.0.so.*

%files -n libjavascriptcoregtk3-devel
%_includedir/webkitgtk-3.0/JavaScriptCore
%_libdir/libjavascriptcoregtk-3.0.so
%_pkgconfigdir/javascriptcoregtk-3.0.pc

%if_enabled webkit2
%files -n libwebkit2gtk
%_libdir/libwebkit2gtk-3.0.so.*
%_libexecdir/WebKitPluginProcess
%_libexecdir/WebKitWebProcess

%files -n libwebkit2gtk-devel
%_libdir/libwebkit2gtk-3.0.so
%_includedir/webkitgtk-3.0/webkit2
%_pkgconfigdir/webkit2gtk-3.0.pc
%endif

%files jsc
%_bindir/jsc*

%files webinspector
%_datadir/webkitgtk-3.0/webinspector

%if_enabled introspection
%files gir
%_typelibdir/WebKit-3.0.typelib

%files gir-devel
%_girdir/WebKit-3.0.gir

%files -n libjavascriptcoregtk3-gir
%_typelibdir/JSCore-3.0.typelib

%files -n libjavascriptcoregtk3-gir-devel
%_girdir/JSCore-3.0.gir
%endif

%changelog
* Fri May 25 2012 Alexey Shabalin <shaba@altlinux.ru> 1.8.1-alt2
- update and cleanup configure option
- enable some features:
  + page-visibility-api
  + style-scoped
  + link-prefetch
  + animation-api
- add and fixed webkit2 support, but not enable; welcome for tests

* Fri May 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Wed Mar 28 2012 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Tue Feb 07 2012 Alexey Shabalin <shaba@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Wed Feb 01 2012 Alexey Shabalin <shaba@altlinux.ru> 1.6.2-alt1
- 1.6.2
- drop upstreamed patch3

* Fri Oct 28 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt4
- add %%set_verify_elf_method textrel=relaxed and don't apply patch2

* Thu Oct 27 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt3
- fix webkit.pc

* Tue Oct 25 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt2
- add javascriptcoregtk3* subpackages

* Mon Oct 17 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Wed Aug 31 2011 Alexey Shabalin <shaba@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Tue Jul 12 2011 Alexey Shabalin <shaba@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Fri Apr 29 2011 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Tue Mar 22 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3.13-alt1
- 1.3.13

* Thu Mar 10 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3.12-alt1
- 1.3.12
- disable image resize
- update conditions

* Thu Jan 20 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3.10-alt1
- 1.3.10
- enable blob

* Wed Dec 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.3.7-alt1
- 1.3.7
- enable mathml, 3D-transforms, geolocation, coverage

* Mon Oct 04 2010 Alexey Shabalin <shaba@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Mon Jul 19 2010 Alexey Shabalin <shaba@altlinux.ru> 1.3.3-alt1
- 1.3.3
- build with libgtk+3
- rename to libwebkitgtk3

* Sun Jul 18 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.3-alt1
- 1.2.3
- disable patch1(webkit-1.1.23-alt-icu4.4.patch); upstream fixed
- fixed the following CVEs (thanks to the Debian security team):
  + CVE-2010-1386 CVE-2010-1392 CVE-2010-1405 CVE-2010-1407
  + CVE-2010-1416 CVE-2010-1417 CVE-2010-1665 CVE-2010-1418
  + CVE-2010-1421 CVE-2010-1422 CVE-2010-1501 CVE-2010-1767
  + CVE-2010-1664 CVE-2010-1758 CVE-2010-1759 CVE-2010-1760
  + CVE-2010-1761 CVE-2010-1762 CVE-2010-1770 CVE-2010-1771
  + CVE-2010-1772 CVE-2010-1773 CVE-2010-1774

* Tue May 18 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Thu Apr 22 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- current stable release 1.2.0

* Tue Mar 30 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1.90-alt1
- 1.1.90

* Mon Mar 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1.23-alt2
- rebuild with icu-4.4
- disable Patch0 WebKit-alt-plugins.patch

* Fri Mar 12 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1.23-alt1
- 1.1.23
- package gir-devel as noarch

* Wed Feb 24 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1.22-alt1
- 1.1.22

* Tue Feb 09 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1.21-alt1
- 1.1.21
- new gir{,-devel} subpackages

* Thu Dec 03 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.15.4-alt1
- 1.1.15.4

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.15.3-alt1
- 1.1.15.3

* Fri Oct 09 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.15.2-alt1
- 1.1.15.2

* Wed Sep 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.15.1-alt1
- 1.1.15.1

* Thu Sep 10 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.14-alt1
- 1.1.14

* Tue Aug 25 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.13-alt1
- release 1.1.13

* Thu Aug 20 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.12-alt1.r46499
- 1.1.12
- nightly builds r46499

* Tue Jul 14 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.11-alt1.r45855
- nightly builds r45855
- fixed CVE-2009-1724, CVE-2009-1725, webkit: #27136,#27110,#26918,#27071 (ALT#20761)

* Tue Jun 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.10-alt2.r44815
- rebuild with libpng12

* Sat Jun 20 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.10-alt1.r44815
- nightly builds r44815
- drop gtklauncher package
- build with freetype font backend

* Thu May 14 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.7-alt1.r43663
- nightly builds r43663

* Wed May 06 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.6-alt1.r43284
- nightly builds r43284

* Tue May 05 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.6-alt1.r43000
- nightly builds r43000
- update BuildRequires

* Sun Apr 05 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.4-alt1.r42162
- nightly builds r42162
- update buildrequires
- build with gnome-keyring support
- thx to shrek@ :
  + fixed plugins path
  + fixed install GtkLauncher

* Fri Jan 16 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1.r39953
- nightly builds 39953
- webinspector package

* Mon Dec 08 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1.r39060
- nightly builds 39090
- drop obsolete post scripts

* Sat Oct 25 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt0.3.r37790
- nightly builds 37790
- http_backend soup
- font_backend pango

* Sun Sep 07 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt0.2.r36247
- nightly builds 36247

* Mon Sep 01 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt0.2.r35933
- nightly builds r35933

* Fri Aug 22 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt0.2.r35417
- fix build for x86_64
- define libexecdir as /usr/libexec

* Thu Aug 21 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt0.1.r35417
- 1.0.2 (r35704)
- cleanup spec
- rename package from libwebkit-gtk to libwebkit
- add package %name-gtklauncher and %name-jsc

* Tue Mar 11 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.r30716-alt1 
- new version
- libWebKitGtk.so placed into -devel package.
- changed includes dir

* Fri Nov 16 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.r27953-alt1 
- initital build.


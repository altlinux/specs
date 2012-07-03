# vim: set ft=spec: -*- rpm-spec -*-
# TODO: create-native-map - ? 

%def_with gtkhtml
# gecko-sharp don't worked with libxul-1.9(firefox-3)
%def_without gecko
%def_with webkit

Name: mono-tools
Version: 2.10
Release: alt1

Summary: Mono Tools is a collection of utility programs for Mono
License: %gpllgpl2only
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
URL: http://www.mono-project.com/
Source0: http://go-mono.com/sources/%name/%name-%version.tar
Source2: gnunit2.desktop
Source3: monodoc.filetrigger

Patch1: %name-%version-alt-monodoc.patch
Patch2: %name-%version-alt-cecil.patch

Requires: desktop-file-utils
Requires: monodoc-browser

BuildPreReq: rpm-build-mono rpm-build-licenses
BuildPreReq: intltool libtool
BuildPreReq: desktop-file-utils
BuildPreReq: mono-mcs mono-nunit-devel monodoc-devel
BuildPreReq: glib2-devel
BuildPreReq: libgtk-sharp2-devel libgnome-sharp-devel
BuildPreReq: mono-winforms mono-extras mono-data-oracle mono-csharp

%{?_with_gtkhtml:BuildPreReq: libgnome-desktop-sharp-devel}
%{?_with_gecko:BuildPreReq: libgecko-sharp2-devel}
%{?_with_webkit:BuildPreReq: libwebkit-sharp-devel}

BuildRequires: mono-devel >= %version
BuildRequires: /proc

%description
Mono Tools is a collection of development and testing programs and 
utilities for use with Mono.

%package devel
Summary: Mono Tools is a collection of utility programs for Mono
Group: Development/Other
Requires: %name = %version-%release

%description devel
Mono Tools is a collection of development and testing programs and 
utilities for use with Mono.

This package contains development pkg-config files for %name

%package -n monodoc-browser
Summary: MonoDoc GTK+ based viewer
Group: Development/Other
Requires: monodoc-browser-render = %version-%release

%description -n monodoc-browser
This package contains the GTK+ based viewer of the Mono documentation.

%package -n monodoc-browser-gtkhtml
Summary: Gtkhtml render for monodoc-browser
Group: Development/Other
Provides: monodoc-browser-render = %version-%release

%description -n monodoc-browser-gtkhtml
Gtkhtml render for monodoc-browser.

%package -n monodoc-browser-webkit
Summary: Webkit render for monodoc-browser
Group: Development/Other
Provides: monodoc-browser-render = %version-%release

%description -n monodoc-browser-webkit
Webkit render for monodoc-browser.

%package -n monodoc-browser-gecko
Summary: Gecko render for monodoc-browser
Group: Development/Other
Provides: monodoc-browser-render = %version-%release

%description -n monodoc-browser-gecko
Gecko render for monodoc-browser.

%package -n monodoc-browser-monowebbrowser
Summary: MonoWebBrowser render for monodoc-browser
Group: Development/Other
Provides: monodoc-browser-render = %version-%release

%description -n monodoc-browser-monowebbrowser
MonoWebBrowser render for monodoc-browser.

%package -n monodoc-browser-webdoc
Summary: Webdoc for monodoc
Group: Development/Other
BuildArch: noarch
Provides: monodoc-browser-render = %version-%release

%description -n monodoc-browser-webdoc
Web pages for HTTP server(xsp or mod_mono or monodoc server).

%package doc
Summary: Documentation for mono-tools
Group: Documentation
BuildArch: noarch
Requires: monodoc >= 2.2

%description doc
This package contains the documentation for the mono-tools class libraries(Gendarme.Framework and other Gendarme.*)

%prep
%setup -q
%patch1 -p1
%patch2 -p1

subst "s|^pkgconfigdir *= \$(prefix)/lib/pkgconfig|pkgconfigdir = %_pkgconfigdir|" \
	gendarme/framework/Makefile.am \
	create-native-map/lib/pkgconfig/Makefile.am
subst 's|^libdir=@libdir@|libdir=${prefix}/lib|' create-native-map/lib/pkgconfig/create-native-map.pc.in
subst "s|^assemblydir = \$(libdir)/ilcontrast|assemblydir = \$(prefix)/lib/ilcontrast|" ilcontrast/Makefile.am
#subst "s|^programfilesdir = @libdir@/@PACKAGE@|programfilesdir = \$(prefix)/lib/@PACKAGE@|" Mono.Profiler/Makefile.include
subst "s|^pkglib_DATA|pkglibexec_DATA |" Mono.Profiler/{profiler-decoder-library,Mono.Profiler.Widgets,heap-snapshot-explorer,heap-snapshot-viewer,mprof-gui,profiler-file-decoder}/Makefile.am

%build
glib-gettextize --force --copy
%autoreconf
%configure --enable-release

%make

%install
%make_install DESTDIR=%buildroot install
%find_lang %name
mkdir asn1view.doc && ln -s ../asn1view/{AUTHORS,ChangeLog,README,TODO} asn1view.doc
mkdir docbrowser.doc && ln -s ../docbrowser/ChangeLog docbrowser.doc
mkdir gnunit.doc && ln -s ../gnunit/{AUTHORS,ChangeLog,README,TODO} gnunit.doc

install -p -m644 %SOURCE2 %buildroot%_desktopdir/

# posttrans filetrigger 
install -pD -m755 %SOURCE3 %buildroot%_rpmlibdir/monodoc.filetrigger
install -pD -m644 /dev/null %buildroot%_datadir/monodoc/monodoc.index

%files -f %name.lang
%doc AUTHORS ChangeLog README asn1view.doc docbrowser.doc
%_bindir/*
%_prefix/lib/mono/*
%_prefix/lib/mono-tools
%_prefix/lib/gendarme
%_prefix/lib/gui-compare
%_prefix/lib/ilcontrast
%_prefix/lib/gsharp
%_prefix/lib/mperfmon
%_prefix/lib/minvoke
%_prefix/lib/create-native-map
%_man1dir/*
%_man5dir/*
%_pixmapsdir/*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*
%exclude %_bindir/monodoc

%files devel
%_pkgconfigdir/*.pc

%files -n monodoc-browser
%_bindir/monodoc
%_prefix/lib/monodoc/browser.exe
%_rpmlibdir/monodoc.filetrigger
%ghost %_datadir/monodoc/monodoc.index

%if_with gtkhtml
%files -n monodoc-browser-gtkhtml
%_prefix/lib/monodoc/GtkHtmlHtmlRender.dll
%endif

%if_with webkit
%files -n monodoc-browser-webkit
%_prefix/lib/monodoc/WebKitHtmlRender.dll
%endif

%if_with gecko
%files -n monodoc-browser-gecko
%_prefix/lib/monodoc/GeckoHtmlRender.dll
%endif

%files -n monodoc-browser-monowebbrowser
%_prefix/lib/monodoc/MonoWebBrowserHtmlRender.dll

%files -n monodoc-browser-webdoc
%_datadir/monodoc/web

%files doc
%_monodocdir/*

%changelog
* Wed Oct 12 2011 Alexey Shabalin <shaba@altlinux.ru> 2.10-alt1
- 2.10

* Tue Nov 23 2010 Alexey Shabalin <shaba@altlinux.ru> 2.8-alt1
- 2.8

* Wed Mar 17 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Sun Dec 20 2009 Alexey Shabalin <shaba@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Wed Dec 16 2009 Alexey Shabalin <shaba@altlinux.ru> 2.6-alt1
- 2.6

* Mon Dec 14 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.2-alt2
- update buildreq

* Wed Jul 01 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.2-alt1
- 2.4.2
- move pkg-config files to devel package
- add monodoc-browser-webdoc package

* Mon Apr 13 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4-alt1
- 2.4

* Thu Jan 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1
- 2.2
- remove deprecated pre/post macros
- build with gtkhtml, gecko, webkit (in separated packages)
- add doc package
- add %%_rpmlibdir/monodoc.filetrigger

* Sat Oct 25 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt4
- rebuild with gnome-sharp-2.24

* Wed Oct 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt3
- fix build for x86_64 (define libdir as %_prefix/lib)

* Tue Oct 07 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt2
- 2.0 release

* Mon Sep 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1.pre2
- 2.0 preview2

* Tue Aug 12 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1.pre1
- 2.0 preview1

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 1.9-alt3.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for mono-tools

* Fri Mar 28 2008 Alexey Shabalin <shaba@altlinux.ru> 1.9-alt3
- fix ilcontrast path (for x86_64)

* Thu Mar 27 2008 Alexey Shabalin <shaba@altlinux.ru> 1.9-alt2
- fix build for x86_64

* Thu Mar 20 2008 Alexey Shabalin <shaba@altlinux.ru> 1.9-alt1
- Update to 1.9
- use system cecil (patch1)

* Mon Dec 17 2007 Alexey Shabalin <shaba@altlinux.ru> 1.2.6-alt1
- Update to 1.2.6
- update buildreqiures

* Sat Jul 28 2007 Alexey Shabalin <shaba@altlinux.ru> 1.2.4-alt1
- Update to 1.2.4

* Thu Oct 19 2006 Ildar Mulyukov <ildar@altlinux.ru> 1.1.17-alt1
- rpm-build-mono support
- turned off gecko support

* Fri Apr 14 2006 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.11-alt2
- Fix x86_64 build

* Wed Feb 22 2006 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.11-alt1
- Update to release

* Sat Nov 26 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.10-alt1
- Update to release

* Tue Oct 11 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.9-alt1
- Update to release

* Fri Aug 05 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.0-alt1
- Initial Release 


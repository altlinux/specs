%define realname gtk-sharp
%def_disable doc

Summary: GTK+ and GNOME bindings for Mono
Name: lib%{realname}2
Version: 2.12.11
Release: alt1
License: LGPLv2+
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Url: http://www.mono-project.com/
Source: http://ftp.gnome.org/pub/GNOME/sources/%realname/2.12/%name-%version.tar

Patch0: %name-%version-%release.patch

Requires: libglade libgtk+2 >= 2.12.0

BuildPreReq: glib2-devel >= 2.12.0
BuildPreReq: libpango-devel
BuildPreReq: libatk-devel
BuildPreReq: libgtk+2-devel >= 2.12.0
BuildPreReq: libglade-devel >= 2.3.6
BuildPreReq: rpm-build-mono perl-XML-LibXML

BuildRequires: gcc-c++ mono-devel mono-mcs
%{?_enable_doc:BuildRequires: monodoc-devel}
BuildRequires: /proc

%description
This package provides a library that allows you to build
fully native graphical GNOME applications using Mono. Gtk#
is a binding to GTK+, the cross platform user interface
toolkit used in GNOME. It includes bindings for Gtk, Atk,
Pango, Gdk, libgnome, libgnomeui and libgnomecanvas. Gtk#
2.10.x binds GTK+ 2.10.

%package gapi
Summary: Glib and GObject C source parser and C generator for the creation and maintenance of managed bindings for Mono and .NET
Group: Development/Other
Requires: %name = %version-%release

%description gapi
This package provides developer tools for the creation and
maintainance of managed bindings to native libraries which utilize
glib and GObject. Some examples of libraries currently bound using
the GAPI tools and found in Gtk# include Gtk, Atk, Pango, Gdk,
libgnome, libgnomeui and libgnomecanvas.

%package devel
Summary: .Net language bindings for Gtk+ and GNOME development files
Group: Development/Other
Requires: %name-gapi = %version-%release

%description devel
This package includes development files for the Gtk\# project
to parse and bind GObject libraries.

%package doc
Summary: %name documentation in monodoc format
Group: Documentation
Provides: %name-monodoc = %version-%release
Obsoletes: %name-monodoc
Requires: monodoc >= 2.2
BuildArch: noarch

%description doc
This package includes documentation in monodoc format for the Gtk\# project
for use with monodoc / monodoc Gtk# (from mono-tools) / monodevelop.

%prep
%setup -q

%patch0 -p1

%build
NOCONFIGURE=1 ./bootstrap-2.12
%configure --disable-static
%make

%install
%make_install DESTDIR=%buildroot install

%files
%doc README COPYING ChangeLog
%prefix/lib/gtk-sharp-2.0
%exclude %prefix/lib/gtk-sharp-2.0/gapi*
%_monodir/gac/*
%_monodir/gtk-sharp-2.0
%_libdir/*.so
%_pkgconfigdir/*
%exclude %_pkgconfigdir/gapi-2.0.pc

%files gapi
%_bindir/gapi2*
%prefix/lib/gtk-sharp-2.0/gapi*
%dir %_datadir/gapi-2.0

%files devel
%_datadir/gapi-2.0/*.xml
%_pkgconfigdir/gapi-2.0.pc

%if_enabled doc
%files doc
%_monodocdir/*
%endif

%changelog
* Wed Oct 12 2011 Alexey Shabalin <shaba@altlinux.ru> 2.12.11-alt1
- 2.12.11
- build with mono-2.10.x
- disable build docs

* Tue Nov 23 2010 Alexey Shabalin <shaba@altlinux.ru> 2.12.10-alt2
- rebuild with mono-2.8

* Wed Mar 17 2010 Alexey Shabalin <shaba@altlinux.ru> 2.12.10-alt1
- 2.12.10

* Mon Jul 06 2009 Alexey Shabalin <shaba@altlinux.ru> 2.12.9-alt1
- 2.12.9
- move pkgconfig files from main to devel package

* Mon Feb 16 2009 Alexey Shabalin <shaba@altlinux.ru> 2.12.8-alt1
- 2.12.8

* Fri Jan 16 2009 Alexey Shabalin <shaba@altlinux.ru> 2.12.7-alt1
- 2.12.7

* Thu Nov 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.12.6-alt1
- 2.12.6
- rebuild(and fix build) with new macros _monodocdir
- remove post scripts
- rename package %name-monodoc to %name-doc

* Mon Oct 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.12.5-alt1
- 2.12.5
- build docs(monodoc) as noarch

* Thu Oct 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.12.4-alt1
- 2.12.4

* Thu Aug 21 2008 Alexey Shabalin <shaba@altlinux.ru> 2.12.2-alt1
- 2.12.2

* Sat May 03 2008 Alexey Shabalin <shaba@altlinux.ru> 2.12.1-alt1
- 2.12.1

* Thu Mar 20 2008 Alexey Shabalin <shaba@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Mon Nov 26 2007 Alexey Shabalin <shaba@altlinux.ru> 2.10.2-alt2
- add --disable-static to configure
- rebuild with new rpm-build-mono-1.2
- move pkgconfig files from devel to main package

* Sun Oct 28 2007 Alexey Shabalin <shaba@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Wed Sep 12 2007 Alexey Shabalin <shaba@altlinux.ru> 2.10.1-alt3
- drop Debian patches 01_glue-locations.dpatch and 02_missing_dllmaps.dpatch
- add gtk-sharp-2.10.1-fix-configs.patch, based on Debian patches

* Sat Sep 08 2007 Alexey Shabalin <shaba@altlinux.ru> 2.10.1-alt2
- Alexey Morozov added patches from Debian package (2.10.1-3):
  + 01_glue-locations.dpatch (#10) 
  + 02_missing_dllmaps.dpatch (#11) both adding missing DLLs to generated configs
  + fix_callback_code_generator.dpatch (#12) Fix gapi's code generator for
    callbacks with out parameters (Closes: Debian bug #430027, fixes
    problems with libgmime compilation:
    http://www.mail-archive.com/debian-bugs-rc%%40lists.debian.org/msg105916.html)

* Sat Jul 28 2007 Alexey Shabalin <shaba@altlinux.ru> 2.10.1-alt1
- Update to 2.10.1

* Thu Nov 30 2006 Alexey Shabalin <shaba@altlinux.ru> 2.10.0-alt1.1
- rebuild with fixed rpm-build-mono

* Tue Oct 10 2006 Ildar Mulyukov <ildar@altlinux.ru> 2.10.0-alt1
- rpm-build-mono support
- spec cleanup

* Thu Mar 16 2006 Evgeny Sinelnikov <sin@altlinux.ru> 2.8.2-alt1
- Update to release

* Wed Feb 22 2006 Evgeny Sinelnikov <sin@altlinux.ru> 2.8.1-alt1
- Update to release

* Wed Nov 23 2005 Evgeny Sinelnikov <sin@altlinux.ru> 2.6.0-alt1
- Update to release

* Sat Oct 08 2005 Evgeny Sinelnikov <sin@altlinux.ru> 2.5.91-alt1
- Update to release

* Sat May 21 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.9.5-alt1
- Inital release for ALT

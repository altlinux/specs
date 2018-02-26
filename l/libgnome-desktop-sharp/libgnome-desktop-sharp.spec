%define realname gnome-desktop-sharp

Summary: GnomeDesktop bindings for Mono
Name: lib%{realname}
Version: 2.26.0
Release: alt5
License: LGPLv2+
Group: Development/Other
Url: http://www.mono-project.com/
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Source: http://ftp.gnome.org/pub/GNOME/sources/%realname/2.20/%realname-%version.tar.bz2

Patch1: %realname-2.20.1-fix-gapidir.patch
Patch11: %realname-2.20.0-fix-configs.patch

Provides: libgtksourceview2-sharp = 2.0.0.0-%release
Obsoletes: libgtksourceview2-sharp < 2.0.0.0
Provides: libgtksourceview-sharp = 2.0.0.0-%release
Obsoletes: libgtksourceview-sharp < 2.0.0.0

BuildPreReq: glib2-devel >= 2.10.0
BuildPreReq: libgtk-sharp2-devel >= 2.12.2
BuildPreReq: libgtk-sharp2-gapi >= 2.12.2
BuildPreReq: libgnome-sharp-devel >= 2.24.0
BuildPreReq: libgnome-desktop-devel >= 2.25.0
BuildPreReq: librsvg-devel >= 2.22.2
# BuildPreReq: libgnome-panel-devel >= 2.25.0
BuildPreReq: libgtkhtml3-devel >= 3.23.5
BuildPreReq: libgtksourceview-devel >= 2.2.2
BuildPreReq: libvte-devel >= 0.16.14
BuildPreReq: libwnck-devel >= 2.25.0

# libnautilus-cd-burner-devel >= 2.22.1
# libgnomeprint-devel  >= 2.18.0

BuildPreReq: rpm-build-mono
BuildRequires: /proc
BuildRequires: mono-mcs libSM-devel mono-devel

%description
GnomeDesktop# a .NET language binding for assorted GNOME libraries.
This assembly has following configuration:
   Optional assemblies included in the build:
      * gnome-panel-sharp.dll: yes
      * gnome-print-sharp.dll: yes
      * gtkhtml-sharp.dll: yes
      * gtksourceview2-sharp.dll: yes
      * nautilusburn-sharp.dll: yes
      * rsvg-sharp.dll: yes
      * vte-sharp.dll: yes
      * wnck-sharp.dll: yes

%package devel
Summary: .Net language bindings for GnomeDesktop: development files
Group: Development/Other
Requires: %name = %version-%release

Provides: libgtksourceview2-sharp-devel = 2.0.0.0-%release
Obsoletes: libgtksourceview2-sharp-devel < 2.0.0.0
Provides: libgtksourceview-sharp-devel = 2.0.0.0-%release
Obsoletes: libgtksourceview-sharp-devel < 2.0.0.0

%description devel
This package includes development files for the Gtk\# project
to parse and bind Gnome libraries.

%prep
%setup -n %realname-%version -q
%patch1 -p1
%patch11 -p1

%build
%autoreconf
%configure --disable-static
%make

%install
%makeinstall

%files
%_libdir/*.so
%_monogacdir/*
%_monodir/*-sharp*
%doc AUTHORS README ChangeLog

%files devel
%_datadir/gapi-2.0/*.xml
%_pkgconfigdir/*

%changelog
* Wed Oct 12 2011 Alexey Shabalin <shaba@altlinux.ru> 2.26.0-alt5
- rebuild for mono-2.10

* Fri May 27 2011 Alexey Shabalin <shaba@altlinux.ru> 2.26.0-alt4
- build without libgnome-panel

* Thu Mar 10 2011 Alexey Shabalin <shaba@altlinux.ru> 2.26.0-alt3
- move pkgconfig file to devel

* Sat Apr 03 2010 Alexey Shabalin <shaba@altlinux.ru> 2.26.0-alt2
- update patch11 for gnome-desktop-2.30.0

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- shaba@:
    2.26.0
    build without support gnomeprint and nautilus-burn

* Thu Oct 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- 2.24.0

* Thu Mar 20 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.1-alt1
- build for Sisyphus
- obsoletes libgtksourceview2-sharp
- fix gapidir (patch1)

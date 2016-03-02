%define _name xplayer-plparser
%define _alt_name xplayer-pl-parser
%define _libexecdir %_prefix/libexec
%def_enable gtk_doc
%def_enable introspection

Name: lib%_name
Version: 1.0.1
Release: alt1

Summary: Shared libraries of the Xplayer media player play list parser
Group: System/Libraries
License: GPL
URL: https://github.com/linuxmint/xplayer-plparser

Source: %_name-%version.tar

%define glib_ver 2.34
%define soup_ver 2.43
%define quvi_ver 0.9.1
%define archive_ver 3.0

BuildPreReq: libgio-devel >= %glib_ver libquvi0.9-devel >= %quvi_ver
BuildPreReq: libarchive-devel >= %archive_ver libsoup-gnome-devel >= %soup_ver
BuildRequires: gnome-common gtk-doc intltool libgmime-devel
BuildRequires: libxml2-devel libgcrypt-devel
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 0.9.5}

%description
Shared libraries that come with the Xplayer media player.

%package devel
Summary: Development files for Xplayer media player play list parser
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides files needed to build applications using Xplayer
libraries.

%package devel-doc
Summary: Development documentation for Xplayer media player play list parser
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package contains documentation needed to develop applications using Xplayer
libraries.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Xplayer playlist parser library

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Xplayer playlist parser library


%prep
%setup -n %_name-%version
[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure \
	--disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection}

%make_build

%install
%makeinstall_std

%find_lang --with-gnome --output=%name.lang %_name %_alt_name

%files -f %name.lang
%doc AUTHORS NEWS README
%_libdir/*.so.*
%_libexecdir/xplayer-pl-parser-videosite

%files -n %name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n %name-devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/*

%files gir-devel
%_datadir/gir-1.0/*
%endif

%changelog
* Wed Mar 2 2016 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

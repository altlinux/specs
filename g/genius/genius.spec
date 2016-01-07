%define ver_major 1.0
%define _libexecdir %_prefix/libexec

Name: genius
Version: %ver_major.21
Release: alt1

Summary: Genius Calculator
License: LGPLv3+
Group: Sciences/Mathematics

URL: http://www.jirka.org/genius.html
#Source: %name-%version.tar
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: scrollkeeper

%define gtk_ver 2.18.0
%define glib_ver 2.16.0

BuildPreReq: libgio-devel >= %glib_ver libgtk+2-devel >= %gtk_ver
BuildRequires: libgtksourceview-devel >= 2.0.2 libvte-devel
BuildRequires: libreadline-devel libncurses-devel libgmp-devel libmpfr-devel >= 2.3.0
BuildRequires: gnome-common gnome-doc-utils librarian intltool xsltproc bison flex
# for non-UTF korean trnslation
BuildRequires: perl-Encode-KR

%description
Genius calculator is a general purpose calculator and mathematics tool
with many features.

See %url for more information.

%package devel
Summary: Genius development package
Group: Development/C
BuildArch: noarch
Requires: %name = %version-%release

%description devel
Genius calculator is a general purpose calculator and mathematics tool
with many features.

This package provides headers needed to develop Genius plugins.

%prep
%setup

subst '/GTK_UPDATE_ICON_CACHE/d' pixmaps/Makefile.am

%build
gnome-doc-prepare --force
%autoreconf
%configure --disable-static \
	--disable-scrollkeeper \
	--disable-update-mimedb

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%check
%make check
pushd src
./geniustest.pl
popd


%files -f %name.lang
%_bindir/%name
%_bindir/gnome-%name
%_libexecdir/%name-readline-helper-fifo
%dir %_libdir/%name
%_libdir/%name/libtestplugin.so
%_datadir/application-registry/genius.applications
%_desktopdir/gnome-genius.desktop
%_iconsdir/hicolor/*x*/apps/*.png
%_iconsdir/hicolor/scalable/apps/gnome-%name.svg
%_datadir/mime/packages/genius.xml
%_datadir/%name
%doc AUTHORS NEWS README TODO

%files devel
%_includedir/genius/

%exclude %_libdir/%name/*.la
%exclude %_datadir/mime-info/genius.keys
%exclude %_datadir/mime-info/genius.mime

%changelog
* Thu Jan 07 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.21-alt1
- 1.0.21

* Tue Mar 10 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.20-alt1
- 1.0.20

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.19-alt1
- 1.0.19

* Tue Aug 26 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.18-alt1
- 1.0.18 release

* Mon Nov 18 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.18-alt0.1
- 1.0.18 snapshot (1d2cb260)

* Sun Jun 30 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.17-alt1
- 1.0.17

* Tue Dec 18 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.16-alt1
- 1.0.16

* Mon Oct 29 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.15-alt2
- fixed %%install

* Sat Sep 01 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0.15-alt1.3
- Rebuilt with libgmp.so.10.

* Tue Jun 05 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.15-alt1.2
- updated buildreqs

* Fri Apr 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.15-alt1.1
- fixed url and license
- new -devel subpackage

* Fri Apr 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.15-alt1
- first build for Sisyphus


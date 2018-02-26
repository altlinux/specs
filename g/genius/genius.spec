%define ver_major 1.0
%define _libexecdir %_prefix/libexec

Name: genius
Version: %ver_major.15
Release: alt1.2

Summary: Genius Calculator
License: LGPLv3+
Group: Graphical desktop/GNOME

URL: http://www.jirka.org/genius.html
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: scrollkeeper

%define gtk_ver 2.18.0
%define glib_ver 2.16.0

BuildPreReq: libgio-devel >= %glib_ver libgtk+2-devel >= %gtk_ver
BuildRequires: libgtksourceview-devel >= 2.0.2 libvte-devel
BuildRequires: libreadline-devel libncurses-devel libgmp-devel libmpfr-devel
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

%build
gnome-doc-prepare --force
%autoreconf
%configure --disable-static \
	--disable-scrollkeeper \
	--disable-update-mimedb

%make_build

%install
%makeinstall

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
%_datadir/mime/packages/genius.xml
%_datadir/%name
%doc AUTHORS NEWS README TODO

%files devel
%_includedir/genius/

%exclude %_libdir/%name/*.la
%exclude %_datadir/mime-info/genius.keys
%exclude %_datadir/mime-info/genius.mime

%changelog
* Tue Jun 05 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.15-alt1.2
- updated buildreqs

* Fri Apr 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.15-alt1.1
- fixed url and license
- new -devel subpackage

* Fri Apr 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.15-alt1
- first build for Sisyphus


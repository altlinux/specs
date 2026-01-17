%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: gpscorrelate
Version: 2.3
Release: alt1

Summary: GPS photo tagging application
License: GPL-2.0-or-later
Group: Graphics
Url: https://github.com/dfandrich/gpscorrelate

Source: %name-%version.tar

BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(exiv2)
BuildRequires: gcc-c++
BuildRequires: /usr/bin/xsltproc
BuildRequires: docbook-style-xsl
BuildRequires: intltool

%if_with check
BuildRequires: /usr/bin/exiv2
%endif

%description
gpscorrelate fills EXIF (Exchangeable Image File Format) fields of
digital photos related to GPS (Global Positioning System) information
(e.g.: GPSLatitude, GPSLongitude, GPSAltitude, ...). The act of filling
those fields is referred to as "correlation".

Inputs of the correlation process are a set of JPEG images and GPS data
encoded in GPX (GPS Exchange Format) format.

If GPS data are available at the precise moment the photo was taken
(with a 1-second granularity) the GPS data are stored unmodified in
EXIF fields. If they are not linear interpolation of GPS data
available at moments before and after the photo was taken can be used.

Both a command line tool (package gpscorrelate) and a GTK+ graphical
user interface for it (package gpscorrelate-gui) are provided.

This package also contains documentation in HTML format.

%prep
%setup
sed -i "s|Categories=.*|Categories=Graphics;Viewer;Photography;GTK;|" gpscorrelate.desktop

%build
%make_build CFLAGS="%optflags -DENABLE_NLS"

%install
%makeinstall_std prefix=%_prefix install-po install-desktop-file io.github.dfandrich.gpscorrelate.metainfo.xml

install -D -m 644 io.github.dfandrich.gpscorrelate.metainfo.xml %buildroot%_datadir/metainfo/io.github.dfandrich.gpscorrelate.metainfo.xml

%find_lang %name

%check
%make_build check

%files -f %{name}.lang
%doc README.md
%_bindir/gpscorrelate
%_bindir/gpscorrelate-gui
%_desktopdir/gpscorrelate.desktop
%_iconsdir/hicolor/scalable/apps/gpscorrelate-gui.svg
%_man1dir/gpscorrelate.1.*
%dir %_datadir/doc/gpscorrelate
%_datadir/doc/gpscorrelate/README.md
%_datadir/doc/gpscorrelate/concepts.html
%_datadir/doc/gpscorrelate/corr.png
%dir %_datadir/doc/gpscorrelate/fr
%_datadir/doc/gpscorrelate/fr/command.html
%_datadir/doc/gpscorrelate/fr/concepts.html
%_datadir/doc/gpscorrelate/fr/corr.png
%_datadir/doc/gpscorrelate/fr/gui.html
%_datadir/doc/gpscorrelate/fr/index.html
%_datadir/doc/gpscorrelate/gpscorrelate-gui.svg
%_datadir/doc/gpscorrelate/gpscorrelate.html
%_datadir/doc/gpscorrelate/gui.html
%_datadir/doc/gpscorrelate/index.html
%_datadir/metainfo/io.github.dfandrich.gpscorrelate.metainfo.xml

%changelog
* Fri Jan 16 2026 Nikolay Strelkov <snk@altlinux.org> 2.3-alt1
- Initial build for Sisyphus

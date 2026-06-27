Name: chemical-mime-data
Version: 0.1.94
Release: alt3.2

Summary: Chemical MIME types database
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://github.com/dleidert/chemical-mime

Vcs: https://github.com/dleidert/chemical-mime.git

Source: https://downloads.sourceforge.net/chemical-mime/%name-%version.tar.gz

# from Fedora
Patch: chemical-mime-data-0.1.94-turbomole.patch
Patch1: %name-0.1.94-alt-use-rsvg-convert.patch

BuildArch: noarch

Requires: shared-mime-info
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: intltool xml-utils xsltproc
#BuildRequires: ImageMagick-tools
BuildRequires: /usr/bin/rsvg-convert

%description
A collection of data files which tries to give support for various chemical
MIME types (chemical/*) on Linux/UNIX desktops. Chemical MIME's have been
proposed in 1995, though it seems they have never been registered with IANA.

%define pkgdocdir %_docdir/%name-%version

%prep
%setup -q
%patch -p1 -b .turbomole
%patch1 -b .rsvg

%build
%autoreconf -I %_datadir/gettext/m4
%configure --disable-update-database \
           --without-gnome-mime \
           --without-pixmaps \
           --without-kde-mime \
           --docdir=%pkgdocdir
%make_build

%install
%makeinstall_std
cp AUTHORS ChangeLog HACKING NEWS README THANKS TODO %buildroot%pkgdocdir
%find_lang %name

%files -f %name.lang
%_datadir/mime/packages/*.xml
%_datadir/icons/hicolor/*/*/*
%_datadir/pkgconfig/*
%doc %pkgdocdir

%changelog
* Sat Jun 27 2026 Yuri N. Sedunov <aris@altlinux.org> 0.1.94-alt3.2
- fixed build with gettext-1.0

* Mon Oct 20 2025 Yuri N. Sedunov <aris@altlinux.org> 0.1.94-alt3.1
- fixed BR
- used rsvg-convert instead of convert (from ImageMagick)
  to avoid difference of types (RGB(A)) of produced png's files for aarch64

* Tue Dec 24 2019 Yuri N. Sedunov <aris@altlinux.org> 0.1.94-alt3
- disabled "chemical/x-turbomole-vibrational" (ALT #37671)
- updated Url and License tags

* Thu Oct 21 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.94-alt2
- updated buildrqs

* Mon Mar 15 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.94-alt1
- first build for Sisyphus


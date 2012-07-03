Name: chemical-mime-data
Version: 0.1.94
Release: alt2

Summary: Chemical MIME types database
Group: System/Libraries
License: LGPLv2+
Url: http://sourceforge.net/projects/chemical-mime/

Source: http://downloads.sourceforge.net/chemical-mime/%name-%version.tar.gz

# from Fedora
Patch: chemical-mime-data-0.1.94-turbomole.patch

BuildArch: noarch

Requires: shared-mime-info
BuildRequires: shared-mime-info intltool xml-utils xsltproc ImageMagick-tools

%description
A collection of data files which tries to give support for various chemical
MIME types (chemical/*) on Linux/UNIX desktops. Chemical MIME's have been
proposed in 1995, though it seems they have never been registered with IANA.

%define pkgdocdir %_docdir/%name-%version

%prep
%setup -q
%patch -p1 -b .turbomole

%build
%configure --disable-update-database \
           --without-gnome-mime \
           --without-pixmaps \
           --without-kde-mime \
           --docdir=%pkgdocdir
%make_build

%install
%make DESTDIR=%buildroot install

cp AUTHORS ChangeLog HACKING NEWS README THANKS TODO %buildroot%pkgdocdir

%find_lang %name

%files -f %name.lang
%_datadir/mime/packages/*.xml
%_datadir/icons/hicolor/*/*/*
%_datadir/pkgconfig/*
%doc %pkgdocdir

%changelog
* Thu Oct 21 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.94-alt2
- updated buildrqs

* Mon Mar 15 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.94-alt1
- first build for Sisyphus


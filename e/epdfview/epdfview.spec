Summary:        A lightweight PDF viewer for GNOME
Name:           epdfview
Version:        0.1.8
Release:        alt6
URL:            http://trac.emma-soft.com/epdfview/
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License:	GPL v2+
Group:		Office

BuildRequires:	libpoppler-glib-devel cups-devel gtk+-devel libgtk+2-devel gcc-c++ libkrb5-devel
Source:		%name-%version.tar
Patch0:		%name-locale.patch
Patch1:		%name-0.1.8-alt3-color-fix.patch
Patch2:		%name-0.1.8-alt3-color-print-fix.patch

%description
ePDFView is a free lightweight PDF document viewer using Poppler and
GTK+ libraries.

The aim of ePDFView is to make a simple PDF document viewer, in the
lines of Evince but without using the GNOME libraries.

%description -l pl.UTF-8
ePDFView to darmowa, lekka przeglądarka dokumentów PDF, używająca
bibliotek Poppler i GTK+.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
# locales quick fix
mv po/pt_PT.gmo po/pt.gmo
mv po/pt_PT.po po/pt.po
mv po/he_IL.gmo po/he.gmo
mv po/he_IL.po po/he.po
mv po/nl_NL.gmo po/nl.gmo
mv po/nl_NL.po po/nl.po




%build
%autoreconf
%configure
%make

%install
%makeinstall_std PREFIX=/usr

install -d %buildroot%_liconsdir
install -D -m 644 %buildroot%_datadir/%name/pixmaps/icon_epdfview-48.png %buildroot/%_liconsdir/%name.png
sed -i -e 's,Icon=icon_epdfview-48,Icon=%name,' %buildroot%_desktopdir/%name.desktop

%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %_bindir/%name
%_man1dir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_liconsdir/%name.png

%changelog
* Sat Apr 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.8-alt6
- NMU: rebuilt with new toolchain.

* Tue Jul 08 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.1.8-alt5
- Add buildreq

* Wed Jul 02 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.1.8-alt4
- Add color print support (RGB)

* Tue Jul 01 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.1.8-alt3
- Fixed colors in images

* Tue Jul 01 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.1.8-alt2
- PNG moved to %_liconsdir

* Fri Jun 27 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.1.8-alt1
- Initial build


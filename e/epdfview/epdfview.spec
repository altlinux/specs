Summary:        A lightweight PDF viewer for GNOME
Name:           epdfview
Version:        0.1.8
Release:        alt1
URL:            http://trac.emma-soft.com/epdfview/
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License:	GPL v2+
Group:		Office

BuildRequires:	libpoppler-glib-devel cups-devel gtk+-devel libgtk+2-devel gcc4.7-c++
Source:		%name-%version.tar
Patch0:		%name-locale.patch

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

install -d %buildroot%_pixmapsdir
install -D -m 644 %buildroot%_datadir/%name/pixmaps/icon_epdfview-48.png %buildroot/%_pixmapsdir/%name.png
sed -i -e 's,Icon=icon_epdfview-48,Icon=%name,' %buildroot%_desktopdir/%name.desktop

%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %_bindir/%name
%_man1dir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Fri Jun 27 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.1.8-alt1
- Initial build


Name:		calizo
Version:	0.2.5
Release:	alt1
License:	GPLv3
Summary:	The zoomable timeline calendar
Group:		Office
URL:		http://calizo.sourceforge.net/
Source:		%name-%{version}_src.zip

# Automatically added by buildreq on Mon Jul 04 2011
# optimized out: fontconfig libgdk-pixbuf libstdc++-devel
BuildRequires: gcc-c++ libwxGTK-devel unzip

%description
Calizo is a calendar application using a timeline visualization with nearly
unrestricted zooming. Thereby historical timelines, family history, and
biographical information are manageable in the same way as day-to-day tasks,
project management or life planing.

%prep
%setup -n %name
touch NEWS README AUTHORS ChangeLog
touch `find *`

%build
%autoreconf
%configure
%make_build
cat > %name.desktop <<@@@
[Desktop Entry]
Name=Calizo
Comment=Zoomable timeline calendar
Exec=%name
Icon=%name
Terminal=false
Categories=Office;Calendar;
StartupNotify=true
@@@

%install
%makeinstall
install -D artworks/icon.png %buildroot%_iconsdir/hicolor/32x32/%name.png
install -D artworks/icon.svg %buildroot%_iconsdir/hicolor/scalable/%name.svg
install -D i18n/locale/de/calizo.mo %buildroot%_datadir/locale/de/LC_MESSAGES/calizo.mo
install -D i18n/locale/ru/calizo.mo %buildroot%_datadir/locale/ru/LC_MESSAGES/calizo.mo
install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%find_lang %name

%files -f %name.lang
%doc help/help/calizo.htb help/help_calizo.pdf README?*
%_bindir/%name
%_iconsdir/hicolor/*/*
%_desktopdir/%name.desktop

%changelog
* Mon Jul 04 2011 Fr. Br. George <george@altlinux.ru> 0.2.5-alt1
- Initial build from scratch


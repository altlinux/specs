Name:		uget
Version:	2.2.0
Release:	alt1
Summary:	Download manager using GTK+ and libcurl
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group:		Networking/File transfer
License:	LGPLv2+
URL:		http://urlget.sourceforge.net/
Source0:	http://downloads.sourceforge.net/urlget/%{name}-%{version}.tar.gz


# Automatically added by buildreq on Wed Jun 09 2010
BuildRequires: desktop-file-utils libgtk+3-devel gstreamer-devel intltool libcurl-devel libnotify-devel libssl-devel rpm-build-gir

%description
uGet is a download manager with downloads queue, pause/resume, 
clipboard monitor, batch downloads, browser integration (Firefox & Chrome), 
multiple connections, speed limit controls, powerful category based control
and much more. Each Category has an independent configuration that can
be inherited by each download in that category.

Uget is the successor of urlgfe, which was called URLget before.

%prep
%setup -q
#patch1 -p2
touch NEWS
find . | xargs touch
autoreconf -fisv

%build
%configure
%make_build

%install
%makeinstall

desktop-file-install \
	--dir $RPM_BUILD_ROOT%_desktopdir \
	--delete-original \
	$RPM_BUILD_ROOT%_desktopdir/%{name}-gtk.desktop

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog README
%_bindir/*
%_desktopdir/%name-gtk.desktop
%_datadir/icons/hicolor/*/apps/%name-icon.*
%_datadir/icons/hicolor/*/apps/%name-tray-*.png
%_datadir/pixmaps/%name/logo.png
%_datadir/sounds/%name


%changelog
* Mon Jan 15 2018 Ilya Mashkin <oddity@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Thu Oct 26 2017 Ilya Mashkin <oddity@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Mon Oct 02 2017 Ilya Mashkin <oddity@altlinux.ru> 2.0.10-alt1
- 2.0.10

* Mon Mar 20 2017 Ilya Mashkin <oddity@altlinux.ru> 2.0.9-alt1
- 2.0.9

* Fri Jun 03 2016 Ilya Mashkin <oddity@altlinux.ru> 2.0.8-alt1
- 2.0.8

* Wed Jan 13 2016 Ilya Mashkin <oddity@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Thu Oct 08 2015 Ilya Mashkin <oddity@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Thu May 14 2015 Ilya Mashkin <oddity@altlinux.ru> 2.0-alt1
- 2.0 (Closes: #31001)

* Thu Sep 04 2014 Ilya Mashkin <oddity@altlinux.ru> 1.10.4-alt1
- 1.10.4
- update description

* Thu Jul 07 2011 Mykola Grechukh <gns@altlinux.ru> 1.8.0-alt1
- new stable version

* Fri Aug 20 2010 Mykola Grechukh <gns@altlinux.ru> 1.6.0-alt1
- new stable version

* Wed Jul 14 2010 Mykola Grechukh <gns@altlinux.ru> 1.5.9.2-alt2.svn317
- new snapshot

* Wed Jun 09 2010 Mykola Grechukh <gns@altlinux.ru> 1.5.9.2-alt1
- first build for ALT

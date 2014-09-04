Name:		uget
Version:	1.10.4
Release:	alt1
Summary:	Download manager using GTK+ and libcurl
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group:		Networking/File transfer
License:	LGPLv2+
URL:		http://urlget.sourceforge.net/
Source0:	http://downloads.sourceforge.net/urlget/%{name}-%{version}.tar.gz


# Automatically added by buildreq on Wed Jun 09 2010
BuildRequires: desktop-file-utils libgtk+3-devel gstreamer-devel intltool libcurl-devel libnotify-devel

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
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--delete-original \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}-gtk.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README
%_bindir/%name-gtk
%_desktopdir/%name-gtk.desktop
%_datadir/icons/hicolor/*/apps/%name-icon.*
%_datadir/icons/hicolor/*/apps/%name-tray-*.png
%_datadir/pixmaps/%name/logo.png
%_datadir/sounds/%name


%changelog
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
Чтв Июл 15 12:04:24 EEST 2010

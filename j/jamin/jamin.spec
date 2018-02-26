%define _ladspa_path %_libdir/ladspa

Name: jamin
Version: 0.95.0
Release: alt2

Summary: JAMin is a Realtime Mastering Processor
Summary(ru_RU.KOI8-R): JAMin -- приложение для мастеринга звука
License: GPL
Group: Sound
Url: http://%name.sourceforge.net
Packager: Fr. Br. George <george@altlinux.ru>
Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.gz

Requires: ladspa-swh-plugins >= 0.4.11
Requires: jackd

BuildPreReq: ladspa_sdk

# Automatically added by buildreq on Sat Jun 13 2009
BuildRequires: gcc-c++ gcc-fortran jackit-devel libfftw3-devel libgtk+2-devel liblo-devel libxml2-devel perl-XML-Parser intltool
BuildRequires: desktop-file-utils

#BuildRequires: XFree86-libs fontconfig freetype2 gcc-c++ gcc-g77 glib2-devel intltool jackit-devel libatk-devel libfftw3-devel libgtk+2-devel liblo-devel libpango-devel libstdc++-devel libxml2-devel perl-XML-Parser pkgconfig zlib-devel

%description
JAMin is a realtime mastering processor designed to bring out the detail
in recorded music and provide the final layer of polish. Every effort
has been made to ensure a clean, distortion-free signal path. All
processing elements use linear-phase filtering, ensuring that no phase
distortion is introduced. JAMin uses the JACK Audio Connection Kit, a
low-latency audio server, which can connect a number of different
applications to an audio device, and also allow them to share audio
among themselves.

%description -l ru_RU.KOI8-R
JAMin -- приложение, работающее через сервер JACK, он
спроектирован для профессионального мастеринга звука, посылаемого с
любого количества источников.  Программа  состоит из нескольких
инструментов: 1024-полосного рисуемого от руки эквалайзера с
изменяемыми параметрическими точками контроля, 31-полосного графического
эквалайзера, 3-полосного компрессора, 3-полосного контроллера
стереопанорамы, lookahead-ограничителя (лимитера), усилителя сигнала и
некоторых других.

%prep
%setup -q -n %name-%version
# Fix lib
for file in controller/Makefile.am src/plugin.c; do
   sed -i 's|/lib/|/%_lib/|g' $file
done

sed -i 's/JAMIN_LIBS="/JAMIN_LIBS="$lt_cv_dlopen_libs /' configure.in

# .desktop file fixes:
sed -i 's|\(GenericName=\)|\1Jack Audio Mastering|
	s|\.svg||
	s|AudioVideo|Audio|
	/^Encoding=/d' data/%{name}.desktop.in

%build
NOCONFIGURE=indeed ./autogen.sh
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

# remove none-packaged files
rm -f %buildroot%_ladspa_path/*.la

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=AudioVideo \
	--add-category=Sequencer \
	%buildroot%_desktopdir/jamin.desktop

%files -f %name.lang
%_bindir/*
%_datadir/applications/*
%_datadir/mime/packages/*
%_datadir/%name
%_iconsdir/*
%_ladspa_path/*.so
%_man1dir/*
%doc AUTHORS ChangeLog NEWS README TODO

%changelog
* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 0.95.0-alt2
- DSO list completion

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.95.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for jamin

* Sun Jun 14 2009 Fr. Br. George <george@altlinux.ru> 0.95.0-alt1
- Version up
- Resurrecting from orphand

* Sun Jan 16 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.95.0-alt0.5beta6
- 0.9.5beta6.
- some i18n fixes.
- .desktop file.
- .jam mime description.

* Tue Sep 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9.0-alt0.5
- First build for Sisyphus.
- Russian summary, description by avp@.

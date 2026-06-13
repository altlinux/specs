Name: gtkwave
Version: 3.3.127
Release: alt1
Summary: GTKWave is a fully featured GTK+ based wave viewer
License: GPL-2.0
Group: Development/Other

URL: http://gtkwave.sourceforge.net/
VCS: https://github.com/gtkwave/gtkwave

# Source-url: https://gtkwave.sourceforge.net/gtkwave-gtk3-%version.tar.gz
Source: %name-%version.tar

BuildRequires: bzlib-devel
BuildRequires: zlib-devel
BuildRequires: desktop-file-utils
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: gperf
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires: pkgconfig(gtk+-unix-print-3.0)
BuildRequires: pkgconfig(libtirpc)
BuildRequires: liblzma-devel
BuildRequires: tk-devel
BuildRequires: libjudy-devel
BuildRequires: libappstream-glib
BuildRequires: hardlink

%description
%summary.

%prep
%setup

%build
#autoreconf
%configure \
	--disable-dependency-tracking \
	--disable-mime-update \
	--enable-gtk3 \
	--enable-judy \
	--with-gsettings \
	--with-tirpc

%make_build

%install
%makeinstall_std pkgdatadir=%_pkgdocdir

# Icons and desktop entry
desktop-file-install --vendor "" --dir %buildroot%_desktopdir \
	share/applications/gtkwave.desktop
install -D -m 644 -p share/icons/gnome/16x16/mimetypes/gtkwave.png \
	%buildroot%_iconsdir/hicolor/16x16/apps/gtkwave.png
install -D -m 644 -p share/icons/gnome/32x32/mimetypes/gtkwave.png \
	%buildroot%_iconsdir/hicolor/32x32/apps/gtkwave.png
install -D -m 644 -p share/icons/gnome/48x48/mimetypes/gtkwave.png \
	%buildroot%_iconsdir/hicolor/48x48/apps/gtkwave.png
install -D -m 644 -p share/icons/gtkwave_256x256x32.png \
	%buildroot%_iconsdir/hicolor/256x256/apps/gtkwave.png

# Appdata
install -D -m 644 -p share/appdata/io.github.gtkwave.GTKWave.metainfo.xml \
	%buildroot%_datadir/metainfo/io.github.gtkwave.GTKWave.metainfo.xml

# Include extra docs
install -p -m 644 AUTHORS %buildroot%_pkgdocdir/
install -p -m 644 ChangeLog %buildroot%_pkgdocdir/

# hardlink identical icons together
hardlink -cv %buildroot%_iconsdir}/

%files
%_bindir/*
%_man5dir/*.5.*
%_man1dir/*.1.*
#_datadir/%name
%_datadir/metainfo/io.github.gtkwave.GTKWave.metainfo.xml
%_datadir/mime/packages/x-gtkwave-extension-*.xml
%_datadir/glib-2.0/schemas/com.geda.gtkwave.gschema.xml
%_desktopdir/%name.desktop
%_iconsdir/gnome/16x16/mimetypes/*.png
%_iconsdir/gnome/32x32/mimetypes/*.png
%_iconsdir/gnome/48x48/mimetypes/*.png
%_iconsdir/gtkwave_256x256x32.png
%_iconsdir/gtkwave_files_256x256x32.png
%_iconsdir/gtkwave_savefiles_256x256x32.png
%_iconsdir/hicolor/*/apps/gtkwave.png
%_iconsdir/hicolor/scalable/apps/gtkwave.svg

%changelog
* Sat Jun 13 2026 Anton Midyukov <antohami@altlinux.org> 3.3.127-alt1
- New version 3.3.127.

* Wed Aug 16 2023 Cronbuild Service <cronbuild@altlinux.org> 3.3.117-alt1
- New version 3.3.117.

* Sun Jul 23 2023 Cronbuild Service <cronbuild@altlinux.org> 3.3.116-alt1
- New version 3.3.116.

* Sun Apr 09 2023 Cronbuild Service <cronbuild@altlinux.org> 3.3.115-alt1
- New version 3.3.115.

* Mon Dec 19 2022 Cronbuild Service <cronbuild@altlinux.org> 3.3.114-alt1
- new version 3.3.114

* Wed Oct 05 2022 Cronbuild Service <cronbuild@altlinux.org> 3.3.113-alt1
- new version 3.3.113

* Wed Sep 08 2021 Cronbuild Service <cronbuild@altlinux.org> 3.3.111-alt1
- new version 3.3.111

* Tue Jun 22 2021 Cronbuild Service <cronbuild@altlinux.org> 3.3.110-alt1
- new version 3.3.110

* Wed May 05 2021 Cronbuild Service <cronbuild@altlinux.org> 3.3.109-alt1
- new version 3.3.109

* Sat Jan 02 2021 Cronbuild Service <cronbuild@altlinux.org> 3.3.108-alt1
- new version 3.3.108

* Wed Oct 07 2020 Cronbuild Service <cronbuild@altlinux.org> 3.3.107-alt1
- new version 3.3.107

* Sat Aug 08 2020 Cronbuild Service <cronbuild@altlinux.org> 3.3.106-alt1
- new version 3.3.106

* Fri Jul 03 2020 Cronbuild Service <cronbuild@altlinux.org> 3.3.105-alt1
- new version 3.3.105

* Sun Feb 16 2020 Cronbuild Service <cronbuild@altlinux.org> 3.3.104-alt1
- new version 3.3.104

* Tue Nov 12 2019 Cronbuild Service <cronbuild@altlinux.org> 3.3.103-alt1
- new version 3.3.103

* Fri Oct 04 2019 Cronbuild Service <cronbuild@altlinux.org> 3.3.102-alt1
- new version 3.3.102

* Sat May 25 2019 Cronbuild Service <cronbuild@altlinux.org> 3.3.101-alt1
- new version 3.3.101

* Sat Mar 23 2019 Cronbuild Service <cronbuild@altlinux.org> 3.3.100-alt1
- new version 3.3.100

* Tue Feb 12 2019 Cronbuild Service <cronbuild@altlinux.org> 3.3.99-alt1
- new version 3.3.99

* Wed Dec 26 2018 Cronbuild Service <cronbuild@altlinux.org> 3.3.98-alt1
- new version 3.3.98

* Mon Nov 26 2018 Cronbuild Service <cronbuild@altlinux.org> 3.3.97-alt1
- new version 3.3.97

* Tue Nov 20 2018 Cronbuild Service <cronbuild@altlinux.org> 3.3.96-alt1
- new version 3.3.96

* Fri Oct 12 2018 Cronbuild Service <cronbuild@altlinux.org> 3.3.95-alt1
- new version 3.3.95

* Sun Sep 09 2018 Cronbuild Service <cronbuild@altlinux.org> 3.3.94-alt1
- new version 3.3.94

* Tue Aug 07 2018 Cronbuild Service <cronbuild@altlinux.org> 3.3.93-alt1
- new version 3.3.93

* Tue Jul 17 2018 Cronbuild Service <cronbuild@altlinux.org> 3.3.92-alt1
- new version 3.3.92

* Tue Jun 05 2018 Cronbuild Service <cronbuild@altlinux.org> 3.3.91-alt1
- new version 3.3.91

* Tue May 15 2018 Cronbuild Service <cronbuild@altlinux.org> 3.3.90-alt1
- new version 3.3.90

* Sun Mar 25 2018 Cronbuild Service <cronbuild@altlinux.org> 3.3.89-alt1
- new version 3.3.89

* Wed Mar 07 2018 Cronbuild Service <cronbuild@altlinux.org> 3.3.88-alt1
- new version 3.3.88

* Thu Jan 11 2018 Cronbuild Service <cronbuild@altlinux.org> 3.3.87-alt1
- new version 3.3.87

* Mon Oct 09 2017 Cronbuild Service <cronbuild@altlinux.org> 3.3.86-alt1
- new version 3.3.86

* Sun Sep 24 2017 Cronbuild Service <cronbuild@altlinux.org> 3.3.85-alt1
- new version 3.3.85

* Wed Sep 06 2017 Cronbuild Service <cronbuild@altlinux.org> 3.3.84-alt1
- new version 3.3.84

* Mon Aug 07 2017 Cronbuild Service <cronbuild@altlinux.org> 3.3.83-alt1
- new version 3.3.83

* Wed Jul 05 2017 Cronbuild Service <cronbuild@altlinux.org> 3.3.82-alt1
- new version 3.3.82

* Wed Jun 14 2017 Cronbuild Service <cronbuild@altlinux.org> 3.3.81-alt1
- new version 3.3.81

* Wed Mar 31 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.3.80-alt1.qa1
- NMU: rebuild against Tcl/Tk 8.6

* Fri Mar 31 2017 Cronbuild Service <cronbuild@altlinux.org> 3.3.80-alt1
- new version 3.3.80

* Sat Dec 31 2016 Cronbuild Service <cronbuild@altlinux.org> 3.3.79-alt1
- new version 3.3.79

* Sat Oct 29 2016 Cronbuild Service <cronbuild@altlinux.org> 3.3.78-alt1
- new version 3.3.78

* Mon Oct 17 2016 Cronbuild Service <cronbuild@altlinux.org> 3.3.77-alt1
- new version 3.3.77

* Thu Aug 18 2016 Denis Smirnov <mithraen@altlinux.ru> 3.3.76-alt1
- new version 3.3.76

* Tue Aug 09 2016 Cronbuild Service <cronbuild@altlinux.org> 3.3.75-alt1
- new version 3.3.75

* Sun Jul 31 2016 Cronbuild Service <cronbuild@altlinux.org> 3.3.74-alt1
- new version 3.3.74

* Mon Jun 13 2016 Cronbuild Service <cronbuild@altlinux.org> 3.3.73-alt1
- new version 3.3.73

* Thu Apr 14 2016 Cronbuild Service <cronbuild@altlinux.org> 3.3.72-alt1
- new version 3.3.72

* Wed Feb 17 2016 Cronbuild Service <cronbuild@altlinux.org> 3.3.70-alt1
- new version 3.3.70

* Mon Feb 08 2016 Cronbuild Service <cronbuild@altlinux.org> 3.3.69-alt1
- new version 3.3.69

* Sun Nov 22 2015 Cronbuild Service <cronbuild@altlinux.org> 3.3.68-alt1
- new version 3.3.68

* Fri Oct 02 2015 Cronbuild Service <cronbuild@altlinux.org> 3.3.67-alt1
- new version 3.3.67

* Tue Jul 07 2015 Cronbuild Service <cronbuild@altlinux.org> 3.3.66-alt1
- new version 3.3.66

* Fri Apr 17 2015 Cronbuild Service <cronbuild@altlinux.org> 3.3.65-alt1
- new version 3.3.65

* Wed Nov 26 2014 Cronbuild Service <cronbuild@altlinux.org> 3.3.64-alt1
- new version 3.3.64

* Sat Nov 08 2014 Cronbuild Service <cronbuild@altlinux.org> 3.3.63-alt1
- new version 3.3.63

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 3.3.62-alt1
- new version 3.3.62

* Sun Aug 10 2014 Denis Smirnov <mithraen@altlinux.ru> 3.3.61-alt1
- new version 3.3.61

* Tue Jun 10 2014 Denis Smirnov <mithraen@altlinux.ru> 3.3.60-alt1
- new version 3.3.60

* Fri May 02 2014 Denis Smirnov <mithraen@altlinux.ru> 3.3.59-alt1
- new version 3.3.59

* Thu Apr 03 2014 Cronbuild Service <cronbuild@altlinux.org> 3.3.58-alt1
- new version 3.3.58

* Mon Feb 17 2014 Cronbuild Service <cronbuild@altlinux.org> 3.3.57-alt1
- new version 3.3.57

* Fri Feb 14 2014 Cronbuild Service <cronbuild@altlinux.org> 3.3.56-alt1
- new version 3.3.56

* Tue Feb 11 2014 Cronbuild Service <cronbuild@altlinux.org> 3.3.55-alt1
- new version 3.3.55

* Sun Jan 05 2014 Cronbuild Service <cronbuild@altlinux.org> 3.3.54-alt1
- new version 3.3.54

* Thu Dec 19 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.53-alt1
- new version 3.3.53

* Tue Nov 12 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.52-alt1
- new version 3.3.52

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.51-alt1
- new version 3.3.51

* Thu Oct 17 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.50-alt1
- new version 3.3.50

* Sat Sep 14 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.49-alt1
- new version 3.3.49

* Thu Aug 08 2013 Denis Smirnov <mithraen@altlinux.ru> 3.3.48-alt1
- new version 3.3.48

* Tue Jun 11 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.47-alt1
- new version 3.3.47

* Fri May 03 2013 Denis Smirnov <mithraen@altlinux.ru> 3.3.46-alt1
- new version 3.3.46

* Sun Mar 24 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.45-alt1
- new version 3.3.45

* Sat Mar 02 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.44-alt1
- new version 3.3.44

* Fri Feb 08 2013 Denis Smirnov <mithraen@altlinux.ru> 3.3.43-alt1
- new version 3.3.43

* Mon Jan 21 2013 Denis Smirnov <mithraen@altlinux.ru> 3.3.42-alt1
- new version 3.3.42

* Thu Nov 08 2012 Denis Smirnov <mithraen@altlinux.ru> 3.3.41-alt1
- 3.3.41

* Fri Oct 12 2012 Denis Smirnov <mithraen@altlinux.ru> 3.3.40-alt1
- 3.3.40

* Wed Apr 04 2012 Denis Smirnov <mithraen@altlinux.ru> 3.3.34-alt1
- 3.3.34

* Tue Oct 04 2011 Denis Smirnov <mithraen@altlinux.ru> 3.3.26-alt2
- add buildrequires to liblzma-devel

* Tue Oct 04 2011 Denis Smirnov <mithraen@altlinux.ru> 3.3.26-alt1
- 3.3.26

* Fri Mar 25 2011 Denis Smirnov <mithraen@altlinux.ru> 3.3.0-alt5
- rebuild

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 3.3.0-alt4
- auto rebuild

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 3.3.0-alt3
- auto rebuild

* Thu Dec 31 2009 Denis Smirnov <mithraen@altlinux.ru> 3.3.0-alt2
- add Url tag

* Sun Dec 27 2009 Denis Smirnov <mithraen@altlinux.ru> 3.3.0-alt1
- first build for Sisyphus

Name: gtkwave
Version: 3.3.87
Release: alt1
Summary: %name
License: GPL
Group: Development/Other

Packager: Denis Smirnov <mithraen@altlinux.ru>

Url: http://gtkwave.sourceforge.net/

Source: %name-%version.tar
Source100: %name.watch

# Automatically added by buildreq on Thu Aug 08 2013 (-bb)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel gnu-config libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel libwayland-client libwayland-server pkg-config python-base rpm-build-tcl shared-mime-info tcl tcl-devel xorg-xproto-devel zlib-devel
BuildRequires: bzlib-devel desktop-file-utils flex gcc-c++ gperf libgtk+2-devel liblzma-devel tk-devel

%description
%summary

%prep
%setup

%build
%configure --disable-mime-update
%make_build
%install
%makeinstall_std

%files
%_bindir/*
%_man5dir/*
%_man1dir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/gnome/16x16/mimetypes/*.png
%_iconsdir/gnome/32x32/mimetypes/*.png
%_iconsdir/gnome/48x48/mimetypes/*.png
%_iconsdir/gtkwave_256x256x32.png
%_iconsdir/gtkwave_files_256x256x32.png
%_iconsdir/gtkwave_savefiles_256x256x32.png
%_datadir/mime/packages/*.xml

%changelog
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

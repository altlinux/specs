Name: geda
Version: 20060123
Release: alt0.1

Summary: Project browser for gEDA

License: GPL
Group: Video
Url: http://www.geda.seul.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://ftp.geda.seul.org/pub/geda/devel/%version/%name-%version.tar.bz2

# Automatically added by buildreq on Sat Jul 22 2006
BuildRequires: fontconfig imake libgtk+2-devel libXt-devel xorg-cf-files

%description
Project browser for gEDA/gaf.

%prep
%setup -q

%build
%configure
make

%install
make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%_bindir/*

%changelog
* Sun Jun 11 2006 Vitaly Lipatov <lav@altlinux.ru> 20060123-alt0.1
- new version (20060123)

* Wed Sep 14 2005 Vitaly Lipatov <lav@altlinux.ru> 20050820-alt0.1
- new version

* Sun Feb 06 2005 Vitaly Lipatov <lav@altlinux.ru> 20041228-alt0.1
- new version

* Tue Dec 14 2004 Vitaly Lipatov <lav@altlinux.ru> 20041214-alt0.1
- first build for ALT Linux Sisyphus

* Fri Aug 13 2004 Andy Shevchenko <andriy@asplinux.ru>
- update to version 20040111

* Thu Oct 09 2003 Andy Shevchenko <andriy@asplinux.ru>
- initial build

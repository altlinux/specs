# SPEC-file for gutenpy
#
#

%define real_name GutenPy

Name: gutenpy
Version: 0.3.0
Release: alt5.1.1

Summary: text reader and catalog browser for Project Gutenberg
Summary(ru_RU.UTF-8): утилита для поиска и чтения текстов из Project Gutenberg

License: %gpl2only
Group: Text tools
URL: http://gutenpy.sourceforge.net/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
#BuildArch: noarch

Source0: %name-%version.tar.gz
Source1: %name.desktop
Source2: %name.png
Source3: %name-16.png
Source4: %name-32.png
Source5: %name-48.png

BuildPreReq: python-base  python-modules  python-modules-encodings rpm-build-licenses

%description
GutenPy  is designed to be a comfortable  text reader and catalog
browser for Project Gutenberg. It provides automatic bookmarking,
navigational sidebar, offline catalog browser and other useful 
features.

%description -l ru_RU.UTF-8
GutenPy  предназначается для комфортного чтения текстов и 
просмотра каталога  Project Gutenberg.   Он предоставляет 
возможности  автоматической  установки закладок,  боковую
навигационную панель, просмотр каталога в оффлайне и
другие полезные возможности.

%define gp_libdir %python_sitelibdir/%real_name
%define gp_pixdir %_pixmapsdir/%name
%define gp_docdir %_datadir/%name

%prep
%setup

%build
%__subst 's@share/doc/gutenpy@share/gutenpy@' %name.py
%__subst 's@#!/usr/bin/python2.4@#!/usr/bin/python@' gutenpy.py py2exe_setup.py setup.py


%install
mkdir -p -- %buildroot%_bindir
mkdir -p -- %buildroot%gp_libdir
mkdir -p -- %buildroot%gp_pixdir
mkdir -p -- %buildroot%gp_docdir

install -m 0644 -- GutenPy/* %buildroot%gp_libdir/
install -m 0755 -- %name.py  %buildroot%gp_libdir/
install -m 0644 -- docs/*    %buildroot%gp_docdir/
install -m 0644 -- icons/*   %buildroot%gp_pixdir/

cat >%name <<END 
#!/bin/sh
exec %gp_libdir/%name.py
END

install -m 0755 -- %name %buildroot%_bindir/%name

mkdir -p -- %buildroot%_desktopdir
install -m 0644 -- %SOURCE1 %buildroot%_desktopdir/%name.desktop

mkdir -p -- %buildroot%_miconsdir %buildroot%_liconsdir \
		%buildroot%_niconsdir %buildroot%_iconsdir/hicolor/64x64/apps

install -m0644 -- %SOURCE2 %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -m0644 -- %SOURCE3 %buildroot%_miconsdir/%name.png
install -m0644 -- %SOURCE4 %buildroot%_niconsdir/%name.png
install -m0644 -- %SOURCE5 %buildroot%_liconsdir/%name.png

%files
%doc ChangeLog README.txt
%dir %gp_libdir
     %gp_libdir/*
%dir %gp_docdir
     %gp_docdir/*
%dir %gp_pixdir
     %gp_pixdir/*
%_bindir/%name
%_desktopdir/%name.desktop

%_miconsdir/%{name}*
%_niconsdir/%{name}*
%_liconsdir/%{name}*
%_iconsdir/hicolor/64x64/apps/%{name}*


%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt5.1.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt5.1
- Rebuilt with python 2.6

* Fri Dec 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.0-alt5
- Remove obsolete %%update_menus calls
- Fix .desktop file to meet standards

* Mon Apr 07 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.0-alt4
- Remove Python's version from shebangs (#14596)
- Add pre-scaled icons
- Add %%update_menus call 

* Fri Feb 22 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.0-alt3
- Rebuild with Python 2.5.1

* Thu Aug 9 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.0-alt2
- Spec file cleanup
- Fix typos in package description

* Wed Aug 09 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.0-alt1
- First build for ALT Linux Sisyphus

* Thu Jul 27 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.0-alt0.2
- Modifing icon

* Thu Jul 27 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.0-alt0.1
- Adding desktop file and icon

* Fri Jul 21 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.0-alt0
- New version 0.3.0
  * automatic and manual document's charset recognition

* Thu Jul 13 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.6-alt0.1
- SPEC file fix

* Wed Jul 12 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.6-alt0
- Initial build


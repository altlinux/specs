# test new macroses
%define python_build CFLAGS="%optflags" %__python setup.py build
%define python_install %__python setup.py install --root %buildroot

Name: winki
Version: 0.4.5
Release: alt1.qa1.1

Summary: Winki The Ripper

Url: http://www.winki-the-ripper.de/
License: GPL
Group: Development/Python

Source: http://www.winki-the-ripper.de/share/dist/%name-%version.tar.bz2
Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

AutoProv: yes, nopython
Requires: python%__python_version(pygtk) python%__python_version(libglade) python%__python_version(gnome)
%add_python_req_skip winki winkirip

BuildPreReq: python-devel

%description
Winki The Ripper aims to be the most easiest to use program for video
encoding. It is actually just a graphical frontend for GNOME written
in python to command line tools like mencoder, mplayer, mkvtoolnix,
oggenc and lsdvd.

%prep
%setup -q

%build
%python_build

%install
install -d %buildroot%_bindir
%python_install

%find_lang %name --with-gnome

%files -f %name.lang
#%_sysconfdir/*
%_bindir/%name
%_datadir/winkirip/
%_pixmapsdir/*
%_desktopdir/*
%python_sitelibdir/winkirip/

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.5-alt1.qa1.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.5-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for winki
  * postclean-05-filetriggers for spec file

* Thu Feb 21 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.5-alt1
- new version 0.4.5 (with rpmrb script)
- cleanup spec, build as noarch

* Sun May 13 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.3-alt1
- new version 0.4.3 (with rpmrb script)

* Sun Feb 25 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- new version 0.4.2
- remove Debian menu

* Wed Sep 20 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt0.1
- new version 0.4.1
- add python libglade, gnome requires

* Tue May 16 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt0.1
- new version 0.4.0
- remove old hacks
- disable noarch (python_sitelibdir is arch dependent)

* Sat Oct 15 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.11-alt1
- new version

* Sun Jun 05 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.8-alt1
- new version
- fix name of binary in menu file

* Wed Mar 23 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.6-alt2
- fix winki require

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.6-alt1
- new version
- add pygtk require

* Sat Mar 05 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.5-alt2
- fix files section

* Fri Mar 04 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.5-alt1
- first build for ALT Linux Sisyphus

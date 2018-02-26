Name: filezilla
Version: 3.3.3
Release: alt1
Summary: FileZilla is a fast and reliable FTP client
Packager: Stanislav Yadykin <tosick@altlinux.ru>

Group: Networking/File transfer
License: GPL
URL: http://filezilla.sourceforge.net/
Source: FileZilla_%{version}_src.tar.bz2

BuildRequires: gcc-c++ libgnutls-devel libidn-devel libgtk+2-devel wxGTK-devel libdbus-devel xdg-utils

%description
FileZilla is a fast and reliable FTP client and server with lots
of useful features and an intuitive interface

%prep
%setup -n %name-%version

%build
%configure
%make

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_bindir/*
%dir %_datadir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_pixmapsdir/%name.png
%_man1dir/*
%_man5dir/*

%changelog
* Wed Jun 30 2010 Stanislav Yadykin <tosick@altlinux.ru> 3.3.3-alt1
- 3.3.3

* Sat Mar 27 2010 Stanislav Yadykin <tosick@altlinux.ru> 3.3.2.1-alt1
- 3.3.2.1

* Sun Jan 24 2010 Stanislav Yadykin <tosick@altlinux.ru> 3.3.1-alt1
- 3.3.1

* Thu Dec 10 2009 Stanislav Yadykin <tosick@altlinux.ru> 3.3.0.1-alt1
- 3.3.0.1

* Tue Oct 27 2009 Stanislav Yadykin <tosick@altlinux.ru> 3.2.8.1-alt1
- 3.2.8.1

* Tue Sep 08 2009 Stanislav Yadykin <tosick@altlinux.ru> 3.2.7.1-alt1
- 3.2.7.1

* Wed Apr 01 2009 Stanislav Yadykin <tosick@altlinux.ru> 3.2.3.1-alt1
- 3.2.3.1

* Tue Mar 24 2009 Stanislav Yadykin <tosick@altlinux.ru> 3.2.3-alt1
- 3.2.3

* Thu Nov 06 2008 Stanislav Yadykin <tosick@altlinux.org> 3.1.5-alt1
- New version

* Fri Mar 30 2007 Nicolas Le'cureuil <neoclust на mandriva.org>
3.0.0-0.beta6.2mdv2007.1
+ Revision: 150123
- Fix summary
- Add icon into menu (bug #29881)

* Sat Mar 03 2007 Emmanuel Andry <eandry на mandriva.org>
3.0.0-0.beta6.1mdv2007.1
+ Revision: 131879
- New version 3.0.0 beta 6
- create menu entry

* Tue Jan 23 2007 Nicolas Le'cureuil <neoclust на mandriva.org>
3.0.0-0.beta5.1mdv2007.1
+ Revision: 112676
- Import filezilla
 

%define oname FileZilla

Name: filezilla
Version: 3.30.0
Release: alt1
Summary: FileZilla is a fast and reliable FTP client

Group: Networking/File transfer
License: GPL
Url: http://filezilla.sourceforge.net/
# Repacked http://download.filezilla-project.org/client/%{oname}_%{version}_src.tar.bz2
Source: %oname-%version.tar

# Automatically added by buildreq on Fri Sep 02 2016 (-ba)
# optimized out: at-spi2-atk elfutils fontconfig glib2-devel gnu-config libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libp11-kit libpango-devel libstdc++-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server perl pkg-config python-base python-modules xz
BuildRequires: gcc-c++ libdbus-devel libfilezilla-devel libgnutls-devel libgtk+3-devel libnettle-devel libpugixml-devel libsqlite3-devel libwxGTK3.0-devel xdg-utils

%description
FileZilla is a fast and reliable FTP client and server with lots
of useful features and an intuitive interface

%prep
%setup -n %oname-%version

%build
%configure --disable-autoupdatecheck
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_bindir/*
%dir %_datadir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_datadir/appdata/filezilla.appdata.xml
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_pixmapsdir/%name.png
%_iconsdir/hicolor/scalable/apps/filezilla.svg
%_man1dir/*
%_man5dir/*

%changelog
* Wed Jan 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.30.0-alt1
- Updated to upstream version 3.30.0.

* Thu Aug 10 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.26.1-alt1.1
- Rebuilt for changed libwxGTK3.0 ABI.

* Thu Jun 08 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.26.1-alt1
- Updated to 3.26.1.

* Wed Apr 12 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.25.1-alt1
- Updated to 3.25.1.

* Wed Feb 22 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.24.1-alt1
- Updated to 3.24.1.

* Thu Dec 22 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.23.0.2-alt1
- Updated to 3.23.0.2.

* Thu Sep 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.21.0-alt1
- Updated to 3.21.0.

* Mon Jul 04 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.19.0-alt1
- Updated to 3.19.0.

* Thu Jun 02 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.18.0-alt1
- Updated to 3.18.0.

* Wed May 04 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.17.0-alt1
- Updated to 3.17.0.

* Wed Mar 30 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.16.1-alt1
- Updated to 3.16.1.

* Thu Oct 29 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.14.1-alt1
- Updated to 3.14.1.

* Sun Aug 09 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.12.0.2-alt1
- Updated to 3.12.0.2.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.3.3-alt1.qa1
- NMU: rebuilt for debuginfo.

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


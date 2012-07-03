Summary: Graphical client for Firebird
Name: flamerobin
Version: 0.9.0
Release: alt2.qa1
License: BSD style
Group: Databases
Packager: Boris Savelev <boris@altlinux.org>

Source: %name-%version-src.tar.gz
Patch: flamerobin-0.9.0-gcc4.patch
Url: http://www.flamerobin.org/

# Automatically added by buildreq on Sat Oct 04 2008
BuildRequires: firebird-devel gcc-c++ wxGTK-contrib-stc-devel wxGTK-devel ImageMagick

%description
FlameRobin is a database administration tool for Firebird DBMS based on wxgtk
toolkit.

%prep
%setup -q -n %name-%version-src
%patch0 -p1

%build
%configure
%make_build

%install
%makeinstall_std

install -d %buildroot{%_niconsdir,%_miconsdir,%_liconsdir}
convert -size 16x16 ./res/fricon128.png %buildroot%_miconsdir/%name.png
convert -size 32x32 ./res/fricon128.png %buildroot%_niconsdir/%name.png
convert -size 48x48 ./res/fricon128.png %buildroot%_liconsdir/%name.png

%files
%doc docs
%_man1dir/flamerobin.1*
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_pixmapsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png

%changelog
* Tue Nov 17 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.0-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for flamerobin
  * postclean-05-filetriggers for spec file

* Mon May 25 2009 Boris Savelev <boris@altlinux.org> 0.9.0-alt2
- fix build with new toolchain

* Sat Oct 04 2008 Boris Savelev <boris@altlinux.org> 0.9.0-alt1
- initial build for Sisyphus from Mandriva

* Thu Jan 31 2008 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.8.3-1mdv2008.1
+ Revision: 160873
- New upstream: 0.8.3

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 18 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.8.1-1mdv2008.1
+ Revision: 99959
- Fix configure permission.
- New upstream: 0.8.1
- New upstream: 0.8.0

* Tue May 15 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.7.6-3mdv2008.0
+ Revision: 26964
- Rebuilt against new wx stuff.

* Wed Dec 20 2006 Götz Waschk <waschk@mandriva.org> 0.7.6-2mdv2007.0
+ Revision: 100700
- rebuild

* Mon Nov 27 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.7.6-1mdv2007.1
+ Revision: 87367
- New upstream: 0.7.6
- Added menu icon.

* Thu Nov 16 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.7.5-5mdv2007.1
+ Revision: 84903
- Added BuildRequires for ImageMagick: due to convert usage.
- Rebuilt against firebird 2.0 final.

* Thu Sep 07 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.7.5-4mdv2007.0
+ Revision: 60258
- New upstream: 0.7.5

* Wed Sep 06 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.7.2-4mdv2007.0
+ Revision: 59989
- Removed old-style menu entry. The new one (.desktop) will be added later.
- Import flamerobin

* Sat Sep 02 2006 Marcelo Ricardo Leitner <mrl@mandriva.com>
- Fixed BuildRequires.
- Removed hardcoded buildrequires to libraries: they should be automatic.
- Enhanced package description.

* Thu Aug 24 2006 Philippe Makowski <makowski@firebird-fr.eu.org>
- change Requires to libfirebird2

* Thu Aug 17 2006 Philippe Makowski <makowski@firebird-fr.eu.org>
- initial release


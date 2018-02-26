#%%define __kde4_alternate_placement 1
%define origname krusader

Name: kde4-%origname
Version: 2.4.0
Release: alt0.1

Source: %origname.tar.gz
Patch1: not_show_hidden_files.patch

Packager: Aeliya Grevnyov <gray_graff@altlinux.org>

Group: File tools
Summary: Advanced KDE twin-panel file-manager
License: GPLv3+
Url: http://www.krusader.org/

BuildRequires(pre): kde-common-devel
BuildRequires: kde4libs-devel gcc-c++ libjpeg-devel

%description
Krusader is an advanced twin panel (commander style) file manager
for KDE and other desktops in the *nix world, silar to Midnight
or Total Commander. It provides all the file management features
you could possibly want.

Plus: extensive archive handling, mounted filesystem support, FTP,
advanced search module, an internal viewer/editor, directory
synchronisation, file content comparisons, powerful batch renaming
and much much more. It supports a wide variety of archive formats
and can handle other KIO slaves such as smb or fish.

It is (almost) completely customizable, very user friendly,
fast and looks great on your desktop! You should give it a try.

This piece of software is developed by the Krusader Krew,
published under the GNU General Public Licence
(http://www.gnu.org/copyleft/gpl.html).

%prep
%setup -qn %origname
%patch1 -p2

%build
%K4build

%install
%K4install

%K4find_lang %origname --with-kde

%files -f %origname.lang
%doc README AUTHORS ChangeLog TODO COPYING SVNNEWS FAQ INSTALL
%_K4bindir/%origname
%_K4xdg_apps/*.desktop
%_K4apps/%origname
%_K4srv/*.protocol
%_K4conf/kio_isorc
%_K4iconsdir/*/*/apps/*.png
%_K4lib/*.so
%_K4doc/*
%_man1dir/%origname.*

%changelog
* Wed Jan 18 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 2.4.0-alt0.1
- Update to 2.4.0-beta1 (ALT#26829)

* Mon Jun 27 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.3.0-alt0.2
- Update to 2.3.0-beta1

* Fri Feb 25 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.3.0-alt0.1
- Update to git a65a9653fdb230fa65a8b6bd230eb04a4b0f33ac
- move to standart place

* Tue Nov 09 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.0-alt2.svn20101108
- Update to svn 20101108

* Sat May 08 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.0-alt1.beta1
- Update to 2.2.0-beta1

* Mon Feb 08 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt2.beta1
- Update to svn 20100208 (ALT #22223)
- Not show hidden files by default (ALT #22496)

* Mon Nov 02 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt1.beta1
- Update to 2.1.0-beta1

* Fri Aug 28 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.0-alt4
- Picked up from orphaned
- Update to svn 20090828

* Sun Apr 12 2009 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt3
- Krusader 2.0.0 "Mars Pathfinder" released!

* Sat Apr 11 2009 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt2.svn6287.1
- new version - 2.0.0-svn6287
- temporary disabled russian docs (docs old ald not compileable)

* Wed Mar 11 2009 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt2.svn6247.2
- delete CVSNEWS from spec

* Wed Mar 11 2009 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt2.svn6247.1
- new version - 2.0.0-svn6247

* Tue Mar 10 2009 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt1.svn6244.1
- new version - 2.0.0-svn6244

* Tue Jan 20 2009 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt0.beta2.1
- new version - 2.0.0-beta2

* Wed Nov 19 2008 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt0.beta1.2
- fix repocop errors - remove update-desktop-database, update_menus macroses

* Fri Oct 24 2008 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt0.beta1.1
- initial build for Sisyphus (KDE4)

Name: kxdocker-resources
Version: 0.14
Release: alt1.1.qa2
Summary: Resources for KXDocker
License: GPL
Group: Graphical desktop/KDE
Url: http://www.xiaprojects.com/www/prodotti/kxdocker/main.php
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: %name-%version.tar.bz2
BuildArch: noarch

# Automatically added by buildreq on Sun Dec 11 2005 (-bi)
BuildRequires: fontconfig freetype2 kde-settings kdelibs


Requires: kxdocker

# just need kde-config
BuildRequires: kdelibs-devel


%description
Plugins, backgrounds, icons, sounds for KXDocker

%description -l ru_RU.KOI8-R
Плагины, фоны, иконки, звуки для KXDocker

%prep

%setup -q

%build
%K3configure

%install
%K3install KXDPREFIX=apps/kxdocker

# remove crud
find $RPM_BUILD_ROOT -type d -depth -name '.xv*' -exec rm -vrf {} \; 
find $RPM_BUILD_ROOT -type f -name '.DS*' -o -name '*copia.png' | xargs rm -vf

# fixup permissions
find $RPM_BUILD_ROOT -type f -name '*.png' -exec chmod 0644 {} \; 


#menu
%files
%doc readme.txt 
%_K3apps/kxdocker

%changelog
* Mon Apr 25 2011 Andrey Cherepanov <cas@altlinux.org> 0.14-alt1.1.qa2
- Adapt to new KDE3 placement

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.14-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for kxdocker-resources
  * postclean-05-filetriggers for spec file

* Tue Oct 06 2008 Ilya Mashkin <oddity@altlinux.ru> 0.14-alt1.1
- rebuild

* Sun Dec 11 2005 Ilya Mashkin <oddity at altlinux.ru> 0.14-alt1
- new version 0.14
- add russian description

* Tue Oct 19 2004 Dmitriy Porollo <spider@altlinux.ru> 0.7-alt2
-0.7-alt1 ADD: Network usage applet. 

* Tue Sep 15 2004 Dmitriy Porollo <spider@altlinux.ru> 0.7-alt1
-0.7-alt1 ADD: Some Icons.
-0.7-alt1 ADD: New Theme.

* Mon Jun 21 2004 Dmitriy Porollo <spider@altlinux.ru> 0.6-alt2
-0.6-alt1 ADD: Crystal-pink background.
-0.6-alt1 ADD: Crystal-suse background.
-0.6-alt1 ADD: Transparent-pink background.

* Wed Jun 11 2004 Dmitriy Porollo <spider@altlinux.ru> 0.6-alt1
-0.6-alt1 ADD: CPU monitor

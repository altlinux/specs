Name: kmobiletools
Version: 0.4.3.3
Release: alt4.1

Summary: KMobileTools is a nice KDE-based application that allows to control mobile phones with your PC.
License: GPL
Group: Communications
Url: http://www.kmobiletools.org/
Packager: Ilya Mashkin <oddity at altlinux dot ru>

Source0: %name-%version.tar.bz2
Source1: %name.mo
#Patch0: kmt_kde_3.2-1.patch
#Patch1: kmt_kde_3.2-2.patch

BuildRequires: flex fontconfig freetype2 gcc-c++ gcc-g77 kdelibs-devel libjpeg-devel libpng-devel libqt3-devel libqt3-settings libstdc++-devel qt3-designer xml-utils zlib-devel

%description
KMobileTools (was QTMobileTools) is a nice KDE-based application that allows to control mobile phones with your PC.
It handles full SMS control, dialing calls, reading from phonebook, last dials, received and unanswered calls and phone 
status monitoring (battery and signal for now). It's based on a Motorola C350 mobile phone, but's also tested on some 
Nokia and Ericsson phones.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1

make -f admin/Makefile.common cvs

%build
%K3configure
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%K3install

mkdir -p %buildroot/%_K3i18n/ru/LC_MESSAGES
install -pD -m644 %SOURCE1 %buildroot/%_K3i18n/ru/LC_MESSAGES/

%K3find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog README
%_K3bindir/%name
%_K3xdg_apps/%name.desktop
%_K3apps/%name
%_kde3_iconsdir/hicolor/*/apps/%name.*

%changelog
* Wed Feb 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3.3-alt4.1
- Removed bad RPATH

* Tue Apr 26 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.3.3-alt4
- fix build requires

* Sat Mar 05 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.3.3-alt3
- move to alternate place

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.3.3-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for kmobiletools
  * postclean-05-filetriggers for spec file

* Mon Jan 01 2007 Ilya Mashkin <oddity@altlinux.ru> 0.4.3.3-alt2
- update URL

* Tue May 02 2006 Ilya Mashkin <oddity at altlinux dot ru> 0.4.3.3-alt1
- new version 0.4.3.3, step to 0.5

* Wed Mar 23 2006 Ilya Mashkin <oddity at altlinux dot ru> 0.4.3.2-alt1
- new version 0.4.3.2

* Wed Mar 30 2005 Ilya Mashkin <oddity at altlinux dot ru> 0.4.3.1-alt1
- new version 0.4.3.1

* Wed Feb 02 2005 Ilya Mashkin <oddity at altlinux dot ru> 0.4.2-alt1
- new version, just little fixes

* Tue Jan 11 2005 Ilya Mashkin <oddity at altlinux dot ru> 0.4.1-alt1
- New Version 0.4.1
- Cleanup spec

* Thu Nov 02 2004 Dmitriy Porollo <spider@altlinux.ru> 0.4.0-alt1
- New release.
- Russian translation updated.

* Wed Sep 29 2004 Dmitriy Porollo <spider@altlinux.ru> 0.3.1-alt2
- Russian translate added (Thanks to Genix). 
- Build bugs fixed.

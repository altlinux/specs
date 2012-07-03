Name: yakuake
Version: 2.9.7
Release: alt1

Summary: Very powerful Quake style Konsole
License: GPLv2, GPLv3 or any later version accepted by the membership of KDE e.V.
Group: Terminals

Url: http://extragear.kde.org/apps/yakuake/
Packager: Andrey Rahmatullin <wrar@altlinux.org>

Source: http://download.berlios.de/yakuake/%name-%version.tar.bz2

BuildPreReq: bzlib-devel gcc-c++ kde4libs-devel
BuildRequires(pre): kde-common-devel

Requires: kde4base-konsole

%define _unpackaged_files_terminate_build 1
%define __kde4_alternate_placement 1

Obsoletes: kde4-yakuake < 2.9.6-alt2
Provides: kde4-yakuake = %version-%release

%description
A KDE konsole which looks like those found in Quake.

This version is built with KDE4.

%prep
%setup

%build
%K4build

%install
%K4install

%K4find_lang --with-kde %name


%files -f %name.lang
%doc AUTHORS ChangeLog KDE4FAQ NEWS README TODO
%_kde4_bindir/*
%_kde4_xdg_apps/*.desktop
%_kde4_iconsdir/*/*/apps/*
%_K4apps/%name


%changelog
* Sat Jul 17 2010 Andrey Rahmatullin <wrar@altlinux.org> 2.9.7-alt1
- 2.9.7

* Tue Jun 02 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.6-alt2
- rename back to yakuake

* Fri May 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.6-alt1
- 2.9.6

* Tue May 12 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.5-alt1
- 2.9.5

* Mon Nov 17 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.4-alt3
- remove update_*/clean_* invocations

* Wed Oct 29 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.4-alt2
- Sisyphus build
- rename to kde4-yakuake, enable __kde4_alternate_placement

* Sat Sep 06 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.4-alt1
- 2.9.4

* Sat Aug 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.3-alt2
- rebuild

* Mon Jun 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.3-alt1
- 2.9.3

* Sat May 10 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.2-alt1
- 2.9.2
- use %%K4find_lang

* Sun Mar 30 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.1-alt1
- 2.9.1

* Mon Mar 10 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9-alt1
- 2.9 (KDE4 version)
- Daedalus build

* Sun Feb 10 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Tue Nov 20 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.8-alt2
- spec cleanup
- enable _unpackaged_files_terminate_build
- fix packaging of icons (#10173, php-coder@)

* Sat Oct 13 2007 Nick S. Grechukh <gns@altlinux.org> 2.8-alt1
- new version (wrar@ reminded ;)

* Thu May 04 2006 Nick S. Grechukh <gns@altlinux.org> 2.7.5-alt1
- new version. fixed Url and Source. i18n removed (fixed in upstream)

* Mon Feb 13 2006 Nick S. Grechukh <gns@altlinux.org> 2.7.3-alt5
- removed kdedesktop2mdkmenu

* Sun Nov 13 2005 Nick S. Grechukh <gns@altlinux.ru> 2.7.3-alt4
- new version with i18n patch from Albert Valiev

* Mon Oct 24 2005 Nick S. Grechukh <gns@altlinux.org> 2.7.2-alt1
- new version

* Thu Oct 13 2005 Nick S. Grechukh <gns@altlinux.org> 2.6-alt1
- initial build 

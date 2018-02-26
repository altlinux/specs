%define parent_app k3b
%define real_name %parent_app-i18n
%define reqiures_version %parent_app >= 1.0.1
%define	stable_patchset	1.0.5


Name: %real_name
Version: 1.0.5
Release: alt1.1

Summary: Multilingual support for k3b CD-burning tool.
Summary(ru_RU.KOI8-R): Многоязыковая поддержка для утилиты записи CD k3b.
License: GPL
Group: Archiving/Cd burning
Packager: Ilya Mashkin <oddity@altlinux.ru>
URL: http://www.k3b.org/

Requires: %reqiures_version
Obsoletes: %real_name-cs %real_name-de %real_name-et %real_name-fr %real_name-ru %real_name-uk %real_name-world

Source: %real_name-%version.tar.bz2
#Patch0: %real_name-%stable_patchset-ru_fixes.patch
Patch1: %real_name-%stable_patchset-messages-alt.patch
#Patch2: %real_name-%stable_patchset-format_dvd_+-_rw.patch
Patch3: %real_name-%stable_patchset-noarch-config.patch

BuildArch: noarch
BuildRequires: kdelibs-devel >= 3.1, xml-utils

%description
Multilingual support for k3b CD-burning tool.
%description -l ru_RU.KOI8-R
Многоязыковая поддержка для утилиты записи CD k3b.


%prep
%setup -q -n %real_name-%version
#%patch0 -p1
%patch1 -p1
#%patch2 -p1
%patch3 -p1
%__subst 's/\.la\>/.so/g' admin/acinclude.m4.in
MAKE="%__make" /bin/sh admin/cvs.sh cvs


%build
%set_automake_version 1.10
%configure --without-qt --without-arts
make


%install
make install DESTDIR=%buildroot
%find_lang --with-kde %parent_app libk3bdevice --output=%parent_app.lang

#Brasilian portuguese language files
echo '%lang(pt) /usr/share/doc/HTML/pt_BR/k3b/' >> %parent_app.lang


%files -f %parent_app.lang


%changelog
* Tue May 26 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.5-alt1.1
- fix build

* Mon Jun 02 2008 Alexey Lokhin <warframe@altlinux.ru> 1.0.5-alt1
- Version 1.0.5 build.

* Tue Aug 07 2007 Alexey Lokhin <warframe@altlinux.ru> 1.0.3-alt2
- Language subpackages have been removed.

* Mon Aug 06 2007 Alexey Lokhin <warframe@altlinux.ru> 1.0.3-alt1
- Version 1.0.3 build from SVN.

* Mon Oct 16 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.17-alt1
- Version 0.12.17 build.
- Some patches considered unneeded. Removed.

* Wed Jul 19 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.16-alt1
- Version 0.12.16 build.

* Tue Apr 25 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.15-alt1
- Version 0.12.15 build.

* Wed Mar 08 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.14-alt1
- Version 0.12.14 build.

* Thu Feb 16 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.12-alt1
- Version 0.12.12 build.

* Sat Feb 11 2006 Alexey Lokhin <warframe@altlinux.ru> 0.12.11-alt1
- Version 0.12.11 build.

* Wed Dec 21 2005 Alexey Lokhin <warframe@altlinux.ru> 0.12.10-alt1
- Version 0.12.10 build.
- Russian translation files corrected. Thanks to Vitaly Lipatov <lav@>
- Reorganized patchset.
- Added patch, correcting Russian translation mistakes - 'ru_fixes.patch'.
- New patch for ALT-Specific messages - 'messages-alt.patch'.
- Added patch, correcting translation of "Format DVD+-RW" message - 'format_dvd_+-_rw.patch'.

* Mon Nov 21 2005 Alexey Lokhin <warframe@altlinux.ru> 0.12.7-alt1
- Version 0.12.7 build.
- Small fixes in russian translation patch.

* Fri Oct 07 2005 Alexey Lokhin <warframe@altlinux.ru> 0.12.4a-alt1
- Version 0.12.4a build.
- Russian translation files corrected/rewritten and completed. Many big thanks to Alexey Borovskoy <alb@>.

* Mon Aug 08 2005 Alexey Lokhin <warframe@altlinux.ru> 0.12.2-alt1
- Version 0.12.2 build.
- Added patch for ALT-specific russian messages (no K3bSetup2 but ALT Control Center and 'control').
- Package moved to noarch. Added patch for configure to work with 'noarch'.

* Wed Feb 23 2005 Alexey Lokhin <warframe@altlinux.ru> 0.11.1-alt3
- Spec file cleaning

* Thu Jan 13 2005 Alexey Lokhin <warframe@altlinux.ru> 0.11.1-alt2
- 'cvs.sh' script modified to work with automake 1.9.x.

* Wed Sep 08 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11.1-alt1
- Translations from KDE CVS.

* Mon Jun 28 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11-alt2
- Changed requirement for k3b since 'k3b' package was renamed to 'k3b-minimal'.

* Mon Mar 22 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11-alt1
- i18n package for k3b-0.11.
- Main package splitted into multiple localization packages.
- Removed undone k3b Handbook localizations.

* Sat Feb 14 2004 Alexey Lokhin <warframe@altlinux.ru> 0.11-alt0.1
- No translations found on k3b's site. Custom translation package has been made.

* Thu Dec 18 2003 Alexey Lokhin <warframe@altlinux.ru> 0.10-alt2
- Spec file fixed for building without libtool

* Tue Oct 28 2003 Alexey Lokhin <warframe@altlinux.ru> 0.10-alt1
- i18n package for k3b-0.10 has been built

* Tue Oct 21 2003 Rider <rider@altlinux.ru> 0.9-alt2
- more russian translated

* Tue Oct 07 2003 Alexey Lokhin <warframe@altlinux.ru> 0.9-alt1
- k3b i18n package has been built

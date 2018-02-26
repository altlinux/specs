%add_findpackage_path %_kde4_bindir

%define cid	plasmanotify\@andreas-demmer.de
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name: firefox-kde4
Version: 0.3.2
Release: alt5

Summary: Plasma Notifications for Firefox
License: GPLv3
Group: Networking/WWW
BuildArch: noarch

Provides: firefox-plasmanotify = %version-%release
Obsoletes: firefox-plasmanotify < %version-%release

Requires: firefox kmozillahelper kde4base-kdialog
#Requires: firefox-oxygen


Source: plasmanotify-%version-fx-linux.xpi
Source1: ru-RU.tar
Patch1: kde-only.patch
Patch2: add-ru.patch
Patch3: requires.patch

BuildRequires(pre): rpm-build-firefox
BuildRequires: unzip

%description
This addon makes Firefox notifications appear as Plasma notifications

%prep
%setup -c
#pushd chrome/locale
#tar xf %SOURCE1
#popd
#%patch1 -p1
#%patch2 -p1
%patch3 -p0

%build

%install
mkdir -p %buildroot/%ciddir
cp -r * %buildroot/%ciddir

%files
#%ciddir

%changelog
* Tue Feb 07 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.2-alt5
- don't package PlasmaNotify

* Wed Jan 25 2012 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt3.M60P.2
- Add compatibility with Firefox 9.x

* Mon Nov 21 2011 Sergey V Turchin <zerg@altlinux.org> 0.3.2-alt3.M60P.1
- built for M60P

* Mon Nov 21 2011 Sergey V Turchin <zerg@altlinux.org> 0.3.2-alt4
- fix conflict with Firefox 8

* Fri Oct 14 2011 Sergey V Turchin <zerg@altlinux.org> 0.3.2-alt2.M60P.1
- built for M60P

* Fri Oct 14 2011 Sergey V Turchin <zerg@altlinux.org> 0.3.2-alt3
- fix conflict with Firefox 7

* Wed Aug 24 2011 Sergey V Turchin <zerg@altlinux.org> 0.3.2-alt2
- fix conflict with Firefox 6

* Wed Jul 06 2011 Sergey V Turchin <zerg@altlinux.org> 0.3.2-alt1
- new version

* Wed Apr 06 2011 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt2
- don't require firefox-oxygen
- resolve conflict with firefox4

* Sat Nov 13 2010 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt0.M51.1
- built for M51

* Thu Nov 11 2010 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- package PlasmaNotify again

* Thu Sep 24 2009 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt3
- don't package PlasmaNotify because provided by kmozillahelper-0.5
- require firefox-oxygen

* Mon Sep 21 2009 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt2
- fix to add Russian translation

* Thu Sep 17 2009 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- initial specfile


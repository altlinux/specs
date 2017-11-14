# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           iapetal
Version:        1.3
Release:        alt1_5
Summary:        A 2D space rescue game

Group:          Games/Other
License:        GPLv3+
URL:            http://iapetal.sourceforge.net
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        iapetal.desktop
BuildArch:      noarch
BuildRequires:  desktop-file-utils
Requires:       python3-module-pygame python3-module-pygobject3 icon-theme-hicolor
Source44: import.info

%description
Fly your lander carefully to rescue the scientists in the habitat module
from the falling asteroids.

%prep
%setup -q


%build


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/iapetal
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata

install -m 755 iapetal.py $RPM_BUILD_ROOT%{_bindir}/iapetal
install -m 755 iapetal-launcher.py $RPM_BUILD_ROOT%{_bindir}/iapetal-launcher
install -m 644 *.ogg $RPM_BUILD_ROOT%{_datadir}/iapetal/
install -m 644 *.png $RPM_BUILD_ROOT%{_datadir}/iapetal/
install -m 644 iapetal.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 habitat.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}


%files
%doc COPYING TODO
%{_bindir}/*
%{_datadir}/iapetal
%{_datadir}/applications/iapetal.desktop
%{_datadir}/icons/hicolor/32x32/apps/habitat.png
%{_datadir}/appdata/iapetal.appdata.xml

%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_5
- NMU (for oddity@): new version by fcimport

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.qa1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.1-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * obsolete-call-in-post-gtk-update-icon-cache for iapetal

* Tue Dec 21 2010 Ilya Mashkin <oddity@altlinux.ru> 1.1-alt1
- Build for ALT Linux

* Wed Jul 14 2010 Jon Ciesla <limb@jcomserv.net> - 1.1-1
- New upstream, fixed rescue collision bugs.

* Wed Jun 09 2010 Jon Ciesla <limb@jcomserv.net> - 1.0-3
- More desktop file corrections.

* Tue May 18 2010 Jon Ciesla <limb@jcomserv.net> - 1.0-2
- Corrected desktop file.

* Thu May 06 2010 Jon Ciesla <limb@jcomserv.net> - 1.0-1
- First build.

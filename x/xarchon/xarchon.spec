# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ imake libXt-devel xorg-cf-files
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           xarchon
Version:        0.50
Release:        alt2_27
Summary:        Arcade board game
Group:          Games/Other
License:        GPL+
URL:            http://xarchon.seul.org/
Source0:        http://xarchon.seul.org/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Patch0:         %{name}-fonts.patch
Patch1:         %{name}-destdir.patch
Patch2:         http://ftp.debian.org/debian/pool/main/x/%{name}/%{name}_0.50-10.1.diff.gz
Patch3:         xarchon-0.50-gcc43.patch
BuildRequires:  gtk+-devel libesd-devel libXpm libXpm-devel
BuildRequires:  desktop-file-utils ImageMagick-tools libappstream-glib
Requires:       icon-theme-hicolor
Source44: import.info
Patch33: xarchon-0.50-alt-DSO.patch

%description
XArchon is a chess with a twist board game.


%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch33 -p2


%build
%configure
%make_build
convert -resize 64x64 data/icon.xpm %{name}.png


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install      \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc AUTHORS ChangeLog README
%doc --no-dereference COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_mandir}/man6/%{name}.6*


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_27
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_25
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_23
- update to new release by fcimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_22
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_20
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_17
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_16
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_15
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_14
- update to new release by fcimport

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_13
- new fc release and picked up real@'s patch

* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.50-alt2_12.1
- Fixed build

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_12
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_12
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_11
- converted from Fedora by srpmconvert script


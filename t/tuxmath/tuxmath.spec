# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/makensis gcc-c++ libxml2-devel pkgconfig(cairo)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           tuxmath
Version:        2.0.3
Release:        alt1_1
Summary:        Educational math tutor for children

Group:          Games/Other
License:        GPLv3+ and CC-BY and OFL
URL:            http://tux4kids.alioth.debian.org/
Source0:        https://alioth.debian.org/frs/download.php/3271/%{name}_w_fonts-%{version}.tar.gz
Source1:        %{name}.appdata.xml
#Patch0:	        tuxmath_w_fonts-2.0.1-scandir.patch
Patch1:         tuxmath_w_fonts-2.0.1-gcc5.patch
#Patch2:         tuxmath_w_fonts-2.0.1-powerup-crash.patch

BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires:  libSDL-devel
BuildRequires:  libSDL_image-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libSDL_pango-devel
BuildRequires:  libSDL_net-devel
BuildRequires:  librsvg-devel librsvg-gir-devel
BuildRequires:	t4k_common-devel
Requires:       icon-theme-hicolor
Source44: import.info

%description
TuxMath is an educational math tutor for children. It features several
different types of gameplay, at a variety of difficulty levels.


%prep
%setup -q -n %{name}_w_fonts-%{version}
# remove unneeded font files
rm -f data/fonts/*.ttf
#%patch0 -p1
%patch1 -p1
#%patch2 -p1


%build
%configure
%make_build


%install
%makeinstall_std
%find_lang %{name}

desktop-file-install --vendor="" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 data/images/icons/icon.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 data/images/icons/tuxmath.svg \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files -f %{name}.lang
%{_docdir}/%{name}
%{_bindir}/%{name}*
%{_bindir}/generate_lesson
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt1_1
- new version

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_12
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_11
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_9
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_3
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_2
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_2
- update to new release by fcimport

* Fri Oct 28 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_1
- use fedora versions

* Tue Aug 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_0
- new version; manual update (#26080); note the patch

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_2
- rebuild with new librsvg

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_2
- converted from Fedora by srpmconvert script


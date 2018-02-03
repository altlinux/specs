# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           worminator
Version:        3.0R2.1
Release:        alt2_27
Summary:        Sidescrolling platform and shoot'em up action-game
Group:          Games/Other
License:        GPLv2+
URL:            http://sourceforge.net/projects/worminator/
Source0:        http://downloads.sourceforge.net/worminator/worminator-%{version}.tar.gz
Source1:        worminator.png
Source2:        worminator.desktop
Patch0:         worminator-3.0R2.1-speed.patch
Patch1:         worminator-3.0R2.1-format-security.patch
BuildRequires:  liballegro-devel, desktop-file-utils
Requires:       worminator-data >= 3.0R2.1, icon-theme-hicolor
Source44: import.info

%description
You play as The Worminator and fight your way through many levels of madness
and mayhem. Worminator features nine unique weapons, visible character damage,
full screen scrolling, sound and music, and much more!


%prep
%setup -q
%patch0 -p1 -z .speed
%patch1 -p1
sed -i 's/\r//' ReadMe.txt


%build
gcc $RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations \
  -Wno-char-subscripts -DDATADIR=\"%{_datadir}/%{name}/\" -o %{name} \
  Worminator.c `allegro-config --libs` -lm


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

desktop-file-install                           \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        %{SOURCE2}

%files
%doc ReadMe.txt changes.unix license.txt license-change.txt
%{_bindir}/%{name}
%{_datadir}/applications/worminator.desktop
%{_datadir}/icons/hicolor/32x32/apps/worminator.png


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_27
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_26
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_24
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_23
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_22
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_21
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_20
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_18
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_17
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_16
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_15
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt1_15
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt1_14
- update to new release by fcimport

* Thu May 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0R2.1-alt1_13.1
- fix build

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt1_13
- converted from Fedora by srpmconvert script


Name: slingshot
Version:  0.8.1p
Release:  alt4_9
Summary: A Newtonian strategy game

Group: Games/Other
License: GPLv2+        
URL: http://www.slingshot-game.org/
Source0: http://downloads.sourceforge.net/slingshot-game/slingshot-%{version}.tar.gz
Source1: slingshot.desktop
Source2: slingshot
Patch0: slingshot-font-path.patch
Patch1: slingshot-0.8.1p-type-mismatch.patch
BuildArchitectures: noarch
BuildRequires: desktop-file-utils
Requires: icon-theme-hicolor fonts-ttf-gnu-freefont-sans
Source44: import.info

%description
Slingshot is a two dimensional, turn based simulation-strategy game 
set in the gravity fields of several planets. It is a highly 
addictive game, and never the same from round to round due to its 
randomly generated playing fields.

%prep
%setup -q

%patch0 -p0
%patch1 -p1

%build

rm -f slingshot/data/FreeSansBold.ttf

%install

mkdir -p  %{buildroot}%{_bindir}
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}/slingshot

mkdir -p  %{buildroot}%{_datadir}/slingshot
install -m 644 slingshot/*.py %{buildroot}%{_datadir}/slingshot
mkdir -p  %{buildroot}%{_datadir}/slingshot/data
install -m 644 slingshot/data/* %{buildroot}%{_datadir}/slingshot/data

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mv slingshot/data/icon64x64.png slingshot/data/slingshot.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 slingshot/data/slingshot.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps

%files
%{_bindir}/slingshot
%{_datadir}/slingshot/
%doc Readme.txt slingshot/licence.txt
%{_datadir}/applications/slingshot.desktop
%{_datadir}/icons/hicolor/64x64/apps/slingshot.png

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt4_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt4_8
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt4_7
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt3_7
- update to new release by fcimport

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1p-alt3_6.1
- Rebuild with Python-2.7

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt3_6
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt2_6
- rebuild with new rpm desktop cleaner

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt1_6
- converted from Fedora by srpmconvert script


# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++
# END SourceDeps(oneline)
BuildRequires: liballegro-devel
%define oldname ants
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           Ants
Version:        1.4
Release:        alt2_22
Summary:        Guide the insects safely home before they drop of the cliff
Group:          Games/Other
License:        Public Domain
URL:            http://www.allegro.cc/depot/Ants
Source0:        http://games.linux.sk/files/ants-1.4.tar.gz
Source1:        ants.desktop
Source2:        ants-level-editor.desktop
Source3:        ants.png
Source4:        license-info
Patch0:         ants-1.4-fixes.patch
BuildRequires:  liballegro-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
You take command in the game of a bunch of small ants and have to guide them
around in levels. Since the ants walk on their own, the player can only
influence them by giving them commands, like build a bridge, dig a hole or
redirect all ants in the other direction. The goal of each level is to
reach the exit, for which multiple combination of commands are necessary.
The game is presented in a 2D side view.


%package        level-editor
Summary:        Ants level editor
Group:          Games/Other
Requires:       %{name} = %{version}-%{release}

%description    level-editor
This package contains a level editor for ants, notice that you must run this
at root, or change the owner of the files under %{_datadir}/%{oldname}, as the
level editor edits the files directly under %{_datadir}/%{oldname} .

%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p1 -z .fix
sed -i 's/\r//g' ants.txt
cp %{SOURCE4} .

%build
%make_build EXTRACFLAGS="$RPM_OPT_FLAGS"

%install
#no make install target, DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{oldname}
install -m 755 %{oldname} %{oldname}_le $RPM_BUILD_ROOT%{_bindir}
cp -a %{oldname}.dat levels1 levels2 $RPM_BUILD_ROOT%{_datadir}/%{oldname}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/

%files
%doc Changelog ants.txt license-info
%{_bindir}/%{oldname}
%{_datadir}/%{oldname}
%{_datadir}/applications/%{oldname}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{oldname}.png

%files level-editor
%{_bindir}/%{oldname}_le
%{_datadir}/applications/%{oldname}-level-editor.desktop

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_22
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_21
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_19
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_18
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_17
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_15
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_14
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_13
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_12
- update to new release by fcimport

* Sun Jul 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_11
- new release

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_10
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_10
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_9
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_8
- initial release by fcimport


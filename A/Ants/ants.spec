# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: liballegro-devel
%define oldname ants
Name:           Ants
Version:        1.4
Release:        alt2_10
Summary:        Guide your ants safely home before they drop of the cliff
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
Requires:       Ants = %{version}-%{release}

%description    level-editor
This package contains a level editor for ants, notice that you must run this
at root, or change the owner of the files under %{_datadir}/%{oldname}, as the
level editor edits the files directly under %{_datadir}/%{oldname} .


%prep
%setup -q -n %{oldname}-%{version}
%patch0 -p1 -z .fix
sed -i 's/\r//g' ants.txt
cp %{SOURCE4} .


%build
make %{?_smp_mflags} EXTRACFLAGS="$RPM_OPT_FLAGS"


%install
#no make install target, DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{oldname}
install -m 755 %{oldname} %{oldname}_le $RPM_BUILD_ROOT%{_bindir}
cp -a %{oldname}.dat levels1 levels2 $RPM_BUILD_ROOT%{_datadir}/%{oldname}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
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
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_10
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_10
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_9
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_8
- initial release by fcimport


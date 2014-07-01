# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libqt4-devel unzip
# END SourceDeps(oneline)
Name:           GLC_Player
Version:        2.3.0
Release:        alt2_7
Summary:        GLC_Player is an Open Source software used to view 3d models (OBJ Format)

Group:          Graphics
License:        GPLv2+
URL:            http://www.glc-player.net/
Source0:        http://downloads.sourceforge.net/glc-player/GLC_Player_src_%{version}.zip
Source1:        glc_player.desktop
Patch0:         GLC_Player_src_2.3.0-cache.patch
Patch1:         GLC_Player_src_2.3.0-prefix.patch

BuildRequires:  GLC_lib-devel >= 2.0.0
BuildRequires:  desktop-file-utils
Source44: import.info

%description
GLC_Player is an Open Source software used to view 3d models (OBJ Format).
With the session concept and navigation possibilities GLC_Player is the
accurate tools to review a lot of 3D models. GLC_Player is a 
cross-platform, Qt 4 and GLC_lib application.


%prep
%setup -q -c
%patch0 -p1 -b .cache
%patch1 -p1 -b .prefix


%build
qmake-qt4 glc_player.pro
make %{?_smp_mflags}


%install

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -pm 0755 glc_player $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}

install -pm 0644 ressources/images/GLC_logo_blanc.png \
  $RPM_BUILD_ROOT%{_datadir}/pixmaps/glc_player.png

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --mode 644 \
  %{SOURCE1}	


%files
%doc
%{_bindir}/glc_player
%{_datadir}/pixmaps/glc_player.png
%{_datadir}/applications/*.desktop


%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt2_7
- update to new release by fcimport

* Thu May 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt2_6
- moved to Sisyphus by request of dd@

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_6
- update to new release by fcimport

* Sat Apr 13 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_5
- update to new release by fcimport

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_4
- update to new release by fcimport

* Wed Jan 16 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_3
- initial fc import


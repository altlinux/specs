# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-install gcc-c++ libdevil-devel
# END SourceDeps(oneline)
Name:           cdogs-sdl
Version:        0.5.8
Release:        alt1_4
Summary:        C-Dogs is an arcade shoot-em-up
Group:          Games/Other
# The game-engine is GPLv2+
# The original game art is Redistributable, no modification permitted
# This is slowly being replaced upstream by CC art
License:        GPLv2+ and Redistributable, no modification permitted and CC-BY and CC-BY-SA and CC0
URL:            http://cxong.github.io/cdogs-sdl/
# This uses git-submodules and github's foo/bat/archive/tag.tar.gz feature
# does not deal with this. To regenerate do:
# git clone git clone https://github.com/cxong/cdogs-sdl.git
# cd cdogs-sdl
# git checkout %{version}
# git submodule init
# git submodule update --init --recursive
# git submodule update --recursive
# rm -rf `find -name .git`
# cd ..
# mv cdogs-sdl cdogs-sdl-%{version}
# tar cvfJ cdogs-sdl-%{version}.tar.xz cdogs-sdl-%{version}
Source0:        cdogs-sdl-%{version}.tar.xz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Patch0:         cdogs-sdl-0.5.8-cmake.patch
BuildRequires: ctest cmake libSDL_mixer-devel libSDL_image-devel ncurses-devel libphysfs-devel
BuildRequires:  desktop-file-utils libicns-utils libappstream-glib
Requires:       icon-theme-hicolor
Obsoletes:      cdogs-data < 0.5
Provides:       cdogs-data = %{version}-%{release}
Source44: import.info

%description
C-Dogs SDL is a port of the old DOS arcade game C-Dogs to modern operating
systems utilising the SDL Media Libraries. C-Dogs is an arcade shoot-em-up
which lets players work alone and cooperatively during missions or fight
against each other in the a.'dogfighta.' deathmatch mode. The DOS version of
C-Dogs came with several built in missions and dogfight maps. This version
does too. The author of the DOS version of C-Dogs was Ronny Wester. We would
like to thank Ronny for releasing the C-Dogs sources to the public.


%prep
%setup -q
%patch0 -p1
sed -i 's/\r//' doc/original_readme.txt


%build
%{fedora_cmake} -DCDOGS_DATA_DIR=/usr/share/cdogs-sdl/
make %{?_smp_mflags}
icns2png -x build/macosx/cdogs-icon.icns

%install
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

for i in 16 32 48 128; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/apps
  install -m 644 cdogs-icon_${i}x${i}x32.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done


%files
%doc doc/AUTHORS doc/CREDITS doc/original_readme.txt
%doc doc/COPYING.BSD doc/COPYING.GPL
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.8-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.5.8-alt1_2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt4_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt4_13
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt4_12
- update to new release by fcimport

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt4_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt4_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt4_8
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt3_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.4-alt3_7
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_7
- rebuild with new rpm desktop cleaner

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_7
- converted from Fedora by srpmconvert script


Name:         glob2
Version:      0.9.4.4
Release:      alt1.qa7
Summary:      Globulation 2 is a Real-Time Strategy (RTS) game which reduces micro-management by automatically assigning tasks to units
License:      GPL
Group:        Games/Strategy 
URL:          http://globulation2.org
Packager:     Ilya Mashkin <oddity@altlinux.ru>
Requires:     glob2-data
Source0:       %{name}-%{version}.tar.gz
Source1:      %{name}-icons.tar.bz2
Source2:      %{name}.desktop
#Patch1:       glob2-0.8.19-gcc41.patch
#Patch2:	      glob2-sdl_ttf.patch

Patch0:         glob2-texts.pl.patch
Patch2:         glob2-gcc43.patch
Patch3:         glob2-0.9.4.1-gcc44.patch
Patch4:         glob2-0.9.4.4-gcc49.patch
Patch5:         glob2-0.9.4.4-alt-gcc6.patch

# Automatically added by buildreq on Wed Feb 15 2006
BuildRequires: boost-devel esound freetype2-devel gcc-c++ libSDL-devel libSDL_image-devel libSDL_net-devel libSDL_ttf-devel libogg-devel libspeex-devel libstdc++-devel libvorbis-devel zlib-devel scons desktop-file-utils

BuildPreReq: libssl-devel libGL-devel libGLU-devel

%description
The player chooses the number of units to assign to various tasks, and the units do their best to satisfy the requests. This allows the user to manage more units and focus on strategy rather than individual units' jobs. It can be played by a single player, through your Local Area Network [LAN], or over the Internet thanks to Ysagoon Online Gaming (pronounced yog as in yoghurt) - a meta-server allowing transparent interaction between players and the IRC chatters on #glob2 (irc.freenode.net). It features AI allowing single-player games or any possible combination of human-computer teams. Also included is a scripting language for versatile gameplay or tutorials and an integrated map editor. 


%package data
Summary:    Data files for %name
Group:      Games/Strategy

%description data
Data files for %name

%prep
%setup -q
#setup -a 1 -n %{name}-%{version}
#patch0 -p0
%patch3 -p0
%patch4 -p1
%patch5 -p2

sed -i -e '3d' -e '12d' data/glob2.desktop
sed -i s#"Icon=glob2-icon-48x48"#"Icon=glob2.png"# data/glob2.desktop

chmod -x campaigns/Tutorial_Campaign.txt
sed -i 's/\r//' campaigns/Tutorial_Campaign.txt

%build
scons %{?_smp_mflags} INSTALLDIR=$RPM_BUILD_ROOT%{_datadir} BINDIR=$RPM_BUILD_ROOT%{_bindir} DATADIR=%{_datadir} CXXFLAGS="%{optflags}"


%install

scons install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/
cp -p data/icons/glob2-icon-64x64.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/glob2.png

for f in 128x128 16x16 24x24 32x32 48x48; do
mv $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$f/apps/glob2-icon-$f.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$f/apps/glob2.png
done
rm -rf $RPM_BUILD_ROOT%{_datadir}/glob2/data/icons

desktop-file-install                   \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications   \
        --remove-category=Application                   \
        --delete-original                               \
        $RPM_BUILD_ROOT%{_datadir}/applications/glob2.desktop

%files 
%doc  COPYING INSTALL README
%_bindir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/applications/*.desktop

%files data

%_datadir/%{name} 

%changelog
* Wed Feb 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.4.4-alt1.qa7
- Fixed build with gcc-6.

* Fri Jul 24 2015 Michael Shigorin <mike@altlinux.org> 0.9.4.4-alt1.qa6
- NMU: added debian patch to fix FTBFS

* Mon Feb 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4.4-alt1.qa5
- Rebuilt with Boost 1.53.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4.4-alt1.qa4
- Rebuilt with Boost 1.52.0

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4.4-alt1.qa3
- Rebuilt with Boost 1.51.0

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4.4-alt1.qa2
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4.4-alt1.qa1.4
- Rebuilt with Boost 1.48.0

* Sat Jul 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4.4-alt1.qa1.3
- Rebuilt with Boost 1.47.0

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4.4-alt1.qa1.2
- Rebuilt with Boost 1.46.1
- Added libssl-devel into BuildPreReq
- BuildRequires: replaced libmesa-devel by libGL-devel and libGLU-devel

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.9.4.4-alt1.qa1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Mon Dec 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.4.4-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for glob2
  * postclean-05-filetriggers for spec file

* Sat Oct 17 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.4.4-alt1
- 0.9.4.4 beta

* Tue Jul 14 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.4.1-alt1
- 0.9.4.1 beta
- fix build with gcc4.4

* Tue Dec 30 2008 Ilya Mashkin <oddity@altlinux.ru> 0.9.3-alt1.1
- rebuild

* Mon Dec 22 2008 Ilya Mashkin <oddity@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Mon Aug 07 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.8.21-alt1
- new version

* Mon May 22 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.8.19-alt3
- removed included SDL_ttf 

* Tue May 16 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.8.19-alt2
- gcc4.1 patch added 

* Tue Mar 14 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.8.19-alt1
- New version build for sisyphus

* Wed Feb 15 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.8.18-alt2
- buildreq boost-devel dependency added 

* Fri Feb 10 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.8.18-alt1
- New version build for sisyphus

* Wed Jan 11 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.8.17-alt2
- Menu bugfix 

* Mon Dec 12 2005 Eugene Suchkov <cityhawk@altlinux.ru> 0.8.17-alt1
- New version build for sisyphus

* Tue Oct 25 2005 Eugene Suchkov <cityhawk@altlinux.ru> 0.8.15-alt1
- Inital build for sisyphus


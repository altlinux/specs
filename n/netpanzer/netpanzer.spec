Name: netpanzer
Version: 0.8.7
Release: alt1
Summary: An Online Multiplayer Tactical Warfare Game

Group: Games/Arcade
License: GPLv2+
Packager: Ilya Mashkin <oddity@altlinux.ru>

URL:            http://www.netpanzer.info
Source0:	http://www.netpanzer.info/Download/NetPanzer/Releases/0.8.7/netpanzer-0.8.7-source.zip
Source1:	netpanzer.desktop
Patch0: netpanzer-desktop.patch

Patch4:         netpanzer-0.8.2-MapSelectionView-memory.patch
Patch6:         netpanzer-0.8.7-ccflags.patch
Patch8:		netpanzer-0.8.7-syslibs.patch
Patch9:         netpanzer-python3.patch

#set_gcc_version 8
BuildRequires: jam libphysfs-devel unzip desktop-file-utils doxygen gcc gcc-c++ scons liblua5.1-compat-devel
BuildRequires: libSDL-devel >= 1.2.5, libSDL_mixer-devel >= 1.2, libSDL_image-devel >= 1.2
Obsoletes: netpanzer-data <= 0.8 
Provides: netpanzer-data = %version-%release
Requires(post): coreutils
Requires(postun): coreutils

%description
netPanzer is an online multiplayer tactical warfare game designed for FAST
ACTION combat. Gameplay concentrates on the core -- no resource management is
needed. The game is based on quick tactical action and unit management in
real-time. Battles progress quickly and constantly as destroyed players respawn
with a set of new units. Players can join or leave multiplayer games at any
time.

%prep
%setup -qcn netpanzer-0.8.7


#Correct .desktop file
#patch0 -p0

%patch4 -p0
%patch6 -p1
%patch8 -p1
%patch9 -p0
rm -r src/Lib/lua src/Lib/physfs


%build
CCFLAGS="%{optflags} -std=c++14" scons datadir=%{_datadir}/netpanzer %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 netpanzer $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr cache/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr maps/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr pics/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr powerups/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr scripts/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr units/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr wads/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr sound/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/

# Install desktop item
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/netpanzer.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/netpanzer.xpm

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mv netpanzer.png \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

desktop-file-install \
	--dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

%files
%doc  COPYING README*  docs/
%_bindir/netpanzer
#{_datadir}/appdata/%{name}.appdata.xml
%_datadir/applications/netpanzer.desktop
%_datadir/icons/hicolor/48x48/apps/netpanzer.png
%_datadir/netpanzer

%changelog
* Tue Mar 30 2021 Ilya Mashkin <oddity@altlinux.ru> 0.8.7-alt1
- 0.8.7

* Wed Nov 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.qa3
- Fixed build with gcc 4.7

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.qa2
- Rebuilt with libphysfs 2.0.2

* Mon Dec 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.2-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for netpanzer
  * postclean-05-filetriggers for spec file

* Thu Aug 13 2009 Ilya Mashkin <oddity@altlinux.ru> 0.8.2-alt1
- Build for ALT Linux

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Jon Ciesla <limb@jcomserv.net> 0.8.2-4
- Fixed coreutils deps, BZ 475920.

* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> 0.8.2-3
- GCC 4.3 rebuild.

* Thu Jan 10 2008 Jon Ciesla <limb@jcomserv.net> 0.8.2-2
- Added memory, algorithm patches.

* Wed Aug 29 2007 Jon Ciesla <limb@jcomserv.net> 0.8.2-1
- Bumped to 0.8.2.
- Merged in and obsoleted/provided netpanzer-data to follow upstream.
- Patch to correct upstream .desktop file.

* Thu Aug 16 2007 Jon Ciesla <limb@jcomserv.net> 0.8.1-2
- License tag correction.

* Thu Mar 01 2007 Jon Ciesla <limb@jcomserv.net> 0.8.1-1
- Bumped to upstream
- Pulled gcc 4.1 patch, fixed upstream
- Pulled CVE 2006-2575, 2005-2295 patches, fixed upstream
- Updated netpanzer-data RQ to allow update of app without update of data.

* Wed Sep 13 2006 Hugo Cisneiros <hugo@devin.com.br> 0.8-5
- Rebuilt for FC6

* Thu Jun  8 2006 Hugo Cisneiros <hugo@devin.com.br> 0.8-4
- Fix Remote Server Termination vulnerability (CVE 2006-2575)
- Add proper packet size check (CVE 2005-2295) (patch from Gentoo)

* Thu May  4 2006 Hugo Cisneiros <hugo@devin.com.br> 0.8-3
- Changed netpanzer.png to comply with freedesktop.org standards.
- Added scripts to update the icon cache after installing

* Mon May  1 2006 Hugo Cisneiros <hugo@devin.com.br> 0.8-2
- Changed Package's RPM Group
- Fixed Changelog entries to specify versions
- Stripped '\r' EOL from RELNOTES file
- Added COPYING file

* Mon May  1 2006 Hugo Cisneiros <hugo@devin.com.br> 0.8-1
- Initial RPM release

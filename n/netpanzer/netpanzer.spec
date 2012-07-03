Name: netpanzer
Version: 0.8.2
Release: alt1.qa2
Summary: An Online Multiplayer Tactical Warfare Game

Group: Games/Arcade
License: GPLv2+
Url: http://netpanzer.berlios.de
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: http://download.berlios.de/netpanzer/netpanzer-%version.tar.bz2
Patch0: netpanzer-desktop.patch
Patch1: netpanzer-0.8.2-Pallette-memory.patch
Patch2: netpanzer-0.8.2-ColorTable-memory.patch
Patch3: netpanzer-0.8.2-Log-algorithm.patch
Patch4: netpanzer-0.8.2-MapSelectionView-memory.patch

BuildRequires: jam, libphysfs-devel, desktop-file-utils, doxygen, gcc, gcc-c++
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
%setup -q

# Strip \r from RELNOTES file
sed -i 's/\r//' RELNOTES

#Correct .desktop file
%patch0 -p0

%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0

%build
%configure
jam %{?_smp_mflags}

%install
export DESTDIR=$RPM_BUILD_ROOT
jam install

# Install desktop item
rm -f $RPM_BUILD_ROOT%_datadir/applications/netpanzer.desktop
rm -f $RPM_BUILD_ROOT%_datadir/pixmaps/netpanzer.xpm

mkdir -p $RPM_BUILD_ROOT%_datadir/icons/hicolor/48x48/apps
mv $RPM_BUILD_ROOT%_datadir/pixmaps/netpanzer.png \
   $RPM_BUILD_ROOT%_datadir/icons/hicolor/48x48/apps

desktop-file-install --vendor fedora				\
	--dir $RPM_BUILD_ROOT%_datadir/applications		\
	--add-category X-Fedora					\
	netpanzer.desktop

%files
%doc ChangeLog COPYING README RELNOTES TODO docs/serverhowto.html docs/tipofday.txt
%_bindir/netpanzer
%_datadir/applications/fedora-netpanzer.desktop
%_datadir/icons/hicolor/48x48/apps/netpanzer.png
%_datadir/netpanzer

%changelog
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

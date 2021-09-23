Name: marsshooter
Summary: M.A.R.S. - A Ridiculous Shooter
Group: Games/Arcade
Version: 0.7.6
Release: alt2

License: GPLv3+
Url: http://www.marsshooter.org/

Source: %name-%version.tar
Patch: marsshooter-0.7.6-shader.patch
Patch1: marsshooter-0.7.6-no-return-in-nonvoid-fix.patch
Patch2: marsshooter-0.7.6-remove-glu.patch
# Thnx Fedora Team!
Patch3: marsshooter-0.7.6-CMakelists-fix.patch
# https://www.mail-archive.com/devel@lists.fedoraproject.org/msg161636.html
Patch4: marsshooter-gcc11-fix.patch
BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkg-config
BuildRequires: glibc-core
BuildRequires: glibc-devel
BuildRequires: libstdc++-devel
BuildRequires: cmake
BuildRequires: dos2unix
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libSFML-devel
BuildRequires: libGL-devel
BuildRequires: libglvnd-devel
# BuildRequires: libGLU-devel
BuildRequires: libfribidi-devel
BuildRequires: libtag-devel
# We BuildRequire these, so that we can check their name does not change
BuildRequires: fonts-ttf-aajohan-comfortaa fonts-ttf-dejavu fonts-ttf-gargi
BuildRequires: fonts-ttf-wqy-microhei  fonts-ttf-thai-scalable-waree
Requires: %name-data = %version-%release
Requires: icon-theme-hicolor

%description
M.A.R.S. - a ridiculous shooter is a 2D space shooter with awesome visual
effects and attractive physics. Players can battle each other or computer
controlled enemies in exciting game modes:
    * awesome 2D-graphics with an unique style
    * a stunning amount of particles
    * single- and multi-player-support
    * an artificial intelligence using an aggro-system, which
      reacts differently upon varying situations
    * many impressive weapons
    * customizable ships
    * a very sexy GUI
    * several game modes: Space-ball, TeamDeathmatch, Cannonkeep,
      Deathmatch, Grave-Itation Pit

%package data
Summary: Audio, icons and XML files for %name
Group: Games/Arcade
License: CC-BY and CC-BY-SA
BuildArch: noarch
Requires: %name = %version-%release
Requires: fonts-ttf-aajohan-comfortaa fonts-ttf-dejavu fonts-ttf-gargi
Requires: fonts-ttf-wqy-microhei  fonts-ttf-thai-scalable-waree

%description data
This package contains audio, icons and XML files for %name.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

rm -fr cmake data_src ext_libs_for_windows
for i in data/locales/Polish.txt \
         include/Interface/ComboBox.hpp src/Interface/ComboBox.cpp \
         include/Interface/DropDownWindow.hpp src/Interface/DropDownWindow.cpp \
         include/Items/PUSleep.hpp src/Items/PUSleep.cpp; do
  chmod -x $i;
done
dos2unix credits.txt license.txt

%build
%cmake_insource

%make_build

%install
%makeinstall_std

desktop-file-validate %buildroot%_desktopdir/%name.desktop
appstream-util validate-relax --nonet \
%buildroot%_datadir/appdata/%name.appdata.xml
%files
%doc README.md
%doc license.txt credits.txt
%_gamesbindir/%name
%_datadir/appdata/%name.appdata.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_man6dir/%name.6.xz

%files data
%doc credits.txt music-license.eml
%_gamesdatadir/%name/

%changelog
* Fri Sep 24 2021 Artyom Bystrov <arbars@altlinux.org> 0.7.6-alt2
- Add patch for fixing build on GCC11

* Wed Mar 18 2020 Artyom Bystrov <arbars@altlinux.org> 0.7.6-alt1
- initial build for ALT Sisyphus

# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-install gcc-c++ libGL-devel libSDL-devel libmad-devel libogg-devel zlib-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           vavoom
Version:        1.33
Release:        alt2_23
Summary:        Enhanced Doom, Heretic, Hexen and Strife source port - meta package
Source0:        http://downloads.sourceforge.net/vavoom/%{name}-%{version}.tar.bz2
Source1:        doom.autodlrc
Source2:        heretic.autodlrc
Source3:        hexen.autodlrc
Source4:        strife.autodlrc
Source5:        doom-shareware.sh
Source6:        heretic-shareware.sh
Source7:        hexen-demo.sh
Source8:        strife-demo.sh
Source9:        doom-shareware.desktop
Source10:       heretic-shareware.desktop
Source11:       hexen-demo.desktop
Source12:       strife-demo.desktop
Source13:       vavoom.desktop
Source14:       doom-shareware.appdata.xml
Source15:       heretic-shareware.appdata.xml
Source16:       hexen-demo.appdata.xml
Source17:       strife-demo.appdata.xml
Source18:       vavoom.appdata.xml
Source19:       vavoom.png
Source20:       doom-logo.png
Source21:       tux-b2f.png
Source22:       vavoom.6
Patch0:         vavoom-1.21-datadir.patch
Patch1:         vavoom-1.27-CMakeLists.patch
Patch2:         vavoom-1.33-format-security.patch
Patch3:         vavoom-1.33-dont-override-delete.patch
Patch4:         vavoom-1.33-default-iwaddir.patch
Patch5:         vavoom-1.33-gcc6.patch
Patch6:         vavoom-1.33-misc-fixes.patch
# Incomplete patch to build with -std=c++11 not used as this crashes on exit
Patch7:         vavoom-1.33-cx11.patch
# Hack for crash on exit when building with -std=c++11, not used
Patch8:         vavoom-1.33-crash-on-exit.patch
URL:            http://vavoom-engine.com/
Group:          Games/Other
License:        GPLv2+
BuildRequires:  libSDL_mixer-devel libSDL_net-devel libpng-devel libjpeg-devel
BuildRequires:  libvorbis-devel libmikmod-devel libflac++-devel libflac-devel libopenal-devel libopenal1
BuildRequires:  libGLU-devel libwxGTK-contrib-gizmos-devel libwxGTK-contrib-ogl-devel libwxGTK-contrib-stc-devel libwxGTK-devel desktop-file-utils ctest cmake
BuildRequires:  libappstream-glib
Requires:       vavoom = %{version}-%{release}
Requires:       %{name}-doom-shareware = %{version}-%{release}
Requires:       %{name}-heretic-shareware = %{version}-%{release}
Requires:       %{name}-hexen-demo = %{version}-%{release}
Requires:       %{name}-strife-demo = %{version}-%{release}
Source44: import.info
Patch33: timidity-alt-buffer-overflow.patch

%description
Vavoom is an enhanced open-source port of Doom. The "vavoom" meta-package
installs vavoom-engine, and launchers / menu-entries to download and play
doom-shareware, heretic-shareware, hexen-demo and strife-demo.


%package engine
Group: Games/Other
Summary:        Enhanced Doom, Heretic, Hexen and Strife game engine
Requires:       timidity-instruments icon-theme-hicolor

%description engine
Vavoom is an enhanced open-source port of Doom. Allowing you to play not only
the classic 3D first-person shooter Doom, but also the Doom derived classics
Heretic, Hexen and Strife. Compared to the original games it adds extra
features such as translucency and freelook support and ofcourse the capability
to play these classics under Linux.


%package doom-shareware
Group: Games/Other
Summary:        Doom shareware installer
BuildArch:      noarch
Requires:       vavoom = %{version}-%{release}
Requires:       autodownloader unzip

%description doom-shareware
Doom is id Software's classic first person shooter follow-up to
Wolfenstein 3D. The Doom engine is Open Source. The original Doom datafiles
however are not Open Source. There is a gratis, but not Open Source shareware
version available on the internet.

This package contains an applications menu entry for playing Doom shareware
using the vavoom engine.  The first time you click this menu entry, it will
offer to download and install the Doom shareware datafiles for you.


%package heretic-shareware
Group: Games/Other
Summary:        Heretic shareware installer
BuildArch:      noarch
Requires:       vavoom = %{version}-%{release}
Requires:       autodownloader unzip

%description heretic-shareware
Heretic is Raven's classic dark fantasy first person shooter using a
modified Doom engine. The Heretic engine is Open Source. The original
Heretic datafiles however are not Open Source. There is a gratis, but not
Open Source shareware version available on the internet.

This package contains an applications menu entry for playing Heretic
shareware using the vavoom engine. The first time you click this menu
entry, it will offer to download and install the Heretic shareware
datafiles for you.


%package hexen-demo
Group: Games/Other
Summary:        Hexen demo installer
BuildArch:      noarch
Requires:       vavoom = %{version}-%{release}
Requires:       autodownloader unzip

%description hexen-demo
Hexen: Beyond Heretic is Raven's classic dark fantasy first person shooter
follow-up to Heretic. The Hexen engine is Open Source. The original Hexen
datafiles however are not Open Source. There is a gratis, but not Open
Source demo version available on the internet.

This package contains an applications menu entry for playing Hexen
demo using the vavoom engine. The first time you click this menu
entry, it will offer to download and install the Hexen demo
datafiles for you.


%package strife-demo
Group: Games/Other
Summary:        Strife demo installer
BuildArch:      noarch
Requires:       vavoom = %{version}-%{release}
Requires:       autodownloader unzip

%description strife-demo
Strife is Rogue Entertainment's classic first person shooter with
role-playing game elements. The Strife engine is Open Source. The original
Strife datafiles however are not Open Source. There is a gratis, but not
Open Source demo version available on the internet.

This package contains an applications menu entry for playing Strife
demo using the vavoom engine. The first time you click this menu
entry, it will offer to download and install the Strife demo
datafiles for you.


%prep 
%setup -q
%patch0 -p1 -b .datadir
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch33 -p1


%build
# Build with -std=gnu++98, c++11 causes issues on exit, likely due to
# bad interactions with the new / delete overloading in vc_object.cpp
export CXXFLAGS="$RPM_OPT_FLAGS -std=gnu++98 -fno-strict-aliasing -Wno-unused -Wno-unused-but-set-variable -Wno-unused-result -Wno-sign-compare -Wno-reorder"
%{fedora_cmake} -DWITH_LIBMAD:BOOL=OFF

# This one line sed command is easier than trying to muck with the Makefile
# to add the proper -D definition.
sed -i "s|#define FL_BASEDIR.*|#define FL_BASEDIR \"%{_datadir}/%{name}\"|" source/files.h
sed -i "s|#define CONFIG_FILE.*|#define CONFIG_FILE \"%{_sysconfdir}/timidity.cfg\"|" source/timidity/timidity.h

# source/CMakeLists.txt lacks dependencies to generate svnrev.h, force it
make -C source revision_check
# no -j# because there are more dependency issues in source/CMakeLists.txt
make VERBOSE=1

%install
make install \
        DESTDIR=$RPM_BUILD_ROOT \
        INSTALL_PARMS="-m 0755" \
        INSTALL_EXEPARMS="-m 0755" \
        INSTALL_DIRPARMS="-m 0755 -d"

mv $RPM_BUILD_ROOT%{_bindir}/%{name}.* $RPM_BUILD_ROOT%{_bindir}/%{name}
mv $RPM_BUILD_ROOT%{_bindir}/%{name}-dedicated.* $RPM_BUILD_ROOT%{_bindir}/%{name}-dedicated

# rm obsolete icon
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.png

# install autodl files and wrapper scripts
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/%{name}

install -p -m 755 %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/doom-shareware
install -p -m 755 %{SOURCE6} $RPM_BUILD_ROOT%{_bindir}/heretic-shareware
install -p -m 755 %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/hexen-demo
install -p -m 755 %{SOURCE8} $RPM_BUILD_ROOT%{_bindir}/strife-demo

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
for i in %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13}; do
  desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications "$i"
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
for i in %{SOURCE14} %{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18}; do
  install -p -m 644 "$i" $RPM_BUILD_ROOT%{_datadir}/appdata
  appstream-util validate-relax --nonet \
    $RPM_BUILD_ROOT%{_datadir}/appdata/$(basename "$i")
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{48x48,96x96}/apps
install -p -m 644 %{SOURCE19} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/96x96/apps/
install -p -m 644 %{SOURCE20} %{SOURCE21} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 %{SOURCE22} $RPM_BUILD_ROOT%{_mandir}/man6


%files
# no files, meta-package

%files engine
%doc docs/*.log docs/vavoom.txt
%doc docs/gnu.txt
%{_bindir}/*
%{_mandir}/man6/%{name}.6*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/basev
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.png

%files doom-shareware
%{_datadir}/%{name}/doom.autodlrc
%{_datadir}/appdata/doom-shareware.appdata.xml
%{_datadir}/applications/doom-shareware.desktop

%files heretic-shareware
%{_datadir}/%{name}/heretic.autodlrc
%{_datadir}/appdata/heretic-shareware.appdata.xml
%{_datadir}/applications/heretic-shareware.desktop

%files hexen-demo
%{_datadir}/%{name}/hexen.autodlrc
%{_datadir}/appdata/hexen-demo.appdata.xml
%{_datadir}/applications/hexen-demo.desktop

%files strife-demo
%{_datadir}/%{name}/strife.autodlrc
%{_datadir}/appdata/strife-demo.appdata.xml
%{_datadir}/applications/strife-demo.desktop


%changelog
* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 1.33-alt2_23
- fixed build

* Mon Oct 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.33-alt2_4.1
- Rebuilt with libpng15

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.33-alt2_4
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.33-alt2_3
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_3
- update to new release by fcimport

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_2
- update to new release by fcimport

* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_1
- update to new release by fcimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1_6
- initial release by fcimport


# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/xmllint cppunit-devel gcc-c++ pkgconfig(atlascpp-0.6) pkgconfig(eris-1.3) pkgconfig(mercator-0.3) pkgconfig(sigc++-2.0) pkgconfig(varconf-1.0) pkgconfig(wfmath-1.0) pkgconfig(x11)
# END SourceDeps(oneline)
Name:           ember
Version:        0.7.2
Release:        alt1.1
Summary:        3D client for WorldForge

Group:          Games/Other
License:        GPLv3+
URL:            http://www.worldforge.org/dev/eng/clients/ember
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2
Patch1:         ember-0.6.3-fix_implicit_dso.patch
Patch3:         ember-start.patch
Patch4:         ember-0.7.0-boost_shared_array.patch
Patch5:		ember-0.7.0-lua-5.2.patch
Patch6:		ember-doc-nover.patch

BuildRequires:  libSDL-devel tinyxml-devel libdevil-devel cegui-devel libogre-devel
BuildRequires:  liblua5-devel tolua++-devel libopenal-devel libalut-devel
BuildRequires:  atlascpp-devel chrpath
BuildRequires:  eris-devel >= 1.3.16
BuildRequires:  mercator-devel
BuildRequires:  varconf-devel
BuildRequires:	wfmath-devel >= 1.0
BuildRequires:	libwfut-devel
BuildRequires:  desktop-file-utils

Requires:       %{name}-media >= 0.7.2 %{name}-media < 0.7.3

Obsoletes:      sear < 0.6.4-0.16
Source44: import.info
Patch33: ember-0.7.0-alt-linkage.patch

%description
Ember is a client for MMORPGs using the WorldForge system.
It uses the Ogre 3D engine with CEGUI.


%prep
%setup -q
#patch1 -p1 -b .fix_implicit_dso
%patch3 -p2 -b .start
#patch4 -p1 -b .boost_shared_array
#patch5 -p1 -b .lua-52
#patch6 -p0 -b .doc-nover

# Encoding fix
iconv -f iso-8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
%patch33 -p1


%build
autoreconf -fisv
%configure --disable-static --disable-freeimage-check
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install \
    --remove-category="Application" --add-category="RolePlaying" \
    --delete-original --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mv $RPM_BUILD_ROOT%{_datadir}/icons/worldforge/ember.png \
    $RPM_BUILD_ROOT%{_datadir}/pixmaps/

# Don't need zero length files
rm -f $RPM_BUILD_ROOT%{_datadir}/ember/media/shared/modeldefinitions/{drystan_archer,vehicles,outdoor_structures,buildings,fencegate,palissade,house_A,choppingblockA,choppingblockB,mushroom,male,humanoid}.modeldef
rm -f $RPM_BUILD_ROOT%{_datadir}/ember/media/shared/common/resources/ogre/scripts/materials/smoke.material

chrpath -d %buildroot%_bindir/%name.bin

%check
%make_build check


%files
%doc COPYING README* INSTALL AUTHORS ChangeLog
%{_bindir}/%{name}
%{_bindir}/%{name}.bin
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/ember.png
# datadir/%{name} is owned by ember-media
# datadir/%{name}/media is owned by ember-media
# datadir/%{name}/media/shared is owned by ember-media
%{_datadir}/%{name}/media/shared/gui
%{_datadir}/%{name}/media/shared/entityrecipes
%{_datadir}/%{name}/media/shared/data/
%{_datadir}/%{name}/media/shared/scripting
%{_datadir}/%{name}/media/shared/sounddefinitions
# datadir/%{name}/media/user is owned by ember-media

# Not using noreplace: having old config file can make things not working as was intended. User can override settings with config in homedir.
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/*

%changelog
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.7.2-alt1.1
- rebuild with boost 1.57.0

* Thu Sep 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1
- Version 0.7.2

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_10
- update to new release by fcimport

* Fri Jul 26 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.0-alt1_7.1
- rebuild for new ogre

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_7
- new fc release


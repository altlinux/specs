#filter_from_requires /^debug64.libtolua..-5.1.so./d
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/xmllint boost-interprocess-devel pkgconfig(sigc++-2.0) pkgconfig(x11)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           ember
Version:        0.7.2
Release:        alt2_25
Summary:        3D client for WorldForge

Group:          Games/Other
License:        GPLv3+
URL:            http://www.worldforge.org/dev/eng/clients/ember
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2
Patch1:         ember-0.6.3-fix_implicit_dso.patch
Patch3:         ember-start.patch
Patch6:         ember-doc-nover.patch
# From upstream commit f605bd4bd15ea83da4d7864d45018e6f9a175b76
Patch7:         ember-0.7.2-fix-boost-m4.patch
Patch8:         ember-0.7.2-sigc++.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libSDL-devel tinyxml-devel libdevil-devel cegui-devel libogre-devel
BuildRequires:  lua-devel tolua++-devel libopenal-devel libalut-devel
BuildRequires:  libatlascpp-devel 
BuildRequires:  liberis-devel >= 1.3.16 
BuildRequires:  libmercator-devel 
BuildRequires:  libvarconf-devel 
BuildRequires:  libwfmath-devel >= 1.0
BuildRequires:  libwfut-devel
BuildRequires:  desktop-file-utils
BuildRequires:  cppunit-devel
# libtool is only needed while we need to run autogen.sh
BuildRequires:  libtool

Requires:       %{name}-media >= 0.7.2 %{name}-media < 0.7.3

Obsoletes:      sear < 0.6.4-0.16
Source44: import.info
Patch33: ember-0.7.0-alt-linkage.patch

%description
Ember is a client for MMORPGs using the WorldForge system.
It uses the Ogre 3D engine with CEGUI.


%prep
%setup -q
%patch1 -p1 -b .fix_implicit_dso
%patch3 -p0 -b .start
%patch6 -p0 -b .doc-nover
%patch7 -p1 -b .boost-m4
%patch8 -p1 -b .sigc++

# Encoding fix
iconv -f iso-8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
%patch33 -p1


%build
autoreconf -fisv
# configure.ac needs to be rebuilt for the updated boost.m4 needed to 
# work with gcc 5. This shouldn't be needed after the next ember release.
./autogen.sh
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

%check
%ifnarch %{arm} aarch64
make check
%endif


%files
%doc AUTHORS ChangeLog COPYING NEWS README.md
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
* Thu Feb 14 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt2_25
- rebuild with ogre 1.9.0

* Wed Jun 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.2-alt2_22.1
- NMU: rebuilt with boost-1.67.0.

* Tue Oct 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt2_22
- rebuild with libaltascpp

* Mon Feb 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt2_14.src.rpm
- fixed build

* Tue Jun 09 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.2-alt1.1.1
- Rebuilt for gcc5 C++11 ABI.

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

